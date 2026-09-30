"""
scalp_backtest.py

First-cut viability check for automating a scalping strategy, BEFORE any
broker integration gets built. Answers one question: does an edge big
enough to net ~$10/trade after realistic costs actually exist, on a
strategy simple enough to automate?

WHY THIS EXISTS SEPARATELY FROM THE MAIN SCREENER: everything else in
this repo (technicals_scan.py, fundamentals_scan.py, etc.) is built for
swing trades -- signals that stay valid for hours to days. Scalping
needs 1-minute-resolution price action and an entry/exit logic that
holds positions for minutes, not days. Sharing infra (yfinance, the same
config-constants-at-top style) makes sense; sharing the actual signal
logic does not -- these are different problems.

DATA LIMITATION -- READ THIS FIRST: Yahoo Finance's free tier (via
yfinance) only serves 1-minute bars for the TRAILING 7 CALENDAR DAYS.
There's no way to backtest a 1-minute strategy further back than that
without a paid data source. Two consequences:
  1. Running this script today gives you a real but SMALL first sample
     (however many trading days fall in the last 7 days).
  2. To build toward the "week or two" of validation you wanted, the
     practical path is to re-run this script every day or two over the
     next couple weeks -- each run's NEW trading day(s) get appended to
     scalp_backtest_trades.csv (de-duped by timestamp), so the sample
     grows day by day instead of needing a single giant historical pull
     that free data can't provide.

STRATEGY -- THIS IS A DELIBERATELY SIMPLE BASELINE, NOT A TUNED SYSTEM:
a VWAP-reclaim momentum burst with volume confirmation. Chosen because
it's simple enough to reason about and automate, not because it's
expected to be optimal -- the point of this first pass is "is there
ANY edge here worth building on," not "is this the final strategy."
  - LONG entry: price crosses above the day's running VWAP, WITH recent
    3-minute momentum >= SCALP_MOMENTUM_PCT_MIN, WITH this minute's
    volume >= SCALP_VOLUME_MULT x the trailing 20-minute average volume.
  - Exit: whichever hits first -- profit target, stop-loss, or a time
    stop (SCALP_MAX_HOLD_MINUTES) so a trade can't just sit open with
    no thesis playing out.
  - One open position per symbol at a time (no pyramiding). Symbols are
    evaluated independently -- this does NOT model running out of
    buying power if many symbols signal at once. Real position-sizing
    across a real account is a later problem, once/if the core edge
    checks out.

COST MODEL -- READ THIS TOO, IT'S THE MOST IMPORTANT PART: yfinance
gives OHLCV bars, not real bid/ask quotes, so there's no way to measure
the ACTUAL spread a scalp would have paid. SCALP_ASSUMED_SPREAD_CENTS
below is a placeholder, deliberately conservative-leaning, not a real
number -- treat every result from this script as optimistic until it's
been checked against real Level 1 quotes or actual (small, controlled)
live fills. This is the single biggest reason a backtest can show a
strategy "working" that then fails to work with real money: scalping
profit margins are thin enough that the spread assumption alone can be
the difference between a strategy that works and one that doesn't.
Commissions are assumed to be $0 (standard for Schwab equity trades as
of this writing) -- confirm that hasn't changed before trusting it.

NOTE: needs yfinance and outbound network access -- same requirement as
technicals_scan.py. Run this locally or in GitHub Actions, not in a
network-restricted sandbox.
"""

import csv
import json
import os
import sys
from datetime import datetime, timezone

import pandas as pd
import yfinance as yf

# --- Candidate universe -------------------------------------------------
# Deliberately restricted to well-known, heavily-traded large caps --
# scalping needs names where the spread is tight enough in absolute
# cents that it doesn't eat the whole target on its own. Pulled from
# eligible.csv's most-liquid names, then hand-trimmed to exclude names
# that are high-volume but low-priced/speculative (SPCX, GRAB, ONDS,
# BMNR, SMR, KEEL, CIFR, etc.) -- those can have deceptively wide
# spreads relative to a small scalp target even with big share volume.
# Adjust freely; this is a starting list, not a fixed universe.
CANDIDATES = [
    "NVDA", "AAPL", "TSLA", "AMZN", "INTC", "BAC", "F", "T", "AAL",
    "SOFI", "SMCI", "WBD", "NIO", "SNAP", "PATH",
]

# --- Strategy thresholds -------------------------------------------------
SCALP_MOMENTUM_PCT_MIN = 0.15      # min 3-minute % move to count as a
                                    # "burst", not just noise
SCALP_VOLUME_MULT = 2.0            # this minute's volume vs trailing
                                    # 20-min average
