"""
compose_alerts.py

The final step of each intraday cycle. Reads everything recorded by
technicals_scan.py, news_scan.py, fundamentals_scan.py, and
short_interest_scan.py (via signals_store.py), and decides what's
actually worth pushing to your phone:

  1. Only tickers with signals from >= MIN_SIGNAL_CATEGORIES DISTINCT
     categories qualify (per your preference: require 2+ signals to agree
     before it counts as a real opportunity, not noise).
  2. Qualifying tickers are ranked by a confidence score: category count
     first (agreement across more independent signal types matters most),
     then combined signal strength as a tiebreaker.
  3. Tickers already pushed recently are NOT excluded -- a stock that
     keeps qualifying stays visible every cycle rather than disappearing
     just because you've seen it before (missing it once shouldn't mean
     missing it entirely). Instead, still-qualifying repeats are shown
     plainly and newly-qualifying tickers get a \U0001F195 NEW tag so you can
     scan for what's fresh at a glance.
  4. For the top TOP_N_ALERTS, fetches a live price and Finnhub's analyst
     consensus price target -- giving each alert an actual "why" and a
     defensible target, rather than a bare list of tickers.
  5. Sends ONE push with the top-ranked picks (push length is limited, so
     everything qualifying -- not just the top N -- gets written to
     latest_alerts.md in the repo for full reference).
  6. Attaches sector-level context (e.g. "tariff news affecting Steel")
     to any ticker whose industry matches an active sector alert from
     news_scan.py. This is ANNOTATION ONLY -- it never counts toward the
     MIN_SIGNAL_CATEGORIES confluence requirement, so a broad macro
     headline can't inflate confidence on its own.

Run this as the last step of the intraday workflow, after technicals_scan
and news_scan. Fundamentals/short-interest signals recorded earlier that
day remain active per their validity window and get pulled in here too.
"""

import json
import re
import sys
import urllib.request
from datetime import datetime, timezone

import yfinance as yf

from config import (
    FINNHUB_API_KEY,
    ELIGIBLE_FILE,
    MIN_SIGNAL_CATEGORIES,
    MIN_QUALIFYING_STRENGTH,
    STRONG_TIER_MIN_CATEGORIES,
    STRONG_TIER_STRENGTH_FOR_TWO,
    TOP_N_ALERTS,
    LATEST_ALERTS_FILE,
    TICKER_SECTORS_FILE,
    SECTOR_ALERTS_FILE,
    SECTOR_ALERT_VALIDITY_HOURS,
    REPO_URL,
    MOMENTUM_MAX_PICKS_IN_PUSH,
    MOMENTUM_PUSH_CHAR_BUDGET,
)
from signals_store import get_active_signals
from alert_log import was_recently_alerted, mark_alerted
from daily_pushes import record_push, prune_old_days
from notify import send_alert

CATEGORY_LABELS = {
    "technical": "Technical",
    "news": "News",
    "fundamentals": "Fundamentals",
    "short_interest": "Short Interest",
}

# "caution" is a distinct pseudo-category: risk/warning flags (overextended
# above the 50-day MA, unhealthy market regime, unconfirmed breakout volume)
# that should never count toward the confluence requirement -- they're
# context to weigh, not confirmation of an opportunity.
CAUTION_CATEGORY = "caution"

# "momentum" is a deliberately SEPARATE track (low-float + volume-spike
# speculative setups -- see momentum_scan.py) with its own philosophy,
# opposite to the quality/confluence approach used everywhere else. It's
# excluded from the main scoring/STRONG-tier calculation for the same
# reason CAUTION_CATEGORY is: blending it in would let a single
# speculative volume spike plus one weak technical signal masquerade as a
# "STRONG" quality-backed pick, which would quietly erode what that label
# is supposed to mean. It gets its own separate section of the push
# instead (see build_momentum_section below).
MOMENTUM_CATEGORY = "momentum"


def score_ticker(categories: dict) -> tuple:
    """Returns (category_count, total_strength) -- used as a sort key.
    Excludes the caution AND momentum categories from both count and
    strength -- neither should influence the main confluence score."""
    real_categories = {
        k: v for k, v in categories.items()
        if k not in (CAUTION_CATEGORY, MOMENTUM_CATEGORY)
    }
    count = len(real_categories)
    total_strength = sum(info.get("strength", 0.5) for info in real_categories.values())
    return (count, total_strength)


