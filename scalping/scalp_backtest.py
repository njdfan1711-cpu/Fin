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
    "SOFI", "SMCI", "NIO", "SNAP", "PATH",
    # Added 2026-10-02: more liquid large/mid-priced names plus SPY/QQQ
    # as tight-spread benchmarks, to widen the sample.
    "AMD", "MSFT", "META", "GOOGL", "AVGO", "NFLX", "MU", "PLTR",
    "COIN", "HOOD", "UBER", "JPM", "XOM", "SPY", "QQQ",
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

# --- Trailing-stop variant (run side by side with the fixed target on
# the SAME entries, results kept in separate files so the original
# history stays comparable) ---
# No fixed profit target. The initial stop (SCALP_STOP_PCT) applies until
# price has risen TRAIL_ARM_PCT above entry; from then on the stop trails
# TRAIL_PCT below the highest high seen, and never drops below the
# initial stop. The time-stop still applies.
TRAIL_ARM_PCT = 0.175              # roughly half of SCALP_TARGET_PCT
TRAIL_PCT = 0.15                   # trail distance below the high-water mark

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

# --- Measured-spread cost model (added 2026-10) ---
# measured_spreads.csv (next to this script) holds each symbol's measured
# median bid/ask spread as a % of price, produced by spread_report.py from
# the local spread_logger.py data. Summaries re-cost EVERY accumulated trade
# from its gross P&L using these numbers:
#   cost per share = max(MIN_TICK_COST, entry_price x median_pct / 100) x multiplier
# Symbols with no measured data fall back to SCALP_ASSUMED_SPREAD_CENTS and
# are listed in the summary. The cost/net_pnl columns in the trades CSVs
# stay on the OLD flat-cents model so older and newer rows are consistent;
# the summary JSON is where the measured-cost results live.
MEASURED_SPREADS_FILE = "measured_spreads.csv"
MIN_TICK_COST = 0.01               # one-cent minimum tick per share
SPREAD_COST_MULTIPLIER = 1.0       # e.g. 1.5 to stress-test (stops/fast markets cost more)
TIGHT_SPREAD_PCT = 0.03            # tier boundary used in the summary

# --- Cost gate (added 2026-10-19) -----------------------------------------
# A symbol is only traded if its measured round-trip spread is a small
# fraction of the profit target. Why: through 2026-10-19 the wide-spread
# names lost money almost entirely to cost (trades costing >0.10% of
# notional: gross -$105, cost $282, net -$387 over 38 trades), and NIO's
# spread alone was ~83% of the 0.35% target. This replaces hand-removing
# tickers one at a time: any symbol that fails the rule is skipped
# automatically, including ones added to CANDIDATES later.
#   max spread % = SCALP_TARGET_PCT x MAX_SPREAD_TARGET_RATIO  (0.35 x 0.15 = 0.0525%)
# Symbols with no measured spread are skipped too (cost unknown), unless
# SKIP_UNMEASURED_SYMBOLS is False. The gate is a COST rule only -- entry
# and exit logic are unchanged. SPY is always fetched for market context
# even if it were gated out. Set COST_GATE_ENABLED = False to restore the
# old behaviour. NOTE: this is not a profitability fix by itself; the
# remaining ungated trades were still about break-even-to-negative.
COST_GATE_ENABLED = True
MAX_SPREAD_TARGET_RATIO = 0.15
MAX_SPREAD_PCT = SCALP_TARGET_PCT * MAX_SPREAD_TARGET_RATIO
SKIP_UNMEASURED_SYMBOLS = True

# --- Day-boundary fixes (added 2026-10-20) ---------------------------------
# Before this, momentum, the 20-bar volume average and the VWAP-cross check
# ran straight across the overnight gap, so at 9:30 the "3-minute momentum"
# was mostly yesterday's close -> today's gap, and the "volume spike" was
# the opening bar vs yesterday's quiet last minutes. Positions could also
# roll overnight (16 stored trades "exited" at the next day's 9:30 at the
# stop/target price, ignoring the gap). Fixes:
#   * every indicator is computed within one trading day only;
#   * no entry until MIN_MINUTES_AFTER_OPEN (= a full 20-bar same-day window);
#   * no entry on the last bar of the day, and any open position is closed
#     at that bar's close ("eod") -- the live bot is flat at the close.
# Stored trades that violate these rules are ignored when summarizing and
# when simulating the account (see row_is_valid); trades that follow them
# are unchanged, so earlier history stays usable.
MIN_MINUTES_AFTER_OPEN = 20
FLATTEN_AT_CLOSE = True
LAST_BAR_MINUTE = 389              # the 15:59 bar, in minutes after 9:30

