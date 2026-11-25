# Random-entry baseline

Generated 2026-11-25T14:31:08+00:00. 25 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.143 | $0.512 | 48.0 | 36.0 |
| Random: A_same_symbol_day | $-0.233 (5-95%: -2.516 to 2.0) | $-0.862 | 37.2 | 25.4 |
| Random: B_within_15_min | $1.709 (5-95%: -0.38 to 4.012) | $1.078 | 50.4 | 38.0 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.161
- B_within_15_min: p = 0.658

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 25 | $1.143 | $0.512 | 48.0 | 36.0 | - |
| +1 min | 25 | $-2.065 | $-2.697 | 28.0 | 12.0 | -3.208 (+/- 1.249) |
| +2 min | 25 | $-1.834 | $-2.466 | 28.0 | 12.0 | -2.977 (+/- 1.187) |
| +3 min | 25 | $-1.489 | $-2.121 | 36.0 | 12.0 | -2.633 (+/- 1.19) |
| +5 min | 20 | $-1.856 | $-2.442 | 30.0 | 15.0 | -1.182 (+/- 1.924) |
| +10 min | 19 | $-0.257 | $-0.828 | 36.8 | 21.1 | +0.141 (+/- 2.337) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

25 trades: avg gross $1.392, avg net $0.76, win 48.0%, target 36.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
