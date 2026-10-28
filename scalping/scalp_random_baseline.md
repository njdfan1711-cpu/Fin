# Random-entry baseline

Generated 2026-10-28T19:31:14+00:00. 29 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.29 | $-1.046 | 37.9 | 20.7 |
| Random: A_same_symbol_day | $-0.03 (5-95%: -1.939 to 1.885) | $-0.789 | 40.4 | 19.8 |
| Random: B_within_15_min | $2.086 (5-95%: 0.283 to 3.861) | $1.329 | 54.3 | 36.2 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.592
- B_within_15_min: p = 0.984

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 29 | $-0.29 | $-1.046 | 37.9 | 20.7 | - |
| +1 min | 28 | $3.121 | $2.359 | 57.1 | 42.9 | +3.427 (+/- 1.209) |
| +2 min | 28 | $2.682 | $1.92 | 53.6 | 39.3 | +2.988 (+/- 1.336) |
| +3 min | 28 | $0.123 | $-0.639 | 39.3 | 25.0 | +0.429 (+/- 1.116) |
| +5 min | 27 | $1.523 | $0.748 | 51.9 | 25.9 | +1.824 (+/- 1.567) |
| +10 min | 26 | $-0.973 | $-1.762 | 30.8 | 15.4 | -0.266 (+/- 1.778) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

29 trades: avg gross $-0.442, avg net $-1.198, win 34.5%, target 20.7%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
