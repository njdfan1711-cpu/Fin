# Random-entry baseline

Generated 2026-11-06T14:31:03+00:00. 33 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $2.033 | $1.257 | 51.5 | 33.3 |
| Random: A_same_symbol_day | $-0.336 (5-95%: -2.214 to 1.599) | $-1.116 | 37.0 | 21.9 |
| Random: B_within_15_min | $2.774 (5-95%: 0.82 to 4.859) | $1.994 | 57.2 | 44.3 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.026
- B_within_15_min: p = 0.728

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 33 | $2.033 | $1.257 | 51.5 | 33.3 | - |
| +1 min | 32 | $-0.319 | $-1.077 | 37.5 | 18.8 | -2.481 (+/- 1.117) |
| +2 min | 30 | $1.139 | $0.405 | 50.0 | 26.7 | -0.642 (+/- 1.012) |
| +3 min | 30 | $0.578 | $-0.156 | 46.7 | 23.3 | -1.203 (+/- 1.245) |
| +5 min | 28 | $0.418 | $-0.306 | 46.4 | 28.6 | -1.736 (+/- 1.513) |
| +10 min | 22 | $-1.636 | $-2.354 | 27.3 | 13.6 | -3.831 (+/- 2.208) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

33 trades: avg gross $-1.294, avg net $-2.071, win 33.3%, target 15.2%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
