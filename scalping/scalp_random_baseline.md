# Random-entry baseline

Generated 2026-11-24T14:31:10+00:00. 33 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.373 | $-0.973 | 36.4 | 24.2 |
| Random: A_same_symbol_day | $-0.419 (5-95%: -2.257 to 1.489) | $-1.016 | 36.2 | 23.6 |
| Random: B_within_15_min | $1.755 (5-95%: -0.023 to 3.585) | $1.158 | 51.3 | 38.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.481
- B_within_15_min: p = 0.98

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 33 | $-0.373 | $-0.973 | 36.4 | 24.2 | - |
| +1 min | 33 | $-2.255 | $-2.855 | 24.2 | 6.1 | -1.882 (+/- 0.888) |
| +2 min | 33 | $-2.105 | $-2.704 | 30.3 | 6.1 | -1.731 (+/- 0.779) |
| +3 min | 32 | $-2.249 | $-2.818 | 31.2 | 3.1 | -1.538 (+/- 1.057) |
| +5 min | 24 | $-1.594 | $-2.138 | 29.2 | 12.5 | +1.111 (+/- 1.452) |
| +10 min | 24 | $0.516 | $-0.027 | 45.8 | 20.8 | +3.22 (+/- 1.82) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

33 trades: avg gross $1.511, avg net $0.912, win 48.5%, target 36.4%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
