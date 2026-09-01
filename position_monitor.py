"""
position_monitor.py

The piece that was missing between "Fin computes a stop/target at
signal time" and what actually happens to a position afterward.
track_outcomes.py grades old signals for hit-rate stats regardless of
whether they were ever traded; this script only cares about positions
that were actually entered (synced from the trade log to
OPEN_POSITIONS_FILE) and checks them, every run, against the specific
trade_plan that was live when that symbol was pushed.

For each open position:
  1. Find the trade_plan Fin generated for that symbol on/near its
     entry_date (searches daily_pushes.json). If the symbol was never
     a Fin signal (a manual pick, or entry_date missing/unmatched),
     there's nothing to check it against -- reported as such, skipped.
  2. Fetch the current price.
  3. Flag it if price has breached the recorded stop, reached the
     recorded target, or if it's been held for OVERDUE_HOLD_MULTIPLIER
     times the empirical median days-to-resolution (computed fresh each
     run from outcome_history.json, so this stays current as more data
     accumulates rather than being a hardcoded guess).

Alerts are pushed once per NEW condition per position, not every run --
POSITION_MONITOR_STATE_FILE tracks what was last alerted so a breached
stop doesn't repeat the same notification every day. If a condition
clears (price recovers back above a breached stop) the state resets,
so a future re-breach alerts again.

Run once daily (see scan.yml) -- position status doesn't need
intraday-level granularity, and running it there would multiply
yfinance calls for little added value.
"""

import json
import os
import sys
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import pandas as pd
import yfinance as yf

from config import (
    OPEN_POSITIONS_FILE,
    POSITION_MONITOR_STATE_FILE,
    DAILY_PUSHES_FILE,
    POSITION_PLAN_LOOKBACK_DAYS,
    OVERDUE_HOLD_MULTIPLIER,
)
from notify import send_alert
from track_outcomes import typical_resolution_days

ET = ZoneInfo("America/New_York")
FALLBACK_OVERDUE_DAYS = 10  # used only if outcome_history.json has no resolved samples yet


