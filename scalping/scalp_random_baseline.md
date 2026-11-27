# Random-entry baseline

Generated 2026-11-27T18:31:11+00:00. 23 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.779 | $0.155 | 43.5 | 34.8 |
| Random: A_same_symbol_day | $-0.005 (5-95%: -2.33 to 2.347) | $-0.629 | 39.3 | 24.2 |
| Random: B_within_15_min | $1.66 (5-95%: -0.354 to 3.78) | $1.036 | 51.1 | 35.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.294
- B_within_15_min: p = 0.757

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 23 | $0.779 | $0.155 | 43.5 | 34.8 | - |
| +1 min | 23 | $-2.084 | $-2.709 | 26.1 | 17.4 | -2.864 (+/- 1.202) |
| +2 min | 23 | $-1.84 | $-2.466 | 26.1 | 17.4 | -2.62 (+/- 1.238) |
| +3 min | 23 | $-1.637 | $-2.26 | 30.4 | 17.4 | -2.416 (+/- 1.263) |
| +5 min | 22 | $-1.675 | $-2.295 | 31.8 | 18.2 | -2.097 (+/- 1.54) |
| +10 min | 20 | $0.077 | $-0.539 | 40.0 | 25.0 | -0.977 (+/- 2.049) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

22 trades: avg gross $1.475, avg net $0.842, win 50.0%, target 36.4%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
