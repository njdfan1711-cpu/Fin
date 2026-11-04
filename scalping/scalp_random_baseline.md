# Random-entry baseline

Generated 2026-11-04T20:31:19+00:00. 45 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.346 | $-0.385 | 42.2 | 24.4 |
| Random: A_same_symbol_day | $0.028 (5-95%: -1.492 to 1.63) | $-0.707 | 40.2 | 20.5 |
| Random: B_within_15_min | $2.371 (5-95%: 0.691 to 4.002) | $1.636 | 54.8 | 39.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.363
- B_within_15_min: p = 0.976

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 45 | $0.346 | $-0.385 | 42.2 | 24.4 | - |
| +1 min | 43 | $0.805 | $0.089 | 44.2 | 30.2 | +0.443 (+/- 1.032) |
| +2 min | 43 | $0.877 | $0.161 | 46.5 | 30.2 | +0.515 (+/- 0.613) |
| +3 min | 43 | $0.093 | $-0.626 | 34.9 | 27.9 | -0.269 (+/- 0.988) |
| +5 min | 43 | $0.269 | $-0.451 | 37.2 | 27.9 | -0.094 (+/- 0.679) |
| +10 min | 38 | $-2.967 | $-3.695 | 21.1 | 7.9 | -3.666 (+/- 1.296) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

45 trades: avg gross $-0.548, avg net $-1.279, win 37.8%, target 22.2%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
