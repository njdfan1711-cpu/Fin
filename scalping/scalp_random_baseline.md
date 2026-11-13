# Random-entry baseline

Generated 2026-11-13T19:31:09+00:00. 34 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.495 | $-1.181 | 38.2 | 26.5 |
| Random: A_same_symbol_day | $0.056 (5-95%: -1.789 to 1.977) | $-0.629 | 40.0 | 24.0 |
| Random: B_within_15_min | $1.687 (5-95%: -0.324 to 3.621) | $1.002 | 49.6 | 39.6 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.67
- B_within_15_min: p = 0.966

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 34 | $-0.495 | $-1.181 | 38.2 | 26.5 | - |
| +1 min | 34 | $-1.706 | $-2.392 | 26.5 | 20.6 | -1.211 (+/- 1.317) |
| +2 min | 33 | $-1.585 | $-2.256 | 27.3 | 21.2 | -1.2 (+/- 1.471) |
| +3 min | 33 | $-0.867 | $-1.537 | 30.3 | 24.2 | -0.482 (+/- 1.608) |
| +5 min | 31 | $-0.215 | $-0.906 | 35.5 | 25.8 | +0.082 (+/- 1.729) |
| +10 min | 30 | $-1.299 | $-1.994 | 30.0 | 20.0 | -1.19 (+/- 1.763) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

34 trades: avg gross $-0.384, avg net $-1.07, win 38.2%, target 26.5%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
