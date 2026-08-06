"""
alert_log.py - prevents the same ticker+reason from re-alerting every
30 minutes for as long as the condition stays true (e.g. RSI staying
under 30 for hours shouldn't ping your phone every cycle).
"""

import json
import os
from datetime import datetime, timedelta, timezone
from config import ALERT_LOG_FILE, DEDUPE_HOURS


def _load() -> dict:
    if os.path.exists(ALERT_LOG_FILE):
        with open(ALERT_LOG_FILE) as f:
            return json.load(f)
    return {}


def _save(log: dict):
    with open(ALERT_LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)


def filter_new(symbol: str, reasons: list[str]) -> list[str]:
    """
    Given a ticker and the reasons it matched this scan cycle, returns only
    the reasons that haven't already been alerted on within DEDUPE_HOURS.
    Updates the log as a side effect.
    """
    log = _load()
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=DEDUPE_HOURS)

    entry = log.get(symbol, {})
    fresh_reasons = []

    for reason in reasons:
        last_seen = entry.get(reason)
        if last_seen:
            last_seen_dt = datetime.fromisoformat(last_seen)
            if last_seen_dt > cutoff:
                continue  # already alerted recently, skip
        fresh_reasons.append(reason)
        entry[reason] = now.isoformat()

    if fresh_reasons:
        log[symbol] = entry
        _save(log)

    return fresh_reasons


def prune_old_entries():
    """Optional housekeeping -- call occasionally to keep the log file small."""
    log = _load()
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=DEDUPE_HOURS * 4)

    pruned = {}
    for symbol, reasons in log.items():
        kept = {r: ts for r, ts in reasons.items() if datetime.fromisoformat(ts) > cutoff}
        if kept:
            pruned[symbol] = kept

    _save(pruned)
