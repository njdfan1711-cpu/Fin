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
]

LOW_ATR_PCT = 3.0   # mirrors config.LOW_ATR_PCT_CAUTION (kept local: no import cycle)


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
                     category_count=None, atr_pct=None, chase_flagged=None) -> list:
    """
    signals:  {"technical": "<detail>", "fundamentals": "<detail>", "news": "<detail>", ...}
              (non-caution categories only; unknown keys are ignored)
    cautions: list of caution detail strings (earnings-quality / caution /
              news-caution lines). A 'news caution' is any caution whose text
              matches none of the known patterns.
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
    return sorted(tags)
