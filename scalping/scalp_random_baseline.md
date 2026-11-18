# Random-entry baseline

Generated 2026-11-18T17:31:09+00:00. 25 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.214 | $-1.939 | 36.0 | 16.0 |
| Random: A_same_symbol_day | $-0.196 (5-95%: -2.139 to 2.033) | $-0.917 | 38.1 | 22.7 |
| Random: B_within_15_min | $2.191 (5-95%: -0.006 to 4.431) | $1.467 | 53.5 | 38.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.777
- B_within_15_min: p = 0.994

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 25 | $-1.214 | $-1.939 | 36.0 | 16.0 | - |
| +1 min | 25 | $-1.371 | $-2.095 | 36.0 | 12.0 | -0.156 (+/- 1.024) |
| +2 min | 25 | $-1.531 | $-2.256 | 32.0 | 12.0 | -0.317 (+/- 0.978) |
| +3 min | 24 | $-0.985 | $-1.71 | 33.3 | 16.7 | +0.037 (+/- 1.359) |
| +5 min | 20 | $-0.926 | $-1.629 | 30.0 | 15.0 | +1.971 (+/- 1.663) |
| +10 min | 19 | $-0.275 | $-0.952 | 31.6 | 21.1 | +2.462 (+/- 1.967) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

25 trades: avg gross $2.325, avg net $1.601, win 60.0%, target 36.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
