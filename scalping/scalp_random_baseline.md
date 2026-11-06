# Random-entry baseline

Generated 2026-11-06T19:31:10+00:00. 35 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $2.044 | $1.273 | 51.4 | 34.3 |
| Random: A_same_symbol_day | $-0.329 (5-95%: -1.958 to 1.465) | $-1.102 | 37.1 | 21.8 |
| Random: B_within_15_min | $2.67 (5-95%: 0.761 to 4.57) | $1.896 | 56.4 | 44.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.023
- B_within_15_min: p = 0.714

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 35 | $2.044 | $1.273 | 51.4 | 34.3 | - |
| +1 min | 34 | $-0.17 | $-0.922 | 38.2 | 20.6 | -2.335 (+/- 1.055) |
| +2 min | 32 | $1.207 | $0.477 | 50.0 | 28.1 | -0.601 (+/- 0.948) |
| +3 min | 32 | $0.681 | $-0.049 | 46.9 | 25.0 | -1.127 (+/- 1.167) |
| +5 min | 30 | $0.012 | $-0.709 | 43.3 | 26.7 | -2.146 (+/- 1.488) |
| +10 min | 24 | $-1.971 | $-2.686 | 25.0 | 12.5 | -4.169 (+/- 2.088) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

35 trades: avg gross $-1.104, avg net $-1.875, win 34.3%, target 17.1%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
