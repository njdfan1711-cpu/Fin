"""
Feature tagging for the Fin swing-track scorecard.

Turns a push's signal/caution text into stable, normalized tags such as
"tech:rsi_oversold" or "caut:extended_above_ma", so outcomes can be
grouped per feature (see scorecard.py). Works on the plain detail strings
that already exist at push time AND in alerts_history/*.md, so the same
code tags live pushes and recovers tags for historical ones.

Pure functions, no I/O, no network.
"""

import re
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")

# (regex, tag) -- matched against each ';'-separated finding in a category's
# detail string. First match wins per finding. Order matters where phrases
# overlap (the '52-week high' variants).
_TECH_PATTERNS = [
    (r"^Outperforming S&P 500", "tech:outperform_sp500"),
    (r"^Price above rising", "tech:above_rising_50_200ma"),
    (r"^RSI oversold", "tech:rsi_oversold"),
    (r"^RSI overbought", "tech:rsi_overbought"),
    (r"^MACD bullish crossover", "tech:macd_bullish_cross"),
    (r"^Relative strength line", "tech:rs_line_new_high"),
    (r"^New ALL-TIME high", "tech:all_time_high"),
    (r"52-week high confirmed by volume", "tech:52wk_high_vol_confirmed"),
    (r"52-week high, but still", "tech:52wk_high_below_ath"),
    (r"^Volume spike", "tech:volume_spike"),
    (r"MA bullish crossover", "tech:ma_20_50_cross"),
]
_FUND_PATTERNS = [
    (r"^Revenue growth", "fund:revenue_growth"),
    (r"^EPS growth", "fund:eps_growth"),
    (r"^Quality checklist passed", "fund:quality_passed"),
    (r"^Analyst sentiment improving", "fund:analyst_improving"),
    (r"^Earnings beat", "fund:earnings_beat"),
]
_CAUTION_PATTERNS = [
    (r"Net margin -", "caut:negative_net_margin"),
    (r"Extended .*above .*MA", "caut:extended_above_ma"),
    (r"on light volume", "caut:high_on_light_volume"),
    (r"Analyst sentiment deteriorating", "caut:analyst_deteriorating"),
    (r"Earnings scheduled today", "caut:earnings_today"),
    (r"Earnings scheduled in", "caut:earnings_soon"),
    (r"^up [+-]?[\d.]+% today", "caut:chase"),
]

LOW_ATR_PCT = 3.0   # mirrors config.LOW_ATR_PCT_CAUTION (kept local: no import cycle)


# ---------------------------------------------------------------------------
# Time-of-day and volume helpers (added 2026-10-07)
#
# The scan's relative-volume ratio is volume so far today / the 20-day average
# of FULL days, so it is structurally low mid-session (a normal day reads ~0.4x
# at noon). These helpers tag WHEN a push fired and a time-adjusted volume
# bucket for new-52-week-high pushes. Tag-only: nothing here changes ranking,
# cautions or alert text.
# ---------------------------------------------------------------------------

# (minutes after 9:30 ET, approx cumulative share of the day's volume). A rough
# U-shaped US-equity intraday profile -- a heuristic, not measured from this
# repo's data. Revisit if the scorecard shows the buckets are mis-calibrated.
_CUM_VOLUME_CURVE = [(0, 0.0), (30, 0.15), (90, 0.30), (150, 0.43), (210, 0.53),
                     (270, 0.63), (330, 0.75), (360, 0.85), (390, 1.0)]
_VOL_RATIO = re.compile(r"(?:on light volume|confirmed by volume) \(([\d.]+)x")


def _to_et(asof):
    if asof is None:
        return None
    if asof.tzinfo is None:
        asof = asof.replace(tzinfo=timezone.utc)
    return asof.astimezone(ET)


def expected_volume_fraction(asof):
    """Approx. share of a full day's volume traded by `asof` (1.0 outside RTH
    hours or on weekends; None if no timestamp)."""
    et = _to_et(asof)
    if et is None:
        return None
    if et.weekday() >= 5:
        return 1.0
    mins = et.hour * 60 + et.minute - (9 * 60 + 30)
    if mins <= 0:
        return 0.0
    if mins >= 390:
        return 1.0
    for (m0, f0), (m1, f1) in zip(_CUM_VOLUME_CURVE, _CUM_VOLUME_CURVE[1:]):
        if m0 <= mins <= m1:
            return f0 + (f1 - f0) * (mins - m0) / (m1 - m0)
    return 1.0


