# Random-entry baseline

Generated 2026-11-17T18:31:13+00:00. 22 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.219 | $-1.989 | 36.4 | 13.6 |
| Random: A_same_symbol_day | $0.007 (5-95%: -2.202 to 2.276) | $-0.763 | 40.3 | 20.1 |
| Random: B_within_15_min | $2.588 (5-95%: 0.34 to 4.71) | $1.818 | 57.6 | 37.7 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.805
- B_within_15_min: p = 0.998

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 22 | $-1.219 | $-1.989 | 36.4 | 13.6 | - |
| +1 min | 22 | $-1.323 | $-2.094 | 36.4 | 13.6 | -0.105 (+/- 1.163) |
| +2 min | 22 | $-1.046 | $-1.817 | 36.4 | 13.6 | +0.172 (+/- 1.393) |
| +3 min | 21 | $-0.639 | $-1.413 | 33.3 | 19.0 | +0.36 (+/- 1.805) |
| +5 min | 21 | $0.299 | $-0.475 | 38.1 | 19.0 | +1.298 (+/- 1.819) |
| +10 min | 20 | $-0.15 | $-0.904 | 40.0 | 20.0 | +0.601 (+/- 2.263) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

22 trades: avg gross $1.357, avg net $0.587, win 54.5%, target 31.8%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
