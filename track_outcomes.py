"""
track_outcomes.py

Revisits past pushes (from daily_pushes.json) once they're at least
OUTCOME_LOOKBACK_DAYS old, and records what price actually did afterward:
did it hit the recorded trade-plan target, the recorded stop, or neither.

This is the feedback loop the system didn't have -- every threshold
(STOP_ATR_MULT, MIN_QUALIFYING_STRENGTH, the strength weights themselves)
was a reasonable-sounding guess, never checked against what actually
happened. This turns "we think this is predictive" into a measurable
record you can look back on.

Design choices, and why:
  - Reads daily_pushes.json but NEVER writes back to it. Results go to a
    SEPARATE file (outcome_history.json). Two different workflows already
    write daily_pushes.json (via record_push/prune_old_days) -- adding a
    third writer to the same file is exactly the kind of shared-mutable-
    state setup that needed a custom merge driver for signals_state.json.
    Keeping this strictly read-only on that file sidesteps the whole
    problem.
  - Each push is evaluated EXACTLY ONCE: the first run where it's old
    enough, it gets resolved and marked so in outcome_history.json, and
    is never re-fetched or re-evaluated again. Keeps API usage bounded
    and predictable regardless of how long this runs for.
  - OUTCOME_LOOKBACK_DAYS is calendar days, not trading days -- there's no
    market-calendar dependency in this codebase, and being off by a
    weekend/holiday day or two doesn't meaningfully change what a 5-8 day
    swing-trade evaluation window is trying to measure.
  - A push with no recorded trade_plan (fetch failed at push time, or no
    ATR available) is marked "no_data" and skipped -- there's nothing to
    evaluate it against.

Run once daily (see scan.yml) -- there's no reason to check this more
often than that; a 7-day-minimum-old push doesn't need hourly re-checking.
"""

import json
import os
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pandas as pd
import yfinance as yf

from config import (
    DAILY_PUSHES_FILE,
    OUTCOME_LOOKBACK_DAYS,
    OUTCOME_HISTORY_FILE,
)

ET = ZoneInfo("America/New_York")