def conviction_tier(category_count: int, total_strength: float) -> str:
    """
    'Strong' requires either genuine agreement across 3+ independent
    categories, OR just 2 categories but with strength high enough that
    it's clearly not a borderline case. Anything else that still clears
    the qualifying bar is 'Moderate' -- worth a look, but less conviction.
    """
    if category_count >= STRONG_TIER_MIN_CATEGORIES:
        return "STRONG"
    if category_count == 2 and total_strength >= STRONG_TIER_STRENGTH_FOR_TWO:
        return "STRONG"
    return "MODERATE"


def fetch_price_target(symbol: str):
    if not FINNHUB_API_KEY:
        return None
    url = f"https://finnhub.io/api/v1/stock/price-target?symbol={symbol}&token={FINNHUB_API_KEY}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "personal-stock-scanner"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data.get("targetMean")
    except Exception:
        return None


def fetch_current_prices(symbols: list[str]) -> dict:
    """Live-ish prices for just the shortlist -- cheap since it's a small batch."""
    if not symbols:
        return {}
    try:
        data = yf.download(
            tickers=" ".join(symbols),
            period="1d",
            interval="1d",
            group_by="ticker",
            threads=True,
            progress=False,
        )
    except Exception as e:
        print(f"[price fetch error] {e}", file=sys.stderr)
        return {}

    prices = {}
    for sym in symbols:
        try:
            df = data if len(symbols) == 1 else data[sym]
            prices[sym] = float(df["Close"].dropna().iloc[-1])
        except Exception:
            continue
    return prices


def load_company_names() -> dict:
    names = {}
    try:
        import csv
        with open(ELIGIBLE_FILE, newline="") as f:
            for row in csv.DictReader(f):
                names[row["symbol"]] = row.get("name", "")
    except FileNotFoundError:
        pass
    return names


# Strips common "-Common Stock", "Class A Common Shares", etc. suffixes
# from Nasdaq/NYSE security names for display -- just a display cleanup,
# original names stay untouched everywhere else (matching, storage).
_NAME_SUFFIX_PATTERNS = [
    re.compile(r",?\s*-?\s*Class\s+[A-Z]\s+Common\s+(Stock|Shares)\b.*$", re.IGNORECASE),
    re.compile(r",?\s*-?\s*Common\s+(Stock|Shares)\b.*$", re.IGNORECASE),
    re.compile(r",?\s*-?\s*Ordinary\s+Shares\b.*$", re.IGNORECASE),
]


def clean_company_name(name: str) -> str:
    if not name:
        return name
    cleaned = name
    for pattern in _NAME_SUFFIX_PATTERNS:
        cleaned = pattern.sub("", cleaned).strip()
    return cleaned if cleaned else name


