# Random-entry baseline

Generated 2026-11-02T19:31:19+00:00. 42 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.456 | $-1.17 | 38.1 | 21.4 |
| Random: A_same_symbol_day | $-0.062 (5-95%: -1.604 to 1.488) | $-0.781 | 39.8 | 18.8 |
| Random: B_within_15_min | $2.124 (5-95%: 0.508 to 3.738) | $1.406 | 54.2 | 37.0 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.661
- B_within_15_min: p = 0.996

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 42 | $-0.456 | $-1.17 | 38.1 | 21.4 | - |
| +1 min | 41 | $1.887 | $1.19 | 51.2 | 36.6 | +2.304 (+/- 1.035) |
| +2 min | 40 | $1.091 | $0.391 | 50.0 | 30.0 | +1.658 (+/- 0.823) |
| +3 min | 40 | $0.642 | $-0.061 | 42.5 | 30.0 | +1.209 (+/- 1.018) |
| +5 min | 40 | $0.897 | $0.193 | 47.5 | 30.0 | +1.464 (+/- 0.899) |
| +10 min | 36 | $-1.966 | $-2.667 | 27.8 | 11.1 | -1.717 (+/- 1.359) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

42 trades: avg gross $0.425, avg net $-0.289, win 42.9%, target 28.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
