#!/usr/bin/env python3
"""
Swing backtest: what if an API had acted on Fin's push alerts automatically?

Replays every Fin alert on file (outcome_history.json for Aug-Oct, plus
daily_pushes.json for the latest days) against real DAILY price bars and applies
the rules you trade by:
  * ENTRY: at the alert (see "Entry timing" below), sized at POSITION_USD.
  * STOP: Fin's own stop (entry - STOP_ATR_MULT x ATR, config.py).
  * TARGET: Fin's take-profit (entry + TAKE_PROFIT_ATR_MULT x ATR) -- or, as a
    second scenario, the full target (entry + 3 ATR).
  * INACTIVITY STOP: after INACTIVITY_DAYS checked closes, if the stock has
    not closed outside +/- INACTIVITY_BAND_ATR x ATR of entry, sell at that
    close ("it's going nowhere").
  * MAX HOLD: sell at the close after MAX_HOLD_DAYS (matches Fin's 7-day outcome window).

Entry timing (alerts arrive at all hours, so it matters):
  * pushed during the regular session -> fill at the alert's price_at_push; exits
    are checked starting the NEXT trading day (we can't see the rest of that day);
  * pushed pre-open / weekend / holiday -> fill at the next session's OPEN;
  * pushed after the close -> fill at the next session's OPEN.
Daily-bar conventions (deliberately conservative): if a day's range touches both
the stop and the target, the STOP counts first; a gap through the stop fills at
the open, not at the stop; a gap through the target fills at the open.

WHICH ALERTS TO ACT ON (Fin sends ~300 STRONG pushes a day, far more than you
trade): two views are reported for every scenario --
  "all": the FIRST alert of each symbol each day, no limits (how good are the
         alerts themselves?)
  "top1": an account that takes at most MAX_NEW_PER_DAY new position(s) a day,
         the highest-"strength" first-alert not already held, with at most
         MAX_OPEN positions open. (Strength is Fin's own ranking, not your manual
         analyst/Snowflake screen, which can't be replayed without look-ahead.)

Costs: ROUND_TRIP_COST_PCT of the position per trade (an assumption -- small
caps cost more). In-sample on ~2 months of one market regime: use it to find out
whether the idea is worth pursuing, not to tune parameters.

Run from the repo root (needs yfinance and pandas, like the rest of Fin):
    python swing_backtest.py
Writes swing_backtest_trades.csv, swing_backtest_summary.json, swing_backtest.md.
"""

import csv
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pandas as pd

try:
    import config
except ImportError:          # lets the file be tested on its own
    config = None

# ---- rules (see the docstring) ----------------------------------------------
STOP_ATR_MULT = getattr(config, "STOP_ATR_MULT", 1.5)
TAKE_PROFIT_ATR_MULT = getattr(config, "TAKE_PROFIT_ATR_MULT", 0.5)
FULL_TARGET_ATR_MULT = STOP_ATR_MULT * getattr(config, "REWARD_RISK_RATIO", 2.0)
POSITION_USD = 3500
ROUND_TRIP_COST_PCT = 0.10
INACTIVITY_DAYS = 3
INACTIVITY_BAND_ATR = 0.25
MAX_HOLD_DAYS = 7
MAX_NEW_PER_DAY = 1
MAX_OPEN = 5
QUICK_TARGET_PCT = 1.0       # scenarios E/F: fixed percentage target (your median exit is ~ +1.2%)

OUTCOME_FILE = "outcome_history.json"
PUSHES_FILE = "daily_pushes.json"
MY_TRADES_FILE = "open_positions.json"     # your Fin Trade Log export
OUT_MY = "swing_backtest_my_trades.csv"
OUT_TRADES = "swing_backtest_trades.csv"
OUT_JSON = "swing_backtest_summary.json"
OUT_MD = "swing_backtest.md"
NY = ZoneInfo("America/New_York")


