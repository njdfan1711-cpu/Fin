#!/usr/bin/env python3
"""
Trade drawdown report.

Reads open_positions.json (the Fin Trade Log export, closed AND open trades),
pulls daily price bars, and writes trade_drawdown_report.md showing, per trade:

  * the worst dip below the entry price while the trade was held
  * how many closes finished below entry ("days underwater")
  * where Fin's stop would have been (entry - STOP_ATR_MULT x ATR) and
    whether the price ever traded down to it
  * final result (exit price, or latest close for open positions)

Purpose: your closed trades are all wins, but holding through a dip keeps a
would-be loss "open" instead of recorded. This shows how deep each win dipped
first, and whether Fin's stop would have fired on any of them.

Conservative method (daily bars can't show intraday order of events):
  * entry day and exit day use that day's CLOSE only (the low of those days may
    have happened before you bought or after you sold);
  * days strictly between entry and exit use the daily LOW.
This slightly UNDERSTATES the worst dip, never overstates it.

Run (GitHub): Actions tab -> "Trade drawdown report" -> Run workflow.
Run (PC):     python trade_drawdown_report.py
"""

import json
import os
import sys
from datetime import date, datetime, timedelta

import pandas as pd
import yfinance as yf

try:
    from config import STOP_ATR_MULT, ATR_PERIOD
except Exception:  # config missing or changed: fall back to Fin's current defaults
    STOP_ATR_MULT, ATR_PERIOD = 1.5, 14

HERE = os.path.dirname(os.path.abspath(__file__))
POSITIONS_FILE = os.path.join(HERE, "open_positions.json")
REPORT_FILE = os.path.join(HERE, "trade_drawdown_report.md")
LOOKBACK_DAYS_FOR_ATR = 60   # calendar days of history before entry (covers 14 bars)


def flatten(df):
    if isinstance(df.columns, pd.MultiIndex):
        df = df.copy()
        df.columns = df.columns.get_level_values(0)
    return df


def fetch_bars(symbol, start, end):
    """Daily bars with one retry. Returns a DataFrame (may be empty)."""
    for attempt in (1, 2):
        try:
            df = yf.download(symbol, start=start.isoformat(), end=end.isoformat(),
                             interval="1d", progress=False, auto_adjust=False)
            df = flatten(df)
            if df is not None and not df.empty and "Close" in df.columns:
                df = df.dropna(subset=["High", "Low", "Close"])
                df.index = pd.to_datetime(df.index).tz_localize(None).normalize()
                return df
        except Exception as e:
            print(f"[{symbol}] download attempt {attempt} failed: {e}", file=sys.stderr)
    return pd.DataFrame()


def atr_before(df, entry_ts, period=ATR_PERIOD):
    """Fin's ATR (rolling mean of true range) using only bars BEFORE entry day."""
    hist = df[df.index < entry_ts]
    if len(hist) <= period:
        return None
    prev_close = hist["Close"].shift(1)
    tr = pd.concat([hist["High"] - hist["Low"],
                    (hist["High"] - prev_close).abs(),
                    (hist["Low"] - prev_close).abs()], axis=1).max(axis=1)
    val = tr.rolling(period).mean().iloc[-1]
    return float(val) if pd.notna(val) else None


def analyze(trade, today):
    sym = trade["symbol"]
    entry = float(trade["entryPrice"])
    shares = float(trade["shares"])
    is_closed = trade.get("status") == "closed"
    out = {"symbol": sym, "entry": entry, "shares": shares, "closed": is_closed,
           "entry_date": trade.get("entryDate") or "", "exit_date": trade.get("exitDate") or ""}

    if not out["entry_date"]:
        out["note"] = "entry date missing in log"
        return out
    entry_ts = pd.Timestamp(out["entry_date"])
    exit_ts = pd.Timestamp(out["exit_date"]) if (is_closed and out["exit_date"]) else None

    start = entry_ts.date() - timedelta(days=LOOKBACK_DAYS_FOR_ATR)
    end = (exit_ts.date() if exit_ts is not None else today) + timedelta(days=3)
    df = fetch_bars(sym, start, end)
    if df.empty:
        out["note"] = "price data unavailable"
        return out

    last_ts = exit_ts if exit_ts is not None else df.index.max()
    window = df[(df.index >= entry_ts) & (df.index <= last_ts)]
    if window.empty:
        out["note"] = "no price bars in holding window yet"
        out["hold_days"] = 0
        return out

    # conservative path of prices: closes on entry/exit days, lows in between
    lows, closes = [], []
    for ts, row in window.iterrows():
        closes.append(float(row["Close"]))
        is_edge = (ts == entry_ts) or (exit_ts is not None and ts == exit_ts)
        lows.append(float(row["Close"]) if is_edge else float(row["Low"]))
    worst = min(lows)
    worst_ts = window.index[lows.index(worst)]
    out["worst_dip_pct"] = min(0.0, (worst / entry - 1) * 100)
    out["worst_dip_usd"] = min(0.0, (worst - entry) * shares)
    out["worst_date"] = worst_ts.date().isoformat()
    out["days_underwater"] = sum(1 for c in closes[1:] if c < entry)  # closes after entry day
    out["hold_days"] = (last_ts.date() - entry_ts.date()).days

    if is_closed and trade.get("exitPrice") is not None:
        final = float(trade["exitPrice"])
        out["final_label"] = "exit"
    else:
        final = float(window["Close"].iloc[-1])
        out["final_label"] = "latest close"
    out["final_pct"] = (final / entry - 1) * 100
    out["final_usd"] = (final - entry) * shares

    atr = atr_before(df, entry_ts)
    if atr is not None:
        stop = entry - STOP_ATR_MULT * atr
        out["stop"] = stop
        out["stop_pct"] = (stop / entry - 1) * 100
        out["stop_hit"] = worst <= stop
    else:
        out["note"] = "not enough history to compute ATR/stop"
    return out


