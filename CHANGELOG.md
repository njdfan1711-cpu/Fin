# Changelog

Manual code/config changes only — automated data commits (scans, trade log
syncs) are not logged here. Check this file at the start of any work
session before diagnosing or re-fixing something, since commit messages
for automated runs all look identical and won't show what's already
been touched.

## 2026-10-06 (cleanup)
Built from live `main` (HEAD 662ea41, pulled 2026-10-06). Housekeeping only;
no ranking, trade-plan or alert-content changes. Swing track only.

- Deploy note: the 2026-10-03 (scorecard) package below, plus the
  `track_outcomes.py` and `scan.yml` edits, were uploaded to `main` on
  2026-10-06 (commits 185189b, 088a73d, 662ea41), not 10-03.
- `config.py`: added `"caution": 4` to `SIGNAL_VALIDITY_HOURS`. The
  technicals scan writes cautions under the `"caution"` category and
  rewrites them every run, but with no key they fell through to the 24h
  default and could linger well past the 4h `"technical"` window.
- `compose_alerts.py`: two stale comments (in `tiebreak_key` and the
  ranking step) referred to an upstream "evidence-count bonus" that no
  longer exists; they now point to `combine_strengths` (9/26 change).
- `compose_alerts.py`: the per-symbol `except` in `fetch_prices_and_atr`
  now logs `[price/ATR parse error] SYM: ...` to stderr instead of
  silently skipping the ticker.
- Still open: delete stray `compose_alerts-1.py` (manual, via GitHub UI);
  `intraday.yml` guard step mentioned in `scalping/CHANGELOG.md` is absent.

## 2026-10-03 (scorecard)
Built from live `main` (HEAD 0deca82, pulled 2026-10-03). Per-feature
scorecard for the swing track only (not scalping). Tested offline
(synthetic data + a real backfill run); first live runs should be watched.

- New `features.py`: turns a push's signal/caution text into stable tags
  (`tech:rsi_oversold`, `fund:eps_growth`, `caut:extended_above_ma`,
  `atr:low(<3%)`, `caut:chase`, `tier:*`, `cats:*`, ...). Pure functions.
- `compose_alerts.py`: new `build_push_features()`; `record_push()` now
  stores a `features` list per push (daily_pushes.json is pruned long
  before outcomes resolve, so the tags must be saved at push time).
- `track_outcomes.py`: copies `features` into each new outcome_history
  entry.
- New `backfill_features.py` (idempotent): recovers features for entries
  resolved before this existed, by matching each to its run in
  `alerts_history/*.md` (push timestamp + symbol) and rejecting any match
  whose tier / signal count / strength disagrees with the entry. Writes
  the sidecar `outcome_features.json` (a separate static-ish file, so it
  never clobbers `outcome_history.json`). First run: 4,554 of 5,220
  entries recovered, 0 rejected. Unrecoverable: pushes before 2026-08-19
  (alerts_history starts 8/19 18:05), 5 on 9/21, and 142 no_data entries.
- New `scorecard.py` -> `scorecard.md`: per feature, n, distinct tickers,
  stop%, target%, avg R-multiple (stop = -1R, target = +2R, else marked at
  the day-7 close), win% with a 95% Wilson interval, lift vs baseline;
  < 30 samples labelled insufficient data; always-present features hidden;
  one sample per ticker per day; includes a take-profit/path section that
  fills in as path-tracked entries resolve. Regenerates weekly (skips if
  the report is < 7 days old; `--force` overrides). Stop-outs are capped
  at -1R by construction (gap-throughs not modelled).
- `scan.yml`: two new `continue-on-error` steps after "Track outcomes"
  (backfill, then scorecard); `outcome_features.json` and `scorecard.md`
  added to the commit list. The backfill step is a no-op once every
  pre-feature push has resolved (~1-2 weeks).
- Early read (hypotheses, NOT tuning guidance): baseline over 958
  ticker-days (8/19-9/25): stop 32%, target 5%, avg R -0.11, win 41%.
  `caut:extended_above_ma` (n=183) and `caut:analyst_deteriorating`
  (n=53) did worse than baseline with intervals excluding it;
  `atr:high(>=4.5%)` did better. `atr:low(<3%)` was roughly average,
  which does not support the premise behind LOW_ATR_PCT_CAUTION (0/171
  targets in a smaller sample) -- revisit with more data, don't retune
  yet. ~30 features were tested, so a few flags are expected by chance.

