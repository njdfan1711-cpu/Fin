#!/usr/bin/env python3
"""
Random-entry baseline for the scalping backtest.

QUESTION IT ANSWERS: does the entry signal (VWAP reclaim + momentum + volume
spike) do any better than entering at a random time? It uses the SAME symbols,
the SAME days, the SAME stop / target / time-stop / end-of-day exit rules and
the same position size as scalp_backtest.py -- only the entry time is random.

For every real signal in the current 7-day Yahoo window it draws a random
entry time and simulates the exit, 1,000 times. Two versions:
  A. same symbol, same day, any eligible minute
  B. same symbol, same day, within +/-15 minutes of the real entry
     (also controls for time-of-day effects)
and compares the real signals' average result with the spread of random
results. If the real average sits inside the random range, the entry signal
adds nothing beyond the exit rules and costs.

Compare GROSS first (cost is the same for matched random entries, because
they use the same symbols). A small p-value (say under 0.05) means the real
signals did better than random entries; a large one means they did not.

ALSO (added 2026-10-21) -- two timing diagnostics on the same real signals:
  * DELAY SWEEP: enter 0, 1, 2, 3, 5 and 10 minutes AFTER the signal instead of
    on it, same exits. If waiting does better, the signal is firing at the top of
    a burst and the fix is to wait for a pullback, not to tune thresholds.
  * MIRROR (short) TEST: take the opposite side at the signal minute with the
    mirrored stop/target. Diagnostic ONLY -- the bot is long-only and shorting
    has borrow and availability issues. A clearly positive mirror result would
    mean the signal tends to mark exhaustion, not the start of a move.
Both use the same ~7-day window and the same handful of signals, so treat
them as clues to test properly later, not as findings.

LIMITS (read before trusting it): only the ~7 trading days Yahoo provides;
a few hundred trades at most, so it can show "no edge" much more easily
than it can prove an edge; random entries can overlap in a symbol while real
ones cannot (negligible). Only symbols that pass the cost gate are used.

Run (same requirements as scalp_backtest.py, same folder):
    python scalp_random_baseline.py
Writes scalp_random_baseline.json and scalp_random_baseline.md.
"""

import json
import random
import sys
from datetime import datetime, timezone

import scalp_backtest as sb

DELAYS = [0, 1, 2, 3, 5, 10]
DRAWS = 1000
WINDOW_MINUTES = 15
SEED = 20261020
OUT_JSON = "scalp_random_baseline.json"
OUT_MD = "scalp_random_baseline.md"


def simulate_exit(high, low, close, last_bar, i, entry_price):
    """Same exit order as find_trades (fixed mode): target, stop, time-stop,
    end-of-day. Returns (exit_index, reason, exit_price) or None if the data
    ends before the trade resolves."""
    target = entry_price * (1 + sb.SCALP_TARGET_PCT / 100)
    stop = entry_price * (1 - sb.SCALP_STOP_PCT / 100)
    for j in range(i + 1, len(close)):
        held = j - i
        if high[j] >= target:
            return j, "target", target
        if low[j] <= stop:
            return j, "stop", stop
        if held >= sb.SCALP_MAX_HOLD_MINUTES:
            return j, "time_stop", close[j]
        if sb.FLATTEN_AT_CLOSE and last_bar[j]:
            return j, "eod", close[j]
    return None


def simulate_exit_short(high, low, close, last_bar, i, entry_price):
    """Mirror of simulate_exit for a short entered at the same price: target
    below, stop above, same time-stop and end-of-day rules, same within-bar
    priority (target checked before stop)."""
    target = entry_price * (1 - sb.SCALP_TARGET_PCT / 100)
    stop = entry_price * (1 + sb.SCALP_STOP_PCT / 100)
    for j in range(i + 1, len(close)):
        held = j - i
        if low[j] <= target:
            return j, "target", target
        if high[j] >= stop:
            return j, "stop", stop
        if held >= sb.SCALP_MAX_HOLD_MINUTES:
            return j, "time_stop", close[j]
        if sb.FLATTEN_AT_CLOSE and last_bar[j]:
            return j, "eod", close[j]
    return None


def prepare(df):
    """Arrays + per-bar helpers for one symbol."""
    idx = list(df.index)
    day = [t.date() for t in idx]
    n = len(df)
    last_bar = [
        (day[i + 1] != day[i]) if i < n - 1
        else sb._minutes_since_open(idx[i]) >= sb.LAST_BAR_MINUTE
        for i in range(n)
    ]
    minute = [sb._minutes_since_open(t) for t in idx]
    return {
        "high": df["High"].to_numpy(float), "low": df["Low"].to_numpy(float),
        "close": df["Close"].to_numpy(float), "idx": idx, "day": day,
        "last_bar": last_bar, "minute": minute,
        "pos": {str(t): i for i, t in enumerate(idx)},
    }


