#!/usr/bin/env python3
"""
Project 100 -- gate check.

Reads your trade files and prints PASS / FAIL / NOT STARTED for each gate.
Standard library only: no pip installs needed.

HOW TO RUN (Windows, from the folder that holds this file and your CSVs):
    python gate_check.py

FILES IT LOOKS FOR (same folder as this script):
    scalp_backtest_trades.csv   from the repo's scalping folder (Gate 1)
    measured_spreads.csv        from the repo's scalping folder (Gate 1 costs)
    paper_trades.csv            optional, Gate 2 (see FORMAT below)
    live_trades.csv             optional, Gates 3 and 4 (see FORMAT below)

FORMAT for paper_trades.csv / live_trades.csv (header row required):
    entry_time,symbol,net_pnl            <- required
    position_usd                         <- optional (needed for Gate 4 size checks)
    model_cost,actual_cost               <- optional (Gate 3 cost-vs-model check)
    incident                             <- optional, any text = a problem happened
                                            (duplicate order, guardrail breach, etc.)

IMPORTANT: Gate 1 only counts as a real pass on data tuned-on-never-touched.
Set FREEZE_DATE below to the day you froze the rules. Only trades ENTERED ON
OR AFTER that date count for Gate 1. Until you set it, Gate 1 is reported as
IN-SAMPLE and can never say PASS.
"""

import csv
import math
import os
import statistics
import sys
from collections import defaultdict
from datetime import date

# ----------------------------------------------------------------------
# SETTINGS -- change these here, nowhere else
# ----------------------------------------------------------------------
FREEZE_DATE = None          # e.g. "2026-10-20" once the rules are frozen; None = not frozen yet

# Cost model (must match scalp_backtest.py)
MIN_TICK_COST = 0.01
SPREAD_COST_MULTIPLIER = 1.0
FLAT_FALLBACK_CENTS = 2.0

# Reference size the dollar thresholds were written for
REFERENCE_POSITION_USD = 3000.0

# Gate 1 (backtest on frozen, untouched data)
G1_MIN_TRADES = 400
G1_MIN_NET_PER_TRADE_PCT = 0.05     # 0.05% of notional = $1.50 on $3,000
G1_MIN_POSITIVE_WEEK_FRACTION = 0.75
G1_MIN_WEEKS = 4
G1_MAX_SYMBOL_SHARE = 0.25          # no stock above 25% of profit
G1_MAX_DRAWDOWN_REF = 500.0         # dollars at the reference size (scaled automatically)

# Gate 2 (paper)
G2_MIN_DAYS = 10
G2_MIN_TRADES = 100
G2_MAX_GAP_PCT = 0.0667             # within ~$2 of backtest at $3,000 = 0.0667% of notional

# Gate 3 (tiny live)
G3_MIN_DAYS = 20
G3_MIN_TRADES = 200
G3_MIN_NET_PER_TRADE_PCT = 0.0333   # $1 on $3,000
G3_MAX_COST_OVERRUN = 0.25          # actual costs within 25% of model

# Gate 4 (scaling)
G4_MIN_PROFITABLE_DAYS_AT_SIZE = 20
G4_PAUSE_LOSING_STREAK = 5

HERE = os.path.dirname(os.path.abspath(__file__))


# ----------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------
def p(*a):
    print(*a)


def load_csv(name):
    path = os.path.join(HERE, name)
    if not os.path.exists(path):
        return None
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def day_of(ts):
    return date.fromisoformat(str(ts).strip()[:10])


def load_spreads():
    rows = load_csv("measured_spreads.csv") or []
    table = {}
    for r in rows:
        try:
            table[r["symbol"].strip().upper()] = float(r["median_pct"])
        except (KeyError, ValueError):
            pass
    return table


