# Random-entry baseline

Generated 2026-11-13T14:31:05+00:00. 21 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $2.187 | $1.489 | 57.1 | 38.1 |
| Random: A_same_symbol_day | $-0.227 (5-95%: -2.511 to 2.085) | $-0.925 | 38.8 | 20.3 |
| Random: B_within_15_min | $2.178 (5-95%: -0.379 to 4.643) | $1.48 | 54.0 | 39.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.041
- B_within_15_min: p = 0.5

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 21 | $2.187 | $1.489 | 57.1 | 38.1 | - |
| +1 min | 21 | $0.708 | $0.01 | 47.6 | 28.6 | -1.479 (+/- 1.581) |
| +2 min | 21 | $2.135 | $1.437 | 57.1 | 33.3 | -0.052 (+/- 1.686) |
| +3 min | 20 | $1.916 | $1.218 | 55.0 | 30.0 | -0.672 (+/- 1.95) |
| +5 min | 19 | $-0.158 | $-0.864 | 36.8 | 15.8 | -3.173 (+/- 2.086) |
| +10 min | 19 | $-2.007 | $-2.713 | 26.3 | 10.5 | -5.023 (+/- 1.993) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

21 trades: avg gross $-1.37, avg net $-2.068, win 33.3%, target 19.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
