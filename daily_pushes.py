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