VWAP_LOOKBACK_RESET = "day"        # VWAP resets each trading day, standard

# --- Exit rules ------------------------------------------------------
SCALP_TARGET_PCT = 0.35            # take-profit, % above entry
SCALP_STOP_PCT = 0.20              # stop-loss, % below entry -- tighter
                                    # than the target (see reward:risk
                                    # note below)
SCALP_MAX_HOLD_MINUTES = 15        # time-stop -- exit regardless of
                                    # price if neither target nor stop
                                    # hit within this many minutes

# reward:risk here is ~1.75:1 (0.35/0.20) -- deliberately less than
# Fin's swing-trade default of 2:1 (see REWARD_RISK_RATIO in config.py),
# since scalping targets have to be reachable within minutes, not days;
# a wider target sounds better on paper but may simply never get hit
# inside SCALP_MAX_HOLD_MINUTES. Tune based on what this backtest shows.

# --- Position sizing (matches Fin's swing-trade default, for a
# comparable per-trade dollar scale -- not a specific recommendation) ---
POSITION_SIZE_USD = 3000

# --- Cost model -- SEE THE MODULE DOCSTRING, this is the part most
# likely to be wrong and most important to get right before trusting
# any result here ---
SCALP_ASSUMED_SPREAD_CENTS = 2.0   # round-trip cost in cents/share,
                                    # applied as a flat haircut per
                                    # trade -- a placeholder, not a
                                    # measured number
COMMISSION_PER_TRADE = 0.0         # Schwab equities are commission-free
                                    # as of this writing -- confirm this
                                    # is still true before trusting it

TRADES_FILE = "scalp_backtest_trades.csv"
SUMMARY_FILE = "scalp_backtest_summary.json"


def fetch_1m_bars(symbols: list[str]) -> dict[str, pd.DataFrame]:
    """Pulls the max available (7 trading days) of 1-minute bars for
    each symbol. One request per symbol rather than a batch download --
    simpler to reason about for a script meant to be read and adjusted,
    and this universe is small enough that it doesn't matter for speed."""
    out = {}
    for sym in symbols:
        try:
            df = yf.download(sym, period="7d", interval="1m", progress=False)
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            df = df.dropna()
            if df.empty:
                print(f"  [{sym}] no data returned", file=sys.stderr)
                continue
            out[sym] = df
            print(f"  [{sym}] {len(df)} 1-minute bars "
                  f"({df.index[0]} to {df.index[-1]})", file=sys.stderr)
        except Exception as e:
            print(f"  [{sym}] fetch error: {e}", file=sys.stderr)
    return out


def compute_session_vwap(df: pd.DataFrame) -> pd.Series:
    """Running VWAP that resets at the start of each trading day (each
    calendar date in the index, in exchange-local time as yfinance
    returns it)."""
    typical_price = (df["High"] + df["Low"] + df["Close"]) / 3
    pv = typical_price * df["Volume"]
    day = df.index.date
    cum_pv = pd.Series(pv, index=df.index).groupby(day).cumsum()
    cum_vol = df["Volume"].groupby(day).cumsum()
    return cum_pv / cum_vol.replace(0, float("nan"))


