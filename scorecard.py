"""
Per-feature scorecard for Fin's swing track.

Joins outcome_history.json (what each push did) with the push-time feature
tags (inline "features" on newer entries, outcome_features.json sidecar for
older ones -- see backfill_features.py) and writes scorecard.md: for every
feature, how pushes that carried it actually turned out vs the baseline.

Design choices (the point is to NOT fool ourselves):
  * One sample per ticker per day (the first push of that ticker that day)
    -- the same ticker re-pushed every 30 minutes is not 30 observations.
  * Hits are rare (target ~5%), so the headline is average R-multiple, not
    hit rate. R = (exit - entry) / (entry - stop): stop_hit = -1, target_hit
    = +reward/risk (2.0), no_hit = marked at the last close of the 7-day
    window. Stop-outs are capped at -1R by construction (gap-throughs are
    not modeled), so losses are slightly understated.
  * Win% (R > 0) gets a Wilson 95% interval; a feature is only marked
    when that interval excludes the baseline, and anything under
    MIN_SAMPLES is labelled insufficient data and never marked.
  * Winners are hypotheses. With ~30 features tested, a couple will look
    significant by chance. Don't retune thresholds off this until the
    sample is much larger and the same feature holds up in later weeks.

Usage:
  python scorecard.py            # weekly: skips if scorecard.md is < 7 days old
  python scorecard.py --force    # regenerate now
"""

import json
import math
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

from config import OUTCOME_HISTORY_FILE, REWARD_RISK_RATIO

FEATURES_SIDECAR = "outcome_features.json"
REPORT_FILE = "scorecard.md"
MIN_SAMPLES = 30
REFRESH_DAYS = 7

GROUPS = [
    ("Conviction", ("tier:", "cats:")),
    ("Signal categories", ("cat:",)),
    ("Technical findings", ("tech:",)),
    ("Fundamental findings", ("fund:",)),
    ("Volatility (ATR % of price)", ("atr:",)),
    ("Cautions", ("caut:",)),
    ("Volume at 52-wk high (time-adjusted)", ("volhi:",)),
    ("Push timing (ET)", ("time:",)),
    ("Signal age / run-up since first push", ("age:", "runup:")),
]


