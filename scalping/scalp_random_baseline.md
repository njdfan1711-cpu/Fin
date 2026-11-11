# Random-entry baseline

Generated 2026-11-11T17:31:09+00:00. 29 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $2.245 | $1.456 | 51.7 | 41.4 |
| Random: A_same_symbol_day | $-0.196 (5-95%: -2.054 to 1.822) | $-0.982 | 38.3 | 21.0 |
| Random: B_within_15_min | $1.895 (5-95%: -0.263 to 3.858) | $1.108 | 50.7 | 40.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.029
- B_within_15_min: p = 0.41

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 29 | $2.245 | $1.456 | 51.7 | 41.4 | - |
| +1 min | 29 | $-0.88 | $-1.668 | 31.0 | 20.7 | -3.125 (+/- 1.103) |
| +2 min | 27 | $1.421 | $0.657 | 48.1 | 33.3 | -0.407 (+/- 1.092) |
| +3 min | 27 | $1.198 | $0.434 | 44.4 | 29.6 | -0.629 (+/- 1.359) |
| +5 min | 25 | $0.11 | $-0.646 | 36.0 | 28.0 | -2.139 (+/- 1.505) |
| +10 min | 24 | $-2.615 | $-3.388 | 25.0 | 8.3 | -4.843 (+/- 2.017) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

29 trades: avg gross $-1.701, avg net $-2.49, win 31.0%, target 10.3%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
