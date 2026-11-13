# Random-entry baseline

Generated 2026-11-13T20:31:05+00:00. 32 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.108 | $-1.802 | 34.4 | 21.9 |
| Random: A_same_symbol_day | $-0.06 (5-95%: -2.045 to 1.954) | $-0.753 | 39.3 | 23.6 |
| Random: B_within_15_min | $1.432 (5-95%: -0.589 to 3.335) | $0.738 | 48.0 | 37.3 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.794
- B_within_15_min: p = 0.98

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 32 | $-1.108 | $-1.802 | 34.4 | 21.9 | - |
| +1 min | 32 | $-2.416 | $-3.111 | 21.9 | 15.6 | -1.308 (+/- 1.216) |
| +2 min | 31 | $-2.309 | $-2.989 | 22.6 | 16.1 | -1.299 (+/- 1.394) |
| +3 min | 31 | $-1.038 | $-1.716 | 29.0 | 22.6 | -0.028 (+/- 1.643) |
| +5 min | 29 | $-0.896 | $-1.597 | 31.0 | 20.7 | +0.063 (+/- 1.685) |
| +10 min | 28 | $-2.096 | $-2.803 | 25.0 | 14.3 | -1.315 (+/- 1.72) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

32 trades: avg gross $0.408, avg net $-0.287, win 43.8%, target 31.2%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
