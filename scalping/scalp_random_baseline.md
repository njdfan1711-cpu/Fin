# Random-entry baseline

Generated 2026-11-05T16:31:16+00:00. 42 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.085 | $0.314 | 45.2 | 28.6 |
| Random: A_same_symbol_day | $-0.053 (5-95%: -1.68 to 1.655) | $-0.826 | 39.3 | 21.6 |
| Random: B_within_15_min | $3.106 (5-95%: 1.503 to 4.777) | $2.331 | 59.7 | 45.3 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.132
- B_within_15_min: p = 0.982

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 42 | $1.085 | $0.314 | 45.2 | 28.6 | - |
| +1 min | 41 | $0.922 | $0.166 | 43.9 | 26.8 | -0.241 (+/- 1.097) |
| +2 min | 39 | $1.874 | $1.137 | 51.3 | 33.3 | +1.056 (+/- 0.943) |
| +3 min | 38 | $0.006 | $-0.749 | 39.5 | 23.7 | -0.591 (+/- 1.055) |
| +5 min | 38 | $0.752 | $0.025 | 44.7 | 28.9 | -0.124 (+/- 1.215) |
| +10 min | 30 | $-2.32 | $-3.05 | 23.3 | 10.0 | -2.379 (+/- 1.828) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

42 trades: avg gross $-1.088, avg net $-1.859, win 35.7%, target 14.3%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
