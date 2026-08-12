"""
fundamentals_scan.py

Runs once daily. Checks eligible.csv against Finnhub's earnings-surprise
and basic-financials endpoints.

IMPORTANT FIX (post-launch): the original version matched on "the most
recent known earnings beat" with no regard for how long ago that was --
which meant a beat from months earlier still matched every single day,
forever. That's what caused the 329-ticker alert. This version only
counts an earnings beat if it was actually reported within the last
EARNINGS_RECENCY_DAYS (see config.py) -- i.e. it has to be genuinely
recent news, not old news still sitting in the data.

PERFORMANCE FIX (this version): the earnings-surprise check used to make
one Finnhub /stock/earnings call PER eligible ticker -- at 2,442 eligible
tickers that's ~2,442 calls, roughly half of this script's ~89-minute
runtime on its own. Finnhub's /calendar/earnings endpoint returns EVERY
company that reported (or is scheduled to report) in a date range in ONE
call, so this version fetches the whole recency window once and matches
it locally against eligible.csv -- same recency window, same surprise-%
threshold, same signal quality, roughly half the API calls.

NOTE ON ACCURACY: /calendar/earnings' "date" field is documented as the
actual earnings release/announcement date. The old /stock/earnings
"period" field used before was actually the fiscal quarter-END date, not
the announcement date -- those can differ by several weeks, so the old
recency check ("Nd ago") was silently measuring the wrong thing for most
tickers. This version should be more accurate, not just faster.

CACHING FIX (this version): the other half of this script's runtime --
/stock/metric for revenue/EPS growth, the quality checklist, and the
float proxy -- still has no bulk equivalent on Finnhub's free tier, so
it's still one call per ticker. But that data only changes when a
company actually reports, not daily, so each ticker's metrics are now
cached (see METRICS_CACHE_FILE / METRICS_REFRESH_DAYS in config.py) and
only re-fetched once stale. The FIRST run after this change still costs
the full per-ticker pass -- every ticker starts with no cache entry, so
everything is "stale." From the second run onward, only tickers whose
cache has aged past METRICS_REFRESH_DAYS get a fresh call; everyone else
reuses their cached findings (and still gets a fresh signal recorded
today from that cached data -- caching the API call is not the same as
skipping the day's signal, so confluence scoring stays continuous).

If a fresh fetch fails (network hiccup, rate limit, etc.), the old cached
value is kept AND the cache timestamp is NOT advanced -- so that ticker
is retried on the next run rather than either losing its data for
METRICS_REFRESH_DAYS or silently caching an empty result.

Signals are RECORDED via signals_store.py, not pushed directly --
compose_alerts.py decides what's push-worthy based on confluence across
multiple signal categories.

IMPORTANT: Finnhub's exact field names (for both /calendar/earnings and
the 'metric' endpoint) can vary/evolve on Finnhub's side. This script
defensively checks a couple of plausible field name variants and skips
gracefully if none are present -- search FINNHUB_KEY_CHECK below if you
need to adjust these against a real response. I could not hit Finnhub's
live API from the network-restricted sandbox this was written in, so
watch the first real run's Actions log (the earnings-calendar record
count printed near the top) to confirm it's returning real data before
trusting it long-term.
"""

import csv
import json
import os
import sys
import time
import urllib.request
from datetime import date, datetime, timedelta, timezone

from config import (
    ELIGIBLE_FILE,
    FINNHUB_API_KEY,
    EARNINGS_SURPRISE_PCT,
    EARNINGS_RECENCY_DAYS,
    REVENUE_GROWTH_YOY_PCT,
    EPS_GROWTH_YOY_PCT,
    MAX_DEBT_TO_EQUITY,
    MIN_CURRENT_RATIO,
    MIN_ROE_PCT,
    MIN_NET_MARGIN_PCT,
    MIN_QUALITY_CHECKS_PASSED,
    FUNDAMENTALS_SIGNALS_FILE,
    FLOAT_DATA_FILE,
    METRICS_CACHE_FILE,
    METRICS_REFRESH_DAYS,
)
from signals_store import record_signal

