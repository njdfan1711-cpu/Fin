# Random-entry baseline

Generated 2026-11-18T15:31:03+00:00. 24 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.042 | $-1.775 | 37.5 | 16.7 |
| Random: A_same_symbol_day | $-0.139 (5-95%: -2.24 to 2.03) | $-0.869 | 38.3 | 22.5 |
| Random: B_within_15_min | $2.371 (5-95%: 0.138 to 4.623) | $1.639 | 54.8 | 38.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.739
- B_within_15_min: p = 0.993

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 24 | $-1.042 | $-1.775 | 37.5 | 16.7 | - |
| +1 min | 24 | $-1.205 | $-1.938 | 37.5 | 12.5 | -0.163 (+/- 1.067) |
| +2 min | 24 | $-1.373 | $-2.105 | 33.3 | 12.5 | -0.33 (+/- 1.019) |
| +3 min | 23 | $-0.795 | $-1.529 | 34.8 | 17.4 | +0.039 (+/- 1.42) |
| +5 min | 19 | $-0.694 | $-1.406 | 31.6 | 15.8 | +2.074 (+/- 1.749) |
| +10 min | 18 | $0.006 | $-0.68 | 33.3 | 22.2 | +2.598 (+/- 2.074) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

24 trades: avg gross $2.032, avg net $1.3, win 58.3%, target 33.3%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
