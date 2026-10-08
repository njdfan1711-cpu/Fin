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
    """Streak info per symbol from the retained push log. Read-only; call
    BEFORE record_push() so the current cycle isn't counted.

    A "trading day" is any day that has a key in the log (weekends/holidays
    have no pushes, so they are simply skipped -- no holiday calendar needed).
    A streak is an UNBROKEN run of those days ending the day before today:
    one missed day resets it.

    prior_days:   length of that unbroken run (0 = not pushed on the latest
                  prior trading day). "Day N" = prior_days + 1.
    first_price:  price at the first push of the run (None if none/unknown).
    pushed_today: already pushed in an earlier cycle today.
    ever_pushed:  pushed any time in the retained log, today included.
    prev_run:     if the ticker was pushed earlier in the log but NOT on the
                  latest prior trading day, the length of its most recent
                  broken run (else 0). Used for the 'Back' marker.

    -> {sym: {"prior_days", "first_price", "pushed_today", "ever_pushed", "prev_run"}}
    """
    log = _load()
    today = _today_et_key()
    prior = sorted(d for d in log if d < today)
    day_syms = {d: {e.get("symbol") for e in log[d]} for d in prior}
    today_syms = {e.get("symbol") for e in log.get(today, [])}
    out = {}
    for sym in symbols:
        i = len(prior) - 1
        run = 0
        while i >= 0 and sym in day_syms[prior[i]]:
            run += 1
            i -= 1
        first_price = None
        if run:
            first_day = prior[i + 1]
            prices = [e.get("price_at_push") for e in log[first_day]
                      if e.get("symbol") == sym and e.get("price_at_push")]
            first_price = float(prices[0]) if prices else None
        prev_run = 0
        ever_prior = run > 0
        if run == 0:
            j = i
            while j >= 0 and sym not in day_syms[prior[j]]:
                j -= 1
            if j >= 0:
                ever_prior = True
                while j >= 0 and sym in day_syms[prior[j]]:
                    prev_run += 1
                    j -= 1
        out[sym] = {"prior_days": run, "first_price": first_price,
                    "pushed_today": sym in today_syms,
                    "ever_pushed": ever_prior or sym in today_syms,
                    "prev_run": prev_run}
    return out
