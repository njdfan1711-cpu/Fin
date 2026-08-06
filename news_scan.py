"""
news_scan.py

Runs every 30 minutes during market hours (same cadence as technicals,
per your preference that news/sentiment can move price fast and deserves
high priority).

Design note: pulling news per-ticker for 2,000-3,000 eligible names every
30 minutes isn't feasible on Finnhub's free tier (60 calls/min would take
40+ minutes just to fetch once, before you even get to the next cycle).
Instead, this pulls Finnhub's general market news feed in ONE call per
cycle, then matches article headlines/summaries against your eligible
tickers' company names and symbols. Less precise than per-ticker news,
but far more sustainable, and it still catches the kind of broad
market-moving stories (earnings surprises, upgrades/downgrades, M&A,
regulatory news) that matter most for a fast catalyst signal.

NOTE: needs FINNHUB_API_KEY and outbound network access. Test in your
actual deployment, not in a network-restricted sandbox.
"""

import csv
import json
import re
import sys
import urllib.request

from config import ELIGIBLE_FILE, FINNHUB_API_KEY
from alert_log import filter_new
from notify import send_batch_alert

NEWS_URL = f"https://finnhub.io/api/v1/news?category=general&token={FINNHUB_API_KEY}"

# Lookback window for "recent" news, in minutes -- should comfortably
# cover the 30-min scan interval plus some overlap in case a cycle runs late.
LOOKBACK_MINUTES = 40


def load_eligible() -> list[dict]:
    with open(ELIGIBLE_FILE, newline="") as f:
        return list(csv.DictReader(f))


def fetch_news() -> list[dict]:
    if not FINNHUB_API_KEY:
        print("FINNHUB_API_KEY not set, skipping news scan.", file=sys.stderr)
        return []
    req = urllib.request.Request(NEWS_URL, headers={"User-Agent": "personal-stock-scanner"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def build_matchers(eligible: list[dict]) -> dict:
    """
    Builds a {symbol: compiled_regex} map. Matches on company name (first
    significant word, to dodge suffixes like 'Inc'/'Corp' mismatches) OR
    the ticker symbol as a standalone word, to cut down false positives
    from short tickers matching common words.
    """
    matchers = {}
    for row in eligible:
        symbol = row["symbol"]
        name = row["name"]
        # Take the first word of the company name that's actually
        # distinctive (skip generic leading words if present)
        first_word = name.split()[0] if name else symbol
        pattern = rf"\b({re.escape(first_word)}|{re.escape(symbol)})\b"
        try:
            matchers[symbol] = re.compile(pattern, re.IGNORECASE)
        except re.error:
            continue
    return matchers


def main():
    eligible = load_eligible()
    print(f"Fetching market news and matching against {len(eligible)} eligible tickers...",
          file=sys.stderr)

    articles = fetch_news()
    if not articles:
        print("No articles returned, nothing to scan.", file=sys.stderr)
        return

    import time
    cutoff_ts = time.time() - (LOOKBACK_MINUTES * 60)
    recent_articles = [a for a in articles if a.get("datetime", 0) >= cutoff_ts]
    print(f"  {len(recent_articles)} article(s) within the last {LOOKBACK_MINUTES} min", file=sys.stderr)

    matchers = build_matchers(eligible)

    all_matches = []
    for row in eligible:
        symbol = row["symbol"]
        pattern = matchers.get(symbol)
        if not pattern:
            continue

        hits = []
        for a in recent_articles:
            text = f"{a.get('headline', '')} {a.get('summary', '')}"
            if pattern.search(text):
                hits.append(a.get("headline", "")[:120])

        if hits:
            reason = [f"News mention: {hits[0]}"]
            fresh = filter_new(symbol, reason)
            if fresh:
                all_matches.append({"symbol": symbol, "reasons": fresh})

    print(f"\n{len(all_matches)} ticker(s) matched news (after de-dup).", file=sys.stderr)
    send_batch_alert(all_matches)


if __name__ == "__main__":
    main()
