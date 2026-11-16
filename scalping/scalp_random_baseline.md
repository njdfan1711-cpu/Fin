# Random-entry baseline

Generated 2026-11-16T18:30:57+00:00. 29 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.641 | $-2.336 | 31.0 | 17.2 |
| Random: A_same_symbol_day | $-0.075 (5-95%: -1.943 to 1.921) | $-0.77 | 39.7 | 20.5 |
| Random: B_within_15_min | $1.524 (5-95%: -0.546 to 3.492) | $0.829 | 49.0 | 36.2 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.911
- B_within_15_min: p = 0.997

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 29 | $-1.641 | $-2.336 | 31.0 | 17.2 | - |
| +1 min | 29 | $-2.545 | $-3.24 | 24.1 | 13.8 | -0.905 (+/- 1.235) |
| +2 min | 28 | $-1.691 | $-2.369 | 28.6 | 17.9 | -0.14 (+/- 1.534) |
| +3 min | 28 | $-1.765 | $-2.443 | 25.0 | 17.9 | -0.214 (+/- 1.65) |
| +5 min | 27 | $-0.223 | $-0.916 | 33.3 | 22.2 | +1.173 (+/- 1.838) |
| +10 min | 26 | $-1.074 | $-1.773 | 30.8 | 19.2 | +0.147 (+/- 1.833) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

29 trades: avg gross $0.335, avg net $-0.36, win 44.8%, target 27.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
