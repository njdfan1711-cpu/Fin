# Random-entry baseline

Generated 2026-11-03T18:31:31+00:00. 38 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.237 | $-0.515 | 42.1 | 21.1 |
| Random: A_same_symbol_day | $-0.016 (5-95%: -1.694 to 1.657) | $-0.772 | 40.4 | 19.0 |
| Random: B_within_15_min | $2.951 (5-95%: 1.341 to 4.668) | $2.193 | 59.7 | 42.0 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.399
- B_within_15_min: p = 0.999

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 38 | $0.237 | $-0.515 | 42.1 | 21.1 | - |
| +1 min | 37 | $2.208 | $1.473 | 54.1 | 35.1 | +1.908 (+/- 1.056) |
| +2 min | 37 | $1.721 | $0.986 | 51.4 | 29.7 | +1.421 (+/- 1.09) |
| +3 min | 37 | $-0.379 | $-1.115 | 40.5 | 18.9 | -0.679 (+/- 1.067) |
| +5 min | 36 | $0.423 | $-0.321 | 47.2 | 22.2 | +0.102 (+/- 1.265) |
| +10 min | 30 | $-1.419 | $-2.135 | 30.0 | 13.3 | -1.154 (+/- 1.665) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

38 trades: avg gross $-0.27, avg net $-1.023, win 39.5%, target 18.4%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
