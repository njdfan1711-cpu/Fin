#!/usr/bin/env python3
"""
Custom git merge driver for signals_state.json.

signals_state.json is written by two independent, concurrently-running
workflows (daily-scan and intraday-scan), each recording different
categories of signal for possibly-overlapping symbols. Git's default
line-based text merge can't reconcile two versions of the same JSON
object, so any time both jobs commit close together, the losing job's
`git pull --rebase` fails with a CONFLICT and the workflow exits 1.

This driver is invoked automatically by git during merge/rebase (see
.gitattributes + `git config merge.signals-state.driver`). It merges the
three versions of the file at the symbol -> category level: for any
symbol/category present in only one side, keep it; if present in both
(the same category updated by both sides -- shouldn't normally happen
since categories are owned by one workflow each, but handle it safely),
keep whichever has the newer "timestamp".

Git calls this as:
    merge_signals_state.py %O %A %B
where:
    %O = common ancestor version
    %A = "ours" (current branch) -- git expects the merge RESULT written here
    %B = "theirs" (branch being merged in)
"""
import json
import sys


def load(path: str) -> dict:
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def newer(a: dict, b: dict) -> dict:
    """Given two {"detail","strength","timestamp"} entries, return the newer one."""
    return a if a.get("timestamp", "") >= b.get("timestamp", "") else b


def merge(ours: dict, theirs: dict) -> dict:
    merged = {}
    symbols = set(ours) | set(theirs)
    for symbol in symbols:
        our_cats = ours.get(symbol, {})
        their_cats = theirs.get(symbol, {})
        merged_cats = {}
        for category in set(our_cats) | set(their_cats):
            if category in our_cats and category in their_cats:
                merged_cats[category] = newer(our_cats[category], their_cats[category])
            elif category in our_cats:
                merged_cats[category] = our_cats[category]
            else:
                merged_cats[category] = their_cats[category]
        merged[symbol] = merged_cats
    return merged


def main():
    if len(sys.argv) != 4:
        print("usage: merge_signals_state.py <base> <ours> <theirs>", file=sys.stderr)
        sys.exit(2)

    _base_path, ours_path, theirs_path = sys.argv[1:4]

    ours = load(ours_path)
    theirs = load(theirs_path)
    result = merge(ours, theirs)

    # Git expects the merge result written back into the "ours" path.
    with open(ours_path, "w") as f:
        json.dump(result, f, indent=2, sort_keys=True)

    # Exit 0 tells git the conflict is resolved.
    sys.exit(0)


if __name__ == "__main__":
    main()
