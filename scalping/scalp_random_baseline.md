# Random-entry baseline

Generated 2026-11-10T15:31:09+00:00. 29 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $2.245 | $1.453 | 51.7 | 41.4 |
| Random: A_same_symbol_day | $-0.271 (5-95%: -2.165 to 1.742) | $-1.062 | 37.7 | 20.7 |
| Random: B_within_15_min | $1.908 (5-95%: -0.237 to 3.986) | $1.117 | 50.8 | 39.5 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.02
- B_within_15_min: p = 0.402

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 29 | $2.245 | $1.453 | 51.7 | 41.4 | - |
| +1 min | 29 | $-0.88 | $-1.672 | 31.0 | 20.7 | -3.125 (+/- 1.103) |
| +2 min | 27 | $1.422 | $0.653 | 48.1 | 33.3 | -0.406 (+/- 1.092) |
| +3 min | 27 | $1.207 | $0.438 | 44.4 | 29.6 | -0.621 (+/- 1.36) |
| +5 min | 25 | $0.276 | $-0.485 | 36.0 | 28.0 | -1.974 (+/- 1.524) |
| +10 min | 24 | $-2.429 | $-3.207 | 25.0 | 8.3 | -4.658 (+/- 2.045) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

29 trades: avg gross $-1.584, avg net $-2.376, win 31.0%, target 10.3%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
