#!/usr/bin/env python3
"""
Custom git merge driver for alert_log.json.

alert_log.json is a flat {symbol: iso_timestamp} dict recording the last
time each symbol was actually pushed, used for DEDUPE_HOURS suppression
(see alert_log.py). It's rewritten on every intraday cycle, so any two
runs that end up committing close together (e.g. a scheduled run and a
manual workflow_dispatch landing near each other) produce two versions
git's default line-based text merge can't reconcile -- same problem
merge_signals_state.py exists to solve, just for a simpler flat shape.

Merge rule: union of symbols; if a symbol appears on both sides with a
different timestamp, keep the newer one (ISO 8601 strings sort correctly
as plain strings). Losing a "recently alerted" mark here would just risk
one extra duplicate push, not lose real data, so this is a safe rule.

Called by git as:
    merge_alert_log.py %O %A %B
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
    for symbol in set(ours) | set(theirs):
        a = ours.get(symbol)
        b = theirs.get(symbol)
        if a is not None and b is not None:
            merged[symbol] = a if a >= b else b
        else:
            merged[symbol] = a if a is not None else b
    return merged


def main():
    if len(sys.argv) != 4:
        print("usage: merge_alert_log.py <base> <ours> <theirs>", file=sys.stderr)
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