def time_bucket(asof):
    et = _to_et(asof)
    if et is None:
        return None
    if et.weekday() >= 5:
        return "time:closed"
    t = et.hour * 60 + et.minute
    if t < 9 * 60 + 30:
        return "time:pre_open"
    if t < 10 * 60 + 30:
        return "time:open_hour"
    if t < 14 * 60 + 30:
        return "time:midday"
    if t < 16 * 60:
        return "time:late_session"
    return "time:after_close"


def volume_at_high_bucket(technical_detail, cautions, asof):
    """Time-adjusted volume bucket for a new-52-week-high push, else None.

    Parses the raw ratio from the existing alert text ('on light volume
    (0.3x average)' / '52-week high confirmed by volume (1.8x average)'),
    divides by the expected cumulative volume share at push time. Skipped
    before 10:00 ET (the share is too small/noisy to divide by)."""
    et = _to_et(asof)
    if et is None:
        return None
    text = " ; ".join([technical_detail or ""] + list(cautions or []))
    m = _VOL_RATIO.search(text)
    if not m:
        return None
    if et.weekday() < 5 and et.hour * 60 + et.minute < 10 * 60:
        return None
    frac = max(expected_volume_fraction(asof) or 0.0, 0.10)
    adj = float(m.group(1)) / frac
    if adj < 0.8:
        return "volhi:low_adj(<0.8x)"
    if adj < 1.5:
        return "volhi:normal_adj(0.8-1.5x)"
    return "volhi:high_adj(>=1.5x)"


def age_tags(prior_days, runup_pct):
    """Signal-age tags from how many EARLIER trading days this ticker was
    already pushed (daily_pushes.py symbol_history) and the % move since the
    first of those pushes."""
    if prior_days is None:
        return []
    tags = []
    if prior_days == 0:
        tags.append("age:new(1d)")
    elif prior_days <= 3:
        tags.append("age:recurring(2-4d)")
    else:
        tags.append("age:stale(5d+)")
    if prior_days > 0 and runup_pct is not None:
        if runup_pct < 2:
            tags.append("runup:<2%")
        elif runup_pct < 5:
            tags.append("runup:2-5%")
        else:
            tags.append("runup:>=5%")
    return tags


def _tag_findings(detail: str, patterns) -> set:
    tags = set()
    for part in re.split(r";\s+", detail or ""):
        part = part.strip()
        for rx, tag in patterns:
            if re.search(rx, part):
                tags.add(tag)
                break
    return tags


def atr_bucket(atr_pct):
    if atr_pct is None:
        return None
    if atr_pct < LOW_ATR_PCT:
        return "atr:low(<3%)"
    if atr_pct < 4.5:
        return "atr:mid(3-4.5%)"
    return "atr:high(>=4.5%)"


def extract_features(signals: dict, cautions: list | None = None, *, tier=None,
                     category_count=None, atr_pct=None, chase_flagged=None,
                     asof=None, prior_push_days=None, runup_pct=None) -> list:
    """
    signals:  {"technical": "<detail>", "fundamentals": "<detail>", "news": "<detail>", ...}
              (non-caution categories only; unknown keys are ignored)
    cautions: list of caution detail strings (earnings-quality / caution /
              news-caution lines). A 'news caution' is any caution whose text
              matches none of the known patterns.
    asof:     tz-aware datetime of the push (enables time:/volhi: tags).
    prior_push_days / runup_pct: signal-age inputs (enables age:/runup: tags).
    Returns a sorted, de-duplicated list of tag strings.
    """
    tags = set()
    signals = signals or {}
    for cat in ("technical", "fundamentals", "news"):
        if signals.get(cat):
            tags.add(f"cat:{cat}")
    tags |= _tag_findings(signals.get("technical", ""), _TECH_PATTERNS)
    tags |= _tag_findings(signals.get("fundamentals", ""), _FUND_PATTERNS)

    for text in (cautions or []):
        matched = False
        for part in re.split(r";\s+", text or ""):
            for rx, tag in _CAUTION_PATTERNS:
                if re.search(rx, part):
                    tags.add(tag)
                    matched = True
        if not matched and text:
            tags.add("caut:news_caution")

    if tier:
        tags.add(f"tier:{tier}")
    if category_count:
        tags.add(f"cats:{category_count}")
    b = atr_bucket(atr_pct)
    if b:
        tags.add(b)
    if chase_flagged is True:
        tags.add("caut:chase")
    tb = time_bucket(asof)
    if tb:
        tags.add(tb)
    vb = volume_at_high_bucket(signals.get("technical", ""), cautions, asof)
    if vb:
        tags.add(vb)
    tags.update(age_tags(prior_push_days, runup_pct))
    return sorted(tags)
