# Changelog — Scalping Project

Separate initiative from the main Fin swing-trade screener (see
`../CHANGELOG.md` for that project). Different trading philosophy,
different timeframe, different code — kept in this `scalping/`
subfolder deliberately so the two don't get tangled together, even
though they share this GitHub repo. Manual code/config changes only,
same convention as the main changelog.

## 2026-10-02
- **Scheduling live.** `scalp_backtest.yml` is now triggered on a schedule
  via a cron-job.org job calling its `workflow_dispatch` endpoint (same
  fix as the main screener). First run (#1) succeeded and committed
  `scalp_backtest_trades.csv` and `scalp_backtest_summary.json`. Related
  fix on the main screener: a cloned cron job that still pointed at
  `intraday.yml` caused duplicate push notifications; URL corrected and a
  guard step added to `intraday.yml`.
- **First baseline results** (42 trades, 7 sessions, fixed target):
  38.1% win rate, avg net -$4.90/trade, total net -$205.68, max drawdown
  -$252.65. Gross P&L was only +$32.50 against $238 of modeled cost, so
  the baseline has roughly zero edge before costs. NIO alone lost ~$205;
  the flat 2c/share cost is proportionally much larger on low-priced
  stocks (more shares per $3,000 position). Too small a sample to judge
  the strategy; revisit at 100+ trades.
- **Added trailing-stop exit variant** to `scalp_backtest.py`. Runs on
  the same entries as the fixed-target version so the two are directly
  comparable. No fixed target: initial stop (`SCALP_STOP_PCT`) applies
  until price rises `TRAIL_ARM_PCT` (0.175%) above entry, then the stop
  trails `TRAIL_PCT` (0.15%) below the high-water mark, never below the
  initial stop; 15-minute time-stop still applies. Results go to
  separate files (`scalp_backtest_trail_trades.csv`,
  `scalp_backtest_trail_summary.json`) so the original history stays
  untouched. Within-bar ordering is unknowable on 1-minute bars, so the
  trailing version assumes the pessimistic case (harsher than the fixed
  version, which checks the target first). Logic verified on synthetic
  price paths only, not yet on real data. If a 0.15% trail is stopped out
  by normal 1-minute noise, try ~0.25%.
- `scalp_backtest.yml` now also commits the two trailing-variant files.
- **Design decisions for the future live bot** (not built yet):
  - Entries: marketable limit orders (ask plus a 1-2c cushion), cancel
    and skip if not filled within a few seconds. No passive bid-side
    limits at first (adverse selection).
  - Profit targets: resting limit orders. Stops: stop-market or an
    aggressive marketable limit, not stop-limit (a gap past the limit
    would leave a losing position open).
  - Exits placed at the broker as linked orders (target + stop, one
    cancels the other) so they survive a process crash; time-stop on top.
  - Missed entries are never chased. The bot logs the miss, keeps
    scanning other symbols, and a missed symbol may re-qualify only on a
    fresh signal after a per-symbol cooldown (starting guess: 5-10 min
    after a miss, ~30 min after a stop-out; tune from paper results).
  - $10/trade is an average goal, not a per-trade rule; the real test is
    positive expectancy (win rate and win/loss size) after costs.
  - Guardrails before any live money: daily loss limit, max concurrent
    positions, daily trade cap, kill switch.
- **Status of the plan:** Schwab API access approved; `schwab-py`
  installed; browser OAuth token step and test-quote script still to do.
  Next: log real Schwab bid/ask quotes to replace the 2c placeholder,
  then build the live signal engine against Alpaca paper trading, then
  1-2 weeks of paper results before small live size on Schwab. Schwab
  refresh tokens expire every 7 days and need a browser re-login.
- **Universe widened 2026-10-02:** added AMD, MSFT, META, GOOGL, AVGO,
  NFLX, MU, PLTR, COIN, HOOD, UBER, JPM, XOM, SPY, QQQ to `CANDIDATES`
  (now 30 symbols) for a bigger sample; SPY/QQQ act as tight-spread
  benchmarks. Existing trade history is kept; new symbols only add rows,
  so later results cover a larger universe than the first 42 trades.
  Added local-only `spread_logger.py` / `spread_report.py` (not for the
  repo) to measure real Schwab bid/ask spreads on the same 30 symbols.
- **Added `guardrails.py` + `test_guardrails.py`** (safety layer for the
  future live bot; no network, nothing connected to Schwab yet). All
  orders must go through `guarded_submit()`. Rules: equities only;
  allowed-symbol list; sides limited to BUY and SELL, with SELL allowed
  only up to shares already held (so short selling is impossible);
  BUYs need a limit price and may not exceed $3,000 notional (fixed,
  does not grow with the account); max 1 open position (pending entries
  count); $500 daily loss limit (realized + open P&L) halts new entries;
  circuit breaker of 40 entries/day (set `MAX_TRADES_PER_DAY = None` to
  disable); `STOP.txt` blocks new entries, `FLATTEN.txt` blocks entries
  and signals the bot loop to cancel orders and close its own positions.
  Multiple simultaneous positions deferred until one-at-a-time results
  are consistent and the account has grown.
- **Added `build_watchlist.py` + `scalp_watchlist.yml`** (daily scalp
  watch list). Reads the Daily Scan's `eligible.csv` and keeps names with
  price $20-$1,000 and price x 20-day avg volume >= $100M/day, ranked by
  dollar volume, capped at 500 -> `scalping/scalp_watchlist.csv`. First
  run: 827 of 2,448 eligible names passed; top 500 written. The
  workflow is `workflow_dispatch` only (trigger from cron-job.org after
  the Daily Scan finishes). Note: the Daily Scan universe excludes ETFs,
  so SPY/QQQ are not on the list. Planned: add a measured-spread filter
  once `spread_logger.py` has data. NOT yet wired into the logger,
  backtest, or `guardrails.py` (whose ALLOWED_SYMBOLS is still the
  30-name list and must be updated before the live bot can trade
  anything else).
- **Added `IDEAS.md`** (backlog of candidate rules; none implemented).
  Includes skipping the first/last 15 minutes, avoiding entries while SPY
  is down, and skipping over-extended entries, plus a guiding principle
  of testing one idea at a time and tagging signals (rather than only
  filtering them) so the cost of each rule in lost good trades is visible.
- **Measured-spread cost model (backtest).** First spread-logger results
  (2 partial days, core hours) showed the flat 2c/share assumption was
  wrong in both directions: too high for cheap stocks (1c on a $3 stock is
  already 0.30% of price) and too low for high-priced ones (e.g. META
  ~20c). `scalp_backtest.py` now re-costs every accumulated trade in the
  SUMMARY from `measured_spreads.csv` (symbol -> median spread as % of
  price): cost/share = max(1c, price x pct) x `SPREAD_COST_MULTIPLIER`;
  symbols with no data fall back to the flat 2c and are listed. The
  `cost` / `net_pnl` columns in the trades CSVs deliberately stay on the
  old flat model so older and newer rows remain consistent; the summary
  JSON now carries total gross/cost/net under the measured model, the old
  flat-model net for comparison, breakdowns by spread tier (<=0.03% vs
  wider) and by symbol. Result on the first 180 trades: net -$551 (flat
  model) -> -$334 (measured); gross edge is only +$25 (about $0.14 per
  trade). The 93 trades in tight-spread names (<=0.03%) netted +$18 (about
  $0.20/trade, within noise); the 86 trades in wider-spread names lost
  $356 (NIO alone about -$245). Conclusion: costs were hurting badly, but
  the entry signal itself shows almost no gross edge yet.
- **Spread logger v2 + report.** `spread_logger.py` now logs the 30 core
  symbols plus the daily watchlist (downloaded from GitHub at startup),
  ~510 symbols, polling every 10s in batches of 100, summarized per symbol
  per minute (`logs\spread_min_YYYY-MM-DD.csv`, roughly 20 MB/day). Stale
  and crossed quotes are dropped; symbols that return no quotes are
  printed after ~5 minutes (WBD returned none in the first run).
  Credentials can live in `schwab_credentials.txt` (key line 1, secret line
  2) so script updates never wipe them. `spread_report.py` reads both the
  old per-quote logs and the new per-minute logs and writes
  `measured_spreads.csv` (upload to the repo's scalping/ folder to update
  backtest costs). p90 in the new report is over 1-minute averages, so it
  reads slightly lower than the first report's per-quote p90.
- **Watchlist spread filter.** `build_watchlist.py` drops names whose
  measured median spread exceeds 0.03% of price (about $0.90 round trip on
  a $3,000 trade, under 10% of the profit target), when
  `measured_spreads.csv` is present. Names with no measurement yet are kept
  (marked `spread_known = no`) so the logger can measure them. First run:
  5 names dropped (AMD, COIN, HOOD, PLTR, T); 500 written, 15 with measured
  spreads.
- **Pending:** consider removing low-priced tickers (NIO, F, AAL, SOFI, T,
  and similar) from `CANDIDATES`; not yet changed.

## 2026-09-29
- Added `scalp_backtest.py` — first-cut viability check for a possible
  future automated scalping track. Baseline VWAP-reclaim + momentum +
  volume-spike strategy, run against 1-minute bars. Appends to
  `scalp_backtest_trades.csv` on each run so results accumulate over
  the next 1-2 weeks rather than requiring one big historical pull
  (yfinance free tier only serves 7 days of 1-minute history). See the
  module docstring for the full cost-model caveat — spread cost is an
  unverified placeholder, treat all results as optimistic until checked
  against real quotes/fills. Does NOT use any of the main screener's
  confluence signals (technical/fundamentals/news/short-interest) —
  self-contained strategy logic, see the "different criteria" note in
  chat for why.
- Added `scalp_backtest.yml` GitHub Actions workflow (see
  `.github/workflows/`) so this runs without any local setup —
  `workflow_dispatch` only for now (not on a schedule yet — see the
  workflow file's comment for why, matches the scheduling lesson
  learned on the main screener).
