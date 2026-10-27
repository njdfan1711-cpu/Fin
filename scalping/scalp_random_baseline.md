# Random-entry baseline

Generated 2026-10-27T18:31:35+00:00. 19 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.198 | $-0.745 | 42.1 | 15.8 |
| Random: A_same_symbol_day | $-0.249 (5-95%: -2.408 to 1.975) | $-0.799 | 39.5 | 13.6 |
| Random: B_within_15_min | $1.684 (5-95%: -0.779 to 4.125) | $1.136 | 51.4 | 31.2 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.453
- B_within_15_min: p = 0.888

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 19 | $-0.198 | $-0.745 | 42.1 | 15.8 | - |
| +1 min | 19 | $2.12 | $1.572 | 57.9 | 31.6 | +2.318 (+/- 1.518) |
| +2 min | 18 | $1.893 | $1.345 | 50.0 | 27.8 | +2.413 (+/- 1.717) |
| +3 min | 18 | $0.49 | $-0.058 | 44.4 | 22.2 | +1.01 (+/- 1.22) |
| +5 min | 18 | $1.341 | $0.793 | 55.6 | 27.8 | +1.861 (+/- 1.511) |
| +10 min | 18 | $-0.338 | $-0.886 | 38.9 | 16.7 | +0.182 (+/- 1.627) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

19 trades: avg gross $-0.162, avg net $-0.709, win 42.1%, target 21.1%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
