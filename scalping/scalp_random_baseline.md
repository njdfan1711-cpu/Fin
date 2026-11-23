# Random-entry baseline

Generated 2026-11-23T20:31:15+00:00. 26 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.342 | $-1.043 | 38.5 | 26.9 |
| Random: A_same_symbol_day | $-0.296 (5-95%: -2.291 to 1.949) | $-0.995 | 37.4 | 22.6 |
| Random: B_within_15_min | $1.448 (5-95%: -0.637 to 3.521) | $0.748 | 49.0 | 33.8 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.498
- B_within_15_min: p = 0.917

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 26 | $-0.342 | $-1.043 | 38.5 | 26.9 | - |
| +1 min | 26 | $-2.343 | $-3.045 | 26.9 | 11.5 | -2.001 (+/- 0.997) |
| +2 min | 26 | $-2.797 | $-3.499 | 23.1 | 7.7 | -2.455 (+/- 1.044) |
| +3 min | 26 | $-2.117 | $-2.819 | 26.9 | 11.5 | -1.775 (+/- 1.222) |
| +5 min | 21 | $-2.106 | $-2.78 | 23.8 | 14.3 | +0.32 (+/- 1.627) |
| +10 min | 20 | $-0.741 | $-1.389 | 35.0 | 15.0 | +1.51 (+/- 2.053) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

26 trades: avg gross $2.522, avg net $1.821, win 57.7%, target 38.5%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