def backtest_trades():
    """Returns list of dicts with date, symbol, notional, net (measured-cost)."""
    rows = load_csv("scalp_backtest_trades.csv")
    if rows is None:
        return None
    spreads = load_spreads()
    out = []
    for r in rows:
        try:
            sym = r["symbol"].strip().upper()
            price = float(r["entry_price"])
            shares = float(r["shares"])
            gross = float(r["gross_pnl"])
        except (KeyError, ValueError):
            continue
        pct = spreads.get(sym)
        if pct is None:
            cps = FLAT_FALLBACK_CENTS / 100
        else:
            cps = max(MIN_TICK_COST, price * pct / 100) * SPREAD_COST_MULTIPLIER
        out.append({
            "ts": r["entry_time"],
            "date": day_of(r["entry_time"]),
            "symbol": sym,
            "notional": shares * price,
            "net": gross - shares * cps,
        })
    out.sort(key=lambda t: t["ts"])
    return out


def simple_trades(name):
    rows = load_csv(name)
    if rows is None:
        return None
    out = []
    for r in rows:
        try:
            net = float(r["net_pnl"])
            d = day_of(r["entry_time"])
        except (KeyError, ValueError):
            continue
        def f(key):
            try:
                return float(r[key])
            except (KeyError, ValueError, TypeError):
                return None
        out.append({
            "ts": r["entry_time"], "date": d,
            "symbol": (r.get("symbol") or "").strip().upper(),
            "net": net,
            "position": f("position_usd"),
            "model_cost": f("model_cost"),
            "actual_cost": f("actual_cost"),
            "incident": (r.get("incident") or "").strip(),
        })
    out.sort(key=lambda t: t["ts"])
    return out


def mean_sd(xs):
    n = len(xs)
    if n == 0:
        return 0.0, 0.0
    m = sum(xs) / n
    sd = statistics.stdev(xs) if n > 1 else 0.0
    return m, sd


def lower_bound(xs):
    n = len(xs)
    m, sd = mean_sd(xs)
    return m - 1.96 * sd / math.sqrt(n) if n > 1 else float("-inf")


def max_drawdown(xs):
    peak = cum = worst = 0.0
    for x in xs:
        cum += x
        peak = max(peak, cum)
        worst = min(worst, cum - peak)
    return worst  # negative number


def week_key(d):
    iso = d.isocalendar()
    return (iso[0], iso[1])


def check(label, ok, detail):
    p(f"   [{'PASS' if ok else 'FAIL'}] {label}: {detail}")
    return ok


def header(title):
    p("\n" + "=" * 64)
    p(title)
    p("=" * 64)


# ----------------------------------------------------------------------
# gates
# ----------------------------------------------------------------------
def gate1():
    header("GATE 1 -- Backtest on frozen, untouched data")
    trades = backtest_trades()
    if trades is None:
        p("   NOT STARTED -- scalp_backtest_trades.csv not found in this folder.")
        return None

    total_days = len({t["date"] for t in trades})
    p(f"   All backtest data on file: {len(trades)} trades over {total_days} trading days "
      f"({trades[0]['date']} to {trades[-1]['date']})")

    frozen = FREEZE_DATE is not None
    if frozen:
        cutoff = date.fromisoformat(FREEZE_DATE)
        use = [t for t in trades if t["date"] >= cutoff]
        p(f"   Rules frozen on {FREEZE_DATE}: counting only trades on/after that date "
          f"({len(use)} trades).")
    else:
        use = trades
        p("   *** FREEZE_DATE is not set. Numbers below are IN-SAMPLE (data you may have")
        p("   *** tuned on). Useful as a progress gauge; Gate 1 cannot PASS until you freeze.")

    if len(use) < 2:
        p("   Not enough trades to evaluate.")
        return False

    nets = [t["net"] for t in use]
    avg_notional = sum(t["notional"] for t in use) / len(use)
    scale = avg_notional / REFERENCE_POSITION_USD
    mean, _ = mean_sd(nets)
    lb = lower_bound(nets)
    mean_pct = 100 * mean / avg_notional
    p(f"   Average position: ${avg_notional:,.0f}   Net per trade (measured costs): "
      f"${mean:.2f} ({mean_pct:.3f}% of notional)   Total net: ${sum(nets):,.2f}")

    results = []
    results.append(check("Trade count", len(use) >= G1_MIN_TRADES,
                         f"{len(use)} of {G1_MIN_TRADES} needed"))
    results.append(check("Net per trade", mean_pct >= G1_MIN_NET_PER_TRADE_PCT,
                        f"{mean_pct:.3f}% vs {G1_MIN_NET_PER_TRADE_PCT}% needed"))
    results.append(check("Edge distinguishable from zero (95% lower bound > 0)", lb > 0,
                         f"lower bound ${lb:.2f}/trade"))

    weeks = defaultdict(float)
    for t in use:
        weeks[week_key(t["date"])] += t["net"]
    pos_weeks = sum(1 for v in weeks.values() if v > 0)
    frac = pos_weeks / len(weeks)
    results.append(check(
        "Positive weeks",
        len(weeks) >= G1_MIN_WEEKS and frac >= G1_MIN_POSITIVE_WEEK_FRACTION,
        f"{pos_weeks} of {len(weeks)} weeks positive "
        f"(need >= {G1_MIN_POSITIVE_WEEK_FRACTION:.0%} over at least {G1_MIN_WEEKS} weeks)"))

    by_sym = defaultdict(float)
    for t in use:
        by_sym[t["symbol"]] += t["net"]
    total = sum(by_sym.values())
    if total > 0:
        top_sym, top_val = max(by_sym.items(), key=lambda kv: kv[1])
        share = top_val / total
        results.append(check("No single-stock dependence", share <= G1_MAX_SYMBOL_SHARE,
                             f"{top_sym} = {share:.0%} of net profit (limit {G1_MAX_SYMBOL_SHARE:.0%})"))
    else:
        results.append(check("No single-stock dependence", False,
                             "total net is not positive, so this can't pass"))

    dd = max_drawdown(nets)
    dd_limit = G1_MAX_DRAWDOWN_REF * scale
    results.append(check("Max drawdown", -dd <= dd_limit,
                         f"${-dd:,.0f} vs limit ${dd_limit:,.0f}"))

    ok = all(results) and frozen
    if all(results) and not frozen:
        p("   -> Every number clears, but data is in-sample. Freeze the rules to make it count.")
    p(f"   GATE 1: {'PASS' if ok else 'FAIL / NOT YET'}")
    return ok, mean_pct if ok else None


