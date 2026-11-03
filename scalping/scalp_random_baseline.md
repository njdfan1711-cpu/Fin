# Random-entry baseline

Generated 2026-11-03T19:32:08+00:00. 39 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.099 | $-0.656 | 41.0 | 20.5 |
| Random: A_same_symbol_day | $0.016 (5-95%: -1.709 to 1.625) | $-0.743 | 40.6 | 19.4 |
| Random: B_within_15_min | $2.838 (5-95%: 1.33 to 4.369) | $2.078 | 59.1 | 41.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.472
- B_within_15_min: p = 0.999

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 39 | $0.099 | $-0.656 | 41.0 | 20.5 | - |
| +1 min | 38 | $2.015 | $1.277 | 52.6 | 34.2 | +1.859 (+/- 1.029) |
| +2 min | 38 | $1.541 | $0.802 | 50.0 | 28.9 | +1.384 (+/- 1.062) |
| +3 min | 38 | $-0.504 | $-1.243 | 39.5 | 18.4 | -0.661 (+/- 1.039) |
| +5 min | 37 | $0.273 | $-0.474 | 45.9 | 21.6 | +0.1 (+/- 1.231) |
| +10 min | 31 | $-1.538 | $-2.259 | 29.0 | 12.9 | -1.116 (+/- 1.611) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

39 trades: avg gross $-0.032, avg net $-0.788, win 41.0%, target 20.5%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
