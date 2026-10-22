## 2026-10-22 -- swing_backtest.py: replay of your own logged trades

Files: swing_backtest.py (replace), .github/workflows/swing_backtest.yml (replace; adds
swing_backtest_my_trades.csv to the commit list). trade_drawdown_report.py is unchanged.

- New section "Your logged trades replayed under the same rules": reads open_positions.json
  and, for each trade with an entry date, replays your real entry price/date under rules A
  (take-profit +0.5 ATR, stop 1.5 ATR, inactivity stop, 7-day max) and D (no stop), with
  ATR = simple 14-day average true range the day before entry. Compares with what you did
  (net %, days held, worst dip, whether Fin's stop level was reached), and shows each
  trade's rank among that day's Fin first-alerts plus Fin's top pick that day under rules A.
- Writes swing_backtest_my_trades.csv; summary also added to swing_backtest_summary.json
  ("your_trades_replayed") and swing_backtest.md.
- Overlaps with trade_drawdown_report.py (worst dip, stop reached); that report is kept.
- Tested offline only (ATR unit test, replay of the real 19-trade log on synthetic prices).

First live results of the base backtest (2026-10-22 run, 1,765 first-alerts): top-1/day
account under rules A: 50 trades, 74% win, -$5.26/trade; full target (B): +$2.13/trade;
no stop (D): +$12.89/trade (50 trades, noisy).


2026-10-21 -- New: swing_backtest.py (what if an API acted on Fin alerts?)
New files (no existing file changed): swing_backtest.py (repo root),
.github/workflows/swing_backtest.yml (workflow_dispatch only).
Outputs: swing_backtest_trades.csv, swing_backtest_summary.json, swing_backtest.md.
Replays every first-alert-of-the-day per symbol from outcome_history.json (Aug 13 on)
and daily_pushes.json against real daily bars (yfinance). Rules: Fin's stop
(STOP_ATR_MULT x ATR below entry); take-profit (TAKE_PROFIT_ATR_MULT x ATR) or the
full 3-ATR target; INACTIVITY stop (default: after 3 closes, if no close outside
+/-0.25 ATR of entry, sell at the close); 7-trading-day max hold; $3,500 position;
0.10% round-trip cost (assumption).
Entry timing: regular-session alert fills at price_at_push with exits checked from the
NEXT day; pre-open/weekend/after-close alerts fill at the next session's open.
Conservative conventions: stop counts first if a day touches both; gaps fill at the open.
Two views per scenario: "all" first-alerts (alert quality) and a "top1" account
(max 1 new position/day by Fin strength, max 5 open, no duplicate symbols).
Scenarios: A take-profit+stop+inactivity (base); B full target; C no inactivity stop;
D no stop (diagnostic for "hold through dips"). Plus an inactivity-rule sensitivity
grid and a cost sensitivity -- in-sample, do not tune on them.
Not replayed: your manual screen (Barchart/Google consensus, Snowflake, earnings
reaction) -- needs point-in-time data to avoid look-ahead.
Tested offline only (14 unit tests on synthetic bars covering every exit path and
entry timing, plus an end-to-end run on fake prices). First live run needs watching.
First read from existing path-tracked outcomes (450 first-alert symbol-days, Fin's own
tracking, no inactivity rule, no costs): take-profit reached before the stop 64.7% of
the time vs ~75% break-even; avg -0.91%/trade (about -$32 per $3,500). Top-1/day by
strength: 9 take-profit / 4 stop over 13 days (about break-even, tiny sample).

# Changelog

Manual code/config changes only — automated data commits (scans, trade log
syncs) are not logged here. Check this file at the start of any work
session before diagnosing or re-fixing something, since commit messages
for automated runs all look identical and won't show what's already
been touched.

## 2026-10-13 (neutral news no longer scores)
Built from live `main` (news_scan.py, config.py, compose_alerts.py pulled
2026-10-13; compose_alerts.py also carries the 2026-10-12 price/ATR changes).
Tested with mocked headlines and by re-scoring the published
`latest_alerts.md` (15:37 ET run); not yet seen in a live run.

Why: the 10-13 ASTS alert showed the headline "AST SpaceMobile's stock is
feeling the heat from SpaceX's wireless plans" as a positive **News** signal.
`classify_headline_sentiment()` is a keyword check, and that headline matched
neither list, so it was called "neutral". Neutral headlines were recorded
under the scored `news` category, which made ASTS 3 categories / strength 2.10
= STRONG. Without that line it is 2 categories / 1.40 = Moderate.

- `news_scan.py`: neutral headlines are now recorded under a new
  `news_neutral` category (shown on the alert, never scored). Only a headline
  that matches the bullish list is recorded as a scored `news` signal.
  Bearish still goes to `news_caution`, and bearish still wins if sources
  disagree. The run log summary now reports bullish / caution / neutral counts.
- `news_scan.py`: bearish keyword list widened with decline/pressure phrasing
  ("feeling the heat", "under pressure", "under fire", "threat(ens)", "slides",
  "slumps", "tumbles", "sinks", "falls", "drops", "sell-off", "disappoints",
  "setback", "outage", "delay(s)(ed)", "fined", "slashes", "cuts forecast /
  outlook / price target", "lowers guidance / outlook", "short seller / report",
  "SEC charges"). Generic words like "falls" and "drops" can mis-fire; a
  false bearish only moves a headline to a warning line, it never adds score.
- `compose_alerts.py`: new `NEWS_NEUTRAL_CATEGORY`, excluded in
  `score_ticker()` (so it can't count toward `MIN_SIGNAL_CATEGORIES` or the
  STRONG tier) and labelled "News (context, not scored)" in the push and in
  `latest_alerts.md`.
- `config.py`: add `"news_neutral": 8,` to `SIGNAL_VALIDITY_HOURS` (same 8-hour
  window as `news`). Done as a one-line edit, not a file replacement. If it is
  missing, the neutral line simply lives 24 hours instead of 8.
- Effect on the 10-13 alerts (807 qualifying; only 5 had a News line):
  ASTS STRONG -> Moderate with a News caution warning; DB stays STRONG (2
  categories, 2.07); FUN, AI, and Z would drop below 2 categories and stop
  alerting. FUN ("Six Flags' stock slumps toward 16-year low") now reads as
  bearish. AI and Z were ticker-symbol false matches (a Meta/AI-model story and
  "Gen Z renters"), not real company news.
- Going forward `features.py` "news" tags and outcome stats only cover
  bullish-headline pushes; earlier history includes neutral ones.
- Not changed, worth a look: single/short-letter ticker symbols (Z, AI) still
  match unrelated headlines. They no longer score, but they still display.
- Signals already stored under `news` before this change expire on their
  normal 8-hour window, so the old behavior can show for up to 8 hours after
  deploy.

## 2026-10-12 (Fin Trade Log: ticker edit, and how the app works)
The Trade Log is a single-file HTML app, `Fin_Trade_Log.html`, kept on Greg's
device. It is NOT in this repo. This entry records how it functions, since
nothing else does. Only the Edit flow was changed today (see "Change").

Why: ISNW was entered instead of INSW and Edit could not change a ticker, so
the drawdown report showed "no price data" for that trade. Edit also could not
set an entry date, so the three older trades with a blank entry date (PSIX,
ETOR, one A) could not be fixed either.

Change (only `editTrade()` was touched; the rest of the file is identical):
- Edit now asks, in order: ticker, entry price, shares, entry date, and for
  closed trades exit price and exit date. Ticker is trimmed and uppercased and
  must match letters/digits/"."/"-" (1-10 chars, starting with a letter, so
  BRK.B works). Entry date must be YYYY-MM-DD, or blank to keep the current
  one. A bad ticker or date shows an alert and changes nothing. Cancel at any
  prompt before the last abandons the edit with nothing changed.
- The trade's id, notes, status and exit data are kept when the ticker is
  renamed, so nothing needs to be deleted and re-added.
- Tested by running the edit function in Node (rename a closed trade, blank
  date keeps old, fill a missing entry date, invalid ticker, invalid date,
  cancel at first prompt, cancel mid-way, open trade). Not yet tried in a
  browser on the device.
- After an edit, the normal save triggers a GitHub sync, which writes the
  corrected symbol to `open_positions.json`. Re-run "Trade drawdown report"
  afterwards.

How the Trade Log works:
- Storage: the browser's localStorage, key `trades` (a JSON array). Per
  device and browser; clearing site data erases it, and opening the file in a
  different browser or from a different location can show an empty log.
  Export is the backup.
- Trade record: `id`, `symbol`, `entryPrice`, `shares`, `entryDate`, `notes`,
  `status` (open/closed), `exitPrice`, `exitDate`.
- Add Trade form: symbol (uppercased), entry price, shares, entry date
  (defaults to today), notes. New trades start as open.
- Close: type the exit price in the open trade's row and tap Close. Sets
  status closed, `exitPrice`, and `exitDate` = today.
- Edit: prompts described above. Notes are not editable.
- Del: removes the trade immediately, with no confirmation.
- Summary cards: realized P&L (sum over closed trades), open position count,
  open cost basis.
- P&L Over Time chart (Chart.js 4.4.1 from cdnjs, so the chart needs internet
  but the trade list does not): Daily (last 30 days), Weekly (52), Monthly
  (12), Yearly, YTD. Trades are bucketed by exit date (entry date if there is
  no exit date). Four widgets for the selected period: period P&L, average
  P&L per trade, win rate, trades closed.
- Trade table: filter All / Open / Closed; open trades first, then by date
  descending. Columns: symbol (+ notes), status, entry price/shares/date,
  exit price/date, P&L in $ and %.
- Export downloads `fin-trades-export-YYYY-MM-DD.json` containing
  `{exportedFrom, exportedAt, trades}`. Import accepts that file (or a bare
  array), skips rows missing symbol/entryPrice/shares, and REPLACES the whole
  log after a confirmation.
- GitHub sync: after every save (add, close, edit, delete, import) and on
  "Sync now", the app reads the current sha of `open_positions.json` and PUTs
  the full `{exportedFrom, exportedAt, trades}` to `main` in
  njdfan1711-cpu/Fin, using a fine-grained token (Contents: read and write)
  stored in localStorage as `gh_sync_token`. The status line shows the result.
  The file contains ALL trades, open and closed (the on-screen note says "open
  positions", which undersells it). The app is the source of truth: any manual
  edit to `open_positions.json` is overwritten at the next save.
  `position_monitor.py` and `trade_drawdown_report.py` read this file.
- Also: dark/light theme (localStorage `theme`) and a phone vs desktop layout
  chosen from the browser's user agent.
- Known quirks, not changed: new-trade and close dates use the UTC date, so
  closing a trade after about 8 PM Eastern records the next calendar day;
  Delete has no confirmation; the sync note text says "open positions".

## 2026-10-12 (price/ATR retry, trade drawdown report)
Built from live `main` (compose_alerts.py pulled 2026-10-12). Tested against
simulated Yahoo data only; first live run still to be checked in the Actions log.

Why: PENG ranked #7 on the 10-12 intraday push (15:37 ET) with no trade plan
and no chase/low-volatility caution. All three need price + ATR from
`fetch_prices_and_atr()`, so that ticker's data came back empty or unusable.
Cause could not be confirmed from here (no access to the run log); the two
candidates were a blank Yahoo batch result for PENG, or gap bars (NaN
High/Low) inside the 14-day ATR window, which made the whole rolling mean NaN
and silently dropped the plan.

- `compose_alerts.py` `compute_atr()`: drops bars with missing High/Low/Close
  before computing, so one gap bar no longer turns the ATR into None. Result
  on clean data is identical to before.
- `compose_alerts.py` `fetch_prices_and_atr()`: any ticker that comes back
  with no price, or a price but no ATR, from the batch call is now retried on
  its own (`period="3mo"`, capped at `MAX_PRICE_RETRIES = 15`). If the whole
  batch download throws, every ticker gets that retry. A ticker that still
  has a price but no ATR (e.g. a very new listing) is kept price-only, as
  before. Per-symbol parsing moved into new helper `_parse_price_atr()`; the
  prior-close / 5-day-close logic is unchanged.
- `compose_alerts.py`: every ticker missing after the batch is now logged by
  name with the reason, then logged again as "recovered on individual retry"
  or "STILL MISSING after retry". Search the Actions log for `price/ATR`.
  Closes the old "known gap" from the 9/24 entry (silent per-symbol skips).
- New `trade_drawdown_report.py` (repo root) + `.github/workflows/trade_drawdown.yml`
  (manual dispatch only). Reads `open_positions.json`, pulls daily bars, and
  commits `trade_drawdown_report.md`: per trade, worst dip below entry, closes
  under entry, Fin's default stop level (entry - `STOP_ATR_MULT` x ATR as of
  the day before entry), and whether price reached it while held. Entry and
  exit days use closes only (daily bars can't show intraday order), so the
  worst dip is never overstated. Trades with a blank `entryDate` in the log
  (PSIX, ETOR, one A) are skipped. Purpose: all 16 closed trades are wins, but
  holding through dips keeps would-be losses open, so this checks how deep the
  wins dipped and whether Fin's stop would have fired on any of them.
- Still open: `DEFAULT_POSITION_SIZE_USD` in `config.py` is still 3000 while
  live position size is ~3,500 (rising to ~4,700); it only affects the
  suggested share count. Delete stray `compose_alerts-1.py` if still present.

## 2026-10-08 (strict streaks, Back marker, NEW = never seen)
Built from live `main` (HEAD c62eb78, pulled 2026-10-08; the streak-tag batch
below verified live by file hash). Display only. Swing track only. Supersedes
the "gaps of up to 4 calendar days" streak rule in the entry below.

Why: that rule counted days pushed, tolerating missed days, so an on-again/
off-again ticker read as a long streak. On the real log (10-08), DHT (pushed
every day except 10-06) showed "Day 8" when strictly it is Day 2, HPE showed
Day 6 vs 3, PTC/PBR showed Day 3 vs 1; 4 of 20 tickers shown at Day 3+ had
broken runs.

- `daily_pushes.py` `symbol_history()`: a streak is now an UNBROKEN run of
  trading days ending the day before today; one missed day resets it. A
  "trading day" is any day with a key in the push log (weekends/holidays have
  no pushes and are skipped, so no holiday calendar). New return fields
  `ever_pushed` (anywhere in the retained log, today included) and `prev_run`
  (length of the most recent broken run). `prior_days`/`first_price`/
  `pushed_today` keep their names. Side effect: the scorecard's `age:` and
  `runup:` tags (via `compose_alerts.py` -> `features.py`) now use the strict
  streak too; they started collecting 10-07, so only a day or two of
  looser-rule data exists.
- `compose_alerts.py`: streak tag shown at Day 3+ (`STREAK_TAG_MIN_DAYS`
  unchanged) only for unbroken runs. New `\u21A9 Back (was Day N)` marker for a
  ticker whose previous run was N >= 3 and was broken by a missed day. Runs of
  1-2 days that broke get no marker. Applies to the ntfy header line and the
  `## N.` header in `alerts_history`.
- `compose_alerts.py`: NEW now means never pushed anywhere in the retained log
  (~10 days), so a ticker that dropped for a day and returned is no longer
  re-labelled NEW. The "N new" count in the push title uses the same rule.
- Replay on the push log: Day 3+ tags 16 of 28 tickers pushed 10-08 (was 20);
  DHT 10-07 -> "Back (was Day 6)"; HPE 10-08 -> Day 3; PTC/PBR -> no tag, not NEW.
- Caveats: the log keeps ~10 days, so streaks cap there; a workflow outage
  that leaves a trading day with no pushes at all breaks every streak that
  day (conservative).

## 2026-10-07 (streak tag + NEW logic fix)
Built from live `main` (HEAD b5454ef, pulled 2026-10-07; the scorecard-features
and pre-open-fix batches below verified live by file hash). Display only: no
ranking, trade-plan or signal changes. Swing track only.

Bug: the NEW tag meant "not pushed in the last DEDUPE_HOURS (12h)". Since the
overnight gap (4:36 PM -> next morning) is longer than 12h, every repeat ticker
was re-labelled NEW on its first push of the next day (and after weekends).
Example: Agilent (A) was pushed all day 10-05 and 10-06 (last 16:36 ET), yet its
first 10-07 push (10:36 ET) showed NEW. `alert_log.py` is a spam-control
timer, not a "have I seen this before" memory.

- `compose_alerts.py`: NEW now means never pushed in the current streak (no
  prior trading day, and not already pushed earlier today). The "N new" count
  in the push title uses the same rule. `was_recently_alerted` is no longer
  used here; `alert_log.py` and `mark_alerted()` are untouched.
- `compose_alerts.py`: new display-only streak tag, e.g.
  `📅 Day 8 (+11.1% since 1st alert)`, appended to the ntfy header line
  and to the `## N.` header of the GitHub `alerts_history` file, shown once a
  ticker has been pushed on `STREAK_TAG_MIN_DAYS` (3) or more consecutive
  trading days. "Day N" = prior streak days + 1; the % is current price vs the
  price at the streak's first push. A streak survives gaps of up to 4 calendar
  days (weekends/holidays). Only tickers that were actually pushed to ntfy can
  have a streak; the log keeps ~10 days (`DAILY_PUSHES_RETENTION_DAYS`), so
  displayed streaks cap around there.
- `daily_pushes.py` `symbol_history()`: rewritten to one pass over the log
  (now called for every ranked ticker, ~850) and now also returns
  `pushed_today`. Same `prior_days` / `first_price` keys as before.
- `config.py`: new `STREAK_TAG_MIN_DAYS = 3`.
- Replay against `daily_pushes.json`: A on 10-07 -> Day 3, not NEW;
  INSW on 10-07 -> Day 8, +11.7% since 1st alert.
- Upload check: `compose_alerts.py`, `features.py`, `daily_pushes.py`,
  `backfill_features.py`, `scorecard.py`, `scorecard.md` and `CHANGELOG.md` were
  byte-identical to the delivered builds; `outcome_features.json` had since been
  regenerated by the workflow (a superset of the delivered entries).

## 2026-10-07 (pre-open prior-close fix)
Built from live `main` (HEAD 2c15594, pulled 2026-10-07) and shipped in the
same upload as the 2026-10-07 scorecard-features batch below, so `compose_alerts.py`
and this changelog are cumulative (both changes). Swing track only.

Bug: `fetch_prices_and_atr` took `prev_close = closes.iloc[-2]`. Before the open
(and on weekends/holidays) yfinance has no bar for today, so `iloc[-1]` is the
last completed session and `iloc[-2]` is the close the day before it. Chase
risk then reported yesterday's move as "up X% today" and named a stale
"prior close" as the pullback level. Checked against `daily_pushes.json`:
39 of 41 pre-open pushes that were re-pushed later the same day had a
`prev_close` equal to the stale value; their pre-open price equalled the
correct `prev_close` seen after the open (e.g. NAT 10-05: $8.17 vs $8.42).
Trade-plan levels (entry/stop/target) use price and ATR only and were not affected.

- `compose_alerts.py` `fetch_prices_and_atr`: `prev_close` is `iloc[-2]` only
  when the last bar's date is today (ET); otherwise it is the last close, so
  the day change is 0 until a session exists. `close_5d` is unchanged.
- `compose_alerts.py` `format_chase_caution`: when there is no day move but the
  5-day run still flags, the caution reads "Chase risk: +X% over ~5 days (N ATR)
  ... consider waiting for a pullback" with no stale price level or "today" claim.
  Wording for in-session pushes is unchanged.
- Effect: pre-open pushes no longer get a day-move chase flag from yesterday's
  session (the 5-day trigger still applies), so some pre-open `caut:chase` tags
  will change. Historical stored `chase` fields and outcome entries are not
  rewritten; scorecard `caut:chase` rows mix old and new definitions until
  enough new pushes accumulate.
- Not changed / still open: `technicals_scan.py` takes `volumes.iloc[-1]` as
  "today's volume" and has the same possible last-bar assumption pre-open
  (not yet checked against data); the `time:`/`volhi:` tags skip pre-10:00 ET
  pushes for that reason.

## 2026-10-07 (scorecard features: volume timing, push time, signal age)
Built from live `main` (HEAD 2c15594, pulled 2026-10-07). Tag/logging only:
no ranking, trade-plan, caution-text or alert-content changes. Swing track only.

Why: the relative-volume ratio in `technicals_scan.py` is volume SO FAR today /
the 20-day average of FULL days, so it reads low mid-session (alert-history
medians: ~0.2-0.6x between 10:00-15:00 ET, ~0.9-1.0x only after the close).
The "new 52-week high on light volume" caution therefore fires on most highs
and says little about real volume. Raw ratio and thresholds are unchanged;
the scorecard can now test volume on a time-adjusted basis.

- `features.py`: new tags. `time:` (pre_open / open_hour / midday /
  late_session / after_close / closed, ET push time); `volhi:` (low_adj <0.8x,
  normal_adj 0.8-1.5x, high_adj >=1.5x: raw ratio parsed from the existing
  light/confirmed-volume text, divided by an approximate cumulative
  intraday-volume share; skipped before 10:00 ET); `age:` (new / recurring
  2-4d / stale 5d+ from prior push days) and `runup:` (<2% / 2-5% / >=5% since
  the first push of the current streak). The intraday curve is a heuristic,
  not measured from this repo. Also: the chase caution line in alert text now
  maps to `caut:chase` when backfilling from alerts_history (it previously
  fell into `caut:news_caution`). `extract_features` gained optional
  `asof`, `prior_push_days`, `runup_pct` args (all default None).
- `daily_pushes.py`: new read-only `symbol_history()` (prior push days in the
  current streak, gaps up to 4 calendar days; price at the streak's first push).
- `compose_alerts.py`: `build_push_features` takes `history`/`asof`;
  `symbol_history()` is called before `record_push()`. Stored push `features`
  now include the new tags going forward.
- `backfill_features.py`: new `--refresh` flag recomputes every entry; passes
  the alert-run timestamp so history gets `time:`/`volhi:` tags. `age:`/`runup:`
  cannot be backfilled (needs push history that was pruned) and accumulate
  from live pushes only.
- `scorecard.py`: three new report sections for the tags above.
- `outcome_features.json` / `scorecard.md`: regenerated with
  `backfill_features.py --refresh` then `scorecard.py --force`.
  Window is now 2026-08-19 to 09-30 (1055 ticker-days) because more outcomes
  resolved since 10-03, so the baseline moved (win 44%, avg R -0.04).
- Early read (hypotheses only; one regime, many tags tested): time-adjusted
  volume at highs shows no clear pattern (low 37% n=111, normal 43% n=104,
  high 36% n=70, baseline 44%). `time:pre_open` pushes look better (57%, n=208)
  and midday/after-close worse; may reflect measurement/price-timing effects.
  Don't retune thresholds on this.

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