def load_sectors() -> dict:
    try:
        with open(TICKER_SECTORS_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def load_active_sector_alerts() -> list[dict]:
    """Returns sector alerts still within their validity window."""
    try:
        with open(SECTOR_ALERTS_FILE) as f:
            alerts = json.load(f)
    except FileNotFoundError:
        return []

    now = datetime.now(timezone.utc)
    active = []
    for keyword, info in alerts.items():
        try:
            ts = datetime.fromisoformat(info["timestamp"])
        except (KeyError, ValueError):
            continue
        age_hours = (now - ts).total_seconds() / 3600
        if age_hours <= SECTOR_ALERT_VALIDITY_HOURS:
            active.append(info)
    return active


def find_sector_annotation(industry: str, active_sector_alerts: list[dict]) -> str | None:
    """
    Annotation-only match: if this ticker's industry overlaps with an
    active sector alert's industry list, return a short context line.
    This is NEVER counted toward MIN_SIGNAL_CATEGORIES -- purely context.
    """
    if not industry:
        return None
    for alert in active_sector_alerts:
        for target_industry in alert.get("industries", []):
            if target_industry.lower() in industry.lower():
                return f"[{alert.get('source', '')}] {alert.get('detail', '')}"
    return None


def format_ticker_line(rank: int, symbol: str, name: str, categories: dict,
                        price, target, sector_note: str | None = None,
                        is_new: bool = False) -> str:
    """
    Markdown-formatted: bold ticker/price header line, reasons as a clean
    indented bullet list underneath instead of one long comma/pipe string.
    """
    price_bit = ""
    if price and target:
        upside = ((target - price) / price) * 100
        direction = "upside" if upside >= 0 else "downside"
        price_bit = f" — ${price:.2f} → target ${target:.2f} ({upside:+.1f}% {direction})"
    elif price:
        price_bit = f" — ${price:.2f}"

    display_name = clean_company_name(name) if name else symbol
    new_tag = "\U0001F195 " if is_new else ""  # 🆕

    count, strength = score_ticker(categories)
    tier = conviction_tier(count, strength)
    tier_tag = "\U0001F525 STRONG" if tier == "STRONG" else "\u2713 Moderate"  # 🔥 / ✓

    header = f"{new_tag}**#{rank} {symbol}** [{tier_tag}] _{display_name}_{price_bit}"

    bullets = []
    for cat, info in categories.items():
        if cat == CAUTION_CATEGORY:
            continue  # shown separately below with a warning marker
        label = CATEGORY_LABELS.get(cat, cat)
        bullets.append(f"  • **{label}:** {info['detail']}")
    if CAUTION_CATEGORY in categories:
        bullets.append(f"  • \u26A0\uFE0F **Caution:** {categories[CAUTION_CATEGORY]['detail']}")
    if sector_note:
        bullets.append(f"  • **Sector:** {sector_note}")

    return header + "\n" + "\n".join(bullets)


def format_momentum_line(rank: int, symbol: str, name: str, info: dict, price) -> str:
    """
    Deliberately distinct formatting from format_ticker_line -- no
    STRONG/Moderate tier tag (that vocabulary belongs to the confluence
    system), a different emoji, and an explicit risk note so this never
    reads as equivalent conviction to a quality-backed pick.
    """
    price_bit = f" — ${price:.2f}" if price else ""
    display_name = clean_company_name(name) if name else symbol
    header = f"\u26A1 **#{rank} {symbol}**{price_bit} _{display_name}_"
    bullet = f"  • {info['detail']}"
    note = "  • _Speculative: low float + volume spike, not fundamentals-backed_"
    return "\n".join([header, bullet, note])


def build_momentum_section(momentum_ranked: list, company_names: dict, prices: dict,
                            char_budget: int, max_picks: int) -> tuple[str, int, int]:
    """
    Builds the reserved speculative section. Returns (section_text,
    included_count, total_qualifying_count). Capped by BOTH max_picks and
    char_budget -- whichever is more restrictive wins -- so this section
    can never grow large enough to threaten the main list's space.
    """
    if not momentum_ranked:
        return "", 0, 0

    capped = momentum_ranked[:max_picks]
    lines = [
        format_momentum_line(i, sym, company_names.get(sym, ""), info, prices.get(sym))
        for i, (sym, info) in enumerate(capped, start=1)
    ]
    body, included = truncate_to_whole_entries(lines, char_budget)
    if not body:
        return "", 0, len(momentum_ranked)

    section = "\u26A1 **Speculative / High-Risk** (low float + volume spike)\n\n" + body
    return section, included, len(momentum_ranked)



def truncate_to_whole_entries(entries: list[str], limit: int) -> tuple[str, int]:
    """
    Joins entries with blank-line separators, but stops adding whole
    entries once the next one would exceed `limit` -- so the message never
    cuts a ticker off mid-way through. Returns (message, entries_included).
    """
    included = []
    total_len = 0
    separator_len = 2  # "\n\n"
    for entry in entries:
        added_len = len(entry) + (separator_len if included else 0)
        if total_len + added_len > limit:
            break
        included.append(entry)
        total_len += added_len
    return "\n\n".join(included), len(included)


def main():
    active = get_active_signals()
    company_names = load_company_names()
    sectors = load_sectors()
    active_sector_alerts = load_active_sector_alerts()
    print(f"{len(active_sector_alerts)} active sector-level alert(s) available for annotation.",
          file=sys.stderr)

    # Require confluence -- excludes the caution category so a single real
    # signal plus a caution flag can't incorrectly count as "2" -- AND a
    # minimum combined strength, so two borderline/weak signals don't
    # qualify as easily as two strong ones.
    qualifying = {}
    for sym, cats in active.items():
        count, strength = score_ticker(cats)
        if count >= MIN_SIGNAL_CATEGORIES and strength >= MIN_QUALIFYING_STRENGTH:
            qualifying[sym] = cats
    print(f"{len(active)} ticker(s) have active signals; "
          f"{len(qualifying)} qualify with {MIN_SIGNAL_CATEGORIES}+ categories.", file=sys.stderr)

    # Momentum/speculative track -- completely separate qualification,
    # ranked purely by its own strength (there's only ever one category
    # here, so category-count ranking wouldn't mean anything).
    momentum_ranked = sorted(
        (
            (sym, cats[MOMENTUM_CATEGORY])
            for sym, cats in active.items()
            if MOMENTUM_CATEGORY in cats
        ),
        key=lambda kv: kv[1].get("strength", 0),
        reverse=True,
    )
    print(f"{len(momentum_ranked)} ticker(s) qualify on the separate momentum/low-float track.",
          file=sys.stderr)

    # Rank by confidence
    ranked = sorted(qualifying.items(), key=lambda kv: score_ticker(kv[1]), reverse=True)
    # Attach each ticker's overall rank now, so the push and the full
    # written list use the same index even after recently-alerted tickers
    # get filtered out of the push.
    ranked_with_rank = [(i, sym, cats) for i, (sym, cats) in enumerate(ranked, start=1)]

    # Write the FULL ranked list to the repo regardless of push cap
    with open(LATEST_ALERTS_FILE, "w") as f:
        f.write(f"# Latest Alerts ({len(ranked)} qualifying tickers)\n\n")
        for rank, sym, cats in ranked_with_rank:
            count, strength = score_ticker(cats)
            name = clean_company_name(company_names.get(sym, ""))
            label = f"{name} ({sym})" if name else sym
            f.write(f"## {rank}. {label} -- [{conviction_tier(count, strength)}] "
                    f"{count} signals, strength {strength:.2f}\n")
            for cat, info in cats.items():
                if cat == CAUTION_CATEGORY:
                    continue  # written separately below, clearly marked
                f.write(f"- **{CATEGORY_LABELS.get(cat, cat)}**: {info['detail']}\n")
            if CAUTION_CATEGORY in cats:
                f.write(f"- \u26A0\uFE0F **CAUTION**: {cats[CAUTION_CATEGORY]['detail']}\n")
            sector_note = find_sector_annotation(sectors.get(sym, ""), active_sector_alerts)
            if sector_note:
                f.write(f"- **Sector note**: {sector_note}\n")
            f.write("\n")

        if momentum_ranked:
            f.write(f"\n# Speculative / High-Risk -- Low Float + Volume Spike "
                     f"({len(momentum_ranked)} qualifying)\n\n")
            f.write("_Separate track, not blended into the confluence scoring above. "
                     "Low float (shares-outstanding proxy) + large price-confirmed volume "
                     "spike -- see momentum_scan.py / config.py for thresholds._\n\n")
            for rank, (sym, info) in enumerate(momentum_ranked, start=1):
                name = clean_company_name(company_names.get(sym, ""))
                label = f"{name} ({sym})" if name else sym
                f.write(f"## {rank}. {label}\n")
                f.write(f"- {info['detail']}\n\n")

    # Tag (not filter) tickers that were already pushed recently, so you
    # can quickly scan for what's fresh vs. what's been holding steady --
    # but nothing gets DROPPED from the push just because you've seen it
    # before. A stock stays visible for as long as it keeps qualifying;
    # it only disappears once it actually stops meeting the criteria.
    push_list = ranked_with_rank[:TOP_N_ALERTS]

    if not push_list and not momentum_ranked:
        print("Nothing qualifies right now.", file=sys.stderr)
        return

    symbols_to_price = [sym for _, sym, _ in push_list]
    prices = fetch_current_prices(symbols_to_price)

    lines = []
    for rank, sym, cats in push_list:
        price = prices.get(sym)
        target = fetch_price_target(sym)
        name = company_names.get(sym, "")
        sector_note = find_sector_annotation(sectors.get(sym, ""), active_sector_alerts)
        is_new = not was_recently_alerted(sym)
        lines.append(format_ticker_line(rank, sym, name, cats, price, target, sector_note, is_new))

    message, included_count = truncate_to_whole_entries(lines, 3800)
    if included_count < len(lines):
        message += f"\n\n_...+{len(lines) - included_count} more, see full list link above_"

    new_count = sum(1 for rank, sym, cats in push_list if not was_recently_alerted(sym))
    strong_count = sum(1 for rank, sym, cats in push_list
                        if conviction_tier(*score_ticker(cats)) == "STRONG")
    # NOTE: no emoji in the title -- it becomes an HTTP header, and Python's
    # urllib encodes headers as Latin-1, which crashes on characters like 🔥.
    # Emoji are fine in the message BODY (sent as UTF-8), just not headers.
    title = f"{len(push_list)} pick(s) ({strong_count} strong)"
    if new_count:
        title += f", {new_count} new"
    if len(ranked_with_rank) > len(push_list):
        title += f" +{len(ranked_with_rank) - len(push_list)} more in repo"

    click_url = f"{REPO_URL}/blob/main/{LATEST_ALERTS_FILE}" if REPO_URL else None

    if push_list:
        send_alert(title, message, priority="high", tags=["chart_with_upwards_trend"],
                   markdown=True, click_url=click_url)
        mark_alerted([sym for _, sym, _ in push_list])

        record_push([
            {
                "symbol": sym,
                "tier": conviction_tier(*score_ticker(cats)),
                "category_count": score_ticker(cats)[0],
                "strength": score_ticker(cats)[1],
                "categories": {
                    cat: info["detail"] for cat, info in cats.items()
                    if cat != CAUTION_CATEGORY
                },
            }
            for _, sym, cats in push_list
        ])
        print(f"\nPushed {included_count}/{len(push_list)} ticker(s) (fit within message limit), "
              f"{new_count} newly qualifying. "
              f"Full ranked list ({len(ranked)} total) written to {LATEST_ALERTS_FILE}.", file=sys.stderr)
    else:
        print("No confluence picks qualify this cycle -- main push skipped "
              "(momentum picks, if any, still send separately below).", file=sys.stderr)

    # Speculative/momentum push -- SEPARATE notification, own fixed budget
    # (not carved out of the main list's 3800 chars). Sent independently
    # of whether the main list fired, so it's never at the mercy of how
    # busy the main confluence list is on a given cycle -- which in
    # practice is "full or nearly full" almost every cycle for this
    # screener, so a shared/leftover budget would rarely show anything.
    momentum_prices = fetch_current_prices([sym for sym, _ in momentum_ranked[:MOMENTUM_MAX_PICKS_IN_PUSH]])
    momentum_section, momentum_included, momentum_total = build_momentum_section(
        momentum_ranked, company_names, momentum_prices, MOMENTUM_PUSH_CHAR_BUDGET, MOMENTUM_MAX_PICKS_IN_PUSH
    )
    if momentum_section:
        momentum_title = f"\u26A1 {momentum_included} speculative pick(s)"
        if momentum_total > momentum_included:
            momentum_title += f" +{momentum_total - momentum_included} more in repo"
        if momentum_included < momentum_total:
            momentum_section += f"\n\n_...+{momentum_total - momentum_included} more speculative, see repo_"
        send_alert(momentum_title, momentum_section, priority="default",
                   tags=["zap"], markdown=True, click_url=click_url)
        print(f"Pushed {momentum_included}/{momentum_total} speculative ticker(s) as a separate alert.",
              file=sys.stderr)
    elif momentum_ranked:
        print(f"{len(momentum_ranked)} speculative ticker(s) qualified but none fit "
              f"the {MOMENTUM_PUSH_CHAR_BUDGET}-char budget -- see {LATEST_ALERTS_FILE}.", file=sys.stderr)

    prune_old_days()


if __name__ == "__main__":
    main()
