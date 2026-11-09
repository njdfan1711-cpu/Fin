# Random-entry baseline

Generated 2026-11-09T14:31:33+00:00. 31 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $2.056 | $1.287 | 51.6 | 35.5 |
| Random: A_same_symbol_day | $-0.386 (5-95%: -2.151 to 1.437) | $-1.158 | 36.6 | 21.4 |
| Random: B_within_15_min | $2.426 (5-95%: 0.394 to 4.361) | $1.654 | 54.3 | 42.6 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.02
- B_within_15_min: p = 0.627

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 31 | $2.056 | $1.287 | 51.6 | 35.5 | - |
| +1 min | 30 | $-0.874 | $-1.623 | 33.3 | 16.7 | -3.068 (+/- 1.004) |
| +2 min | 28 | $0.8 | $0.077 | 46.4 | 28.6 | -0.989 (+/- 0.871) |
| +3 min | 28 | $0.515 | $-0.207 | 42.9 | 25.0 | -1.273 (+/- 1.166) |
| +5 min | 26 | $0.473 | $-0.238 | 42.3 | 30.8 | -1.718 (+/- 1.716) |
| +10 min | 22 | $-2.86 | $-3.572 | 18.2 | 9.1 | -5.102 (+/- 2.068) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

31 trades: avg gross $-0.604, avg net $-1.374, win 38.7%, target 16.1%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