BASE_URL = "https://finnhub.io/api/v1"
CALLS_PER_MINUTE = 55  # stay a little under Finnhub's 60/min free cap
SLEEP_BETWEEN_CALLS = 60.0 / CALLS_PER_MINUTE


def load_eligible() -> list[str]:
    with open(ELIGIBLE_FILE, newline="") as f:
        return [row["symbol"] for row in csv.DictReader(f)]


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "personal-stock-scanner"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_earnings_calendar(from_date: date, to_date: date) -> list[dict]:
    """One bulk call covering every symbol reporting in the window --
    replaces what used to be a /stock/earnings call per eligible ticker."""
    url = (f"{BASE_URL}/calendar/earnings?from={from_date.isoformat()}"
           f"&to={to_date.isoformat()}&token={FINNHUB_API_KEY}")
    try:
        data = _get(url)
    except Exception as e:
        print(f"  [earnings calendar error] {e}", file=sys.stderr)
        return []

    # FINNHUB_KEY_CHECK -- confirm this wrapper key against a real response.
    records = data.get("earningsCalendar")
    if records is None:
        print(f"  [WARNING] Expected key 'earningsCalendar' not found in response "
              f"(got top-level keys: {list(data.keys())}). Finnhub may have changed "
              f"this endpoint's shape -- update fetch_earnings_calendar().",
              file=sys.stderr)
        return []
    return records


def build_earnings_surprise_map(eligible: set) -> dict:
    """
    Returns {symbol: (detail, strength)} for eligible tickers with a
    qualifying, sufficiently-recent earnings beat. Replaces the old
    per-ticker check_earnings_surprise() loop with one bulk calendar call.
    """
    today = date.today()
    from_date = today - timedelta(days=EARNINGS_RECENCY_DAYS)
    records = fetch_earnings_calendar(from_date, today)
    print(f"  Earnings calendar: {len(records)} report(s) in the last "
          f"{EARNINGS_RECENCY_DAYS} day(s) (all symbols, before filtering "
          f"to your eligible universe)", file=sys.stderr)

    results = {}
    skipped_no_estimate = 0
    for rec in records:
        symbol = rec.get("symbol")
        if symbol not in eligible:
            continue

        # FINNHUB_KEY_CHECK -- confirm these field names against a real
        # response: date (announcement date), epsActual, epsEstimate.
        period_str = rec.get("date")
        actual = rec.get("epsActual")
        estimate = rec.get("epsEstimate")
        if not period_str:
            continue
        if actual is None or estimate in (None, 0):
            skipped_no_estimate += 1
            continue

        try:
            period_date = datetime.strptime(period_str, "%Y-%m-%d").date()
        except ValueError:
            continue

        # The calendar can include near-future SCHEDULED reports as well
        # as past ones -- only count ones that have actually happened and
        # fall within the recency window.
        days_ago = (today - period_date).days
        if days_ago < 0 or days_ago > EARNINGS_RECENCY_DAYS:
            continue

        surprise_pct = ((actual - estimate) / abs(estimate)) * 100
        if surprise_pct >= EARNINGS_SURPRISE_PCT:
            detail = f"Earnings beat by {surprise_pct:.1f}% ({days_ago}d ago)"
            strength = min(surprise_pct / 20, 1.0)
            # A symbol shouldn't appear twice inside a 5-6 day window in
            # practice, but keep the stronger reading defensively if it does.
            if symbol not in results or strength > results[symbol][1]:
                results[symbol] = (detail, strength)

    if skipped_no_estimate:
        print(f"  ({skipped_no_estimate} reported symbol(s) skipped -- no analyst "
              f"estimate on file to compare against)", file=sys.stderr)

    return results