def eligible(p):
    return [i for i in range(20, len(p["close"]))
            if p["minute"][i] >= sb.MIN_MINUTES_AFTER_OPEN
            and not (sb.FLATTEN_AT_CLOSE and p["last_bar"][i])]


def result_for(p, symbol, i, spreads):
    entry = float(p["close"][i])
    ex = simulate_exit(p["high"], p["low"], p["close"], p["last_bar"], i, entry)
    if ex is None:
        return None
    _, reason, exit_price = ex
    shares = int(sb.POSITION_SIZE_USD // entry)
    gross = shares * (exit_price - entry)
    cps, _ = sb.measured_cost_per_share(symbol, entry, spreads)
    cost = shares * cps + sb.COMMISSION_PER_TRADE
    return {"gross": gross, "net": gross - cost, "reason": reason}


def result_short(p, symbol, i, spreads):
    entry = float(p["close"][i])
    ex = simulate_exit_short(p["high"], p["low"], p["close"], p["last_bar"], i, entry)
    if ex is None:
        return None
    _, reason, exit_price = ex
    shares = int(sb.POSITION_SIZE_USD // entry)
    gross = shares * (entry - exit_price)
    cps, _ = sb.measured_cost_per_share(symbol, entry, spreads)
    cost = shares * cps + sb.COMMISSION_PER_TRADE
    return {"gross": gross, "net": gross - cost, "reason": reason}


def valid_entry(p, i0, d):
    """Entry d minutes after bar i0 must exist, be the same day and not be the
    last bar of the day."""
    j = i0 + d
    return (j < len(p["close"]) and p["day"][j] == p["day"][i0]
            and not (sb.FLATTEN_AT_CLOSE and p["last_bar"][j]))


def paired_vs_first(rows_d, rows_0):
    """Mean and standard error of (this delay - delay 0) on signals present in both."""
    diffs = [a["gross"] - b["gross"] for a, b in zip(rows_d, rows_0)]
    n = len(diffs)
    if n < 2:
        return None, None
    m = sum(diffs) / n
    se = (sum((x - m) ** 2 for x in diffs) / (n - 1)) ** 0.5 / n ** 0.5
    return round(m, 3), round(se, 3)


def delay_and_mirror(real, prepared, spreads):
    """Delay sweep (long) and mirror-short test on the real signals."""
    sweep = {}
    for d in DELAYS:
        rows, base = [], []
        for tr in real:
            p = prepared[tr["symbol"]]
            if not valid_entry(p, tr["i"], d):
                continue
            r = result_for(p, tr["symbol"], tr["i"] + d, spreads)
            r0 = result_for(p, tr["symbol"], tr["i"], spreads)
            if r and r0:
                rows.append(r)
                base.append(r0)
        if rows:
            row = summarize_real(rows)
            row["paired_gross_diff_vs_signal_minute"], row["paired_std_error"] = (
                paired_vs_first(rows, base) if d else (0.0, None))
            sweep[f"+{d} min"] = row
    shorts = []
    for tr in real:
        r = result_short(prepared[tr["symbol"]], tr["symbol"], tr["i"], spreads)
        if r:
            shorts.append(r)
    mirror = summarize_real(shorts) if shorts else None
    return sweep, mirror


def pct(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, max(0, int(q * (len(xs) - 1))))]


def summarize_real(rs):
    n = len(rs)
    return {
        "trades": n,
        "avg_gross": round(sum(r["gross"] for r in rs) / n, 3),
        "avg_net": round(sum(r["net"] for r in rs) / n, 3),
        "win_rate_pct": round(100 * sum(1 for r in rs if r["net"] > 0) / n, 1),
        "target_rate_pct": round(100 * sum(1 for r in rs if r["reason"] == "target") / n, 1),
        "stop_rate_pct": round(100 * sum(1 for r in rs if r["reason"] == "stop") / n, 1),
    }


def main():
    spreads = sb.load_measured_spreads()
    tradable, blocked = sb.apply_cost_gate(sb.CANDIDATES, spreads)
    print(f"Cost gate: {len(tradable)} of {len(sb.CANDIDATES)} candidate(s) allowed.",
          file=sys.stderr)
    bars = sb.fetch_1m_bars(list(tradable))
    if not bars:
        print("No data fetched -- nothing to do.", file=sys.stderr)
        return

    prepared, real = {}, []
    for sym, df in bars.items():
        if sym not in tradable:
            continue
        p = prepare(df)
        prepared[sym] = p
        for t in sb.find_trades(sym, df, mode="fixed", spy_ctx=None, spreads=spreads):
            i = p["pos"].get(t["entry_time"])
            r = result_for(p, sym, i, spreads) if i is not None else None
            if r:
                real.append({"symbol": sym, "i": i, **r})
    if not real:
        print("No real signals in the current window.", file=sys.stderr)
        return

    # Exit result for EVERY eligible minute, once (draws are then lookups).
    table = {}
    for sym, p in prepared.items():
        table[sym] = {i: result_for(p, sym, i, spreads) for i in eligible(p)}
        table[sym] = {i: r for i, r in table[sym].items() if r}

    def pool(tr, window):
        p, sym = prepared[tr["symbol"]], tr["symbol"]
        out = [i for i in table[sym]
               if p["day"][i] == p["day"][tr["i"]]
               and (window is None or abs(p["minute"][i] - p["minute"][tr["i"]]) <= window)]
        return out or [tr["i"]]

    rng = random.Random(SEED)
    versions = {"A_same_symbol_day": None, "B_within_15_min": WINDOW_MINUTES}
    pools = {name: [pool(tr, w) for tr in real] for name, w in versions.items()}

    real_s = summarize_real(real)
    out = {
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "data_window": f"{min(p['idx'][0] for p in prepared.values()).date()}"
                       f" to {max(p['idx'][-1] for p in prepared.values()).date()}",
        "symbols": sorted(prepared), "draws": DRAWS, "seed": SEED,
        "real_signals": real_s, "random": {},
    }
    for name, plist in pools.items():
        g_means, n_means, wins, tgts = [], [], [], []
        for _ in range(DRAWS):
            picks = []
            for tr, cand in zip(real, plist):
                r = table[tr["symbol"]].get(rng.choice(cand))
                if r:
                    picks.append(r)
            if not picks:
                continue
            g_means.append(sum(r["gross"] for r in picks) / len(picks))
            n_means.append(sum(r["net"] for r in picks) / len(picks))
            wins.append(100 * sum(1 for r in picks if r["net"] > 0) / len(picks))
            tgts.append(100 * sum(1 for r in picks if r["reason"] == "target") / len(picks))
        p_gross = (1 + sum(1 for g in g_means if g >= real_s["avg_gross"])) / (len(g_means) + 1)
        out["random"][name] = {
            "avg_gross_mean": round(sum(g_means) / len(g_means), 3),
            "avg_gross_5th_95th": [round(pct(g_means, .05), 3), round(pct(g_means, .95), 3)],
            "avg_net_mean": round(sum(n_means) / len(n_means), 3),
            "win_rate_pct_mean": round(sum(wins) / len(wins), 1),
            "target_rate_pct_mean": round(sum(tgts) / len(tgts), 1),
            "p_value_real_gross_beats_random": round(p_gross, 3),
        }

    sweep, mirror = delay_and_mirror(real, prepared, spreads)
    out["delay_sweep_long"] = sweep
    out["mirror_short_at_signal"] = mirror
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    lines = [
        "# Random-entry baseline", "",
        f"Generated {out['generated_utc']}. {len(real)} real signals vs {DRAWS} random draws "
        f"(same symbols and days, same exits and sizing). Symbols: {', '.join(out['symbols'])}.", "",
        "| | Avg gross / trade | Avg net / trade | Win % | Target hit % |", "|---|---|---|---|---|",
        f"| Real signals | ${real_s['avg_gross']} | ${real_s['avg_net']} | "
        f"{real_s['win_rate_pct']} | {real_s['target_rate_pct']} |",
    ]
    for name, r in out["random"].items():
        lines.append(f"| Random: {name} | ${r['avg_gross_mean']} (5-95%: "
                     f"{r['avg_gross_5th_95th'][0]} to {r['avg_gross_5th_95th'][1]}) | "
                     f"${r['avg_net_mean']} | {r['win_rate_pct_mean']} | {r['target_rate_pct_mean']} |")
    lines += ["", "p-value = share of random draws whose average gross was at least as good as the "
              "real signals' (small = the signal beat random timing):"]
    for name, r in out["random"].items():
        lines.append(f"- {name}: p = {r['p_value_real_gross_beats_random']}")
    lines += ["", "## Delay sweep (long, same exits): enter N minutes AFTER the signal", "",
              "| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |",
              "|---|---|---|---|---|---|---|"]
    for name, r in sweep.items():
        diff = r["paired_gross_diff_vs_signal_minute"]
        se = r["paired_std_error"]
        lines.append(f"| {name} | {r['trades']} | ${r['avg_gross']} | ${r['avg_net']} | "
                     f"{r['win_rate_pct']} | {r['target_rate_pct']} | "
                     f"{'-' if se is None else f'{diff:+} (+/- {se})'} |")
    if mirror:
        lines += ["", "## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)", "",
                  f"{mirror['trades']} trades: avg gross ${mirror['avg_gross']}, avg net "
                  f"${mirror['avg_net']}, win {mirror['win_rate_pct']}%, target {mirror['target_rate_pct']}%."]
    lines += ["", "Read it as: if the real average gross sits inside the random 5-95% range, the "
              "entry signal is adding nothing beyond the exit rules. Small sample: this can show "
              "'no edge' far more easily than it can prove one."]
    with open(OUT_MD, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines), file=sys.stderr)


if __name__ == "__main__":
    main()
