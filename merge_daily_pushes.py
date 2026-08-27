#!/usr/bin/env python3
"""
Custom git merge driver for daily_pushes.json.

daily_pushes.json is {et_trading_day: [entry, ...]}, appended to on every
intraday cycle that actually pushes something (see daily_pushes.py). Same
problem as signals_state.json/alert_log.json: two runs committing close
together each add different entries under (usually) the same day key,
and git's line-based text merge can't reconcile that.

Merge rule: union of day keys; for a day present on both sides, union the
entry lists (deduped by exact content, since a genuine duplicate entry
would have a different "pushed_at" timestamp) and sort by "pushed_at" so
the merged log stays chronological. This never drops a real push record,
which matters here since -- unlike alert_log.json's dedupe marks -- this
file is the actual historical record of what was sent.

Called by git as:
    merge_daily_pushes.py %O %A %B
where %O = common ancestor, %A = "ours" (git expects the result written
here), %B = "theirs".
"""
import json
import sys


def load(path: str) -> dict:
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def merge(ours: dict, theirs: dict) -> dict:
    merged = {}
    for day in set(ours) | set(theirs):
        our_entries = ours.get(day, [])
        their_entries = theirs.get(day, [])

        seen = set()
        combined = []
        for entry in our_entries + their_entries:
            key = json.dumps(entry, sort_keys=True)
            if key not in seen:
                seen.add(key)
                combined.append(entry)

        combined.sort(key=lambda e: e.get("pushed_at", ""))
        merged[day] = combined
    return merged


def main():
    if len(sys.argv) != 4:
        print("usage: merge_daily_pushes.py <base> <ours> <theirs>", file=sys.stderr)
        sys.exit(2)

    _base_path, ours_path, theirs_path = sys.argv[1:4]

    ours = load(ours_path)
    theirs = load(theirs_path)
    result = merge(ours, theirs)

    with open(ours_path, "w") as f:
        json.dump(result, f, indent=2, sort_keys=True)

    sys.exit(0)


if __name__ == "__main__":
    main()