def find_trades(symbol: str, df: pd.DataFrame) -> list[dict]:
    """Walks the bar series looking for entries per the strategy rules
    above, then simulates the exit for each one. Returns a list of
    trade dicts -- one per completed trade."""
    df = df.copy()
    df["vwap"] = compute_session_vwap(df)
    df["avg_vol20"] = df["Volume"].rolling(20).mean()
    df["mom3"] = df["Close"].pct_change(3) * 100

    trades = []
    in_position = False
    entry_idx = None
    entry_price = None

    for i in range(20, len(df)):
        row = df.iloc[i]
        prev = df.iloc[i - 1]

        if in_position:
            bars_held = i - entry_idx
            target_price = entry_price * (1 + SCALP_TARGET_PCT / 100)
            stop_price = entry_price * (1 - SCALP_STOP_PCT / 100)
            exit_reason = None
            exit_price = None

            if row["High"] >= target_price:
                exit_reason, exit_price = "target", target_price
            elif row["Low"] <= stop_price:
                exit_reason, exit_price = "stop", stop_price
            elif bars_held >= SCALP_MAX_HOLD_MINUTES:
                exit_reason, exit_price = "time_stop", row["Close"]

            if exit_reason:
                shares = int(POSITION_SIZE_USD // entry_price)
                gross_pnl = shares * (exit_price - entry_price)
                cost = shares * (SCALP_ASSUMED_SPREAD_CENTS / 100) + COMMISSION_PER_TRADE
                net_pnl = gross_pnl - cost
                trades.append({
                    "symbol": symbol,
                    "entry_time": str(df.index[entry_idx]),
                    "exit_time": str(df.index[i]),
                    "entry_price": round(entry_price, 4),
                    "exit_price": round(exit_price, 4),
                    "shares": shares,
                    "exit_reason": exit_reason,
                    "held_minutes": bars_held,
                    "gross_pnl": round(gross_pnl, 2),
                    "cost": round(cost, 2),
                    "net_pnl": round(net_pnl, 2),
                })
                in_position = False
            continue

        # Not in a position -- look for an entry.
        if pd.isna(row["vwap"]) or pd.isna(row["avg_vol20"]) or pd.isna(row["mom3"]):
            continue
        crossed_above_vwap = prev["Close"] <= prev["vwap"] and row["Close"] > row["vwap"]
        momentum_ok = row["mom3"] >= SCALP_MOMENTUM_PCT_MIN
        volume_ok = row["avg_vol20"] > 0 and row["Volume"] >= SCALP_VOLUME_MULT * row["avg_vol20"]

        if crossed_above_vwap and momentum_ok and volume_ok:
            in_position = True
            entry_idx = i
            entry_price = row["Close"]

    return trades


def load_existing_trade_keys(path: str) -> set:
    """(symbol, entry_time) pairs already on file, so re-running this
    script as new days of data become available appends only genuinely
    new trades instead of duplicating the whole history every time."""
    if not os.path.exists(path):
        return set()
    keys = set()
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            keys.add((row["symbol"], row["entry_time"]))
    return keys


def main():
    print(f"Fetching 1-minute bars for {len(CANDIDATES)} candidate(s)...", file=sys.stderr)
    bars = fetch_1m_bars(CANDIDATES)
    if not bars:
        print("No data fetched for any symbol -- nothing to backtest.", file=sys.stderr)
        return

    all_trades = []
    for sym, df in bars.items():
        trades = find_trades(sym, df)
        print(f"  [{sym}] {len(trades)} trade(s) found", file=sys.stderr)
        all_trades.extend(trades)

    existing_keys = load_existing_trade_keys(TRADES_FILE)
    new_trades = [t for t in all_trades
                  if (t["symbol"], t["entry_time"]) not in existing_keys]

    file_exists = os.path.exists(TRADES_FILE)
    with open(TRADES_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "symbol", "entry_time", "exit_time", "entry_price", "exit_price",
            "shares", "exit_reason", "held_minutes", "gross_pnl", "cost", "net_pnl",
        ])
        if not file_exists:
            writer.writeheader()
        for t in new_trades:
            writer.writerow(t)

    print(f"\n{len(new_trades)} new trade(s) appended to {TRADES_FILE} "
          f"({len(all_trades) - len(new_trades)} already on file from a prior run).",
          file=sys.stderr)

    # Summary over the FULL accumulated file, not just this run -- so
    # the picture improves as more days accumulate over the next week
    # or two, rather than resetting each run.
    with open(TRADES_FILE, newline="") as f:
        all_rows = list(csv.DictReader(f))

    if not all_rows:
        print("No trades in the accumulated file yet.", file=sys.stderr)
        return

    net_pnls = [float(r["net_pnl"]) for r in all_rows]
    wins = [p for p in net_pnls if p > 0]
    losses = [p for p in net_pnls if p <= 0]

    equity_curve = []
    running = 0.0
    for p in net_pnls:
        running += p
        equity_curve.append(running)
    peak = float("-inf")
    max_drawdown = 0.0
    for e in equity_curve:
        peak = max(peak, e)
        max_drawdown = min(max_drawdown, e - peak)

    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_trades": len(all_rows),
        "win_count": len(wins),
        "loss_count": len(losses),
        "win_rate_pct": round(100 * len(wins) / len(all_rows), 1),
        "avg_net_pnl_per_trade": round(sum(net_pnls) / len(net_pnls), 2),
        "avg_win": round(sum(wins) / len(wins), 2) if wins else None,
        "avg_loss": round(sum(losses) / len(losses), 2) if losses else None,
        "total_net_pnl": round(sum(net_pnls), 2),
        "max_drawdown": round(max_drawdown, 2),
        "exit_reason_counts": {
            reason: sum(1 for r in all_rows if r["exit_reason"] == reason)
            for reason in ("target", "stop", "time_stop")
        },
    }
    with open(SUMMARY_FILE, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n--- Summary (all {len(all_rows)} accumulated trade(s)) ---", file=sys.stderr)
    for k, v in summary.items():
        print(f"  {k}: {v}", file=sys.stderr)


if __name__ == "__main__":
    main()