# --- Account simulation (added 2026-10-20) ---------------------------------
# The per-symbol backtest above treats every symbol as its own account, so
# several symbols can be "in a trade" at once. The live bot holds ONE
# position at a time. The account simulation replays the stored signals
# under that rule: when flat, take a signal; ignore signals while a trade is
# open; if several fire in the same minute, take the best-ranked one.
# RANK_MODE is a declared hypothesis, not a tuned result:
#   "least_extended" -- smallest recent run-up first (the 30-minute move,
#                       or the move since the open when the 30-minute move
#                       is not available yet), then tighter spread, then
#                       symbol. Mirrors "avoid names that already ran".
#   "lowest_spread"  -- tightest measured spread first (for comparison).
# Do NOT tune this on the existing sample; judge it forward using the
# picked-vs-outranked numbers in scalp_account_summary.json.
ACCOUNT_SIM_ENABLED = True
RANK_MODE = "least_extended"
ACCOUNT_MAX_ENTRIES_PER_DAY = 40   # live circuit breaker
ACCOUNT_TRADES_FILE = "scalp_account_trades.csv"
ACCOUNT_SKIPPED_FILE = "scalp_account_skipped.csv"
ACCOUNT_SUMMARY_FILE = "scalp_account_summary.json"

# --- Signal tagging (added 2026-10) ---
# Every entry is recorded with the market conditions at that moment, so
# candidate rules from IDEAS.md (skip open/close, avoid SPY-down, skip
# over-extended, volatility-scaled exits...) can be judged AFTER the fact by
# what the trades they would have removed actually earned -- without adding
# any rule to the strategy. analyze_tags.py does that analysis. One row per
# (mode, symbol, entry_time); trades older than yfinance's 7-day window
# cannot be tagged retroactively, so tagging starts from the first run.
TAGS_FILE = "scalp_signals_tagged.csv"
TAG_FIELDS = [
    "mode", "symbol", "entry_time", "entry_price", "shares", "exit_reason",
    "held_minutes", "gross_pnl",
    "minutes_since_open", "vwap_dist_pct", "mom3_pct", "volume_ratio",
    "range20_pct", "ret15_pct", "ext30_pct", "ext_from_open_pct",
    "spy_ret_open_pct", "spy_ret_15m_pct", "spy_vs_vwap_pct", "rs15_vs_spy_pct",
    "spread_pct", "max_up_pct", "max_down_pct",
    # added 2026-10-20 (blank for older rows until they are re-found):
    "gap_open_pct", "range_to_stop", "dist_from_day_high_pct", "burst_pct",
    "minutes_to_close", "weekday",
]

TRADES_FILE = "scalp_backtest_trades.csv"
SUMMARY_FILE = "scalp_backtest_summary.json"
TRAIL_TRADES_FILE = "scalp_backtest_trail_trades.csv"
TRAIL_SUMMARY_FILE = "scalp_backtest_trail_summary.json"


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


def _num(x, nd=4):
    """Round a number for the tags file; blank if missing/NaN."""
    try:
        if x is None or pd.isna(x):
            return ""
        return round(float(x), nd)
    except (TypeError, ValueError):
        return ""


def _minutes_since_open(ts) -> int:
    """Minutes after 9:30 AM Eastern for a bar timestamp."""
    try:
        if ts.tzinfo is not None:
            ts = ts.tz_convert("America/New_York")
    except (AttributeError, TypeError):
        pass
    return int(ts.hour * 60 + ts.minute - (9 * 60 + 30))


def build_spy_context(spy_df):
    """Per-minute SPY market context (None if SPY data is unavailable)."""
    if spy_df is None or spy_df.empty:
        return None
    ctx = pd.DataFrame(index=spy_df.index)
    day = spy_df.index.date
    vwap = compute_session_vwap(spy_df)
    ctx["spy_vs_vwap_pct"] = (spy_df["Close"] / vwap - 1) * 100
    day_open = spy_df["Open"].groupby(day).transform("first")
    ctx["spy_ret_open_pct"] = (spy_df["Close"] / day_open - 1) * 100
    ctx["spy_ret_15m_pct"] = spy_df["Close"].groupby(day).pct_change(15, fill_method=None) * 100
    return ctx