def paper_or_live(name, title, min_days, min_trades):
    header(title)
    trades = simple_trades(name)
    if trades is None:
        p(f"   NOT STARTED -- {name} not found in this folder.")
        return None
    days = len({t["date"] for t in trades})
    p(f"   {len(trades)} trades over {days} trading days.")
    return trades, days


def gate2(backtest_mean_pct):
    r = paper_or_live("paper_trades.csv", "GATE 2 -- Paper trading", G2_MIN_DAYS, G2_MIN_TRADES)
    if r is None:
        return None
    trades, days = r
    nets = [t["net"] for t in trades]
    mean, _ = mean_sd(nets)
    avg_pos = (sum(t["position"] for t in trades if t["position"]) /
               max(1, sum(1 for t in trades if t["position"]))) or REFERENCE_POSITION_USD
    mean_pct = 100 * mean / avg_pos
    results = [
        check("Trading days", days >= G2_MIN_DAYS, f"{days} of {G2_MIN_DAYS}"),
        check("Trade count", len(trades) >= G2_MIN_TRADES, f"{len(trades)} of {G2_MIN_TRADES}"),
        check("Net per trade positive", mean > 0, f"${mean:.2f} ({mean_pct:.3f}% of notional)"),
    ]
    if backtest_mean_pct is not None:
        gap = abs(mean_pct - backtest_mean_pct)
        results.append(check("Close to backtest", gap <= G2_MAX_GAP_PCT,
                             f"gap {gap:.3f}% (limit {G2_MAX_GAP_PCT}%)"))
    else:
        p("   [ -- ] Close-to-backtest check skipped: Gate 1 hasn't passed yet.")
        results.append(False)
    incidents = [t for t in trades if t["incident"]]
    results.append(check("Zero incidents", not incidents, f"{len(incidents)} logged"))
    ok = all(results)
    p(f"   GATE 2: {'PASS' if ok else 'FAIL / NOT YET'}")
    return ok