def load_metrics_cache() -> dict:
    if os.path.exists(METRICS_CACHE_FILE):
        try:
            with open(METRICS_CACHE_FILE) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_metrics_cache(cache: dict):
    with open(METRICS_CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


def is_cache_stale(entry: dict | None) -> bool:
    """True if there's no cached entry, or it's older than
    METRICS_REFRESH_DAYS. Malformed entries are treated as stale rather
    than crashing the run."""
    if not entry:
        return True
    try:
        checked_at = datetime.fromisoformat(entry["checked_at"])
    except (KeyError, ValueError, TypeError):
        return True
    age_days = (datetime.now(timezone.utc) - checked_at).total_seconds() / 86400
    return age_days >= METRICS_REFRESH_DAYS


def check_revenue_growth(symbol: str):
    """
    Returns (findings, share_outstanding) on a successful API call, where
    findings is the existing list of [detail, strength] pairs and
    share_outstanding is a float (millions) or None. share_outstanding
    comes from the SAME 'metric' call already being made here -- feeds
    the separate momentum/low-float scan (see config.py) at zero extra
    API cost.

    Returns None (not a tuple) if the API call itself failed, so the
    caller can tell "fetched successfully, nothing qualified" apart from
    "fetch failed, don't trust/cache this" and act accordingly (keep the
    old cached value and retry next run instead of caching an empty result).
    """
    url = f"{BASE_URL}/stock/metric?symbol={symbol}&metric=all&token={FINNHUB_API_KEY}"
    try:
        data = _get(url)
    except Exception:
        return None
    metric = data.get("metric", {})
    findings = []

    # FINNHUB_KEY_CHECK -- confirm these field names against a real response
    # before relying on them long-term; trying the most commonly documented
    # variants for each. All of this comes from the ONE call above, so
    # adding these checks costs nothing extra in API calls.

    revenue_growth = (
        metric.get("revenueGrowthTTMYoy")
        or metric.get("revenueGrowthQuarterlyYoy")
        or metric.get("revenueGrowth3Y")
    )
    if revenue_growth is not None and revenue_growth >= REVENUE_GROWTH_YOY_PCT:
        findings.append((f"Revenue growth {revenue_growth:.1f}% YoY", min(revenue_growth / 30, 1.0)))

    eps_growth = (
        metric.get("epsGrowthTTMYoy")
        or metric.get("epsGrowthQuarterlyYoy")
        or metric.get("epsGrowth3Y")
    )
    if eps_growth is not None and eps_growth >= EPS_GROWTH_YOY_PCT:
        findings.append((f"EPS growth {eps_growth:.1f}% YoY", min(eps_growth / 30, 1.0)))

    # Quality checklist -- require most (not all) of these to pass, since
    # requiring every single one is too strict and would exclude solid
    # companies on one weak metric.
    checks_passed = []

    debt_to_equity = metric.get("totalDebt/totalEquityAnnual") or metric.get("totalDebt/totalEquityQuarterly")
    if debt_to_equity is not None and debt_to_equity < MAX_DEBT_TO_EQUITY:
        checks_passed.append(f"D/E {debt_to_equity:.2f}")

    current_ratio = metric.get("currentRatioAnnual") or metric.get("currentRatioQuarterly")
    if current_ratio is not None and current_ratio > MIN_CURRENT_RATIO:
        checks_passed.append(f"Current ratio {current_ratio:.2f}")

    roe = metric.get("roeTTM") or metric.get("roeAnnual")
    if roe is not None and roe > MIN_ROE_PCT:
        checks_passed.append(f"ROE {roe:.1f}%")

    net_margin = metric.get("netProfitMarginTTM") or metric.get("netProfitMarginAnnual")
    if net_margin is not None and net_margin > MIN_NET_MARGIN_PCT:
        checks_passed.append(f"Net margin {net_margin:.1f}%")

    if len(checks_passed) >= MIN_QUALITY_CHECKS_PASSED:
        detail = "Quality checklist passed (" + ", ".join(checks_passed) + ")"
        strength = len(checks_passed) / 4.0
        findings.append((detail, strength))

    # share_outstanding: Finnhub reports this in millions of shares.
    # FINNHUB_KEY_CHECK -- confirm field name against a real response.
    share_outstanding = metric.get("shareOutstanding")

    return findings, share_outstanding


def main():
    if not FINNHUB_API_KEY:
        print("FINNHUB_API_KEY not set -- skipping fundamentals scan.", file=sys.stderr)
        return

    symbols = load_eligible()
    eligible_set = set(symbols)
    metrics_cache = load_metrics_cache()
    stale_count = sum(1 for s in symbols if is_cache_stale(metrics_cache.get(s)))
    print(f"Running fundamentals scan on {len(symbols)} eligible tickers -- "
          f"{stale_count} need a fresh /stock/metric call this run "
          f"(~{stale_count / CALLS_PER_MINUTE:.0f} min expected), "
          f"{len(symbols) - stale_count} served from cache, "
          f"plus one bulk earnings-calendar call.", file=sys.stderr)

    # One bulk call for earnings surprises across the whole eligible
    # universe, instead of one call per ticker.
    earnings_map = build_earnings_surprise_map(eligible_set)
    print(f"  {len(earnings_map)} eligible ticker(s) have a qualifying recent "
          f"earnings beat.", file=sys.stderr)

    signals = {}
    total_signals = 0
    float_data = {}
    fresh_calls = 0
    served_from_cache = 0
    fetch_failures = 0

    for i, symbol in enumerate(symbols, start=1):
        details = []
        strengths = []

        r1 = earnings_map.get(symbol)
        if r1:
            details.append(r1[0])
            strengths.append(r1[1])

        cache_entry = metrics_cache.get(symbol)
        if is_cache_stale(cache_entry):
            result = check_revenue_growth(symbol)
            time.sleep(SLEEP_BETWEEN_CALLS)
            fresh_calls += 1
            if result is None:
                # Fetch failed -- reuse the old cached value if there is
                # one (without advancing its timestamp, so it's retried
                # next run), otherwise treat as "nothing today" without
                # writing a cache entry, so it's attempted fresh again
                # tomorrow rather than caching a false empty result.
                fetch_failures += 1
                if cache_entry:
                    findings = cache_entry.get("findings", [])
                    share_outstanding = cache_entry.get("share_outstanding")
                else:
                    findings, share_outstanding = [], None
            else:
                findings, share_outstanding = result
                metrics_cache[symbol] = {
                    "checked_at": datetime.now(timezone.utc).isoformat(),
                    "findings": findings,
                    "share_outstanding": share_outstanding,
                }
        else:
            served_from_cache += 1
            findings = cache_entry.get("findings", [])
            share_outstanding = cache_entry.get("share_outstanding")

        for detail, strength in findings:
            details.append(detail)
            strengths.append(strength)
        if share_outstanding is not None:
            float_data[symbol] = share_outstanding

        if details:
            # Combine into ONE fundamentals-category signal so a second
            # finding doesn't silently overwrite the first in the store.
            # Recorded every run regardless of whether today's metrics
            # came from a fresh call or the cache, so the signal doesn't
            # go stale/expire in signals_store just because the underlying
            # API call was skipped today.
            # Small per-finding bonus (capped, see technicals_scan.py's
            # matching comment) so tickers with more corroborating
            # fundamentals findings rank slightly ahead of otherwise-tied
            # ones, instead of falling back to arbitrary dict order.
            combined_detail = "; ".join(details)
            combined_strength = max(strengths) + min(0.05, 0.01 * (len(strengths) - 1))
            record_signal(symbol, "fundamentals", combined_detail, strength=combined_strength)
            signals[symbol] = details
            total_signals += len(details)

        if i % 100 == 0:
            print(f"  ...{i}/{len(symbols)} checked", file=sys.stderr)

    # Drop cache entries for tickers no longer in the eligible universe,
    # so this file doesn't grow forever as the universe turns over.
    metrics_cache = {s: v for s, v in metrics_cache.items() if s in eligible_set}
    save_metrics_cache(metrics_cache)

    with open(FUNDAMENTALS_SIGNALS_FILE, "w") as f:
        json.dump(signals, f, indent=2)

    with open(FLOAT_DATA_FILE, "w") as f:
        json.dump(float_data, f, indent=2)

    print(f"\n{total_signals} fundamentals signal(s) recorded "
          f"(only earnings beats within the last {EARNINGS_RECENCY_DAYS} days count).",
          file=sys.stderr)
    print(f"{fresh_calls} fresh /stock/metric call(s) made ({fetch_failures} failed and "
          f"fell back to cached/empty data), {served_from_cache} ticker(s) served "
          f"entirely from cache.", file=sys.stderr)
    print(f"{len(float_data)} share-outstanding value(s) written to {FLOAT_DATA_FILE} "
          f"for the momentum scan.", file=sys.stderr)


if __name__ == "__main__":
    main()
