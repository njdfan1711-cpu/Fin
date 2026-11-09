# Random-entry baseline

Generated 2026-11-09T20:31:13+00:00. 39 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.49 | $-0.235 | 43.6 | 28.2 |
| Random: A_same_symbol_day | $-0.287 (5-95%: -2.062 to 1.438) | $-1.015 | 37.5 | 21.8 |
| Random: B_within_15_min | $1.812 (5-95%: 0.048 to 3.582) | $1.085 | 50.3 | 39.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.243
- B_within_15_min: p = 0.897

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 39 | $0.49 | $-0.235 | 43.6 | 28.2 | - |
| +1 min | 37 | $-1.047 | $-1.755 | 32.4 | 21.6 | -1.564 (+/- 1.272) |
| +2 min | 36 | $-0.445 | $-1.139 | 36.1 | 25.0 | -1.09 (+/- 1.194) |
| +3 min | 36 | $-0.946 | $-1.642 | 27.8 | 22.2 | -1.592 (+/- 1.357) |
| +5 min | 35 | $-0.498 | $-1.201 | 28.6 | 25.7 | -1.098 (+/- 1.287) |
| +10 min | 31 | $-3.043 | $-3.747 | 22.6 | 6.5 | -4.167 (+/- 1.672) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

39 trades: avg gross $-0.473, avg net $-1.198, win 35.9%, target 25.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
