# Random-entry baseline

Generated 2026-11-27T16:31:09+00:00. 27 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.227 | $-1.874 | 29.6 | 22.2 |
| Random: A_same_symbol_day | $-0.057 (5-95%: -2.193 to 2.048) | $-0.705 | 38.8 | 26.0 |
| Random: B_within_15_min | $1.874 (5-95%: -0.124 to 3.864) | $1.228 | 51.8 | 39.2 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.806
- B_within_15_min: p = 0.997

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 27 | $-1.227 | $-1.874 | 29.6 | 22.2 | - |
| +1 min | 27 | $-2.376 | $-3.024 | 22.2 | 11.1 | -1.149 (+/- 0.756) |
| +2 min | 27 | $-2.423 | $-3.071 | 22.2 | 11.1 | -1.196 (+/- 0.824) |
| +3 min | 27 | $-2.298 | $-2.944 | 25.9 | 11.1 | -1.071 (+/- 1.202) |
| +5 min | 25 | $0.25 | $-0.381 | 44.0 | 28.0 | +1.694 (+/- 1.548) |
| +10 min | 24 | $0.503 | $-0.136 | 41.7 | 29.2 | +1.776 (+/- 1.683) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

27 trades: avg gross $1.095, avg net $0.448, win 48.1%, target 33.3%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
