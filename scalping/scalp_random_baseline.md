# Random-entry baseline

Generated 2026-10-26T15:31:21+00:00. 13 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.609 | $-1.117 | 30.8 | 15.4 |
| Random: A_same_symbol_day | $-0.393 (5-95%: -2.788 to 2.125) | $-0.905 | 39.2 | 14.0 |
| Random: B_within_15_min | $2.018 (5-95%: -0.698 to 4.795) | $1.509 | 52.7 | 32.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.525
- B_within_15_min: p = 0.941

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 13 | $-0.609 | $-1.117 | 30.8 | 15.4 | - |
| +1 min | 12 | $1.058 | $0.542 | 50.0 | 25.0 | +1.613 (+/- 1.935) |
| +2 min | 11 | $1.033 | $0.521 | 36.4 | 27.3 | +2.149 (+/- 2.441) |
| +3 min | 11 | $-0.318 | $-0.831 | 36.4 | 18.2 | +0.797 (+/- 1.042) |
| +5 min | 11 | $0.321 | $-0.192 | 45.5 | 27.3 | +1.436 (+/- 2.008) |
| +10 min | 11 | $0.039 | $-0.474 | 36.4 | 18.2 | +1.155 (+/- 2.56) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

13 trades: avg gross $-0.61, avg net $-1.118, win 46.2%, target 15.4%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
