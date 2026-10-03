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