def gate3():
    r = paper_or_live("live_trades.csv", "GATE 3 -- Tiny live", G3_MIN_DAYS, G3_MIN_TRADES)
    if r is None:
        return None, None
    trades, days = r
    nets = [t["net"] for t in trades]
    mean, _ = mean_sd(nets)
    sized = [t["position"] for t in trades if t["position"]]
    avg_pos = sum(sized) / len(sized) if sized else REFERENCE_POSITION_USD
    mean_pct = 100 * mean / avg_pos
    results = [
        check("Trading days", days >= G3_MIN_DAYS, f"{days} of {G3_MIN_DAYS}"),
        check("Trade count", len(trades) >= G3_MIN_TRADES, f"{len(trades)} of {G3_MIN_TRADES}"),
        check("Net per trade", mean_pct >= G3_MIN_NET_PER_TRADE_PCT,
              f"{mean_pct:.3f}% vs {G3_MIN_NET_PER_TRADE_PCT}% needed"),
    ]
    mc = [t["model_cost"] for t in trades if t["model_cost"] is not None and t["actual_cost"] is not None]
    ac = [t["actual_cost"] for t in trades if t["model_cost"] is not None and t["actual_cost"] is not None]
    if mc and sum(mc) > 0:
        over = sum(ac) / sum(mc) - 1
        results.append(check("Real costs vs model", over <= G3_MAX_COST_OVERRUN,
                             f"actual {over:+.0%} vs model (limit +{G3_MAX_COST_OVERRUN:.0%})"))
    else:
        p("   [ -- ] Cost check skipped: add model_cost and actual_cost columns to live_trades.csv.")
        results.append(False)
    incidents = [t for t in trades if t["incident"]]
    results.append(check("Zero incidents", not incidents, f"{len(incidents)} logged"))
    ok = all(results)
    p(f"   GATE 3: {'PASS' if ok else 'FAIL / NOT YET'}")
    return ok, trades


def gate4(live_trades, gate3_ok):
    header("GATE 4 -- Scaling")
    if not live_trades:
        p("   NOT STARTED -- needs live_trades.csv.")
        return
    if not gate3_ok:
        p("   LOCKED -- Gate 3 hasn't passed. Don't raise size yet.")
    sized = [t for t in live_trades if t["position"]]
    if not sized:
        p("   Add a position_usd column to live_trades.csv to enable size checks.")
        return
    cur = max(t["position"] for t in sized)
    at_size = [t for t in sized if t["position"] >= 0.999 * cur]
    day_net = defaultdict(float)
    for t in at_size:
        day_net[t["date"]] += t["net"]
    prof_days = sum(1 for v in day_net.values() if v > 0)
    check(f"Profitable days at ${cur:,.0f}", prof_days >= G4_MIN_PROFITABLE_DAYS_AT_SIZE,
          f"{prof_days} of {G4_MIN_PROFITABLE_DAYS_AT_SIZE} needed before raising size")

    # cost per dollar traded by size level
    by_size = defaultdict(lambda: [0.0, 0.0])
    for t in sized:
        if t["actual_cost"] is not None:
            by_size[t["position"]][0] += t["actual_cost"]
            by_size[t["position"]][1] += t["position"]
    if len(by_size) >= 2:
        p("   Cost per $ traded by size (should not rise as size grows):")
        for size in sorted(by_size):
            c, d = by_size[size]
            p(f"      ${size:>9,.0f}: {100 * c / d:.4f}%")

    # pause rules
    all_day = defaultdict(float)
    for t in live_trades:
        all_day[t["date"]] += t["net"]
    ordered = [all_day[d] for d in sorted(all_day)]
    streak = 0
    for v in reversed(ordered):
        if v < 0:
            streak += 1
        else:
            break
    check("Losing-day streak", streak < G4_PAUSE_LOSING_STREAK,
          f"{streak} straight losing days now (pause at {G4_PAUSE_LOSING_STREAK})")
    p("   Reminder: also pause if drawdown exceeds 2x the worst seen in testing.")


def main():
    r1 = gate1()
    g1_ok, bt_pct = (r1 if isinstance(r1, tuple) else (r1, None))
    gate2(bt_pct)
    g3_ok, live = gate3()
    gate4(live, g3_ok)
    p("\nThese checks are guard rails for decisions, not predictions. Small samples and")
    p("many tested variations both make an edge look better than it is.")


if __name__ == "__main__":
    sys.exit(main())
