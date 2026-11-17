# Random-entry baseline

Generated 2026-11-17T16:31:11+00:00. 19 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.52 | $-1.3 | 42.1 | 15.8 |
| Random: A_same_symbol_day | $0.057 (5-95%: -2.197 to 2.349) | $-0.722 | 41.5 | 17.4 |
| Random: B_within_15_min | $2.757 (5-95%: 0.334 to 5.143) | $1.978 | 59.2 | 36.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.649
- B_within_15_min: p = 0.983

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 19 | $-0.52 | $-1.3 | 42.1 | 15.8 | - |
| +1 min | 19 | $-0.642 | $-1.422 | 42.1 | 15.8 | -0.122 (+/- 1.351) |
| +2 min | 19 | $-0.323 | $-1.103 | 42.1 | 15.8 | +0.197 (+/- 1.618) |
| +3 min | 18 | $0.191 | $-0.593 | 38.9 | 22.2 | +0.416 (+/- 2.115) |
| +5 min | 18 | $0.463 | $-0.322 | 38.9 | 16.7 | +0.688 (+/- 1.977) |
| +10 min | 17 | $-1.916 | $-2.677 | 29.4 | 5.9 | -2.027 (+/- 2.067) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

19 trades: avg gross $0.012, avg net $-0.768, win 47.4%, target 21.1%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
