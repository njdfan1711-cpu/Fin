# Random-entry baseline

Generated 2026-11-03T16:31:53+00:00. 37 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.405 | $-0.335 | 43.2 | 21.6 |
| Random: A_same_symbol_day | $0.051 (5-95%: -1.631 to 1.862) | $-0.693 | 40.6 | 19.8 |
| Random: B_within_15_min | $2.945 (5-95%: 1.244 to 4.611) | $2.2 | 60.1 | 41.6 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.36
- B_within_15_min: p = 0.994

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 37 | $0.405 | $-0.335 | 43.2 | 21.6 | - |
| +1 min | 36 | $2.435 | $1.713 | 55.6 | 36.1 | +1.961 (+/- 1.085) |
| +2 min | 36 | $1.934 | $1.212 | 52.8 | 30.6 | +1.46 (+/- 1.12) |
| +3 min | 36 | $-0.224 | $-0.946 | 41.7 | 19.4 | -0.698 (+/- 1.097) |
| +5 min | 35 | $0.606 | $-0.125 | 48.6 | 22.9 | +0.105 (+/- 1.302) |
| +10 min | 29 | $-1.827 | $-2.526 | 27.6 | 10.3 | -1.759 (+/- 1.605) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

37 trades: avg gross $-0.457, avg net $-1.198, win 37.8%, target 18.9%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
