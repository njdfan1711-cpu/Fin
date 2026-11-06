# Random-entry baseline

Generated 2026-11-06T16:31:04+00:00. 34 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $2.269 | $1.503 | 52.9 | 35.3 |
| Random: A_same_symbol_day | $-0.29 (5-95%: -2.054 to 1.603) | $-1.058 | 37.3 | 22.2 |
| Random: B_within_15_min | $2.738 (5-95%: 0.866 to 4.7) | $1.968 | 57.0 | 44.3 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.015
- B_within_15_min: p = 0.65

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 34 | $2.269 | $1.503 | 52.9 | 35.3 | - |
| +1 min | 33 | $-0.005 | $-0.752 | 39.4 | 21.2 | -2.406 (+/- 1.085) |
| +2 min | 31 | $1.426 | $0.703 | 51.6 | 29.0 | -0.621 (+/- 0.979) |
| +3 min | 31 | $0.883 | $0.16 | 48.4 | 25.8 | -1.164 (+/- 1.205) |
| +5 min | 29 | $0.205 | $-0.508 | 44.8 | 27.6 | -2.221 (+/- 1.538) |
| +10 min | 23 | $-1.815 | $-2.52 | 26.1 | 13.0 | -4.352 (+/- 2.173) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

34 trades: avg gross $-1.425, avg net $-2.191, win 32.4%, target 14.7%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