def _flatten_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Same MultiIndex fix used elsewhere in this codebase."""
    if isinstance(df.columns, pd.MultiIndex):
        df = df.copy()
        df.columns = df.columns.get_level_values(0)
    return df


def load_json(path: str, default):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default


def save_json(path: str, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def find_trade_plan(symbol: str, entry_date: str | None, pushes: dict) -> dict | None:
    """
    Searches daily_pushes.json for the trade_plan that was live for
    `symbol` on/before `entry_date`, within POSITION_PLAN_LOOKBACK_DAYS.
    If entry_date is missing, falls back to the single most recent push
    of that symbol found anywhere in the file (flagged as approximate
    via the "matched_date_is_approximate" key on the returned dict).

    Returns None if no matching push exists at all.
    """
    candidates = []  # (day_date, entry)
    for day_key, entries in pushes.items():
        try:
            day_date = datetime.strptime(day_key, "%Y-%m-%d").date()
        except ValueError:
            continue
        for entry in entries:
            if entry.get("symbol") == symbol:
                candidates.append((day_date, entry))

    if not candidates:
        return None

    candidates.sort(key=lambda c: c[0])

    if entry_date:
        try:
            entry_dt = datetime.strptime(entry_date, "%Y-%m-%d").date()
        except ValueError:
            entry_dt = None
    else:
        entry_dt = None

    if entry_dt:
        window_start = entry_dt.toordinal() - POSITION_PLAN_LOOKBACK_DAYS
        on_or_before = [
            (d, e) for d, e in candidates
            if d.toordinal() <= entry_dt.toordinal() and d.toordinal() >= window_start
        ]
        if on_or_before:
            best_date, best_entry = on_or_before[-1]  # closest to entry_dt, on or before it
            plan = dict(best_entry.get("trade_plan") or {})
            plan["_matched_push_date"] = best_date.isoformat()
            plan["_matched_date_is_approximate"] = False
            plan["price_at_push"] = best_entry.get("price_at_push")
            return plan if plan.get("stop") is not None or plan.get("target") is not None else None

    # No usable entry_date match -- fall back to most recent push of this
    # symbol overall, flagged as approximate.
    best_date, best_entry = candidates[-1]
    plan = dict(best_entry.get("trade_plan") or {})
    if plan.get("stop") is None and plan.get("target") is None:
        return None
    plan["_matched_push_date"] = best_date.isoformat()
    plan["_matched_date_is_approximate"] = True
    plan["price_at_push"] = best_entry.get("price_at_push")
    return plan


def fetch_current_price(symbol: str) -> float | None:
    try:
        df = yf.download(symbol, period="5d", interval="1d", progress=False)
        df = _flatten_columns(df)
        df = df.dropna(subset=["Close"])
        if df.empty:
            return None
        return float(df["Close"].iloc[-1])
    except Exception as e:
        print(f"  [price fetch error for {symbol}] {e}", file=sys.stderr)
        return None


def evaluate_position(pos: dict, plan: dict | None, current_price: float | None,
                       resolution_days: dict, today: datetime.date) -> dict:
    """Returns a dict describing the position's status and any new alert conditions."""
    result = {
        "id": pos["id"],
        "symbol": pos["symbol"],
        "current_price": current_price,
        "conditions": [],  # list of condition keys, e.g. "stop_breached"
        "detail_lines": [],
    }

    entry_price = pos.get("entryPrice")
    if current_price is not None and entry_price:
        pnl_pct = ((current_price - entry_price) / entry_price) * 100
        result["pnl_pct"] = round(pnl_pct, 2)

    if plan and current_price is not None:
        stop = plan.get("stop")
        target = plan.get("target")
        approx = plan.get("_matched_date_is_approximate")
        tag = " (approx. matched plan)" if approx else ""

        if stop is not None and current_price <= stop:
            result["conditions"].append("stop_breached")
            result["detail_lines"].append(
                f"{pos['symbol']}: ${current_price:.2f} is at/below its stop "
                f"(${stop:.2f}){tag}."
            )
        if target is not None and current_price >= target:
            result["conditions"].append("target_reached")
            result["detail_lines"].append(
                f"{pos['symbol']}: ${current_price:.2f} has reached its target "
                f"(${target:.2f}){tag}."
            )

    entry_date = pos.get("entryDate")
    if entry_date:
        try:
            entry_dt = datetime.strptime(entry_date, "%Y-%m-%d").date()
            days_held = (today - entry_dt).days
            result["days_held"] = days_held

            target_stats = resolution_days.get("target_hit")
            median_days = target_stats["median_days"] if target_stats else FALLBACK_OVERDUE_DAYS
            overdue_threshold = median_days * OVERDUE_HOLD_MULTIPLIER
            if "stop_breached" not in result["conditions"] and days_held > overdue_threshold:
                result["conditions"].append("overdue")
                result["detail_lines"].append(
                    f"{pos['symbol']}: held {days_held}d, well past the ~{median_days:.0f}d "
                    f"median resolution time for signals that hit their target -- this "
                    f"trade has likely outrun its original thesis."
                )
        except ValueError:
            pass

    if plan is None:
        result["detail_lines"].append(
            f"{pos['symbol']}: no matching Fin trade_plan found (manual pick, or entry "
            f"predates/doesn't match a push) -- can't check against a stop/target."
        )

    return result


def main():
    positions_data = load_json(OPEN_POSITIONS_FILE, None)
    if positions_data is None:
        print(f"{OPEN_POSITIONS_FILE} not found -- nothing synced yet, skipping.")
        return

    open_positions = [p for p in positions_data.get("trades", []) if p.get("status") == "open"]
    if not open_positions:
        print("No open positions to check.")
        return

    pushes = load_json(DAILY_PUSHES_FILE, {})
    resolution_days = typical_resolution_days()  # imported from track_outcomes
    state = load_json(POSITION_MONITOR_STATE_FILE, {})
    today = datetime.now(timezone.utc).astimezone(ET).date()

    new_alert_lines = []
    updated_state = {}

    for pos in open_positions:
        symbol = pos["symbol"]
        plan = find_trade_plan(symbol, pos.get("entryDate"), pushes)
        price = fetch_current_price(symbol)
        evaluation = evaluate_position(pos, plan, price, resolution_days, today)

        pos_id = pos["id"]
        prev_conditions = set(state.get(pos_id, []))
        current_conditions = set(evaluation["conditions"])
        updated_state[pos_id] = list(current_conditions)

        new_conditions = current_conditions - prev_conditions
        if new_conditions:
            new_alert_lines.extend(
                line for line, cond in zip(evaluation["detail_lines"], evaluation["conditions"])
                if cond in new_conditions
            )

        print(f"{symbol}: price={price}, conditions={sorted(current_conditions)}, "
              f"pnl_pct={evaluation.get('pnl_pct')}, days_held={evaluation.get('days_held')}")

    save_json(POSITION_MONITOR_STATE_FILE, updated_state)

    if new_alert_lines:
        message = "\n".join(f"- {line}" for line in new_alert_lines)
        send_alert(
            title="Position check: action may be needed",
            message=message,
            priority="high",
            tags=["warning"],
        )
        print(f"Sent alert for {len(new_alert_lines)} new condition(s).")
    else:
        print("No new conditions to alert on.")


if __name__ == "__main__":
    main()
