# Random-entry baseline

Generated 2026-11-03T15:31:21+00:00. 40 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.44 | $-1.123 | 37.5 | 17.5 |
| Random: A_same_symbol_day | $-0.008 (5-95%: -1.54 to 1.643) | $-0.694 | 40.5 | 18.7 |
| Random: B_within_15_min | $2.323 (5-95%: 0.788 to 3.929) | $1.638 | 56.1 | 36.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.661
- B_within_15_min: p = 0.997

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 40 | $-0.44 | $-1.123 | 37.5 | 17.5 | - |
| +1 min | 39 | $1.403 | $0.739 | 48.7 | 30.8 | +1.801 (+/- 1.041) |
| +2 min | 39 | $0.726 | $0.061 | 48.7 | 25.6 | +1.124 (+/- 0.767) |
| +3 min | 39 | $0.539 | $-0.127 | 43.6 | 25.6 | +0.937 (+/- 1.069) |
| +5 min | 38 | $-0.171 | $-0.844 | 42.1 | 21.1 | +0.225 (+/- 0.78) |
| +10 min | 34 | $-2.537 | $-3.229 | 23.5 | 8.8 | -2.526 (+/- 1.264) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

40 trades: avg gross $0.361, avg net $-0.322, win 42.5%, target 25.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
