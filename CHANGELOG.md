# Changelog

Manual code/config changes only — automated data commits (scans, trade log
syncs) are not logged here. Check this file at the start of any work
session before diagnosing or re-fixing something, since commit messages
for automated runs all look identical and won't show what's already
been touched.

## 2026-09-30
Audit of this log against the live files (pulled from `main`, 2026-09-30 19:38 UTC).
Corrections to earlier entries are listed first, then changes made.

Corrections:
- 9/24 "migrated off native `schedule:`" was incomplete: cron-job.org
  was added, but the native `schedule:` blocks stayed in `scan.yml` and
  `intraday.yml`, so both triggers fired. Removed below.
- 9/24 "added `timeout=` to `yf.download()` in `filters.py` and
  `compose_alerts.py`" was only true for `filters.py`. The call in
  `compose_alerts.py` (`fetch_prices_and_atr`) had no timeout. Fixed
  below.
- The ranking overhaul from a parallel session (`confidence_score()`,
  widening `REVENUE_EPS_GROWTH_DIVISOR` 30->60 and
  `OUTPERFORMANCE_DIVISOR` 15->40, raising
  `PER_CATEGORY_STRENGTH_CEILING`) is NOT in the repo. Live code still
  uses `/30` (fundamentals) and `/15` (technicals) saturating caps, and
  `score_ticker()` still returns raw total strength. Tie-clustering is
  addressed only by the 9/26 `combine_strengths()` change.

Changes:
- `scan.yml`, `intraday.yml`: removed the native `schedule:` blocks;
  both are now `workflow_dispatch`-only, triggered by cron-job.org.
  Late native runs were overlapping cron-job.org runs in the concurrency
  group (one pending slot, so extras were cancelled) and risking
  duplicate scans/alerts. `watchdog.yml` keeps its native schedule on
  purpose (separate backstop).
- `compose_alerts.py`: added `PRICE_FETCH_TIMEOUT_SECONDS = 30` and
  passed it as `timeout=` to the `yf.download()` in
  `fetch_prices_and_atr()`.
- `technicals_scan.py`, `signals_store.py` (already live, logged here):
  added `clear_signals_batch()`; each intraday cycle now clears stale
  "technical" and "caution" signals for tickers that were evaluated
  successfully but produced no findings. Tickers whose fetch failed are
  left untouched.

Known gaps (not changed):
- `compose_alerts.py`: comments near `tiebreak_key()` and the `ranked =`
  sort still reference the removed "evidence-count bonus".
- `compose_alerts.py`: inner per-symbol `except Exception: continue` in
  `fetch_prices_and_atr()` is still unlogged (see 9/24 note).
- `config.py`: `SIGNAL_VALIDITY_HOURS` has no `"caution"` key, so
  caution signals fall back to the 24h default. Consider `"caution": 4`.

## 2026-09-26
- Rewrote category strength combining (`fundamentals_scan.py`,
  `technicals_scan.py`) from `max(strengths) + capped bonus` to a new
  `combine_strengths()` helper in `signals_store.py`: sorts findings
  strongest-first, sums with geometric decay (0.6x per rank). Fixes
  large exact-tie clusters in rankings (e.g. 9 tickers tied at 2.04 on
  9/24) caused by `max()` discarding all but the top finding. Preserves
  relative signal weighting — top finding still counts most.
  - Note: raises the achievable ceiling per category (a category with
    3-4 findings can now land ~1.6-1.8 vs the old ~1.03-1.05 cap).
    `STRONG_TIER_STRENGTH_FOR_TWO` (1.5) and `MIN_QUALIFYING_STRENGTH`
    (1.0) in `config.py` were tuned against the old scale — watch
    whether more tickers hit STRONG-via-2-categories than expected and
    retune those two constants if so.

## 2026-09-24
- `compose_alerts.py`: removed verbose disclaimer footer and repetitive
  "most signals don't resolve" text from every ticker alert.
- `compose_alerts.py`: added stderr logging for silent price/ATR fetch
  failures in the outer batch-level exception handler. (Known gap: the
  *inner* per-symbol `except Exception: continue` in
  `fetch_prices_and_atr()` still isn't logged — this is why TSLA's
  missing trade plan on 9/24 couldn't be root-caused from logs alone.
  Add logging there next before investigating further per-symbol fetch
  gaps.)
- `filters.py`, `compose_alerts.py`: added `timeout=` to `yf.download()`
  calls — fixed wildly variable daily-scan runtime (15 min vs 2 hrs).
- Migrated `scan.yml` and `intraday.yml` off GitHub Actions' native
  `schedule:` trigger (confirmed unreliable — delayed hours or not
  firing at all, a known GitHub platform issue) to cron-job.org calling
  the `workflow_dispatch` REST API directly. Added `watchdog.py` +
  `watchdog.yml` to alert if the daily scan hasn't started by ~9am ET.
- `news_scan.py`: fixed three regex bugs in the ticker-to-headline
  matcher — single-letter ticker colliding with sentence-initial
  capitalization, digit-stripping breaking tickers like "Five9", and
  single-letter tickers matching inside dotted abbreviations (e.g. "U"
  in "U.S.").
- `delisting_risk_scan.py`: added retries + fail-open behavior so a
  single SEC EDGAR error no longer crashes the entire daily scan
  pipeline.
- `position_monitor.py`: added `drawdown_threshold` condition (alerts
  once when a position drops ≥10% from entry, independent of
  stop/target). Wired into `intraday.yml` to run every 30 min during
  market hours. Added `POSITION_DRAWDOWN_ALERT_PCT = 10.0` to
  `config.py`.
- Considered demoting News from a full confluence signal to
  informational-only — declined for now in favor of the regex fixes.