# ---- alerts -------------------------------------------------------------------
def _parse_ts(s):
    dt = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def load_alerts():
    """First alert per (symbol, day): {symbol, day, pushed_at, price, atr, strength}."""
    raw = []
    if os.path.exists(OUTCOME_FILE):
        for key, v in json.load(open(OUTCOME_FILE)).items():
            parts = key.split("::")
            plan = v.get("trade_plan") or {}
            price = v.get("price_at_push")
            if len(parts) < 3 or not price or not plan.get("stop"):
                continue
            atr = v.get("atr_at_push") or (price - plan["stop"]) / STOP_ATR_MULT
            raw.append((v["symbol"], v.get("pushed_day") or parts[0], _parse_ts(parts[2]),
                        float(price), float(atr), float(v.get("strength") or 0)))
    if os.path.exists(PUSHES_FILE):
        for day, lst in json.load(open(PUSHES_FILE)).items():
            for p in lst:
                plan = p.get("trade_plan") or {}
                price = p.get("price_at_push")
                if not price or not plan.get("stop") or not p.get("pushed_at"):
                    continue
                atr = p.get("atr_at_push") or (price - plan["stop"]) / STOP_ATR_MULT
                raw.append((p["symbol"], day, _parse_ts(p["pushed_at"]),
                            float(price), float(atr), float(p.get("strength") or 0)))
    first = {}
    for sym, day, ts, price, atr, strength in sorted(raw, key=lambda r: r[2]):
        first.setdefault((sym, day), {"symbol": sym, "day": day, "pushed_at": ts,
                                      "price": price, "atr": atr, "strength": strength})
    return sorted(first.values(), key=lambda a: (a["day"], -a["strength"]))


def session_of(pushed_at):
    et = pushed_at.astimezone(NY)
    mins = et.hour * 60 + et.minute
    if et.weekday() >= 5:
        return "closed"
    if mins < 9 * 60 + 30:
        return "pre_open"
    if mins < 16 * 60:
        return "regular"
    return "after_close"