def wilson(k: int, n: int, z: float = 1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def r_multiple(e: dict):
    """R-multiple for a resolved entry, or None if it can't be computed."""
    tp = e.get("trade_plan") or {}
    price, stop, outcome = e.get("price_at_push"), tp.get("stop"), e.get("outcome")
    if not price or stop is None or price - stop <= 0:
        return None
    risk = price - stop
    if outcome == "stop_hit":
        return -1.0
    if outcome == "target_hit":
        t = tp.get("target")
        return (t - price) / risk if t else REWARD_RISK_RATIO
    if outcome == "no_hit" and e.get("outcome_price") is not None:
        return (e["outcome_price"] - price) / risk
    return None


def load_samples():
    history = json.load(open(OUTCOME_HISTORY_FILE))
    sidecar = json.load(open(FEATURES_SIDECAR)) if os.path.exists(FEATURES_SIDECAR) else {}
    first = {}
    for eid, e in history.items():
        if e.get("outcome") not in ("target_hit", "stop_hit", "no_hit"):
            continue
        feats = e.get("features") or (sidecar.get(eid) or {}).get("features")
        if not feats:
            continue
        r = r_multiple(e)
        if r is None:
            continue
        key = (e["symbol"], e["pushed_day"])
        pushed_at = eid.split("::", 2)[2]
        if key in first and first[key]["pushed_at"] <= pushed_at:
            continue
        first[key] = {"symbol": e["symbol"], "day": e["pushed_day"], "pushed_at": pushed_at,
                      "features": set(feats), "outcome": e["outcome"], "r": r, "entry": e}
    return list(first.values()), len(history)


def summarize(rows):
    n = len(rows)
    wins = sum(1 for x in rows if x["r"] > 0)
    lo, hi = wilson(wins, n)
    return {
        "n": n, "tickers": len({x["symbol"] for x in rows}),
        "stop": sum(1 for x in rows if x["outcome"] == "stop_hit") / n if n else 0,
        "target": sum(1 for x in rows if x["outcome"] == "target_hit") / n if n else 0,
        "avg_r": sum(x["r"] for x in rows) / n if n else 0,
        "win": wins / n if n else 0, "win_lo": lo, "win_hi": hi,
    }


def build_report(samples, total_entries):
    base = summarize(samples)
    days = sorted({x["day"] for x in samples})
    by_feat = defaultdict(list)
    for s in samples:
        for f in s["features"]:
            by_feat[f].append(s)

    L = []
    L.append("# Fin swing-track scorecard")
    L.append(f"_Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d')} UTC_  ")
    L.append(f"_Window: {days[0]} to {days[-1]} ({len(days)} push days). "
             f"{base['n']} ticker-days ({base['tickers']} distinct tickers), "
             f"from {total_entries} raw push records._\n")
    L.append("**How to read this.** One sample per ticker per day. Avg R is the headline "
             "(stop = -1R, full target = +2R, otherwise marked at the day-7 close). "
             "Win% is the share with R > 0, with a 95% Wilson interval. "
             f"Anything under {MIN_SAMPLES} samples is *insufficient data*. "
             "\u25B2/\u25BC means the win% interval excludes the baseline -- treat as a "
             "hypothesis, not a finding: with this many features tested, a few will look "
             "significant by chance, the sample is a few weeks of one market regime, and "
             "same-ticker repeats on consecutive days are correlated. Don't retune "
             "thresholds from this yet.\n")
    L.append(f"**Baseline (all):** n={base['n']}, stop {base['stop']*100:.0f}%, "
             f"target {base['target']*100:.0f}%, avg R {base['avg_r']:+.2f}, "
             f"win {base['win']*100:.0f}% ({base['win_lo']*100:.0f}-{base['win_hi']*100:.0f}%)\n")

    rows_out = 0
    for title, prefixes in GROUPS:
        # Hide features carried by EVERY sample (e.g. every push is STRONG-tier
        # and has technical+fundamental signals by construction): they equal
        # the baseline and only add noise.
        feats = sorted(f for f in by_feat
                       if f.startswith(prefixes) and len(by_feat[f]) < base["n"])
        if not feats:
            continue
        L.append(f"## {title}")
        L.append("| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |")
        L.append("|---|--:|--:|--:|--:|--:|--:|---|---|")
        for f in sorted(feats, key=lambda x: -len(by_feat[x])):
            s = summarize(by_feat[f])
            if s["n"] < MIN_SAMPLES:
                note = "insufficient data"
            elif s["win_lo"] > base["win"]:
                note = "\u25B2"
            elif s["win_hi"] < base["win"]:
                note = "\u25BC"
            else:
                note = ""
            L.append(f"| `{f}` | {s['n']} | {s['tickers']} | {s['stop']*100:.0f} | "
                     f"{s['target']*100:.0f} | {s['avg_r']:+.2f} | {s['avg_r']-base['avg_r']:+.2f} | "
                     f"{s['win']*100:.0f} ({s['win_lo']*100:.0f}-{s['win_hi']*100:.0f}) | {note} |")
            rows_out += 1
        L.append("")

    # Take-profit / path check -- only populated by entries resolved after path
    # tracking went live (tp1_outcome, max_favorable_pct, max_adverse_pct).
    tp = [x for x in samples if x["entry"].get("tp1_outcome")]
    L.append("## Take-profit check (entries with path data)")
    if len(tp) < MIN_SAMPLES:
        L.append(f"_{len(tp)} entries so far -- insufficient data (need {MIN_SAMPLES}). Path data "
                 f"only exists for pushes resolved after it went live._\n")
    else:
        first = sum(1 for x in tp if x["entry"]["tp1_outcome"] == "tp1_first")
        stop_first = sum(1 for x in tp if x["entry"]["tp1_outcome"] == "stop_first")
        lo, hi = wilson(first, len(tp))
        mfe = sorted(x["entry"].get("max_favorable_pct", 0) for x in tp)
        L.append(f"- Take-profit touched before the stop: {first}/{len(tp)} "
                 f"({first/len(tp)*100:.0f}%, 95% CI {lo*100:.0f}-{hi*100:.0f}%); "
                 f"stop first: {stop_first} ({stop_first/len(tp)*100:.0f}%)")
        L.append(f"- Median best price in window: {mfe[len(mfe)//2]:+.1f}% vs entry\n")

    constant = sorted(f for f in by_feat if len(by_feat[f]) == base["n"])
    L.append(f"_{len(by_feat)} distinct features tracked; always-present (hidden): "
             f"{', '.join(constant) or 'none'}. Raw push records without recoverable "
             f"features are excluded._")
    return "\n".join(L) + "\n"


def report_is_fresh() -> bool:
    if not os.path.exists(REPORT_FILE):
        return False
    m = re.search(r"_Generated: (\d{4}-\d{2}-\d{2}) UTC_", open(REPORT_FILE, encoding="utf-8").read(2000))
    if not m:
        return False
    age = (datetime.now(timezone.utc).date() - datetime.strptime(m.group(1), "%Y-%m-%d").date()).days
    return age < REFRESH_DAYS


def main():
    if "--force" not in sys.argv and report_is_fresh():
        print(f"{REPORT_FILE} is < {REFRESH_DAYS} days old -- skipping (use --force).", file=sys.stderr)
        return
    samples, total = load_samples()
    if not samples:
        print("No samples with features yet -- nothing to report.", file=sys.stderr)
        return
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(build_report(samples, total))
    print(f"Wrote {REPORT_FILE}: {len(samples)} ticker-days.", file=sys.stderr)


if __name__ == "__main__":
    main()
