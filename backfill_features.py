"""
One-off (idempotent) recovery of push-time feature tags for outcome_history
entries that were resolved BEFORE push-time features were recorded.

Source: alerts_history/latest_alerts_*.md -- every run's full ranked list
with each ticker's signal text and caution lines, never overwritten. Each
outcome entry is matched to the run that produced the push (by push
timestamp + symbol) and validated against the tier / signal count /
strength recorded on the entry itself; a mismatch is rejected, not guessed.

Writes outcome_features.json ({entry_id: {"features": [...]}}), a sidecar
the scorecard joins against. It is a static historical file -- nothing else
writes it -- so there is no risk of clobbering outcome_history.json, which
the daily scan updates. Safe to re-run; entries already present are kept.

Usage:  python backfill_features.py
"""

import glob
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

from features import extract_features

ET = ZoneInfo("America/New_York")
UTC = timezone.utc
HISTORY_DIR = "alerts_history"
OUTCOME_FILE = "outcome_history.json"
OUT_FILE = "outcome_features.json"
REFRESH = "--refresh" in sys.argv    # recompute ALL entries (e.g. after new tags are added)
MATCH_WINDOW = timedelta(minutes=45)   # push happens shortly after the md is written

_HEAD = re.compile(r"^## \d+\. .*\((?P<sym>[^()]+)\) -- \[(?P<tier>[A-Za-z]+)\] "
                   r"(?P<n>\d+) signals, strength (?P<s>[\d.]+)")
_LINE = re.compile(r"^- (?P<warn>\u26a0\ufe0f )?\*\*(?P<label>.+?)\*\*: (?P<detail>.*)$")
_SKIP_LABELS = {"Trade plan", "Sector note"}


def parse_run(path: str):
    """-> (stamp_utc, {symbol: {...}}) for one alerts_history file."""
    m = re.search(r"latest_alerts_(\d{4}-\d{2}-\d{2})_(\d{4})\.md$", path)
    if not m:
        return None, {}
    stamp = datetime.strptime(m.group(1) + m.group(2), "%Y-%m-%d%H%M").replace(tzinfo=ET).astimezone(UTC)
    tickers, cur = {}, None
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            h = _HEAD.match(line)
            if h:
                cur = {"tier": h["tier"], "n": int(h["n"]), "strength": float(h["s"]),
                       "signals": {}, "cautions": []}
                tickers[h["sym"]] = cur
                continue
            if cur is None or line.startswith("#"):
                if line.startswith("# "):
                    cur = None
                continue
            lm = _LINE.match(line)
            if not lm or lm["label"] in _SKIP_LABELS:
                continue
            if lm["warn"]:
                cur["cautions"].append(lm["detail"])
            else:
                key = {"Technical": "technical", "Fundamentals": "fundamentals", "News": "news"}.get(lm["label"])
                if key:
                    cur["signals"][key] = lm["detail"]
    return stamp, tickers


def main():
    runs = []
    for p in sorted(glob.glob(os.path.join(HISTORY_DIR, "latest_alerts_*.md"))):
        stamp, tickers = parse_run(p)
        if stamp:
            runs.append((stamp, tickers))
    runs.sort(key=lambda r: r[0])
    print(f"Parsed {len(runs)} alert runs.", file=sys.stderr)

    outcomes = json.load(open(OUTCOME_FILE))
    out = json.load(open(OUT_FILE)) if os.path.exists(OUT_FILE) else {}
    stats = {"matched": 0, "no_run": 0, "mismatch": 0, "kept": 0}

    for eid, e in outcomes.items():
        if eid in out and not REFRESH:
            stats["kept"] += 1
            continue
        if e.get("outcome") == "no_data" and e.get("category_count") is None:
            continue
        try:
            pushed = datetime.fromisoformat(eid.split("::", 2)[2]).astimezone(UTC)
        except Exception:
            continue
        sym = e["symbol"]
        best = None
        for stamp, tickers in runs:
            if stamp > pushed + timedelta(minutes=2):
                break
            if pushed - stamp <= MATCH_WINDOW and sym in tickers:
                best = (stamp, tickers[sym])        # latest qualifying run <= push time
        if not best:
            stats["no_run"] += 1
            continue
        t = best[1]
        s_ok = e.get("strength") is None or abs(t["strength"] - e["strength"]) <= 0.011
        if t["tier"] != e.get("tier") or t["n"] != e.get("category_count") or not s_ok:
            stats["mismatch"] += 1
            continue
        tp = e.get("trade_plan") or {}
        atr_pct = None
        if tp.get("entry_low") is not None and e.get("price_at_push"):
            atr = (tp["entry_high"] - tp["entry_low"]) / 0.5      # band = +/-0.25 ATR
            atr_pct = atr / e["price_at_push"] * 100
        out[eid] = {"features": extract_features(t["signals"], t["cautions"], tier=t["tier"],
                                                 category_count=t["n"], atr_pct=atr_pct,
                                                 asof=best[0])}
        stats["matched"] += 1

    with open(OUT_FILE, "w") as f:
        json.dump(out, f, separators=(",", ":"))
    total = len(outcomes)
    print(f"Matched {stats['matched']} new, kept {stats['kept']} existing, "
          f"{stats['no_run']} no matching run, {stats['mismatch']} rejected (tier/count/strength mismatch) "
          f"of {total} outcome entries.", file=sys.stderr)


if __name__ == "__main__":
    main()
