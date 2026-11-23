# Random-entry baseline

Generated 2026-11-23T15:31:10+00:00. 35 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.925 | $-2.601 | 25.7 | 14.3 |
| Random: A_same_symbol_day | $-0.297 (5-95%: -2.101 to 1.583) | $-0.971 | 37.1 | 23.3 |
| Random: B_within_15_min | $1.777 (5-95%: -0.125 to 3.626) | $1.103 | 51.3 | 37.2 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.938
- B_within_15_min: p = 1.0

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 35 | $-1.925 | $-2.601 | 25.7 | 14.3 | - |
| +1 min | 35 | $-3.329 | $-4.005 | 17.1 | 2.9 | -1.404 (+/- 0.736) |
| +2 min | 35 | $-2.597 | $-3.273 | 25.7 | 5.7 | -0.672 (+/- 0.755) |
| +3 min | 34 | $-1.949 | $-2.598 | 29.4 | 8.8 | +0.34 (+/- 1.0) |
| +5 min | 26 | $-1.597 | $-2.247 | 26.9 | 15.4 | +3.018 (+/- 1.148) |
| +10 min | 26 | $0.738 | $0.088 | 46.2 | 26.9 | +5.352 (+/- 1.479) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

35 trades: avg gross $2.085, avg net $1.409, win 54.3%, target 37.1%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
