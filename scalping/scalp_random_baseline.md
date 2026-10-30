# Random-entry baseline

Generated 2026-10-30T17:31:28+00:00. 35 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.488 | $-0.209 | 45.7 | 25.7 |
| Random: A_same_symbol_day | $-0.149 (5-95%: -1.735 to 1.579) | $-0.849 | 39.7 | 17.6 |
| Random: B_within_15_min | $1.953 (5-95%: 0.252 to 3.664) | $1.254 | 53.2 | 36.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.249
- B_within_15_min: p = 0.912

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 35 | $0.488 | $-0.209 | 45.7 | 25.7 | - |
| +1 min | 35 | $2.717 | $2.02 | 57.1 | 40.0 | +2.229 (+/- 1.134) |
| +2 min | 34 | $1.805 | $1.104 | 55.9 | 32.4 | +1.467 (+/- 0.856) |
| +3 min | 34 | $0.754 | $0.051 | 44.1 | 29.4 | +0.417 (+/- 1.015) |
| +5 min | 34 | $1.384 | $0.68 | 52.9 | 32.4 | +1.047 (+/- 0.979) |
| +10 min | 33 | $-2.015 | $-2.727 | 27.3 | 12.1 | -2.275 (+/- 1.432) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

35 trades: avg gross $-0.356, avg net $-1.053, win 37.1%, target 25.7%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
