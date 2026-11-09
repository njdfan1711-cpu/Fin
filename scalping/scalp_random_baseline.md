# Random-entry baseline

Generated 2026-11-09T15:31:20+00:00. 37 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.427 | $-0.285 | 43.2 | 27.0 |
| Random: A_same_symbol_day | $-0.308 (5-95%: -2.042 to 1.526) | $-1.023 | 37.1 | 23.0 |
| Random: B_within_15_min | $1.752 (5-95%: -0.007 to 3.702) | $1.037 | 49.6 | 39.8 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.246
- B_within_15_min: p = 0.89

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 37 | $0.427 | $-0.285 | 43.2 | 27.0 | - |
| +1 min | 35 | $-1.202 | $-1.895 | 31.4 | 20.0 | -1.653 (+/- 1.345) |
| +2 min | 34 | $-0.963 | $-1.643 | 32.4 | 23.5 | -1.55 (+/- 1.185) |
| +3 min | 34 | $-1.478 | $-2.159 | 23.5 | 20.6 | -2.065 (+/- 1.369) |
| +5 min | 33 | $-0.831 | $-1.519 | 27.3 | 24.2 | -1.367 (+/- 1.343) |
| +10 min | 29 | $-3.187 | $-3.874 | 20.7 | 6.9 | -4.276 (+/- 1.685) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

37 trades: avg gross $-0.194, avg net $-0.907, win 37.8%, target 27.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
