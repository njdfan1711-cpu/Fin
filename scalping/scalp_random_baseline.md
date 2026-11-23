# Random-entry baseline

Generated 2026-11-23T17:31:20+00:00. 38 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.999 | $-2.649 | 26.3 | 13.2 |
| Random: A_same_symbol_day | $-0.288 (5-95%: -2.032 to 1.426) | $-0.937 | 37.2 | 23.9 |
| Random: B_within_15_min | $1.633 (5-95%: -0.205 to 3.389) | $0.984 | 50.7 | 36.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.949
- B_within_15_min: p = 1.0

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 38 | $-1.999 | $-2.649 | 26.3 | 13.2 | - |
| +1 min | 38 | $-3.179 | $-3.83 | 18.4 | 2.6 | -1.18 (+/- 0.694) |
| +2 min | 38 | $-2.553 | $-3.203 | 26.3 | 5.3 | -0.554 (+/- 0.7) |
| +3 min | 37 | $-1.956 | $-2.581 | 29.7 | 8.1 | +0.379 (+/- 0.92) |
| +5 min | 29 | $-1.166 | $-1.786 | 31.0 | 17.2 | +3.267 (+/- 1.064) |
| +10 min | 28 | $0.636 | $0.011 | 46.4 | 25.0 | +5.013 (+/- 1.446) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

38 trades: avg gross $1.915, avg net $1.265, win 52.6%, target 36.8%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
