# Random-entry baseline

Generated 2026-10-23T13:31:16+00:00. 14 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.811 | $1.076 | 50.0 | 35.7 |
| Random: A_same_symbol_day | $-0.448 (5-95%: -3.143 to 2.24) | $-1.181 | 36.8 | 18.7 |
| Random: B_within_15_min | $1.589 (5-95%: -0.94 to 4.152) | $0.855 | 51.3 | 30.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.086
- B_within_15_min: p = 0.44

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 14 | $1.811 | $1.076 | 50.0 | 35.7 | - |
| +1 min | 13 | $2.796 | $2.049 | 61.5 | 38.5 | +0.858 (+/- 0.591) |
| +2 min | 13 | $2.407 | $1.661 | 53.8 | 38.5 | +0.469 (+/- 2.192) |
| +3 min | 13 | $1.958 | $1.212 | 53.8 | 30.8 | +0.02 (+/- 1.898) |
| +5 min | 13 | $0.372 | $-0.375 | 38.5 | 23.1 | -1.566 (+/- 1.77) |
| +10 min | 12 | $-2.285 | $-3.057 | 16.7 | 8.3 | -3.527 (+/- 2.894) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

14 trades: avg gross $-1.327, avg net $-2.062, win 28.6%, target 14.3%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