def _flatten_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Same fix as technicals_scan.py/compose_alerts.py/filters.py: newer
    yfinance versions default to MultiIndex columns even for a
    single-ticker download. Applied here proactively -- three other files
    in this codebase already needed this exact fix, no reason to ship a
    fourth copy of the same latent bug.
    """
    if isinstance(df.columns, pd.MultiIndex):
        df = df.copy()
        df.columns = df.columns.get_level_values(0)
    return df


def load_daily_pushes() -> dict:
    if os.path.exists(DAILY_PUSHES_FILE):
        with open(DAILY_PUSHES_FILE) as f:
            return json.load(f)
    return {}


def load_outcome_history() -> dict:
    if os.path.exists(OUTCOME_HISTORY_FILE):
        with open(OUTCOME_HISTORY_FILE) as f:
            return json.load(f)
    return {}


def save_outcome_history(history: dict):
    with open(OUTCOME_HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def entry_id(day_key: str, entry: dict) -> str:
    """Unique per (day, symbol, push timestamp) -- a symbol pushed twice
    in one day (different intraday cycles) gets two distinct ids, since
    pushed_at differs."""
    return f"{day_key}::{entry['symbol']}::{entry.get('pushed_at', '')}"


def evaluate_outcome(symbol: str, push_date: str, price_at_push: float,
                      trade_plan: dict) -> dict | None:
    """
    Fetches daily OHLC for `symbol` from push_date through
    push_date + OUTCOME_LOOKBACK_DAYS, and walks it day by day (starting
    the day AFTER the push -- same-day price action was already reflected
    in the decision, evaluating it would be circular) to see which
    happens first: High reaching the target, or Low reaching the stop.

    If both are breached on the SAME day, treated conservatively as
    stop_hit -- there's no intraday granularity here to know which
    actually came first, and assuming the worse outcome is the safer
    default for a system meant to inform real position sizing.

    Returns None if the price fetch fails entirely (retried next run,
    not marked resolved). Returns a result dict with outcome="no_data"
    if the fetch succeeds but there's nothing usable (e.g. delisted).
    """
    try:
        push_dt = datetime.strptime(push_date, "%Y-%m-%d")
    except ValueError:
        return {"outcome": "no_data", "note": "unparseable push_date"}

    end_dt = push_dt + timedelta(days=OUTCOME_LOOKBACK_DAYS + 2)  # +2 slack for weekends
    try:
        df = yf.download(
            symbol,
            start=push_dt.strftime("%Y-%m-%d"),
            end=end_dt.strftime("%Y-%m-%d"),
            interval="1d",
            progress=False,
        )
        df = _flatten_columns(df)
        df = df.dropna(subset=["Close"])
    except Exception as e:
        print(f"  [price fetch error for {symbol}] {e}", file=sys.stderr)
        return None

    if df.empty:
        return {"outcome": "no_data", "note": "no price data returned"}

    target = trade_plan.get("target") if trade_plan else None
    stop = trade_plan.get("stop") if trade_plan else None

    # Skip the push day itself -- start from the next available bar.
    future_bars = df[df.index.strftime("%Y-%m-%d") > push_date]
    window_bars = future_bars.iloc[:OUTCOME_LOOKBACK_DAYS]

    if window_bars.empty:
        return {"outcome": "no_data", "note": "no bars after push date yet -- too recent"}

    if target is not None and stop is not None:
        for idx, row in window_bars.iterrows():
            hit_target = row["High"] >= target
            hit_stop = row["Low"] <= stop
            if hit_target and hit_stop:
                # Ambiguous same-day double-breach -- see docstring.
                return {
                    "outcome": "stop_hit", "outcome_date": idx.strftime("%Y-%m-%d"),
                    "outcome_price": stop, "note": "same-day double-breach, assumed stop first",
                    "days_to_outcome": (idx.to_pydatetime().replace(tzinfo=None) - push_dt).days,
                }
            if hit_target:
                return {
                    "outcome": "target_hit", "outcome_date": idx.strftime("%Y-%m-%d"),
                    "outcome_price": target,
                    "days_to_outcome": (idx.to_pydatetime().replace(tzinfo=None) - push_dt).days,
                }
            if hit_stop:
                return {
                    "outcome": "stop_hit", "outcome_date": idx.strftime("%Y-%m-%d"),
                    "outcome_price": stop,
                    "days_to_outcome": (idx.to_pydatetime().replace(tzinfo=None) - push_dt).days,
                }

    # Neither hit within the window (or no trade_plan levels to check) --
    # report the return as of the last available bar in the window.
    last_bar = window_bars.iloc[-1]
    last_close = float(last_bar["Close"])
    return_pct = ((last_close - price_at_push) / price_at_push) * 100 if price_at_push else None
    return {
        "outcome": "no_hit",
        "outcome_date": window_bars.index[-1].strftime("%Y-%m-%d"),
        "outcome_price": last_close,
        "return_pct": round(return_pct, 2) if return_pct is not None else None,
        "days_to_outcome": OUTCOME_LOOKBACK_DAYS,
    }


def main():
    pushes = load_daily_pushes()
    history = load_outcome_history()
    today_et = datetime.now(timezone.utc).astimezone(ET).date()

    to_evaluate = []
    for day_key, entries in pushes.items():
        try:
            day_date = datetime.strptime(day_key, "%Y-%m-%d").date()
        except ValueError:
            continue
        age_days = (today_et - day_date).days
        if age_days < OUTCOME_LOOKBACK_DAYS:
            continue
        for entry in entries:
            eid = entry_id(day_key, entry)
            if eid in history:
                continue  # already resolved, never re-evaluated
            to_evaluate.append((eid, day_key, entry))

    print(f"{len(to_evaluate)} push(es) old enough (>= {OUTCOME_LOOKBACK_DAYS}d) "
          f"and not yet resolved.", file=sys.stderr)

    resolved_count = 0
    skipped_no_plan = 0
    fetch_failures = 0
    for eid, day_key, entry in to_evaluate:
        trade_plan = entry.get("trade_plan")
        price_at_push = entry.get("price_at_push")
        if not trade_plan or price_at_push is None:
            # Nothing to evaluate against -- mark resolved as "no_data" so
            # it's not retried forever, but don't count it toward any
            # hit-rate stats.
            history[eid] = {
                "symbol": entry["symbol"], "tier": entry.get("tier"),
                "pushed_day": day_key, "outcome": "no_data",
                "note": "no trade_plan/price recorded at push time",
                "resolved_at": datetime.now(timezone.utc).isoformat(),
            }
            skipped_no_plan += 1
            continue

        result = evaluate_outcome(entry["symbol"], day_key, price_at_push, trade_plan)
        if result is None:
            fetch_failures += 1
            continue  # retried next run, not marked resolved

        history[eid] = {
            "symbol": entry["symbol"],
            "tier": entry.get("tier"),
            "category_count": entry.get("category_count"),
            "strength": entry.get("strength"),
            "pushed_day": day_key,
            "price_at_push": price_at_push,
            "trade_plan": trade_plan,
            "resolved_at": datetime.now(timezone.utc).isoformat(),
            **result,
        }
        resolved_count += 1

    save_outcome_history(history)

    # Simple aggregate stats printed for convenience -- not written to a
    # separate file, just a quick read of what's already in history.
    resolved = [h for h in history.values() if h.get("outcome") in ("target_hit", "stop_hit", "no_hit")]
    target_hits = sum(1 for h in resolved if h["outcome"] == "target_hit")
    stop_hits = sum(1 for h in resolved if h["outcome"] == "stop_hit")
    no_hits = sum(1 for h in resolved if h["outcome"] == "no_hit")
    decided = target_hits + stop_hits
    print(f"\nResolved this run: {resolved_count} (skipped {skipped_no_plan} with no trade "
          f"plan, {fetch_failures} price-fetch failure(s) will retry next run).", file=sys.stderr)
    print(f"All-time so far: {target_hits} target-hit, {stop_hits} stop-hit, "
          f"{no_hits} no-hit-in-window ({len(resolved)} total evaluated).", file=sys.stderr)
    if decided > 0:
        print(f"Target-vs-stop hit rate (excludes no-hit): {target_hits / decided * 100:.1f}%",
              file=sys.stderr)


if __name__ == "__main__":
    main()
