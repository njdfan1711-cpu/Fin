# Random-entry baseline

Generated 2026-10-27T14:31:16+00:00. 18 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.008 | $-0.653 | 38.9 | 22.2 |
| Random: A_same_symbol_day | $-0.44 (5-95%: -2.712 to 1.839) | $-1.088 | 37.8 | 17.4 |
| Random: B_within_15_min | $1.437 (5-95%: -0.925 to 3.886) | $0.79 | 50.9 | 31.0 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.381
- B_within_15_min: p = 0.846

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 18 | $-0.008 | $-0.653 | 38.9 | 22.2 | - |
| +1 min | 17 | $2.399 | $1.75 | 58.8 | 35.3 | +2.417 (+/- 1.354) |
| +2 min | 17 | $1.662 | $1.013 | 47.1 | 35.3 | +1.68 (+/- 2.167) |
| +3 min | 17 | $0.91 | $0.26 | 47.1 | 23.5 | +0.927 (+/- 1.597) |
| +5 min | 16 | $1.665 | $1.004 | 56.2 | 25.0 | +1.655 (+/- 2.207) |
| +10 min | 15 | $-0.758 | $-1.436 | 33.3 | 13.3 | -0.084 (+/- 2.565) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

18 trades: avg gross $-0.582, avg net $-1.227, win 27.8%, target 22.2%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