def fmt_pct(x):
    return "" if x is None else f"{x:+.1f}%"


def fmt_usd(x):
    return "" if x is None else (f"-${abs(x):,.0f}" if x < 0 else f"+${x:,.0f}")


def fmt_dip(x):
    return "none" if x >= -0.05 else f"{x:.1f}%"


def fmt_dip_usd(x):
    return "$0" if x > -0.5 else f"-${abs(x):,.0f}"


def build_report(results, generated):
    lines = ["# Trade drawdown report", "",
             f"Generated {generated}. Source: open_positions.json (Fin Trade Log) + Yahoo daily bars.", "",
             f"Stop used: entry minus {STOP_ATR_MULT} x ATR({ATR_PERIOD}) as of the day before entry "
             "(Fin's default plan, not your actual stop).", ""]

    closed = [r for r in results if r["closed"] and "worst_dip_pct" in r]
    opened = [r for r in results if not r["closed"] and "worst_dip_pct" in r]
    skipped = [r for r in results if "worst_dip_pct" not in r]

    if closed:
        dips = [r["worst_dip_pct"] for r in closed]
        wins_with_stop = [r for r in closed if r.get("stop_hit")]
        lines += ["## Summary (closed trades with enough data)", "",
                  f"- Trades analyzed: {len(closed)} of {len([r for r in results if r['closed']])} closed",
                  f"- Dipped below entry at some point: {sum(1 for d in dips if d < 0)}",
                  f"- Dipped 2% or more: {sum(1 for d in dips if d <= -2)}; "
                  f"3% or more: {sum(1 for d in dips if d <= -3)}; "
                  f"5% or more: {sum(1 for d in dips if d <= -5)}",
                  f"- Median worst dip: {fmt_dip(sorted(dips)[len(dips)//2])}; deepest: {fmt_dip(min(dips))}",
                  f"- **Trades where Fin's stop level was reached before you exited: {len(wins_with_stop)}**",
                  f"- Closed with a gain: {sum(1 for r in closed if r['final_usd'] > 0)} of {len(closed)}", ""]
        if wins_with_stop:
            lines += ["Stop reached on: " + ", ".join(r["symbol"] for r in wins_with_stop) +
                      ". On those, holding past Fin's stop turned a would-be loss into a win.", ""]

    def table(rows):
        t = ["| Symbol | Entry | Exit / now | Held (cal. days) | Worst dip | $ at worst | Closes under entry | Stop level | Stop reached? | Result |",
             "|---|---|---|---|---|---|---|---|---|---|"]
        for r in rows:
            stop = "" if "stop" not in r else f"${r['stop']:.2f} ({r['stop_pct']:+.1f}%)"
            reached = "" if "stop_hit" not in r else ("YES" if r["stop_hit"] else "no")
            end = r["exit_date"] if r["closed"] else "open"
            t.append(f"| {r['symbol']} | {r['entry_date']} @ ${r['entry']:.2f} | {end} | {r['hold_days']} | "
                     f"{fmt_dip(r['worst_dip_pct'])} ({r['worst_date']}) | {fmt_dip_usd(r['worst_dip_usd'])} | "
                     f"{r['days_underwater']} | {stop} | {reached} | "
                     f"{fmt_pct(r['final_pct'])} {fmt_usd(r['final_usd'])} ({r['final_label']}) |")
        return t

    if closed:
        lines += ["## Closed trades", ""] + table(sorted(closed, key=lambda r: r["entry_date"])) + [""]
    if opened:
        lines += ["## Open positions (marked to latest close)", ""] + table(opened) + [""]
    if skipped:
        lines += ["## Not analyzed", ""]
        for r in skipped:
            lines.append(f"- {r['symbol']}: {r.get('note', 'unknown reason')}")
        lines.append("")

    lines += ["## How to read this", "",
              "- Daily bars can't show intraday order, so entry and exit days use closes only; "
              "the real worst dip may be slightly deeper than shown.",
              "- 'Stop reached' compares the lowest price while held to Fin's default stop. "
              "If you set a different stop, the answer changes.",
              "- A closed-trade win rate counts only trades that recovered. "
              "Check the open positions too.", ""]
    return "\n".join(lines)


def main():
    if not os.path.exists(POSITIONS_FILE):
        print(f"{POSITIONS_FILE} not found", file=sys.stderr)
        return 1
    with open(POSITIONS_FILE) as f:
        trades = json.load(f).get("trades", [])
    today = date.today()
    results = []
    for t in trades:
        try:
            results.append(analyze(t, today))
        except Exception as e:   # one bad trade must not stop the report
            results.append({"symbol": t.get("symbol", "?"), "closed": t.get("status") == "closed",
                            "note": f"error: {e}"})
            print(f"[{t.get('symbol')}] error: {e}", file=sys.stderr)
    report = build_report(results, datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"))
    with open(REPORT_FILE, "w") as f:
        f.write(report)
    print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
