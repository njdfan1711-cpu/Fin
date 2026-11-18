# Random-entry baseline

Generated 2026-11-18T20:31:08+00:00. 26 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.397 | $-2.11 | 34.6 | 15.4 |
| Random: A_same_symbol_day | $-0.185 (5-95%: -2.203 to 1.907) | $-0.895 | 38.1 | 22.4 |
| Random: B_within_15_min | $2.101 (5-95%: 0.025 to 4.334) | $1.39 | 53.2 | 36.8 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.824
- B_within_15_min: p = 0.995

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 26 | $-1.397 | $-2.11 | 34.6 | 15.4 | - |
| +1 min | 26 | $-1.547 | $-2.26 | 34.6 | 11.5 | -0.151 (+/- 0.984) |
| +2 min | 26 | $-1.702 | $-2.415 | 30.8 | 11.5 | -0.305 (+/- 0.939) |
| +3 min | 25 | $-1.183 | $-1.897 | 32.0 | 16.0 | +0.036 (+/- 1.304) |
| +5 min | 21 | $-1.166 | $-1.856 | 28.6 | 14.3 | +1.877 (+/- 1.584) |
| +10 min | 20 | $-0.154 | $-0.819 | 35.0 | 20.0 | +2.744 (+/- 1.887) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

26 trades: avg gross $2.517, avg net $1.804, win 61.5%, target 34.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
