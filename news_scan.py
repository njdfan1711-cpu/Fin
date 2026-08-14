"""
news_scan.py

Runs every 30 minutes during market hours. Pulls from MULTIPLE free news
sources (not just Finnhub's single curated feed) and matches headlines
against your eligible tickers.

Sources used, and why these specifically:
  - Finnhub general market news (existing API, kept as one input among several)
  - Yahoo Finance RSS (free, no auth, verified working)
  - CNBC RSS (free, no auth, verified working -- needs a browser-like
    User-Agent or it's refused)
  - MarketWatch Top Stories + Real-Time Headlines RSS (via Dow Jones'
    public content feed infrastructure, free, no auth)

NOT included, despite being requested, because there's no free/reliable
path: Seeking Alpha (RSS exists but is behind aggressive bot protection --
unreliable enough that including it would mostly just log failures),
Barchart, Google Finance (no API/feed at all), and CNN/Fox/CBS/MSNBC
(none publish structured financial-news feeds suitable for this -- their
general RSS is politics/world news, not the kind of company-specific
signal this scanner needs). Reuters' public RSS was discontinued back in
2020, despite still showing up in a lot of "best RSS feeds" lists online.

Design note: this fetches EACH FEED ONCE per cycle (not per ticker), then
matches every eligible ticker's name/symbol against the combined article
pool locally. That's what keeps this fast and free regardless of universe
size. Each source is wrapped in its own try/except -- one dead or
rate-limited feed doesn't take down the whole scan, it just contributes
zero articles that cycle.

Signals are RECORDED via signals_store.py, not pushed directly --
compose_alerts.py decides what's push-worthy.

NOTE: needs outbound network access. Test in your actual deployment, not
in a network-restricted sandbox -- I could not verify these feeds against
live traffic from where this was written.
"""

import csv
import json
import os
import re
import sys
import time
import urllib.request

import feedparser

from config import ELIGIBLE_FILE, FINNHUB_API_KEY, SECTOR_KEYWORDS, SECTOR_ALERTS_FILE
from signals_store import record_signal

FINNHUB_NEWS_URL = f"https://finnhub.io/api/v1/news?category=general&token={FINNHUB_API_KEY}"

# Some sites (Yahoo, CNBC) refuse feed requests without a browser-like UA.
FEED_USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

RSS_FEEDS = [
    ("Yahoo Finance", "https://finance.yahoo.com/news/rssindex"),
    ("CNBC", "https://www.cnbc.com/id/100003114/device/rss/rss.xml"),
    ("MarketWatch Top Stories", "https://feeds.content.dowjones.io/public/rss/mw_topstories"),
    ("MarketWatch Real-Time", "https://feeds.content.dowjones.io/public/rss/mw_realtimeheadlines"),
]

# Lookback window for "recent" news, in minutes.
LOOKBACK_MINUTES = 40


def load_eligible() -> list[dict]:
    with open(ELIGIBLE_FILE, newline="") as f:
        return list(csv.DictReader(f))


