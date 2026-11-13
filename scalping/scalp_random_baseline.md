# Random-entry baseline

Generated 2026-11-13T17:31:05+00:00. 23 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.568 | $0.887 | 52.2 | 34.8 |
| Random: A_same_symbol_day | $-0.243 (5-95%: -2.461 to 2.206) | $-0.925 | 39.3 | 19.4 |
| Random: B_within_15_min | $2.229 (5-95%: -0.067 to 4.516) | $1.548 | 55.5 | 37.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.109
- B_within_15_min: p = 0.682

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 23 | $1.568 | $0.887 | 52.2 | 34.8 | - |
| +1 min | 23 | $0.245 | $-0.437 | 43.5 | 26.1 | -1.324 (+/- 1.444) |
| +2 min | 23 | $1.522 | $0.841 | 52.2 | 30.4 | -0.046 (+/- 1.542) |
| +3 min | 22 | $1.303 | $0.623 | 50.0 | 27.3 | -0.601 (+/- 1.769) |
| +5 min | 21 | $-0.213 | $-0.901 | 38.1 | 14.3 | -2.472 (+/- 1.952) |
| +10 min | 20 | $-1.686 | $-2.386 | 30.0 | 10.0 | -4.251 (+/- 2.042) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

23 trades: avg gross $-0.903, avg net $-1.585, win 39.1%, target 17.4%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