Open items found while checking the repo (not changed here):
- Stray `compose_alerts-1.py` in the repo root (from an "Add files via
  upload" commit; differs from `compose_alerts.py`, nothing imports it).
  Safe to delete once confirmed it is not wanted.
- `scalping/CHANGELOG.md` (10/02) says a guard step was added to
  `intraday.yml`; the live `intraday.yml` has no such step. Unresolved.

## 2026-10-03
Built from live `main` (pulled 2026-10-03). Four changes from the review of
13 closed trades (13 wins, +$579.62, avg +2.1%, ~4d hold) and the 1,075
unique resolved pushes in `outcome_history.json`. Offline tests only so far
(synthetic bars / mocked yfinance); first live runs should be watched.

- Take-profit level: `compose_alerts.py` `compute_trade_plan()` now adds
  `take_profit = price + TAKE_PROFIT_ATR_MULT * ATR` (new
  `TAKE_PROFIT_ATR_MULT = 0.5` in `config.py`, ~+1.9% at the median ATR).
  Shown in the push and `latest_alerts.md` ("take-profit $X (+Y%)"); the
  full 3-ATR target stays but is labelled "full target". Why: only ~5% of
  pushes hit the full target inside 7 days; real exits cluster near +2%.
  `position_monitor.py` adds a `take_profit_reached` alert, measured from
  the price actually paid (ATR is recovered from the plan's entry band, so
  it also works on plans recorded before this change).
- Chase flag: `compose_alerts.py` `fetch_prices_and_atr()` now also returns
  `prev_close` and `close_5d`; new `compute_chase_info()` /
  `format_chase_caution()` add a display-only "Chase risk" caution when a
  pick is up >= `CHASE_DAY_ATR_MULT` (1.0) ATR today or
  >= `CHASE_5D_ATR_MULT` (2.0) ATR over ~5 bars. Does not affect ranking.
  Logged per push as `chase` in `daily_pushes.json`. Caveat: a back-test on
  526 consecutive-day push pairs was inconclusive (stop rate ~35% both for
  >=1 ATR run-ups and flat days), so treat as a prompt, not a proven edge.
- Path tracking: `track_outcomes.py` new `compute_path_metrics()` adds
  `max_favorable_pct`, `max_adverse_pct`, `tp1_level`, `tp1_outcome`
  (`tp1_first` / `stop_first` / `neither`; same-day double breach counts as
  stop-first) and `days_to_tp1` to every newly resolved entry, plus
  `atr_at_push` and `chase`. Only entries resolved after this deploys have
  them (no backfill; yfinance history is not stored). Use these to re-tune
  `TAKE_PROFIT_ATR_MULT` and to build the per-filter scorecard.
- Time-based reassess: `position_monitor.py` new `review_due` condition at
  `REVIEW_HOLD_MULTIPLIER` (1.0) x median days-to-target (~6d), softer and
  earlier than `overdue` (2.0x, unchanged). Message states days held and
  P&L vs entry. Suppressed once a stop, take-profit or `overdue` fires.
- `config.py`: added `TAKE_PROFIT_ATR_MULT`, `CHASE_DAY_ATR_MULT`,
  `CHASE_5D_ATR_MULT`, `REVIEW_HOLD_MULTIPLIER`.

Notes:
- Reward/risk reality check: with a 1.5-ATR stop and a 0.5-ATR take-profit,
  taking profit at the first level only pays if it is reached roughly 75%+
  of the time before the stop. Lower-bound hit rate from history is ~29%
  (upper ~61%; stop_hit paths unknown). Path tracking will settle this.
- Still open from earlier entries: stale "evidence-count bonus" comments in
  `compose_alerts.py`, unlogged inner `except` in `fetch_prices_and_atr`,
  and no `"caution"` key in `SIGNAL_VALIDITY_HOURS`.

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
