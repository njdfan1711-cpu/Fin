# Random-entry baseline

Generated 2026-11-05T20:31:18+00:00. 44 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.51 | $0.736 | 47.7 | 31.8 |
| Random: A_same_symbol_day | $-0.089 (5-95%: -1.667 to 1.461) | $-0.865 | 39.0 | 21.9 |
| Random: B_within_15_min | $2.955 (5-95%: 1.276 to 4.576) | $2.178 | 58.5 | 44.8 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.047
- B_within_15_min: p = 0.925

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 44 | $1.51 | $0.736 | 47.7 | 31.8 | - |
| +1 min | 43 | $0.983 | $0.224 | 44.2 | 27.9 | -0.61 (+/- 1.111) |
| +2 min | 41 | $1.893 | $1.151 | 51.2 | 34.1 | +0.607 (+/- 0.992) |
| +3 min | 41 | $0.384 | $-0.358 | 41.5 | 26.8 | -0.902 (+/- 1.034) |
| +5 min | 40 | $0.827 | $0.095 | 45.0 | 30.0 | -0.526 (+/- 1.223) |
| +10 min | 33 | $-2.134 | $-2.849 | 24.2 | 12.1 | -3.099 (+/- 1.751) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

44 trades: avg gross $-1.309, avg net $-2.083, win 34.1%, target 13.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
