"""
alert_log.py

Composite-level dedupe: once a ticker has actually been PUSHED to your
phone, don't push it again for DEDUPE_HOURS even if it's still ranking in
the top 20 next cycle. This is separate from signals_store.py's per-signal
validity windows -- a signal can stay "active" and keep contributing to a
ticker's confluence score without that ticker spamming you every 30 min.
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


def was_recently_alerted(symbol: str) -> bool:
    log = _load()
    last = log.get(symbol)
    if not last:
        return False
    try:
        last_dt = datetime.fromisoformat(last)
    except (TypeError, ValueError):
        # Leftover data in an old/incompatible format (e.g. from before
        # this file's structure changed) -- treat as "not recently
        # alerted" rather than crashing. Gets overwritten with the
        # correct format next time this symbol is actually alerted.
        return False
    return (datetime.now(timezone.utc) - last_dt) < timedelta(hours=DEDUPE_HOURS)


def mark_alerted(symbols: list[str]):
    log = _load()
    now = datetime.now(timezone.utc).isoformat()
    for s in symbols:
        log[s] = now
    _save(log)


def prune_old_entries():
    log = _load()
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=DEDUPE_HOURS * 4)
    pruned = {s: ts for s, ts in log.items() if datetime.fromisoformat(ts) > cutoff}
    _save(pruned)
