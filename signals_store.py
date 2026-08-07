"""
signals_store.py

Replaces the old pattern where every scan script decided on its own to
push an alert. Now each script just RECORDS what it found (category,
ticker, human-readable detail, a rough strength score), and a separate
step (compose_alerts.py) reads everything back, requires agreement across
multiple categories, ranks by confidence, and sends one well-formed push.

Each signal has a validity window (see config.SIGNAL_VALIDITY_HOURS) --
once expired, it stops counting toward confluence even if it's still
sitting in the file. This is what fixes the "329 stocks alerted because a
stale earnings beat from months ago still matched" bug -- fundamentals
signals get a several-day window, technicals get a few hours.
"""

import json
import os
from datetime import datetime, timezone

from config import SIGNALS_STATE_FILE, SIGNAL_VALIDITY_HOURS


def _load() -> dict:
    if os.path.exists(SIGNALS_STATE_FILE):
        with open(SIGNALS_STATE_FILE) as f:
            return json.load(f)
    return {}


def _save(state: dict):
    with open(SIGNALS_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def record_signal(symbol: str, category: str, detail: str, strength: float = 1.0):
    """
    category: one of "technical", "news", "fundamentals", "short_interest"
    detail: human-readable reason, e.g. "Earnings beat by 8.2% (2 days ago)"
    strength: rough 0-1+ scale, higher = more significant within its category
              (doesn't need to be precise -- it's a tiebreaker, not the main ranking)
    """
    state = _load()
    entry = state.get(symbol, {})
    entry[category] = {
        "detail": detail,
        "strength": strength,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    state[symbol] = entry
    _save(state)


def get_active_signals() -> dict:
    """
    Returns {symbol: {category: {"detail", "strength", "timestamp"}}} for
    only the signals still within their category's validity window.
    Also prunes fully-expired symbols from the underlying file as a side
    effect, so the file doesn't grow forever.
    """
    state = _load()
    now = datetime.now(timezone.utc)
    active = {}
    pruned = {}

    for symbol, categories in state.items():
        kept = {}
        for category, info in categories.items():
            window_hours = SIGNAL_VALIDITY_HOURS.get(category, 24)
            ts = datetime.fromisoformat(info["timestamp"])
            age_hours = (now - ts).total_seconds() / 3600
            if age_hours <= window_hours:
                kept[category] = info
        if kept:
            active[symbol] = kept
            pruned[symbol] = kept  # only keep still-valid entries on disk too

    _save(pruned)
    return active
