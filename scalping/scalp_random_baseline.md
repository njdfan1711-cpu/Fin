# Random-entry baseline

Generated 2026-11-24T15:31:12+00:00. 21 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.326 | $-0.305 | 42.9 | 33.3 |
| Random: A_same_symbol_day | $-0.374 (5-95%: -2.663 to 2.071) | $-1.003 | 36.6 | 23.8 |
| Random: B_within_15_min | $1.377 (5-95%: -1.01 to 3.774) | $0.746 | 47.4 | 36.8 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.306
- B_within_15_min: p = 0.788

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 21 | $0.326 | $-0.305 | 42.9 | 33.3 | - |
| +1 min | 21 | $-2.053 | $-2.685 | 28.6 | 14.3 | -2.379 (+/- 1.219) |
| +2 min | 21 | $-2.523 | $-3.155 | 23.8 | 9.5 | -2.849 (+/- 1.262) |
| +3 min | 21 | $-2.236 | $-2.868 | 28.6 | 9.5 | -2.562 (+/- 1.241) |
| +5 min | 16 | $-2.801 | $-3.375 | 18.8 | 12.5 | -0.6 (+/- 1.824) |
| +10 min | 16 | $-0.172 | $-0.746 | 37.5 | 18.8 | +2.029 (+/- 2.365) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

21 trades: avg gross $2.087, avg net $1.455, win 52.4%, target 38.1%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