def find_trades(symbol: str, df: pd.DataFrame, mode: str = "fixed",
                spy_ctx=None, spreads=None) -> list[dict]:
    """Walks the bar series looking for entries per the strategy rules
    above, then simulates the exit for each one. Returns a list of
    trade dicts -- one per completed trade."""
    df = df.copy()
    df["vwap"] = compute_session_vwap(df)
    day_key = df.index.date
    # All indicators are computed WITHIN one trading day (see the
    # day-boundary note near the top of this file).
    df["avg_vol20"] = df["Volume"].groupby(day_key).transform(
        lambda s: s.rolling(20, min_periods=20).mean())
    df["mom3"] = df["Close"].groupby(day_key).pct_change(3, fill_method=None) * 100
    # Extra context columns used only for tagging (no effect on entries/exits).
    df["ret15"] = df["Close"].groupby(day_key).pct_change(15, fill_method=None) * 100
    df["ret30"] = df["Close"].groupby(day_key).pct_change(30, fill_method=None) * 100
    df["day_open"] = df["Open"].groupby(day_key).transform("first")
    df["range20"] = (((df["High"] - df["Low"]) / df["Close"] * 100)
                     .groupby(day_key).transform(lambda s: s.rolling(20, min_periods=10).mean()))
    spreads = spreads or {}

    # True on the final bar of each trading day. The last bar of the data
    # only counts if it is the 15:59 bar, so a mid-session run does not
    # invent end-of-day exits for the still-forming day.
    day_list = list(day_key)
    n_bars = len(df)
    last_bar = [
        (day_list[i + 1] != day_list[i]) if i < n_bars - 1
        else _minutes_since_open(df.index[i]) >= LAST_BAR_MINUTE
        for i in range(n_bars)
    ]

    # More context columns, for tagging only (no effect on entries/exits).
    prev_close_by_day = df["Close"].groupby(day_key).last().shift(1)
    df["prev_close"] = [prev_close_by_day.get(d) for d in day_list]
    df["day_high"] = df["High"].groupby(day_key).cummax()
    df["low10"] = df["Low"].groupby(day_key).transform(
        lambda s: s.rolling(10, min_periods=5).min())

    trades = []
    entry_tags = {}
    in_position = False
    entry_idx = None
    entry_price = None
    high_water = None

    for i in range(20, len(df)):
        row = df.iloc[i]
        prev = df.iloc[i - 1]

        if in_position:
            bars_held = i - entry_idx
            target_price = entry_price * (1 + SCALP_TARGET_PCT / 100)
            stop_price = entry_price * (1 - SCALP_STOP_PCT / 100)
            exit_reason = None
            exit_price = None

            if mode == "trail":
                # Ordering within a 1-minute bar is unknowable, so this
                # takes the pessimistic read: if the stop was not yet
                # trailing and the bar's low touched the initial stop,
                # that is a loss; once trailing, the bar's high is
                # assumed to come first, then the low tests the new trail.
                arm_price = entry_price * (1 + TRAIL_ARM_PCT / 100)
                was_armed = high_water >= arm_price
                if not was_armed and row["Low"] <= stop_price:
                    exit_reason, exit_price = "stop", stop_price
                else:
                    high_water = max(high_water, row["High"])
                    if high_water >= arm_price:
                        trail_stop = max(stop_price, high_water * (1 - TRAIL_PCT / 100))
                        if row["Low"] <= trail_stop:
                            exit_reason, exit_price = "trail_stop", trail_stop
                    if not exit_reason and bars_held >= SCALP_MAX_HOLD_MINUTES:
                        exit_reason, exit_price = "time_stop", row["Close"]
                    if not exit_reason and FLATTEN_AT_CLOSE and last_bar[i]:
                        exit_reason, exit_price = "eod", row["Close"]
            elif row["High"] >= target_price:
                exit_reason, exit_price = "target", target_price
            elif row["Low"] <= stop_price:
                exit_reason, exit_price = "stop", stop_price
            elif bars_held >= SCALP_MAX_HOLD_MINUTES:
                exit_reason, exit_price = "time_stop", row["Close"]
            elif FLATTEN_AT_CLOSE and last_bar[i]:
                exit_reason, exit_price = "eod", row["Close"]

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
                    "tags": {
                        **entry_tags,
                        "max_up_pct": _num((df["High"].iloc[entry_idx + 1:i + 1].max()
                                            / entry_price - 1) * 100),
                        "max_down_pct": _num((df["Low"].iloc[entry_idx + 1:i + 1].min()
                                              / entry_price - 1) * 100),
                    },
                })
                in_position = False
            continue

        # Not in a position -- look for an entry.
        if pd.isna(row["vwap"]) or pd.isna(row["avg_vol20"]) or pd.isna(row["mom3"]):
            continue
        if _minutes_since_open(df.index[i]) < MIN_MINUTES_AFTER_OPEN:
            continue
        if FLATTEN_AT_CLOSE and last_bar[i]:
            continue
        crossed_above_vwap = prev["Close"] <= prev["vwap"] and row["Close"] > row["vwap"]
        momentum_ok = row["mom3"] >= SCALP_MOMENTUM_PCT_MIN
        volume_ok = row["avg_vol20"] > 0 and row["Volume"] >= SCALP_VOLUME_MULT * row["avg_vol20"]

        if crossed_above_vwap and momentum_ok and volume_ok:
            in_position = True
            entry_idx = i
            entry_price = row["Close"]
            high_water = entry_price
            ts = df.index[i]
            spy_now = {}
            if spy_ctx is not None:
                try:
                    spy_now = (spy_ctx.loc[ts] if ts in spy_ctx.index
                               else spy_ctx.loc[:ts].iloc[-1]).to_dict()
                except (KeyError, IndexError):
                    spy_now = {}
            rs15 = (row["ret15"] - spy_now["spy_ret_15m_pct"]
                    if spy_now and not pd.isna(row["ret15"])
                    and not pd.isna(spy_now.get("spy_ret_15m_pct")) else None)
            entry_tags = {
                "minutes_since_open": _minutes_since_open(ts),
                "vwap_dist_pct": _num((row["Close"] / row["vwap"] - 1) * 100),
                "mom3_pct": _num(row["mom3"]),
                "volume_ratio": _num(row["Volume"] / row["avg_vol20"], 3),
                "range20_pct": _num(row["range20"]),
                "ret15_pct": _num(row["ret15"]),
                "ext30_pct": _num(row["ret30"]),
                "ext_from_open_pct": _num((row["Close"] / row["day_open"] - 1) * 100),
                "spy_ret_open_pct": _num(spy_now.get("spy_ret_open_pct")),
                "spy_ret_15m_pct": _num(spy_now.get("spy_ret_15m_pct")),
                "spy_vs_vwap_pct": _num(spy_now.get("spy_vs_vwap_pct")),
                "rs15_vs_spy_pct": _num(rs15),
                "spread_pct": _num(spreads.get(symbol)),
                # gap at the open vs yesterday's close (a "gap-and-go" day?)
                "gap_open_pct": _num((row["day_open"] / row["prev_close"] - 1) * 100),
                # recent 1-minute range relative to the stop distance
                # (> 1 = the stop sits inside normal noise)
                "range_to_stop": _num(row["range20"] / SCALP_STOP_PCT, 3),
                # 0 = entering at the high of the day so far
                "dist_from_day_high_pct": _num((row["day_high"] / row["Close"] - 1) * 100),
                # how far it has already bounced off the last 10 minutes' low
                # (large = buying after the burst)
                "burst_pct": _num((row["Close"] / row["low10"] - 1) * 100),
                "minutes_to_close": (LAST_BAR_MINUTE + 1) - _minutes_since_open(ts),
                "weekday": ts.weekday(),
            }

    return trades


