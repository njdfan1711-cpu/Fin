# Random-entry baseline

Generated 2026-10-23T18:31:20+00:00. 17 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.443 | $-0.327 | 41.2 | 29.4 |
| Random: A_same_symbol_day | $-0.524 (5-95%: -2.842 to 2.099) | $-1.295 | 36.1 | 19.4 |
| Random: B_within_15_min | $1.424 (5-95%: -1.082 to 3.888) | $0.654 | 50.4 | 30.7 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.249
- B_within_15_min: p = 0.739

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 17 | $0.443 | $-0.327 | 41.2 | 29.4 | - |
| +1 min | 16 | $2.185 | $1.402 | 56.2 | 37.5 | +1.724 (+/- 1.093) |
| +2 min | 16 | $1.869 | $1.086 | 50.0 | 37.5 | +1.408 (+/- 2.032) |
| +3 min | 16 | $0.476 | $-0.307 | 43.8 | 25.0 | +0.015 (+/- 1.531) |
| +5 min | 16 | $1.109 | $0.326 | 43.8 | 25.0 | +0.648 (+/- 2.029) |
| +10 min | 15 | $-1.37 | $-2.176 | 26.7 | 13.3 | -1.176 (+/- 2.736) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

17 trades: avg gross $-1.184, avg net $-1.954, win 29.4%, target 17.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
