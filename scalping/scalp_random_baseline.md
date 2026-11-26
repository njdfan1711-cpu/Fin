# Random-entry baseline

Generated 2026-11-26T15:31:17+00:00. 29 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.316 | $0.669 | 48.3 | 37.9 |
| Random: A_same_symbol_day | $-0.018 (5-95%: -2.024 to 2.128) | $-0.663 | 38.6 | 26.5 |
| Random: B_within_15_min | $2.171 (5-95%: 0.124 to 4.232) | $1.525 | 52.7 | 41.7 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.148
- B_within_15_min: p = 0.761

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 29 | $1.316 | $0.669 | 48.3 | 37.9 | - |
| +1 min | 29 | $-1.449 | $-2.097 | 31.0 | 17.2 | -2.765 (+/- 1.094) |
| +2 min | 29 | $-1.249 | $-1.897 | 31.0 | 17.2 | -2.566 (+/- 1.039) |
| +3 min | 29 | $-0.965 | $-1.612 | 37.9 | 17.2 | -2.282 (+/- 1.037) |
| +5 min | 24 | $-1.159 | $-1.771 | 33.3 | 20.8 | -0.997 (+/- 1.599) |
| +10 min | 23 | $0.883 | $0.282 | 43.5 | 30.4 | +0.795 (+/- 2.039) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

29 trades: avg gross $0.942, avg net $0.294, win 44.8%, target 34.5%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
