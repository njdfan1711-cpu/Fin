# Random-entry baseline

Generated 2026-11-11T18:31:03+00:00. 31 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.605 | $0.928 | 51.6 | 35.5 |
| Random: A_same_symbol_day | $-0.077 (5-95%: -1.97 to 1.88) | $-0.752 | 39.4 | 23.1 |
| Random: B_within_15_min | $2.025 (5-95%: 0.006 to 4.024) | $1.349 | 51.6 | 42.2 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.087
- B_within_15_min: p = 0.624

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 31 | $1.605 | $0.928 | 51.6 | 35.5 | - |
| +1 min | 30 | $-0.932 | $-1.609 | 33.3 | 23.3 | -2.522 (+/- 1.432) |
| +2 min | 29 | $-0.004 | $-0.664 | 37.9 | 27.6 | -1.791 (+/- 1.342) |
| +3 min | 29 | $-0.788 | $-1.447 | 27.6 | 20.7 | -2.574 (+/- 1.402) |
| +5 min | 27 | $-0.447 | $-1.129 | 29.6 | 25.9 | -2.496 (+/- 1.333) |
| +10 min | 25 | $-2.893 | $-3.593 | 24.0 | 8.0 | -5.233 (+/- 1.927) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

31 trades: avg gross $-2.634, avg net $-3.311, win 22.6%, target 12.9%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
