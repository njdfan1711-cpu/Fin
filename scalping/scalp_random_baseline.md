# Random-entry baseline

Generated 2026-11-23T19:31:25+00:00. 25 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.749 | $-1.451 | 36.0 | 24.0 |
| Random: A_same_symbol_day | $-0.239 (5-95%: -2.252 to 1.93) | $-0.938 | 37.7 | 22.5 |
| Random: B_within_15_min | $1.659 (5-95%: -0.568 to 3.807) | $0.958 | 50.6 | 34.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.651
- B_within_15_min: p = 0.969

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 25 | $-0.749 | $-1.451 | 36.0 | 24.0 | - |
| +1 min | 25 | $-2.83 | $-3.533 | 24.0 | 8.0 | -2.082 (+/- 1.035) |
| +2 min | 25 | $-2.684 | $-3.387 | 24.0 | 8.0 | -1.935 (+/- 0.942) |
| +3 min | 25 | $-1.977 | $-2.679 | 28.0 | 12.0 | -1.228 (+/- 1.137) |
| +5 min | 20 | $-1.93 | $-2.604 | 25.0 | 15.0 | +1.109 (+/- 1.496) |
| +10 min | 19 | $-0.483 | $-1.13 | 36.8 | 15.8 | +2.403 (+/- 1.949) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

25 trades: avg gross $2.848, avg net $2.145, win 60.0%, target 40.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
