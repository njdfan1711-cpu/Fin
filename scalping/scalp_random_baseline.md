# Random-entry baseline

Generated 2026-11-12T16:31:08+00:00. 24 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $3.127 | $2.378 | 58.3 | 45.8 |
| Random: A_same_symbol_day | $-0.177 (5-95%: -2.309 to 2.053) | $-0.925 | 38.1 | 23.8 |
| Random: B_within_15_min | $1.763 (5-95%: -0.444 to 4.022) | $1.016 | 50.3 | 38.3 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.012
- B_within_15_min: p = 0.161

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 24 | $3.127 | $2.378 | 58.3 | 45.8 | - |
| +1 min | 24 | $0.979 | $0.231 | 45.8 | 29.2 | -2.147 (+/- 1.43) |
| +2 min | 23 | $2.89 | $2.176 | 60.9 | 39.1 | +0.072 (+/- 1.515) |
| +3 min | 23 | $1.975 | $1.261 | 52.2 | 30.4 | -0.843 (+/- 1.622) |
| +5 min | 21 | $1.43 | $0.729 | 47.6 | 28.6 | -1.984 (+/- 1.785) |
| +10 min | 21 | $-3.077 | $-3.777 | 19.0 | 4.8 | -6.491 (+/- 1.956) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

24 trades: avg gross $-2.591, avg net $-3.339, win 25.0%, target 12.5%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
