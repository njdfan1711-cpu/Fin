# Random-entry baseline

Generated 2026-11-23T16:31:22+00:00. 22 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.285 | $-2.014 | 31.8 | 22.7 |
| Random: A_same_symbol_day | $-0.269 (5-95%: -2.416 to 2.107) | $-0.995 | 37.2 | 22.6 |
| Random: B_within_15_min | $1.813 (5-95%: -0.593 to 4.249) | $1.086 | 51.0 | 35.8 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.775
- B_within_15_min: p = 0.983

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 22 | $-1.285 | $-2.014 | 31.8 | 22.7 | - |
| +1 min | 22 | $-2.743 | $-3.472 | 22.7 | 9.1 | -1.458 (+/- 0.957) |
| +2 min | 22 | $-2.611 | $-3.34 | 22.7 | 9.1 | -1.326 (+/- 0.822) |
| +3 min | 22 | $-1.888 | $-2.617 | 27.3 | 13.6 | -0.604 (+/- 1.077) |
| +5 min | 17 | $-1.644 | $-2.347 | 23.5 | 17.6 | +2.493 (+/- 1.338) |
| +10 min | 16 | $-0.098 | $-0.771 | 37.5 | 18.8 | +3.926 (+/- 1.929) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

22 trades: avg gross $3.299, avg net $2.57, win 63.6%, target 40.9%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