def fetch_finnhub_news() -> list[dict]:
    """Returns list of {headline, summary, source, published_ts}."""
    if not FINNHUB_API_KEY:
        return []
    try:
        req = urllib.request.Request(FINNHUB_NEWS_URL, headers={"User-Agent": "personal-stock-scanner"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
        return [
            {
                "headline": a.get("headline", ""),
                "summary": a.get("summary", ""),
                "source": "Finnhub",
                "published_ts": a.get("datetime", 0),
            }
            for a in raw
        ]
    except Exception as e:
        print(f"  [Finnhub news error] {e}", file=sys.stderr)
        return []


def fetch_rss_feed(name: str, url: str) -> list[dict]:
    """Returns list of {headline, summary, source, published_ts}."""
    try:
        parsed = feedparser.parse(url, agent=FEED_USER_AGENT)
        if parsed.bozo and not parsed.entries:
            print(f"  [{name} feed error] {parsed.bozo_exception}", file=sys.stderr)
            return []

        articles = []
        for entry in parsed.entries:
            published_ts = 0
            if getattr(entry, "published_parsed", None):
                published_ts = time.mktime(entry.published_parsed)
            elif getattr(entry, "updated_parsed", None):
                published_ts = time.mktime(entry.updated_parsed)

            articles.append({
                "headline": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "source": name,
                "published_ts": published_ts,
            })
        return articles
    except Exception as e:
        print(f"  [{name} feed error] {e}", file=sys.stderr)
        return []


def fetch_all_articles() -> list[dict]:
    all_articles = []

    print("  Fetching Finnhub general news...", file=sys.stderr)
    finnhub_articles = fetch_finnhub_news()
    print(f"    {len(finnhub_articles)} article(s)", file=sys.stderr)
    all_articles.extend(finnhub_articles)

    for name, url in RSS_FEEDS:
        print(f"  Fetching {name} RSS...", file=sys.stderr)
        articles = fetch_rss_feed(name, url)
        print(f"    {len(articles)} article(s)", file=sys.stderr)
        all_articles.extend(articles)

    return all_articles


# Lightweight keyword-based sentiment, NOT real NLP -- there's no
# LLM/sentiment API in this pipeline's budget. This only exists to catch
# the clear-cut cases (a recall or lawsuit headline shouldn't score
# identically to an earnings beat just because the ticker's name appears
# in both), not to make fine-grained calls on ambiguous headlines. Most
# headlines won't match either list, and that's fine -- they're treated
# as neutral and still count as a normal positive "news" signal, same as
# before this change.
BEARISH_KEYWORDS = [
    "recall", "lawsuit", "sues", "sued", "investigation", "probe", "fraud",
    "resigns", "resignation", "delisting", "delisted", "bankruptcy",
    "bankrupt", "misses estimates", "miss estimates", "guidance cut",
    "cuts guidance", "cut guidance", "layoffs", "plunge", "plunges",
    "crash", "downgrade", "downgraded", "warns", "warning", "scandal",
    "subpoena", "restatement", "restates", "class action", "shortfall",
    "halts production", "data breach", "hack", "impairment",
]
BULLISH_KEYWORDS = [
    "beats estimates", "beat estimates", "upgrade", "upgraded",
    "raises guidance", "raised guidance", "raises outlook",
    "record revenue", "record profit", "record results", "surge", "surges",
    "acquisition", "acquires", "partnership", "buyback",
    "share repurchase", "price target raised", "outperform",
]


def classify_headline_sentiment(headline: str) -> str:
    """
    Returns "bearish", "bullish", or "neutral" based on simple keyword
    presence in the headline (case-insensitive). Bearish is checked first
    and wins on any overlap -- e.g. "Beats estimates despite ongoing
    investigation" should not be treated as a clean positive, a real
    caution flag is the safer default when signals conflict.
    """
    text = headline.lower()
    if any(kw in text for kw in BEARISH_KEYWORDS):
        return "bearish"
    if any(kw in text for kw in BULLISH_KEYWORDS):
        return "bullish"
    return "neutral"


def build_matchers(eligible: list[dict]) -> dict:
    """
    {symbol: compiled_regex} -- matches on the company name's first
    DISTINCTIVE word OR the ticker symbol as a standalone word.

    Two false-positive traps this guards against:

    1. Generic leading words. Many legal names start with "The" (The
       Chefs' Warehouse, The Vita Coco Company, The Baldwin Insurance
       Group, ...) or other boilerplate (Inc, Corp, Group, Company, ...).
       Using that as the match keyword makes the pattern fire on nearly
       any article, since words like "the" appear everywhere. We skip
       leading stopwords/corporate-suffix words and use the first
       genuinely distinctive word instead. If nothing distinctive is
       left, we fall back to symbol-only matching for that ticker.

    2. Case-insensitive ticker collisions with common English words.
       Tickers like ALL (Allstate), ARE (Alexandria Real Estate), CAT
       (Caterpillar), GO (Grocery Outlet), BE (Bloom Energy), A
       (Agilent) are themselves ordinary words. Matching them
       case-insensitively means "all", "are", "cat", "go", "be", "a"
       in any article count as a mention. Real ticker mentions in
       financial news/RSS are capitalized, so the ticker half of the
       pattern is matched case-SENSITIVELY (only the company-name half
       stays case-insensitive), eliminating this class of false hit.
    """
    STOPWORDS = {
        "the", "a", "an", "inc", "incorporated", "corp", "corporation",
        "company", "co", "group", "holding", "holdings", "ltd", "limited",
        "plc", "llc", "class", "common", "stock",
    }
    # Sector-generic words -- legitimate parts of a company's real name,
    # but useless as a standalone match keyword: dozens of unrelated
    # companies share one of these as their "distinctive" first word
    # (Energy Fuels, Energy Vault, Power Solutions, ...), so a headline
    # about ANY company in that sector false-positives on all of them.
    # Real bug this caused: a single "Bloom Energy" headline matched
    # NRGV (Energy Vault), UUUU (Energy Fuels), AND PSIX (Power
    # Solutions) simultaneously -- none of them Bloom Energy.
    GENERIC_SECTOR_WORDS = {
        "energy", "power", "solar", "gold", "silver", "mining", "metals",
        "resources", "capital", "financial", "global", "national",
        "international", "american", "united", "systems", "networks",
        "digital", "health", "healthcare", "pharma", "biosciences",
        "technologies", "tech", "industries", "enterprises", "partners",
        "ventures", "solutions", "services",
    }

    matchers = {}
    for row in eligible:
        symbol = row["symbol"]
        name = row["name"]

        words = re.findall(r"[A-Za-z']+", name)
        distinctive = [w for w in words if w.lower() not in STOPWORDS]

        # Prefer a TWO-word phrase whenever the name has one available --
        # far more specific than any single word ("Power Solutions" vs.
        # "Power"), and self-scaling to new tickers without needing a
        # hand-maintained blocklist to cover every case. Falls back to a
        # single word only when the name doesn't have a second one, and
        # even then, refuses to match on a lone generic sector word --
        # ticker-only in that case.
        first_word = distinctive[0] if distinctive else None
        name_phrase = None
        if len(distinctive) >= 2:
            name_phrase = rf"{re.escape(distinctive[0])}\s+{re.escape(distinctive[1])}"
        elif first_word and first_word.lower() not in GENERIC_SECTOR_WORDS:
            name_phrase = re.escape(first_word)

        symbol_alt = re.escape(symbol)
        if name_phrase:
            # Name half stays case-insensitive (scoped inline flag);
            # symbol half is case-sensitive by default.
            pattern = rf"\b((?i:{name_phrase})|{symbol_alt})\b"
        else:
            # No usable distinctive name phrase (generic single word, or
            # nothing distinctive at all) -- match on the ticker only,
            # case-sensitively.
            pattern = rf"\b({symbol_alt})\b"

        try:
            matchers[symbol] = re.compile(pattern)
        except re.error:
            continue
    return matchers


def detect_sector_alerts(articles: list[dict]):
    """
    Scans articles for broad sector/macro keywords (tariffs, rate moves,
    oil prices, etc.) that don't mention any specific company by name but
    still matter to whole industries. Written to SECTOR_ALERTS_FILE as
    annotation-only context -- compose_alerts.py attaches these to
    matching tickers' pushes WITHOUT counting them toward the 2+ signal
    confluence requirement, so a broad macro story can't inflate a
    ticker's confidence score on its own.
    """
    import re
    from datetime import datetime, timezone

    if os.path.exists(SECTOR_ALERTS_FILE):
        with open(SECTOR_ALERTS_FILE) as f:
            sector_alerts = json.load(f)
    else:
        sector_alerts = {}

    now = datetime.now(timezone.utc).isoformat()
    found_count = 0

    for keyword, industries in SECTOR_KEYWORDS.items():
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        for a in articles:
            text = f"{a.get('headline', '')} {a.get('summary', '')}"
            if pattern.search(text):
                sector_alerts[keyword] = {
                    "detail": a.get("headline", "")[:150],
                    "industries": industries,
                    "source": a.get("source", ""),
                    "timestamp": now,
                }
                found_count += 1
                break  # one matching article per keyword per cycle is enough

    with open(SECTOR_ALERTS_FILE, "w") as f:
        json.dump(sector_alerts, f, indent=2)

    return found_count


def main():
    eligible = load_eligible()
    print(f"Fetching news from {1 + len(RSS_FEEDS)} source(s) and matching "
          f"against {len(eligible)} eligible tickers...", file=sys.stderr)

    all_articles = fetch_all_articles()
    print(f"\n{len(all_articles)} total article(s) fetched across all sources.", file=sys.stderr)

    cutoff_ts = time.time() - (LOOKBACK_MINUTES * 60)
    recent_articles = [a for a in all_articles if a.get("published_ts", 0) >= cutoff_ts]
    print(f"  {len(recent_articles)} article(s) within the last {LOOKBACK_MINUTES} min "
          f"(older articles or ones with no timestamp are excluded)", file=sys.stderr)

    matchers = build_matchers(eligible)

    sector_count = detect_sector_alerts(recent_articles)
    print(f"  {sector_count} sector-level keyword match(es) recorded "
          f"(annotation only, not counted toward confluence)", file=sys.stderr)

    total_signals = 0
    caution_signals = 0
    for row in eligible:
        symbol = row["symbol"]
        pattern = matchers.get(symbol)
        if not pattern:
            continue

        # HEADLINE ONLY, not headline+summary -- matching against the
        # summary body was producing real false positives: an article
        # about an unrelated topic (e.g. energy infrastructure) that
        # merely name-drops a company once in its body text would match
        # just as strongly as an article actually ABOUT that company.
        # Headline-only is a much stronger "this article is about this
        # ticker" signal, at the cost of missing genuine mentions that
        # only appear in the body -- an acceptable tradeoff given the
        # alternative was noise masquerading as confirmation.
        matches = []
        for a in recent_articles:
            headline = a.get("headline", "")
            if pattern.search(headline):
                matches.append(a)

        if not matches:
            continue

        # Sentiment gate: classify each matching headline, bearish wins
        # if there's any disagreement across sources (see
        # classify_headline_sentiment's docstring).
        sentiments = [classify_headline_sentiment(a.get("headline", "")) for a in matches]
        overall = "bearish" if "bearish" in sentiments else (
            "bullish" if "bullish" in sentiments else "neutral"
        )

        headline = matches[0].get("headline", "")[:130]
        source = matches[0].get("source", "")
        detail = f"[{source}] {headline}"
        if len(matches) > 1:
            detail += f" (+{len(matches) - 1} more source(s))"
        # Small per-additional-article bonus (capped, matching the
        # scheme in technicals_scan.py/fundamentals_scan.py) so a
        # story corroborated across multiple outlets ranks slightly
        # ahead of a single-source hit at the same base strength,
        # rather than every news signal being an identical 0.7 and
        # falling back to arbitrary tie order.
        strength = 0.7 + min(0.05, 0.01 * (len(matches) - 1))

        if overall == "bearish":
            # NOT recorded as a positive "news" signal -- a recall or
            # lawsuit headline shouldn't count toward confluence the same
            # way an earnings beat does. Recorded to its own category
            # (see compose_alerts.py's NEWS_CAUTION_CATEGORY) so it's
            # still visible as a warning without inflating the score.
            record_signal(symbol, "news_caution", detail, strength=strength)
            caution_signals += 1
        else:
            record_signal(symbol, "news", detail, strength=strength)
            total_signals += 1

    print(f"\n{total_signals} news signal(s) recorded, "
          f"{caution_signals} flagged as bearish-leaning caution instead.", file=sys.stderr)


if __name__ == "__main__":
    main()
