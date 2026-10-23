# Random-entry baseline

Generated 2026-10-23T16:31:23+00:00. 14 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-2.275 | $-2.879 | 21.4 | 7.1 |
| Random: A_same_symbol_day | $-0.416 (5-95%: -2.931 to 2.28) | $-1.025 | 38.6 | 15.0 |
| Random: B_within_15_min | $1.619 (5-95%: -0.951 to 4.425) | $1.012 | 50.6 | 28.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.879
- B_within_15_min: p = 0.994

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 14 | $-2.275 | $-2.879 | 21.4 | 7.1 | - |
| +1 min | 13 | $-0.484 | $-1.104 | 38.5 | 15.4 | +1.869 (+/- 1.768) |
| +2 min | 13 | $0.139 | $-0.48 | 30.8 | 15.4 | +2.492 (+/- 2.063) |
| +3 min | 13 | $-0.515 | $-1.135 | 38.5 | 15.4 | +1.837 (+/- 0.824) |
| +5 min | 13 | $0.583 | $-0.037 | 38.5 | 30.8 | +2.935 (+/- 1.769) |
| +10 min | 13 | $0.362 | $-0.26 | 38.5 | 23.1 | +2.715 (+/- 2.091) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

14 trades: avg gross $0.091, avg net $-0.514, win 50.0%, target 14.3%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
