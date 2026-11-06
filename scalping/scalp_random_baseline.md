# Random-entry baseline

Generated 2026-11-06T15:30:54+00:00. 37 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.701 | $0.029 | 45.9 | 27.0 |
| Random: A_same_symbol_day | $-0.32 (5-95%: -1.99 to 1.405) | $-0.995 | 37.2 | 21.3 |
| Random: B_within_15_min | $2.115 (5-95%: 0.387 to 3.874) | $1.44 | 52.9 | 39.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.18
- B_within_15_min: p = 0.912

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 37 | $0.701 | $0.029 | 45.9 | 27.0 | - |
| +1 min | 35 | $-0.919 | $-1.57 | 34.3 | 20.0 | -1.66 (+/- 1.185) |
| +2 min | 35 | $-0.354 | $-1.006 | 37.1 | 25.7 | -1.096 (+/- 0.87) |
| +3 min | 35 | $0.119 | $-0.534 | 34.3 | 28.6 | -0.622 (+/- 1.312) |
| +5 min | 34 | $-0.285 | $-0.944 | 32.4 | 26.5 | -0.982 (+/- 1.041) |
| +10 min | 29 | $-2.939 | $-3.599 | 24.1 | 6.9 | -4.135 (+/- 1.65) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

37 trades: avg gross $-0.383, avg net $-1.055, win 35.1%, target 27.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
