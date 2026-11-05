# Random-entry baseline

Generated 2026-11-05T18:31:27+00:00. 43 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.302 | $0.536 | 46.5 | 30.2 |
| Random: A_same_symbol_day | $-0.092 (5-95%: -1.648 to 1.678) | $-0.861 | 39.0 | 21.6 |
| Random: B_within_15_min | $2.943 (5-95%: 1.348 to 4.469) | $2.173 | 58.5 | 44.8 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.097
- B_within_15_min: p = 0.952

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 43 | $1.302 | $0.536 | 46.5 | 30.2 | - |
| +1 min | 42 | $0.758 | $0.007 | 42.9 | 26.2 | -0.625 (+/- 1.137) |
| +2 min | 40 | $1.678 | $0.945 | 50.0 | 32.5 | +0.62 (+/- 1.017) |
| +3 min | 40 | $0.134 | $-0.6 | 40.0 | 25.0 | -0.924 (+/- 1.06) |
| +5 min | 39 | $0.58 | $-0.143 | 43.6 | 28.2 | -0.54 (+/- 1.255) |
| +10 min | 32 | $-2.526 | $-3.23 | 21.9 | 9.4 | -3.195 (+/- 1.804) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

43 trades: avg gross $-1.201, avg net $-1.967, win 34.9%, target 14.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
