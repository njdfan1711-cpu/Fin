# Changelog — Scalping Project

Separate initiative from the main Fin swing-trade screener (see
`../CHANGELOG.md` for that project). Different trading philosophy,
different timeframe, different code — kept in this `scalping/`
subfolder deliberately so the two don't get tangled together, even
though they share this GitHub repo. Manual code/config changes only,
same convention as the main changelog.

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
