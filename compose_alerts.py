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
import hashlib

import pandas as pd
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
    ATR_PERIOD,
    ENTRY_BAND_ATR_MULT,
    STOP_ATR_MULT,
    MOMENTUM_STOP_ATR_MULT,
    REWARD_RISK_RATIO,
    DEFAULT_POSITION_SIZE_USD,
    NTFY_MESSAGE_BYTE_LIMIT,
    NTFY_SAFE_BODY_BYTE_BUDGET,
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

# "earnings_quality" is a SEPARATE caution channel from CAUTION_CATEGORY
# (owned by fundamentals_scan.py, not technicals_scan.py -- see that
# script's docstring for why they can't share one category key). Same
# treatment as CAUTION_CATEGORY: excluded from scoring, shown as a warning.
EARNINGS_QUALITY_CATEGORY = "earnings_quality"

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
        if k not in (CAUTION_CATEGORY, MOMENTUM_CATEGORY, EARNINGS_QUALITY_CATEGORY)
    }
    count = len(real_categories)
    total_strength = sum(info.get("strength", 0.5) for info in real_categories.values())
    return (count, total_strength)


def tiebreak_key(symbol: str) -> int:
    """
    Deterministic-per-day but otherwise arbitrary tiebreaker for tickers
    that still land on an exact (category_count, strength) tie after the
    upstream scans' evidence-count bonus. Rotates daily (seeded by UTC
    date) so a tie doesn't perpetually favor the same tickers/alphabetical
    order run after run -- it's purely a fairness mechanism, not a
    confidence signal, so it's kept as the LAST sort key, after both real
    scoring dimensions.
    """
    day_key = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return int(hashlib.md5(f"{symbol}-{day_key}".encode()).hexdigest(), 16)


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


def compute_atr(df: pd.DataFrame, period: int = ATR_PERIOD) -> float | None:
    """Standard ATR: rolling mean of true range over `period` daily bars.
    Returns None if there isn't enough history to fill the window."""
    if len(df) <= period:
        return None
    high, low, close = df["High"], df["Low"], df["Close"]
    prev_close = close.shift(1)
    true_range = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs(),
    ], axis=1).max(axis=1)
    atr = true_range.rolling(period).mean().iloc[-1]
    return float(atr) if pd.notna(atr) else None


