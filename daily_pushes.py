"""
daily_pushes.py

Running log of actual pushes sent to your phone, grouped by ET trading
day (not UTC calendar day -- the intraday workflow runs 13:00-21:59 UTC,
which is a single ET session, so grouping by ET keeps each day's entries
together instead of splitting near the UTC day boundary).

Separate from alert_log.py's was_recently_alerted()/mark_alerted(), which
is per-symbol dedupe logic used to decide what to push. This module is
just a historical record of what was actually sent, for your own review
in the repo -- it doesn't feed back into any scoring or filtering.
"""

import json
import os
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

from config import DAILY_PUSHES_FILE, DAILY_PUSHES_RETENTION_DAYS

ET = ZoneInfo("America/New_York")


def _load() -> dict:
    if os.path.exists(DAILY_PUSHES_FILE):
        with open(DAILY_PUSHES_FILE) as f:
            return json.load(f)
    return {}


def _save(log: dict):
    with open(DAILY_PUSHES_FILE, "w") as f:
        json.dump(log, f, indent=2)


def _today_et_key() -> str:
    return datetime.now(timezone.utc).astimezone(ET).strftime("%Y-%m-%d")


def record_push(entries: list[dict]):
    """Append this cycle's pushed entries under today's ET trading-day key.

    Each entry gets a UTC timestamp added so you can see when within the
    day a given pick actually fired, if you want to dig into the file.
    """
    if not entries:
        return
    log = _load()
    day_key = _today_et_key()
    now = datetime.now(timezone.utc).isoformat()
    day_entries = log.setdefault(day_key, [])
    for entry in entries:
        day_entries.append({**entry, "pushed_at": now})
    _save(log)


def prune_old_days():
    """Drop trading days older than DAILY_PUSHES_RETENTION_DAYS."""
    log = _load()
    cutoff = (datetime.now(timezone.utc).astimezone(ET) -
              timedelta(days=DAILY_PUSHES_RETENTION_DAYS)).strftime("%Y-%m-%d")
    pruned = {day: entries for day, entries in log.items() if day >= cutoff}
    _save(pruned)


def symbol_history(symbols) -> dict:
    """Streak info per symbol, from the retained push log. Read-only; call
    BEFORE record_push() so the current cycle isn't counted.

    prior_days:   EARLIER ET trading days in the current streak (a streak
                  allows gaps of up to 4 calendar days, so weekends and
                  holidays don't break it).
    first_price:  price at the first push of that streak (None if unknown).
    pushed_today: already pushed in an earlier cycle today.

    -> {sym: {"prior_days": int, "first_price": float | None, "pushed_today": bool}}
    """
    log = _load()
    today = _today_et_key()
    prior = sorted(d for d in log if d < today)
    day_syms = {d: {e.get("symbol") for e in log[d]} for d in list(prior) + ([today] if today in log else [])}
    today_syms = day_syms.get(today, set())
    out = {}
    for sym in symbols:
        streak, nxt = [], datetime.strptime(today, "%Y-%m-%d")
        for d in reversed(prior):
            if sym not in day_syms[d]:
                continue
            dt = datetime.strptime(d, "%Y-%m-%d")
            if (nxt - dt).days > 4:
                break
            streak.append(d)
            nxt = dt
        first_price = None
        if streak:
            first = min(streak)
            prices = [e.get("price_at_push") for e in log[first]
                      if e.get("symbol") == sym and e.get("price_at_push")]
            first_price = float(prices[0]) if prices else None
        out[sym] = {"prior_days": len(streak), "first_price": first_price,
                    "pushed_today": sym in today_syms}
    return out
