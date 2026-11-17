# Random-entry baseline

Generated 2026-11-17T19:31:18+00:00. 37 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-2.012 | $-2.683 | 27.0 | 13.5 |
| Random: A_same_symbol_day | $-0.079 (5-95%: -1.854 to 1.716) | $-0.749 | 38.9 | 21.9 |
| Random: B_within_15_min | $2.336 (5-95%: 0.506 to 4.145) | $1.666 | 54.7 | 41.2 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.961
- B_within_15_min: p = 1.0

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 37 | $-2.012 | $-2.683 | 27.0 | 13.5 | - |
| +1 min | 36 | $-2.979 | $-3.652 | 19.4 | 8.3 | -1.077 (+/- 0.884) |
| +2 min | 36 | $-2.194 | $-2.866 | 30.6 | 11.1 | -0.291 (+/- 1.055) |
| +3 min | 35 | $-1.404 | $-2.08 | 31.4 | 17.1 | +0.488 (+/- 1.349) |
| +5 min | 32 | $-0.214 | $-0.908 | 34.4 | 21.9 | +1.954 (+/- 1.52) |
| +10 min | 30 | $0.485 | $-0.196 | 43.3 | 26.7 | +2.4 (+/- 1.747) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

36 trades: avg gross $1.902, avg net $1.229, win 52.8%, target 38.9%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
