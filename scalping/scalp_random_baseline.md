# Random-entry baseline

Generated 2026-11-12T15:31:30+00:00. 28 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.071 | $0.375 | 46.4 | 35.7 |
| Random: A_same_symbol_day | $-0.165 (5-95%: -2.262 to 1.973) | $-0.859 | 38.0 | 24.5 |
| Random: B_within_15_min | $1.621 (5-95%: -0.579 to 3.715) | $0.927 | 48.5 | 40.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.157
- B_within_15_min: p = 0.655

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 28 | $1.071 | $0.375 | 46.4 | 35.7 | - |
| +1 min | 28 | $-0.778 | $-1.473 | 35.7 | 25.0 | -1.848 (+/- 1.446) |
| +2 min | 27 | $-0.592 | $-1.269 | 37.0 | 25.9 | -1.855 (+/- 1.461) |
| +3 min | 27 | $-1.165 | $-1.842 | 25.9 | 18.5 | -2.429 (+/- 1.503) |
| +5 min | 25 | $-0.607 | $-1.311 | 28.0 | 24.0 | -2.112 (+/- 1.454) |
| +10 min | 24 | $-3.154 | $-3.864 | 16.7 | 8.3 | -4.969 (+/- 1.994) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

28 trades: avg gross $-1.618, avg net $-2.313, win 28.6%, target 21.4%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
