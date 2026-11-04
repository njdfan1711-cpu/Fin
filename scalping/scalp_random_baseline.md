# Random-entry baseline

Generated 2026-11-04T14:31:27+00:00. 38 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.245 | $-1.001 | 39.5 | 21.1 |
| Random: A_same_symbol_day | $0.017 (5-95%: -1.544 to 1.628) | $-0.744 | 40.1 | 19.6 |
| Random: B_within_15_min | $2.402 (5-95%: 0.756 to 4.056) | $1.642 | 55.3 | 39.6 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.578
- B_within_15_min: p = 0.997

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 38 | $-0.245 | $-1.001 | 39.5 | 21.1 | - |
| +1 min | 36 | $0.713 | $-0.027 | 41.7 | 30.6 | +0.971 (+/- 1.159) |
| +2 min | 36 | $0.354 | $-0.386 | 41.7 | 27.8 | +0.613 (+/- 0.713) |
| +3 min | 36 | $0.166 | $-0.576 | 36.1 | 30.6 | +0.425 (+/- 1.084) |
| +5 min | 36 | $0.18 | $-0.563 | 38.9 | 27.8 | +0.439 (+/- 0.74) |
| +10 min | 31 | $-2.479 | $-3.237 | 25.8 | 9.7 | -2.533 (+/- 1.426) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

38 trades: avg gross $-0.015, avg net $-0.771, win 42.1%, target 23.7%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
