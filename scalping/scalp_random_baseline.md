# Random-entry baseline

Generated 2026-11-19T18:31:19+00:00. 42 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.17 | $-1.816 | 33.3 | 16.7 |
| Random: A_same_symbol_day | $-0.231 (5-95%: -1.778 to 1.488) | $-0.876 | 37.6 | 22.5 |
| Random: B_within_15_min | $1.954 (5-95%: 0.218 to 3.61) | $1.309 | 52.1 | 38.5 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.832
- B_within_15_min: p = 0.996

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 42 | $-1.17 | $-1.816 | 33.3 | 16.7 | - |
| +1 min | 42 | $-2.513 | $-3.16 | 23.8 | 7.1 | -1.344 (+/- 0.821) |
| +2 min | 42 | $-2.063 | $-2.71 | 28.6 | 9.5 | -0.893 (+/- 0.853) |
| +3 min | 41 | $-1.577 | $-2.2 | 31.7 | 12.2 | -0.124 (+/- 1.106) |
| +5 min | 33 | $-0.642 | $-1.261 | 33.3 | 18.2 | +2.44 (+/- 1.354) |
| +10 min | 33 | $0.444 | $-0.175 | 42.4 | 24.2 | +3.526 (+/- 1.372) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

42 trades: avg gross $1.568, avg net $0.921, win 50.0%, target 35.7%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
