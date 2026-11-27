# Random-entry baseline

Generated 2026-11-27T20:31:23+00:00. 30 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.629 | $-1.26 | 33.3 | 26.7 |
| Random: A_same_symbol_day | $0.06 (5-95%: -1.967 to 2.049) | $-0.572 | 39.6 | 25.9 |
| Random: B_within_15_min | $1.831 (5-95%: 0.088 to 3.605) | $1.2 | 51.4 | 39.0 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.702
- B_within_15_min: p = 0.991

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 30 | $-0.629 | $-1.26 | 33.3 | 26.7 | - |
| +1 min | 30 | $-1.663 | $-2.295 | 26.7 | 16.7 | -1.035 (+/- 0.682) |
| +2 min | 30 | $-1.705 | $-2.337 | 26.7 | 16.7 | -1.076 (+/- 0.743) |
| +3 min | 28 | $-2.427 | $-3.065 | 25.0 | 10.7 | -1.033 (+/- 1.159) |
| +5 min | 26 | $0.013 | $-0.611 | 42.3 | 26.9 | +1.63 (+/- 1.489) |
| +10 min | 25 | $0.247 | $-0.384 | 40.0 | 28.0 | +1.706 (+/- 1.616) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

30 trades: avg gross $0.946, avg net $0.315, win 46.7%, target 33.3%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