def load_measured_spreads() -> dict:
    """symbol -> median spread as % of price. Empty dict if file missing."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), MEASURED_SPREADS_FILE)
    table = {}
    if not os.path.exists(path):
        print(f"{MEASURED_SPREADS_FILE} not found -- using the flat "
              f"{SCALP_ASSUMED_SPREAD_CENTS}c model for everything.", file=sys.stderr)
        return table
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            try:
                table[r["symbol"].strip().upper()] = float(r["median_pct"])
            except (KeyError, ValueError):
                continue
    return table


def measured_cost_per_share(symbol: str, price: float, table: dict):
    """Returns (round-trip cost per share in dollars, True if measured)."""
    pct = table.get(symbol)
    if pct is None:
        return SCALP_ASSUMED_SPREAD_CENTS / 100, False
    return max(MIN_TICK_COST, price * pct / 100) * SPREAD_COST_MULTIPLIER, True


def apply_cost_gate(symbols: list[str], spreads: dict):
    """Splits symbols into (allowed, blocked). blocked is {symbol: reason}.
    If the spread table is empty (file missing) the gate is skipped with a
    warning rather than blocking everything."""
    if not COST_GATE_ENABLED:
        return list(symbols), {}
    if not spreads:
        print("Cost gate skipped: no measured spread data loaded.", file=sys.stderr)
        return list(symbols), {}
    allowed, blocked = [], {}
    for sym in symbols:
        pct = spreads.get(sym)
        if pct is None:
            if SKIP_UNMEASURED_SYMBOLS:
                blocked[sym] = "no measured spread"
            else:
                allowed.append(sym)
        elif pct > MAX_SPREAD_PCT:
            blocked[sym] = f"spread {pct:.4f}% > {MAX_SPREAD_PCT:.4f}% limit"
        else:
            allowed.append(sym)
    return allowed, blocked


def row_is_valid(row: dict) -> bool:
    """True if a stored trade follows the current day-boundary rules:
    entered at/after MIN_MINUTES_AFTER_OPEN, not on the last bar of the day,
    and closed on the same day. Older rows that break these rules (opening-
    bar entries that used yesterday's data, overnight holds) are ignored by
    the summaries and the account simulation, not deleted from the file."""
    try:
        e = datetime.fromisoformat(str(row["entry_time"]).strip())
        x = datetime.fromisoformat(str(row["exit_time"]).strip())
    except (KeyError, ValueError):
        return False
    minutes = e.hour * 60 + e.minute - (9 * 60 + 30)
    return (minutes >= MIN_MINUTES_AFTER_OPEN and minutes < LAST_BAR_MINUTE
            and e.date() == x.date())


def load_existing_trade_keys(path: str) -> set:
    """(symbol, entry_time) pairs already on file, so re-running this
    script as new days of data become available appends only genuinely
    new trades instead of duplicating the whole history every time.
    Rows that are not valid under the current rules are NOT counted as
    already on file, so a corrected version of the same trade can be
    appended (the old row is then ignored by row_is_valid)."""
    if not os.path.exists(path):
        return set()
    keys = set()
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            if row_is_valid(row):
                keys.add((row["symbol"], row["entry_time"]))
    return keys


def record_and_summarize(all_trades: list[dict], trades_file: str,
                         summary_file: str, label: str) -> None:
    """Appends genuinely new trades to trades_file, then writes a summary
    over the FULL accumulated file."""
    existing_keys = load_existing_trade_keys(trades_file)
    new_trades = [t for t in all_trades
                  if (t["symbol"], t["entry_time"]) not in existing_keys]

    file_exists = os.path.exists(trades_file)
    with open(trades_file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "symbol", "entry_time", "exit_time", "entry_price", "exit_price",
            "shares", "exit_reason", "held_minutes", "gross_pnl", "cost", "net_pnl",
        ], extrasaction="ignore")
        if not file_exists:
            writer.writeheader()
        for t in new_trades:
            writer.writerow(t)

    print(f"\n[{label}] {len(new_trades)} new trade(s) appended to {trades_file} "
          f"({len(all_trades) - len(new_trades)} already on file from a prior run).",
          file=sys.stderr)

    with open(trades_file, newline="") as f:
        all_rows = list(csv.DictReader(f))
    n_before = len(all_rows)
    all_rows = [r for r in all_rows if row_is_valid(r)]
    if n_before != len(all_rows):
        print(f"[{label}] Ignoring {n_before - len(all_rows)} stored trade(s) entered before "
              f"minute {MIN_MINUTES_AFTER_OPEN}, on the last bar, or held overnight "
              f"(old rules); {len(all_rows)} valid trade(s) summarized.", file=sys.stderr)

    if not all_rows:
        print(f"[{label}] No trades in the accumulated file yet.", file=sys.stderr)
        return

    spreads = load_measured_spreads()
    trades = []
    for r in all_rows:
        gross = float(r["gross_pnl"])
        shares = int(float(r["shares"]))
        cps, known = measured_cost_per_share(r["symbol"], float(r["entry_price"]), spreads)
        cost = shares * cps + COMMISSION_PER_TRADE
        trades.append({"symbol": r["symbol"], "gross": gross, "cost": cost,
                       "net": gross - cost, "known": known,
                       "pct": spreads.get(r["symbol"]),
                       "flat_net": float(r["net_pnl"])})

    net_pnls = [t["net"] for t in trades]
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

    def bucket(rows):
        return {
            "trades": len(rows),
            "gross_pnl": round(sum(t["gross"] for t in rows), 2),
            "cost": round(sum(t["cost"] for t in rows), 2),
            "net_pnl": round(sum(t["net"] for t in rows), 2),
            "avg_net_per_trade": round(sum(t["net"] for t in rows) / len(rows), 2) if rows else None,
        }

    tight = [t for t in trades if t["known"] and t["pct"] <= TIGHT_SPREAD_PCT]
    wide = [t for t in trades if t["known"] and t["pct"] > TIGHT_SPREAD_PCT]
    unknown = [t for t in trades if not t["known"]]
    # What the cost gate would allow vs block, applied to ALL stored trades
    # (including ones taken before the gate existed) so history stays comparable.
    gate_pass = [t for t in trades if t["known"] and t["pct"] <= MAX_SPREAD_PCT]
    gate_pass_ids = {id(t) for t in gate_pass}
    gate_block = [t for t in trades if id(t) not in gate_pass_ids]
    by_symbol = {}
    for t in trades:
        by_symbol.setdefault(t["symbol"], []).append(t)
    by_symbol = dict(sorted(((k, bucket(v)) for k, v in by_symbol.items()),
                            key=lambda kv: kv[1]["net_pnl"]))

    reasons = ("target", "stop", "trail_stop", "time_stop")
    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "cost_model": (f"measured median spread per symbol x{SPREAD_COST_MULTIPLIER} "
                       f"(flat {SCALP_ASSUMED_SPREAD_CENTS}c fallback)"),
        "symbols_without_spread_data": sorted({t["symbol"] for t in unknown}),
        "total_trades": len(all_rows),
        "win_count": len(wins),
        "loss_count": len(losses),
        "win_rate_pct": round(100 * len(wins) / len(all_rows), 1),
        "avg_net_pnl_per_trade": round(sum(net_pnls) / len(net_pnls), 2),
        "avg_win": round(sum(wins) / len(wins), 2) if wins else None,
        "avg_loss": round(sum(losses) / len(losses), 2) if losses else None,
        "total_gross_pnl": round(sum(t["gross"] for t in trades), 2),
        "total_cost": round(sum(t["cost"] for t in trades), 2),
        "total_net_pnl": round(sum(net_pnls), 2),
        "total_net_pnl_flat_cost_model": round(sum(t["flat_net"] for t in trades), 2),
        "max_drawdown": round(max_drawdown, 2),
        "exit_reason_counts": {
            reason: sum(1 for r in all_rows if r["exit_reason"] == reason)
            for reason in reasons
            if any(r["exit_reason"] == reason for r in all_rows)
        },
        "by_spread_tier": {
            f"tight_le_{TIGHT_SPREAD_PCT}pct": bucket(tight),
            f"wide_gt_{TIGHT_SPREAD_PCT}pct": bucket(wide),
            "no_spread_data": bucket(unknown),
        },
        "cost_gate": {
            "enabled": COST_GATE_ENABLED,
            "max_spread_pct": round(MAX_SPREAD_PCT, 4),
            "passing": bucket(gate_pass),
            "blocked": bucket(gate_block),
        },
        "by_symbol": by_symbol,
    }
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n--- {label} summary (all {len(all_rows)} accumulated trade(s)) ---", file=sys.stderr)
    for k, v in summary.items():
        print(f"  {k}: {v}", file=sys.stderr)


def _fnum(x):
    try:
        v = float(x)
        return None if v != v else v
    except (TypeError, ValueError):
        return None


def load_tag_lookup() -> dict:
    """(symbol, entry_time) -> tag row, fixed-target mode only."""
    out = {}
    if os.path.exists(TAGS_FILE):
        with open(TAGS_FILE, newline="") as f:
            for r in csv.DictReader(f):
                if r.get("mode") == "fixed":
                    out[(r["symbol"], r["entry_time"])] = r
    return out


def rank_key(sig: dict):
    """Sort key: the signal that sorts FIRST is taken. See RANK_MODE."""
    big = 9e9
    sp = sig["spread_pct"] if sig["spread_pct"] is not None else big
    if RANK_MODE == "lowest_spread":
        return (sp, sig["symbol"])
    ext = sig["ext30_pct"] if sig["ext30_pct"] is not None else sig["ext_from_open_pct"]
    return (ext if ext is not None else big, sp, sig["symbol"])


def simulate_account(signals: list[dict]):
    """Replays signals under the live rule: ONE open position at a time.
    Per day, in time order: if flat, take the best-ranked signal at that
    minute (a signal may start in the same minute the previous trade
    exited); otherwise skip. Returns (taken, skipped)."""
    by_day = {}
    for sg in signals:
        by_day.setdefault(sg["entry_time"][:10], []).append(sg)
    taken, skipped = [], []
    for day in sorted(by_day):
        free_at, entries = None, 0
        minutes = {}
        for sg in sorted(by_day[day], key=lambda x: x["entry_time"]):
            minutes.setdefault(sg["entry_time"], []).append(sg)
        for tm in sorted(minutes):
            group = sorted(minutes[tm], key=rank_key)
            if free_at is not None and tm < free_at:
                reason = "position open"
            elif entries >= ACCOUNT_MAX_ENTRIES_PER_DAY:
                reason = "daily entry limit"
            else:
                pick = group[0]
                pick["outranked"] = group[1:]
                taken.append(pick)
                entries += 1
                free_at = pick["exit_time"]
                for other in group[1:]:
                    skipped.append({**other, "skip_reason": "outranked same minute"})
                continue
            for other in group:
                skipped.append({**other, "skip_reason": reason})
    return taken, skipped


def build_account_simulation() -> None:
    """Reads the stored (valid) fixed-target trades, keeps symbols that pass
    the cost gate, replays them one position at a time, and writes the
    account-level trades, the skipped signals and a summary."""
    if not os.path.exists(TRADES_FILE):
        return
    spreads = load_measured_spreads()
    tags = load_tag_lookup()
    signals = []
    with open(TRADES_FILE, newline="") as f:
        for r in csv.DictReader(f):
            if not row_is_valid(r):
                continue
            sym = r["symbol"]
            pct = spreads.get(sym)
            if COST_GATE_ENABLED and spreads and (pct is None or pct > MAX_SPREAD_PCT):
                continue
            price, shares, gross = float(r["entry_price"]), int(float(r["shares"])), float(r["gross_pnl"])
            cps, _ = measured_cost_per_share(sym, price, spreads)
            cost = shares * cps + COMMISSION_PER_TRADE
            tg = tags.get((sym, r["entry_time"]), {})
            signals.append({
                "symbol": sym, "entry_time": r["entry_time"], "exit_time": r["exit_time"],
                "entry_price": price, "exit_price": float(r["exit_price"]),
                "shares": shares, "exit_reason": r["exit_reason"],
                "held_minutes": r["held_minutes"], "gross_pnl": gross,
                "cost": round(cost, 2), "net_pnl": round(gross - cost, 2),
                "spread_pct": pct,
                "ext30_pct": _fnum(tg.get("ext30_pct")),
                "ext_from_open_pct": _fnum(tg.get("ext_from_open_pct")),
            })
    if not signals:
        return
    taken, skipped = simulate_account(signals)

    cols = ["symbol", "entry_time", "exit_time", "entry_price", "exit_price", "shares",
            "exit_reason", "held_minutes", "gross_pnl", "cost", "net_pnl",
            "spread_pct", "ext30_pct", "ext_from_open_pct"]
    with open(ACCOUNT_TRADES_FILE, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(taken)
    with open(ACCOUNT_SKIPPED_FILE, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols + ["skip_reason"], extrasaction="ignore")
        w.writeheader()
        w.writerows(skipped)

    nets = [t["net_pnl"] for t in taken]
    days = sorted({t["entry_time"][:10] for t in signals})
    by_day = {d: round(sum(t["net_pnl"] for t in taken if t["entry_time"][:10] == d), 2)
              for d in days}
    peak = cum = worst = 0.0
    for x in nets:
        cum += x
        peak = max(peak, cum)
        worst = min(worst, cum - peak)
    ties = [t for t in taken if t["outranked"]]
    diffs = [t["net_pnl"] - sum(o["net_pnl"] for o in t["outranked"]) / len(t["outranked"])
             for t in ties]
    n = len(diffs)
    mean_d = sum(diffs) / n if n else None
    se_d = (((sum((d - mean_d) ** 2 for d in diffs) / (n - 1)) ** 0.5) / n ** 0.5
            if n > 1 else None)
    reasons = {}
    for sk in skipped:
        reasons[sk["skip_reason"]] = reasons.get(sk["skip_reason"], 0) + 1
    summary = {
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "rank_mode": RANK_MODE,
        "rules": "one position at a time; cost gate on; indicators per day; flat at close",
        "signals_available": len(signals),
        "trading_days": len(days),
        "trades_taken": len(taken),
        "trades_per_day": round(len(taken) / len(days), 2) if days else 0,
        "gross_pnl": round(sum(t["gross_pnl"] for t in taken), 2),
        "cost": round(sum(t["cost"] for t in taken), 2),
        "net_pnl": round(sum(nets), 2),
        "net_per_trade": round(sum(nets) / len(nets), 2) if nets else None,
        "win_rate_pct": round(100 * sum(1 for x in nets if x > 0) / len(nets), 1) if nets else None,
        "max_drawdown": round(worst, 2),
        "exit_reasons": {k: sum(1 for t in taken if t["exit_reason"] == k)
                         for k in sorted({t["exit_reason"] for t in taken})},
        "net_by_day": by_day,
        "skipped_by_reason": reasons,
        "picked_vs_outranked": {
            "same_minute_ties": n,
            "avg_net_difference": round(mean_d, 2) if mean_d is not None else None,
            "std_error": round(se_d, 2) if se_d is not None else None,
            "note": "Positive = the ranking's pick beat the signals it outranked. "
                    "Judge on NEW data only; need many ties before trusting it.",
        },
    }
    with open(ACCOUNT_SUMMARY_FILE, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\n[account] one position at a time, rank={RANK_MODE}: {len(taken)} trade(s) over "
          f"{len(days)} day(s) ({summary['trades_per_day']}/day), net ${summary['net_pnl']:.2f} "
          f"(${summary['net_per_trade']}/trade); {len(skipped)} signal(s) skipped "
          f"-> {ACCOUNT_TRADES_FILE}", file=sys.stderr)


def record_tags(trades: list[dict], mode: str) -> None:
    """Adds tagged rows for new trades and fills BLANK tag fields on rows that
    already exist (so columns added later get backfilled when the same signal
    is found again). Existing non-blank values are never overwritten."""
    rows, order = {}, []
    if os.path.exists(TAGS_FILE):
        with open(TAGS_FILE, newline="") as f:
            for r in csv.DictReader(f):
                k = (r["mode"], r["symbol"], r["entry_time"])
                rows[k] = r
                order.append(k)
    added = filled = 0
    for t in trades:
        k = (mode, t["symbol"], t["entry_time"])
        fresh = {"mode": mode, "symbol": t["symbol"], "entry_time": t["entry_time"],
                 "entry_price": t["entry_price"], "shares": t["shares"],
                 "exit_reason": t["exit_reason"], "held_minutes": t["held_minutes"],
                 "gross_pnl": t["gross_pnl"]}
        fresh.update(t.get("tags", {}))
        if k in rows:
            cur, changed = rows[k], False
            for fld in TAG_FIELDS:
                if cur.get(fld) in (None, "") and fresh.get(fld) not in (None, ""):
                    cur[fld] = fresh[fld]
                    changed = True
            filled += changed
        else:
            rows[k] = fresh
            order.append(k)
            added += 1
    with open(TAGS_FILE, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=TAG_FIELDS, extrasaction="ignore", restval="")
        w.writeheader()
        w.writerows(rows[k] for k in order)
    print(f"[tags/{mode}] {added} new tagged signal(s) added, {filled} existing row(s) "
          f"back-filled, in {TAGS_FILE}.", file=sys.stderr)


def main():
    spreads = load_measured_spreads()
    tradable, blocked = apply_cost_gate(CANDIDATES, spreads)
    for sym, why in blocked.items():
        print(f"  [{sym}] SKIPPED by cost gate: {why}", file=sys.stderr)
    print(f"Cost gate: {len(tradable)} of {len(CANDIDATES)} candidate(s) allowed.",
          file=sys.stderr)
    # SPY is fetched for market context even if it is not itself traded.
    to_fetch = list(tradable) + ([] if "SPY" in tradable else ["SPY"])

    print(f"Fetching 1-minute bars for {len(to_fetch)} symbol(s)...", file=sys.stderr)
    bars = fetch_1m_bars(to_fetch)
    if not bars:
        print("No data fetched for any symbol -- nothing to backtest.", file=sys.stderr)
        return

    spy_ctx = build_spy_context(bars.get("SPY"))
    if spy_ctx is None:
        print("SPY data unavailable -- SPY context tags will be blank.", file=sys.stderr)

    fixed_trades, trail_trades = [], []
    for sym, df in bars.items():
        if sym not in tradable:
            continue
        f_t = find_trades(sym, df, mode="fixed", spy_ctx=spy_ctx, spreads=spreads)
        t_t = find_trades(sym, df, mode="trail", spy_ctx=spy_ctx, spreads=spreads)
        print(f"  [{sym}] fixed: {len(f_t)} trade(s), trail: {len(t_t)} trade(s)", file=sys.stderr)
        fixed_trades.extend(f_t)
        trail_trades.extend(t_t)

    record_and_summarize(fixed_trades, TRADES_FILE, SUMMARY_FILE, "fixed target")
    record_and_summarize(trail_trades, TRAIL_TRADES_FILE, TRAIL_SUMMARY_FILE, "trailing stop")
    record_tags(fixed_trades, "fixed")
    record_tags(trail_trades, "trail")
    if ACCOUNT_SIM_ENABLED:
        build_account_simulation()


if __name__ == "__main__":
    main()