# ---- one trade ------------------------------------------------------------------
def simulate_trade(bars, alert, target_mult, use_stop=True, inactivity=True,
                   inact_days=None, inact_band=None, max_hold=None, target_pct=None):
    """bars: DataFrame indexed by date (python date) with Open/High/Low/Close.
    Returns a trade dict, or None if the entry or the exit is not on file yet."""
    inact_days = INACTIVITY_DAYS if inact_days is None else inact_days
    inact_band = INACTIVITY_BAND_ATR if inact_band is None else inact_band
    max_hold = MAX_HOLD_DAYS if max_hold is None else max_hold
    dates = list(bars.index)
    et_date = alert["pushed_at"].astimezone(NY).date()
    sess = session_of(alert["pushed_at"])

    def first_idx(pred):
        return next((i for i, d in enumerate(dates) if pred(d)), None)

    if sess == "regular" and et_date in dates:
        e = dates.index(et_date)
        entry, first_check = alert["price"], e + 1
    elif sess == "after_close":
        e = first_idx(lambda d: d > et_date)
        if e is None:
            return None
        entry, first_check = float(bars["Open"].iloc[e]), e
    else:                      # pre-open, weekend/holiday, or a regular-session day with no bar
        e = first_idx(lambda d: d >= et_date)
        if e is None:
            return None
        entry, first_check = float(bars["Open"].iloc[e]), e
    atr = alert["atr"]
    stop = entry - STOP_ATR_MULT * atr if use_stop else None
    # target_pct (e.g. 1.0 = +1%) overrides the ATR-based target when given
    target = entry * (1 + target_pct / 100) if target_pct is not None else entry + target_mult * atr

    n_closes, widest = 0, 0.0
    for j in range(first_check, len(dates)):
        o, h, l, c = (float(bars[k].iloc[j]) for k in ("Open", "High", "Low", "Close"))
        reason = price = None
        if stop is not None and o <= stop:
            reason, price = "stop_gap", o
        elif o >= target:
            reason, price = "target_gap", o
        elif stop is not None and l <= stop:
            reason, price = "stop", stop
        elif h >= target:
            reason, price = "target", target
        n_closes += 1
        if reason is None:
            widest = max(widest, abs(c - entry))
            if inactivity and n_closes >= inact_days and widest < inact_band * atr:
                reason, price = "inactive", c
            elif n_closes >= max_hold:
                reason, price = "max_hold", c
        if reason:
            shares = int(POSITION_USD // entry) or 1
            gross = shares * (price - entry)
            cost = shares * entry * ROUND_TRIP_COST_PCT / 100
            return {"symbol": alert["symbol"], "alert_day": alert["day"], "strength": alert["strength"],
                    "session": sess, "entry_date": str(dates[e]), "exit_date": str(dates[j]),
                    "entry": round(entry, 4), "exit": round(price, 4), "shares": shares,
                    "atr": round(atr, 4), "exit_reason": reason, "days_held": n_closes,
                    "gross": round(gross, 2), "cost": round(cost, 2), "net": round(gross - cost, 2),
                    "net_pct": round((gross - cost) / (shares * entry) * 100, 3)}
    return None


# ---- your own trades, replayed ---------------------------------------------------
def atr14_before(bars, entry_date):
    """Simple 14-day average true range ending the day BEFORE entry_date."""
    dates = list(bars.index)
    i = next((k for k, d in enumerate(dates) if d >= entry_date), None)
    if i is None or i < 15:
        return None
    trs = []
    for k in range(i - 14, i):
        h, l, pc = (float(bars["High"].iloc[k]), float(bars["Low"].iloc[k]),
                    float(bars["Close"].iloc[k - 1]))
        trs.append(max(h - l, abs(h - pc), abs(l - pc)))
    return sum(trs) / len(trs)


def replay_my_trades(bars_by_symbol, alerts, a_trades):
    """Replays each logged trade (your real entry price/date) under the same rules
    and compares with what you did and with Fin's top alert that day.
    a_trades: scenario-A trades for ALL alerts, to look up Fin's top pick's result."""
    if not os.path.exists(MY_TRADES_FILE):
        return [], {}
    log = json.load(open(MY_TRADES_FILE)).get("trades", [])
    by_day = {}
    for a in alerts:
        by_day.setdefault(a["day"], []).append(a)
    a_lookup = {(t["alert_day"], t["symbol"]): t for t in a_trades}
    rows, skipped = [], []
    for tr in log:
        sym, ed = tr.get("symbol"), tr.get("entryDate")
        b = bars_by_symbol.get(sym)
        if not ed or b is None or b.empty:
            skipped.append(f"{sym}: " + ("entry date missing" if not ed else "no price data"))
            continue
        edate = pd.Timestamp(ed).date()
        atr = atr14_before(b, edate)
        if atr is None:
            skipped.append(f"{sym}: not enough price history for ATR")
            continue
        entry = float(tr["entryPrice"])
        pushed = datetime(edate.year, edate.month, edate.day, 12, 0, tzinfo=NY).astimezone(timezone.utc)
        pseudo = {"symbol": sym, "day": ed, "pushed_at": pushed, "price": entry, "atr": atr, "strength": 0.0}
        ra = simulate_trade(b, pseudo, TAKE_PROFIT_ATR_MULT)
        rd = simulate_trade(b, pseudo, TAKE_PROFIT_ATR_MULT, use_stop=False)
        re_ = simulate_trade(b, pseudo, None, target_pct=QUICK_TARGET_PCT)
        closed = tr.get("status") == "closed" and tr.get("exitPrice")
        exit_date = pd.Timestamp(tr["exitDate"]).date() if closed and tr.get("exitDate") else b.index[-1]
        exit_px = float(tr["exitPrice"]) if closed else float(b["Close"].iloc[-1])
        # worst dip while held: closes on entry/exit days, lows in between (as in trade_drawdown_report.py)
        held = b[(b.index >= edate) & (b.index <= exit_date)]
        dips = []
        for d, r_ in held.iterrows():
            dips.append(float(r_["Close"]) if d in (edate, exit_date) else float(r_["Low"]))
        worst = (min(dips) / entry - 1) * 100 if dips else 0.0
        stop_lvl = entry - STOP_ATR_MULT * atr
        # Fin alert context
        day_alerts = by_day.get(ed, [])
        rank = next((i + 1 for i, a in enumerate(day_alerts) if a["symbol"] == sym), None)
        top = day_alerts[0] if day_alerts else None
        top_t = a_lookup.get((ed, top["symbol"])) if top else None
        mine_pct = (exit_px / entry - 1) * 100 - ROUND_TRIP_COST_PCT
        rows.append({
            "symbol": sym, "entry_date": ed, "entry": entry, "exit_date": str(exit_date),
            "status": "closed" if closed else "open (marked to latest close)",
            "you_net_pct": round(mine_pct, 2),
            "you_net_usd": round(tr["shares"] * (exit_px - entry) - tr["shares"] * entry * ROUND_TRIP_COST_PCT / 100, 2),
            "you_days": len(pd.bdate_range(edate, exit_date)) - 1,
            "your_worst_dip_pct": round(worst, 1),
            "fin_stop_reached": bool(dips and min(dips) <= stop_lvl),
            "rules_A_exit": ra["exit_reason"] if ra else "unresolved",
            "rules_A_net_pct": ra["net_pct"] if ra else None,
            "rules_A_days": ra["days_held"] if ra else None,
            "rules_E_exit": re_["exit_reason"] if re_ else "unresolved",
            "rules_E_net_pct": re_["net_pct"] if re_ else None,
            "rules_D_no_stop_exit": rd["exit_reason"] if rd else "unresolved",
            "rules_D_net_pct": rd["net_pct"] if rd else None,
            "fin_alert_rank_that_day": rank,
            "fin_alerts_that_day": len(day_alerts),
            "fin_top_pick": top["symbol"] if top else None,
            "fin_top_pick_rules_A_net_pct": top_t["net_pct"] if top_t else None,
        })
    def avg(key, only=None):
        v = [r[key] for r in rows if r[key] is not None and (only is None or only(r))]
        return round(sum(v) / len(v), 2) if v else None
    ranks = sorted(r["fin_alert_rank_that_day"] for r in rows if r["fin_alert_rank_that_day"])
    summary = {
        "trades_replayed": len(rows), "skipped": skipped,
        "you_avg_net_pct": avg("you_net_pct"), "you_total_net_usd": round(sum(r["you_net_usd"] for r in rows), 2),
        "you_win_rate_pct": round(100 * sum(1 for r in rows if r["you_net_pct"] > 0) / len(rows), 1) if rows else None,
        "fin_stop_would_have_fired_on": [r["symbol"] for r in rows if r["fin_stop_reached"]],
        "rules_A_avg_net_pct": avg("rules_A_net_pct"),
        "rules_A_win_rate_pct": round(100 * sum(1 for r in rows if (r["rules_A_net_pct"] or 0) > 0) / len(rows), 1) if rows else None,
        "rules_A_stopped_out": sum(1 for r in rows if r["rules_A_exit"] in ("stop", "stop_gap")),
        "rules_D_avg_net_pct": avg("rules_D_net_pct"),
        "rules_E_avg_net_pct": avg("rules_E_net_pct"),
        "rules_E_win_rate_pct": round(100 * sum(1 for r in rows if (r["rules_E_net_pct"] or 0) > 0) / len(rows), 1) if rows else None,
        "rules_E_stopped_out": sum(1 for r in rows if r["rules_E_exit"] in ("stop", "stop_gap")),
        "your_picks_had_a_fin_alert_that_day": len(ranks), "median_alert_rank_of_your_picks": ranks[len(ranks) // 2] if ranks else None,
        "fin_top_pick_avg_net_pct_on_your_entry_days": avg("fin_top_pick_rules_A_net_pct"),
    }
    return rows, summary


# ---- portfolio view / stats -------------------------------------------------------
def pick_account(trades, max_new=None, max_open=None):
    """Takes at most max_new new positions a day (best strength first), with at
    most max_open open; a position occupies a slot through its exit day."""
    max_new = MAX_NEW_PER_DAY if max_new is None else max_new
    max_open = MAX_OPEN if max_open is None else max_open
    chosen = []
    by_day = {}
    for t in trades:
        by_day.setdefault(t["alert_day"], []).append(t)
    for day in sorted(by_day):
        taken = 0
        for t in sorted(by_day[day], key=lambda x: -x["strength"]):
            if taken >= max_new:
                break
            open_now = [c for c in chosen
                        if c["entry_date"] <= t["entry_date"] <= c["exit_date"]]
            if len(open_now) >= max_open or any(c["symbol"] == t["symbol"] for c in open_now):
                continue
            chosen.append(t)
            taken += 1
    return chosen


def stats(trades, label=""):
    if not trades:
        return {"label": label, "trades": 0}
    n = len(trades)
    nets = [t["net"] for t in trades]
    days = sorted({t["entry_date"] for t in trades})
    span = max(1, len(pd.bdate_range(days[0], days[-1])))
    cum = peak = worst = 0.0
    for t in sorted(trades, key=lambda x: x["exit_date"]):
        cum += t["net"]
        peak = max(peak, cum)
        worst = min(worst, cum - peak)
    reasons = {}
    for t in trades:
        reasons[t["exit_reason"]] = reasons.get(t["exit_reason"], 0) + 1
    return {
        "label": label, "trades": n,
        "win_rate_pct": round(100 * sum(1 for x in nets if x > 0) / n, 1),
        "avg_net_pct": round(sum(t["net_pct"] for t in trades) / n, 2),
        "avg_net_usd": round(sum(nets) / n, 2),
        "total_net_usd": round(sum(nets), 2),
        "avg_days_held": round(sum(t["days_held"] for t in trades) / n, 1),
        # only meaningful for the one-position-a-day account view, not "all"
        "usd_per_business_day": None if label == "all" else round(sum(nets) / span, 2),
        "max_drawdown_usd": round(worst, 2),
        "exit_reasons": dict(sorted(reasons.items())),
    }


SCENARIOS = [
    ("A. take-profit +0.5 ATR, stop 1.5 ATR, inactivity stop, 7-day max", dict(target_mult=TAKE_PROFIT_ATR_MULT)),
    ("B. same, but full target +3 ATR", dict(target_mult=FULL_TARGET_ATR_MULT)),
    ("C. take-profit, NO inactivity stop", dict(target_mult=TAKE_PROFIT_ATR_MULT, inactivity=False)),
    ("D. take-profit, NO stop (ride dips; diagnostic of 'hold through dips')",
     dict(target_mult=TAKE_PROFIT_ATR_MULT, use_stop=False)),
    # E/F added 2026-10-22: your median winning exit is about +1.2%, so test a quick fixed +1% target
    (f"E. quick +{QUICK_TARGET_PCT}% target, stop 1.5 ATR, inactivity stop",
     dict(target_mult=None, target_pct=QUICK_TARGET_PCT)),
    (f"F. quick +{QUICK_TARGET_PCT}% target, NO stop",
     dict(target_mult=None, target_pct=QUICK_TARGET_PCT, use_stop=False)),
]


def run_scenario(bars_by_symbol, alerts, **kw):
    trades, missing = [], 0
    for a in alerts:
        b = bars_by_symbol.get(a["symbol"])
        if b is None or b.empty:
            missing += 1
            continue
        t = simulate_trade(b, a, **kw)
        if t:
            trades.append(t)
    return trades, missing


# ---- data -----------------------------------------------------------------------
def fetch_daily_bars(symbols, start, end):
    import yfinance as yf
    out = {}
    symbols = sorted(set(symbols))
    for i in range(0, len(symbols), 80):
        chunk = symbols[i:i + 80]
        try:
            df = yf.download(chunk, start=start, end=end, interval="1d", group_by="ticker",
                             auto_adjust=False, progress=False, threads=True)
        except Exception as exc:
            print(f"  chunk {i // 80 + 1} failed: {exc}", file=sys.stderr)
            continue
        for sym in chunk:
            try:
                sub = df[sym] if isinstance(df.columns, pd.MultiIndex) else df
                sub = sub[["Open", "High", "Low", "Close"]].dropna(how="any")
            except Exception:
                continue
            if sub.empty:
                continue
            sub.index = [d.date() for d in pd.to_datetime(sub.index)]
            out[sym] = sub
        print(f"  fetched {min(i + 80, len(symbols))}/{len(symbols)} symbols", file=sys.stderr)
    # drop today's still-forming bar
    now = datetime.now(NY)
    if now.hour * 60 + now.minute < 16 * 60 + 30:
        for sym, sub in out.items():
            if len(sub) and sub.index[-1] == now.date():
                out[sym] = sub.iloc[:-1]
    return out


# ---- report ---------------------------------------------------------------------
def main():
    global ROUND_TRIP_COST_PCT
    alerts = load_alerts()
    if not alerts:
        print("No alerts found (outcome_history.json / daily_pushes.json).", file=sys.stderr)
        return
    first_day, last_day = alerts[0]["day"], alerts[-1]["day"]
    print(f"{len(alerts)} first-alerts of the day, {first_day} to {last_day}, "
          f"{len({a['symbol'] for a in alerts})} symbols", file=sys.stderr)
    start = (pd.Timestamp(first_day) - pd.Timedelta(days=7)).strftime("%Y-%m-%d")
    end = (pd.Timestamp.now() + pd.Timedelta(days=2)).strftime("%Y-%m-%d")
    my_symbols = []
    if os.path.exists(MY_TRADES_FILE):
        my_symbols = [t["symbol"] for t in json.load(open(MY_TRADES_FILE)).get("trades", [])]
        my_dates = [t["entryDate"] for t in json.load(open(MY_TRADES_FILE)).get("trades", []) if t.get("entryDate")]
        if my_dates and min(my_dates) < start:
            start = (pd.Timestamp(min(my_dates)) - pd.Timedelta(days=30)).strftime("%Y-%m-%d")
        else:
            start = (pd.Timestamp(start) - pd.Timedelta(days=30)).strftime("%Y-%m-%d")   # ATR history
    bars = fetch_daily_bars([a["symbol"] for a in alerts] + my_symbols, start, end)

    result = {"generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "alerts": len(alerts), "alert_days": f"{first_day} to {last_day}",
              "symbols_with_prices": len(bars),
              "assumptions": {"position_usd": POSITION_USD, "round_trip_cost_pct": ROUND_TRIP_COST_PCT,
                              "stop_atr": STOP_ATR_MULT, "take_profit_atr": TAKE_PROFIT_ATR_MULT,
                              "full_target_atr": FULL_TARGET_ATR_MULT, "inactivity_days": INACTIVITY_DAYS,
                              "inactivity_band_atr": INACTIVITY_BAND_ATR, "max_hold_days": MAX_HOLD_DAYS,
                              "max_new_per_day": MAX_NEW_PER_DAY, "max_open": MAX_OPEN},
              "scenarios": {}}
    base_account = []
    for name, kw in SCENARIOS:
        trades, missing = run_scenario(bars, alerts, **kw)
        acct = pick_account(trades)
        result["scenarios"][name] = {"all_first_alerts": stats(trades, "all"),
                                     "top1_account": stats(acct, "top1/day"),
                                     "alerts_without_prices": missing}
        if name.startswith("A."):
            base_account = acct
            base_all = trades
    # sensitivity of the inactivity rule (scenario A, account view); in-sample, do not tune
    grid = []
    for days in (2, 3, 5):
        for band in (0.15, 0.25, 0.5):
            t, _ = run_scenario(bars, alerts, target_mult=TAKE_PROFIT_ATR_MULT,
                                inact_days=days, inact_band=band)
            s = stats(pick_account(t))
            grid.append({"inactivity_days": days, "band_atr": band, "trades": s.get("trades"),
                         "avg_net_usd": s.get("avg_net_usd"), "win_rate_pct": s.get("win_rate_pct")})
    stops = sorted(STOP_ATR_MULT * a["atr"] / a["price"] * 100 for a in alerts)
    med_stop = stops[len(stops) // 2]
    win_gain, loss = QUICK_TARGET_PCT - ROUND_TRIP_COST_PCT, med_stop + ROUND_TRIP_COST_PCT
    result["quick_target_breakeven"] = {"target_pct": QUICK_TARGET_PCT, "median_stop_pct": round(med_stop, 2),
                                        "breakeven_win_rate_pct": round(100 * loss / (loss + win_gain), 1)}
    my_rows, my_summary = replay_my_trades(bars, alerts, base_all)
    result["your_trades_replayed"] = my_summary
    if my_rows:
        with open(OUT_MY, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(my_rows[0].keys()))
            w.writeheader()
            w.writerows(my_rows)
    result["inactivity_sensitivity_top1"] = grid
    cost_check = {}
    saved = ROUND_TRIP_COST_PCT
    for c in (0.05, 0.10, 0.25):
        ROUND_TRIP_COST_PCT = c
        t, _ = run_scenario(bars, alerts, target_mult=TAKE_PROFIT_ATR_MULT)
        cost_check[f"{c}%"] = stats(pick_account(t)).get("avg_net_usd")
    ROUND_TRIP_COST_PCT = saved
    result["cost_sensitivity_avg_net_usd_top1"] = cost_check

    with open(OUT_TRADES, "w", newline="") as f:
        if base_account:
            w = csv.DictWriter(f, fieldnames=list(base_account[0].keys()))
            w.writeheader()
            w.writerows(base_account)
    with open(OUT_JSON, "w") as f:
        json.dump(result, f, indent=2)

    lines = ["# Swing backtest: acting on Fin alerts automatically", "",
             f"Generated {result['generated_utc']}. {len(alerts)} first-alerts of the day "
             f"({result['alert_days']}); {len(bars)} symbols with prices. Position ${POSITION_USD:,}, "
             f"cost {ROUND_TRIP_COST_PCT}% round trip.", "",
             "| Scenario | View | Trades | Win % | Avg net % | Avg net $ | Total net $ | $/biz day | Avg days | Max DD $ |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for name, r in result["scenarios"].items():
        for key in ("all_first_alerts", "top1_account"):
            s = r[key]
            if not s.get("trades"):
                lines.append(f"| {name} | {key} | 0 | | | | | | | |")
                continue
            lines.append(f"| {name} | {s['label']} | {s['trades']} | {s['win_rate_pct']} | {s['avg_net_pct']} | "
                         f"{s['avg_net_usd']} | {s['total_net_usd']} | {s['usd_per_business_day']} | "
                         f"{s['avg_days_held']} | {s['max_drawdown_usd']} |")
    lines += ["", "## Exit reasons (scenario A, top1 account)", "",
              json.dumps(result["scenarios"][SCENARIOS[0][0]]["top1_account"].get("exit_reasons", {})), "",
              "## Inactivity-rule sensitivity (top1 account, in-sample -- do not tune on it)", "",
              "| Days | Band (ATR) | Trades | Win % | Avg net $ |", "|---|---|---|---|---|"]
    lines += [f"| {g['inactivity_days']} | {g['band_atr']} | {g['trades']} | {g['win_rate_pct']} | {g['avg_net_usd']} |"
              for g in grid]
    if my_rows:
        m = my_summary
        lines += ["", "## Your logged trades replayed under the same rules", "",
                  f"{m['trades_replayed']} trades (skipped: {', '.join(m['skipped']) or 'none'}). "
                  "ATR = simple 14-day average true range the day before entry.", "",
                  "| | You (actual) | Rules A (stop + take-profit + inactivity) | Rules D (no stop) | Rules E (+1% target + stop) |",
                  "|---|---|---|---|---|",
                  f"| Win rate | {m['you_win_rate_pct']}% | {m['rules_A_win_rate_pct']}% | | {m['rules_E_win_rate_pct']}% |",
                  f"| Avg net % per trade | {m['you_avg_net_pct']} | {m['rules_A_avg_net_pct']} | {m['rules_D_avg_net_pct']} | {m['rules_E_avg_net_pct']} |", "",
                  f"- Fin's stop level was reached while you held: {', '.join(m['fin_stop_would_have_fired_on']) or 'none'}. "
                  f"Under rules A, {m['rules_A_stopped_out']} of {m['trades_replayed']} would have been stopped out.",
                  f"- Your picks had a Fin alert that day for {m['your_picks_had_a_fin_alert_that_day']} of {m['trades_replayed']} trades "
                  f"(median Fin rank {m['median_alert_rank_of_your_picks']}, 1 = top).",
                  f"- Fin's top pick on your entry days, under rules A: avg {m['fin_top_pick_avg_net_pct_on_your_entry_days']}% per trade.", "",
                  "| Symbol | Entry | You: net % / days / worst dip | Rules A | Rules D | Rules E | Fin rank that day |", "|---|---|---|---|---|---|---|"]
        for r in my_rows:
            rank = r["fin_alert_rank_that_day"]
            rank_txt = f"{rank} of {r['fin_alerts_that_day']}" if rank else "no alert"
            dip = f"{r['your_worst_dip_pct']}%" + (" (Fin stop hit)" if r["fin_stop_reached"] else "")
            lines.append(f"| {r['symbol']} | {r['entry_date']} @ {r['entry']} | "
                         f"{r['you_net_pct']}% / {r['you_days']}d / {dip} | "
                         f"{r['rules_A_exit']} {r['rules_A_net_pct']}% | "
                         f"{r['rules_D_no_stop_exit']} {r['rules_D_net_pct']}% | "
                         f"{r['rules_E_exit']} {r['rules_E_net_pct']}% | {rank_txt} |")
    qb = result["quick_target_breakeven"]
    lines += ["", f"Quick-target break-even: with a +{qb['target_pct']}% target and the median stop of "
              f"-{qb['median_stop_pct']}%, the win rate must exceed {qb['breakeven_win_rate_pct']}% to break even after costs.",
              "", f"Cost sensitivity (avg net $ per trade, top1): {json.dumps(cost_check)}", "",
              "Conventions: stop counts first if a day touches both stop and target; gaps fill at the open; "
              "pre-open and after-close alerts fill at the next open; exits start the day after a regular-session "
              "alert. In-sample, about two months, one market regime."]
    with open(OUT_MD, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines), file=sys.stderr)


if __name__ == "__main__":
    main()