def _flatten_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Newer yfinance versions (0.2.31+) default to MultiIndex columns even
    for a single-ticker download (e.g. ("Close", "AAPL") instead of just
    "Close") -- requirements.txt doesn't pin a version, so this can start
    happening any time yfinance publishes a release. Without this,
    df["Close"] is a one-column DataFrame instead of a Series, and
    float(df["Close"].iloc[-1]) blows up with "must be a string or a real
    number, not 'Series'". Only actually bites when exactly 1 symbol is
    passed in (the len(symbols) == 1 path below uses the raw download
    result directly) -- a real scenario here, since a shortlist push can
    easily have just one qualifying pick.
    """
    if isinstance(df.columns, pd.MultiIndex):
        df = df.copy()
        df.columns = df.columns.get_level_values(0)
    return df


def fetch_prices_and_atr(symbols: list[str]) -> dict:
    """Live-ish price + ATR(14) for just the shortlist -- cheap since it's
    a small batch. Replaces the old fetch_current_prices: everything that
    used to just need a price now also needs ATR for the trade plan, and
    pulling both from one download avoids a second API round-trip.
    Pulls ~2 months of daily bars -- comfortably more than ATR_PERIOD
    needs, with slack for holidays/thin trading."""
    if not symbols:
        return {}
    try:
        data = yf.download(
            tickers=" ".join(symbols),
            period="2mo",
            interval="1d",
            group_by="ticker",
            threads=True,
            progress=False,
        )
    except Exception as e:
        print(f"[price/ATR fetch error] {e}", file=sys.stderr)
        return {}

    results = {}
    for sym in symbols:
        try:
            df = data if len(symbols) == 1 else data[sym]
            df = _flatten_columns(df)
            df = df.dropna(subset=["Close"])
            if df.empty:
                continue
            price = float(df["Close"].iloc[-1])
            atr = compute_atr(df)
            results[sym] = {"price": price, "atr": atr}
        except Exception:
            continue
    return results


def compute_trade_plan(price: float | None, atr: float | None, stop_atr_mult: float,
                        position_size_usd: float = DEFAULT_POSITION_SIZE_USD,
                        reward_risk_ratio: float = REWARD_RISK_RATIO,
                        entry_band_atr_mult: float = ENTRY_BAND_ATR_MULT) -> dict | None:
    """ATR-based volatility-scaled entry/stop/target -- not a flat percent,
    so it naturally widens for volatile names and tightens for calm ones.
    Returns None if there's no price/ATR to work with, or if the computed
    stop would be at or above the entry (degenerate case, shouldn't happen
    with a positive ATR but guarded against regardless)."""
    if not price or not atr or atr <= 0:
        return None

    entry_low = price - entry_band_atr_mult * atr
    entry_high = price + entry_band_atr_mult * atr
    stop = price - stop_atr_mult * atr
    risk_per_share = price - stop
    if risk_per_share <= 0:
        return None
    target = price + reward_risk_ratio * risk_per_share

    shares = int(position_size_usd // price) if price > 0 else 0
    risk_usd = shares * risk_per_share

    return {
        "entry_low": entry_low,
        "entry_high": entry_high,
        "stop": stop,
        "target": target,
        "shares": shares,
        "risk_usd": risk_usd,
    }


def format_trade_plan(plan: dict | None) -> str | None:
    if not plan:
        return None
    return (f"  • **Trade plan:** entry ${plan['entry_low']:.2f}-${plan['entry_high']:.2f}, "
            f"stop ${plan['stop']:.2f}, target ${plan['target']:.2f} "
            f"(~{plan['shares']} sh, ~${plan['risk_usd']:.0f} at risk)")


TRADE_PLAN_DISCLAIMER = (
    "_Trade plan levels are volatility-based (ATR) estimates, not "
    "recommendations -- not historically backtested. Confirm before "
    "entering; exit discipline is on you._"
)


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
                        price, target, atr=None, sector_note: str | None = None,
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
        if cat in (CAUTION_CATEGORY, EARNINGS_QUALITY_CATEGORY):
            continue  # both shown separately below with a warning marker
        label = CATEGORY_LABELS.get(cat, cat)
        bullets.append(f"  • **{label}:** {info['detail']}")
    if CAUTION_CATEGORY in categories:
        bullets.append(f"  • \u26A0\uFE0F **Caution:** {categories[CAUTION_CATEGORY]['detail']}")
    if EARNINGS_QUALITY_CATEGORY in categories:
        bullets.append(f"  • \u26A0\uFE0F **Earnings quality:** {categories[EARNINGS_QUALITY_CATEGORY]['detail']}")
    if sector_note:
        bullets.append(f"  • **Sector:** {sector_note}")
    plan_bullet = format_trade_plan(compute_trade_plan(price, atr, STOP_ATR_MULT))
    if plan_bullet:
        bullets.append(plan_bullet)

    return header + "\n" + "\n".join(bullets)


def format_momentum_line(rank: int, symbol: str, name: str, info: dict, price, atr=None) -> str:
    """
    Deliberately distinct formatting from format_ticker_line -- no
    STRONG/Moderate tier tag (that vocabulary belongs to the confluence
    system), a different emoji, and an explicit risk note so this never
    reads as equivalent conviction to a quality-backed pick. Trade plan
    (when present) uses MOMENTUM_STOP_ATR_MULT -- tighter than the main
    list's, since these setups move fast.
    """
    price_bit = f" — ${price:.2f}" if price else ""
    display_name = clean_company_name(name) if name else symbol
    header = f"\u26A1 **#{rank} {symbol}**{price_bit} _{display_name}_"
    bullet = f"  • {info['detail']}"
    note = "  • _Speculative: low float + volume spike, not fundamentals-backed_"
    lines = [header, bullet, note]
    plan_bullet = format_trade_plan(compute_trade_plan(price, atr, MOMENTUM_STOP_ATR_MULT))
    if plan_bullet:
        lines.append(plan_bullet)
    return "\n".join(lines)


def build_momentum_section(momentum_ranked: list, company_names: dict, prices: dict,
                            byte_budget: int, max_picks: int, atrs: dict | None = None) -> tuple[str, int, int]:
    """
    Builds the reserved speculative section. Returns (section_text,
    included_count, total_qualifying_count). Capped by BOTH max_picks and
    byte_budget (UTF-8 bytes, see truncate_to_whole_entries) -- whichever
    is more restrictive wins -- so this section can never grow large
    enough to threaten the main list's space.
    """
    if not momentum_ranked:
        return "", 0, 0

    atrs = atrs or {}
    capped = momentum_ranked[:max_picks]
    lines = [
        format_momentum_line(i, sym, company_names.get(sym, ""), info, prices.get(sym), atrs.get(sym))
        for i, (sym, info) in enumerate(capped, start=1)
    ]
    header = "\u26A1 **Speculative / High-Risk** (low float + volume spike)\n\n"
    # Header bytes reserved BEFORE truncating the body -- it used to be
    # prepended after truncation, uncounted against the budget, same class
    # of bug fixed in main()'s message assembly.
    body_budget = byte_budget - _utf8_len(header)
    body, included = truncate_to_whole_entries(lines, body_budget)
    if not body:
        return "", 0, len(momentum_ranked)

    section = header + body
    return section, included, len(momentum_ranked)



def _utf8_len(s: str) -> int:
    return len(s.encode("utf-8"))


def _hard_truncate_utf8(s: str, max_bytes: int) -> str:
    """
    Last-resort truncation that can't split a multi-byte UTF-8 character
    in half (which would corrupt the string / crash decoding). Used only
    as a structural safety net -- see the comment at its call site in
    main() -- normal operation should never actually reach this.
    """
    encoded = s.encode("utf-8")
    if len(encoded) <= max_bytes:
        return s
    return encoded[:max_bytes].decode("utf-8", errors="ignore")


def truncate_to_whole_entries(entries: list[str], byte_limit: int) -> tuple[str, int]:
    """
    Joins entries with blank-line separators, but stops adding whole
    entries once the next one would exceed `byte_limit` -- so the message
    never cuts a ticker off mid-way through. Returns (message, entries_included).

    IMPORTANT: byte_limit is UTF-8 encoded BYTES, not Python string
    length. This matters a lot here specifically -- every STRONG tier tag
    and caution bullet has an emoji in it, and emoji are 3-4+ bytes each
    in UTF-8 despite being 1-2 Python characters. Measuring in Python
    string length was the root cause of a real production bug: it let a
    message quietly grow past ntfy's actual (byte-based) 4096-byte limit
    while still reporting as "under budget" -- see NTFY_MESSAGE_BYTE_LIMIT
    in config.py.
    """
    included = []
    total_bytes = 0
    separator_bytes = 2  # "\n\n", both ASCII
    for entry in entries:
        entry_bytes = _utf8_len(entry) + (separator_bytes if included else 0)
        if total_bytes + entry_bytes > byte_limit:
            break
        included.append(entry)
        total_bytes += entry_bytes
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

    # Rank by confidence, category count first then combined strength;
    # tiebreak_key is the last-resort tertiary key for any exact ties
    # left after the upstream scans' evidence-count bonus.
    ranked = sorted(
        qualifying.items(),
        key=lambda kv: (*score_ticker(kv[1]), tiebreak_key(kv[0])),
        reverse=True,
    )
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
    price_atr = fetch_prices_and_atr(symbols_to_price)
    prices = {sym: v["price"] for sym, v in price_atr.items()}
    atrs = {sym: v["atr"] for sym, v in price_atr.items()}

    # Computed BEFORE the message body so we can embed a real markdown
    # hyperlink in the text itself, not just rely on ntfy's Click header
    # (which makes the notification-as-a-whole tappable in some clients,
    # but doesn't reliably work from an expanded/copyable message view --
    # a proper [text](url) markdown link is more consistent across
    # clients since Markdown: yes is already set on this push).
    click_url = f"{REPO_URL}/blob/main/{LATEST_ALERTS_FILE}" if REPO_URL else None

    lines = []
    for rank, sym, cats in push_list:
        price = prices.get(sym)
        atr = atrs.get(sym)
        target = fetch_price_target(sym)
        name = company_names.get(sym, "")
        sector_note = find_sector_annotation(sectors.get(sym, ""), active_sector_alerts)
        is_new = not was_recently_alerted(sym)
        lines.append(format_ticker_line(rank, sym, name, cats, price, target, atr, sector_note, is_new))

    # Footer pieces are built FIRST, in their final form, so their exact
    # byte cost is known BEFORE deciding how many ticker lines fit --
    # rather than truncating lines to a budget and hoping whatever gets
    # appended afterward still fits (that gap is what caused a real
    # message to blow past ntfy's 4096-byte limit and get silently
    # converted to a file attachment instead of shown as text).
    footer = ""
    if len(ranked_with_rank) > len(push_list):
        remaining = len(ranked_with_rank) - len(push_list)
        if click_url:
            footer += f"\n\n**[View all {len(ranked_with_rank)} qualifying picks →]({click_url})** ({remaining} more than fit in this push)"
        else:
            footer += (f"\n\n_{remaining} more qualifying pick(s) in {LATEST_ALERTS_FILE} in the repo "
                        f"(no REPO_URL set, so no direct link -- see config.py)_")
    # Conservative: reserve room for the disclaimer if ANY candidate line
    # has a trade plan, not just the ones that end up fitting -- slightly
    # over-reserves in the rare case every trade-plan line gets truncated
    # out, which is the safe direction to be wrong in.
    disclaimer_needed = any("**Trade plan:**" in line for line in lines)
    if disclaimer_needed:
        footer += f"\n\n{TRADE_PLAN_DISCLAIMER}"

    # Fixed allowance for the "+N more of this push didn't fit here" note
    # -- reserved unconditionally since whether it's actually needed
    # depends on the truncation decision this budget feeds into.
    TRUNCATION_NOTE_ALLOWANCE = 80

    available_for_lines = NTFY_SAFE_BODY_BYTE_BUDGET - _utf8_len(footer) - TRUNCATION_NOTE_ALLOWANCE
    lines_text, included_count = truncate_to_whole_entries(lines, available_for_lines)

    message = lines_text
    if included_count < len(lines):
        message += f"\n\n_...+{len(lines) - included_count} more of this push didn't fit here._"
    message += footer

    # Structural safety net, not just careful arithmetic: if some future
    # change adds text without updating the budget above, this still
    # guarantees the message can never silently become an unreadable
    # attachment -- it gets a visibly-truncated message instead, which is
    # a much louder, easier-to-notice failure mode.
    if _utf8_len(message) > NTFY_MESSAGE_BYTE_LIMIT - 96:
        message = _hard_truncate_utf8(message, NTFY_MESSAGE_BYTE_LIMIT - 96)
        message += "\n\n_(hard-truncated to fit -- see repo for full detail)_"

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
    # (not carved out of the main list's byte budget). Sent independently
    # of whether the main list fired, so it's never at the mercy of how
    # busy the main confluence list is on a given cycle -- which in
    # practice is "full or nearly full" almost every cycle for this
    # screener, so a shared/leftover budget would rarely show anything.
    momentum_symbols = [sym for sym, _ in momentum_ranked[:MOMENTUM_MAX_PICKS_IN_PUSH]]
    momentum_price_atr = fetch_prices_and_atr(momentum_symbols)
    momentum_prices = {sym: v["price"] for sym, v in momentum_price_atr.items()}
    momentum_atrs = {sym: v["atr"] for sym, v in momentum_price_atr.items()}
    momentum_section, momentum_included, momentum_total = build_momentum_section(
        momentum_ranked, company_names, momentum_prices, MOMENTUM_PUSH_CHAR_BUDGET,
        MOMENTUM_MAX_PICKS_IN_PUSH, momentum_atrs
    )
    if momentum_section:
        momentum_title = f"\u26A1 {momentum_included} speculative pick(s)"
        if momentum_total > momentum_included:
            momentum_title += f" +{momentum_total - momentum_included} more in repo"
        if momentum_included < momentum_total:
            remaining = momentum_total - momentum_included
            if click_url:
                momentum_section += f"\n\n**[View all {momentum_total} speculative picks →]({click_url})** ({remaining} more than fit in this push)"
            else:
                momentum_section += f"\n\n_{remaining} more speculative pick(s) in {LATEST_ALERTS_FILE} in the repo_"
        if "**Trade plan:**" in momentum_section:
            momentum_section += f"\n\n{TRADE_PLAN_DISCLAIMER}"
        # Same structural safety net as the main message -- build_momentum_section
        # already reserves its own header's bytes, but this push's footer
        # (link + disclaimer) is appended after that budget check, same
        # gap that caused the main push's bug, so it needs the same guard.
        if _utf8_len(momentum_section) > NTFY_MESSAGE_BYTE_LIMIT - 96:
            momentum_section = _hard_truncate_utf8(momentum_section, NTFY_MESSAGE_BYTE_LIMIT - 96)
            momentum_section += "\n\n_(hard-truncated to fit -- see repo for full detail)_"
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
