# Random-entry baseline

Generated 2026-11-10T19:31:17+00:00. 30 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.973 | $1.191 | 50.0 | 40.0 |
| Random: A_same_symbol_day | $-0.193 (5-95%: -1.992 to 1.656) | $-0.973 | 38.6 | 20.6 |
| Random: B_within_15_min | $1.841 (5-95%: -0.293 to 3.935) | $1.06 | 50.6 | 38.7 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.035
- B_within_15_min: p = 0.478

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 30 | $1.973 | $1.191 | 50.0 | 40.0 | - |
| +1 min | 30 | $-1.048 | $-1.83 | 30.0 | 20.0 | -3.021 (+/- 1.07) |
| +2 min | 28 | $1.159 | $0.401 | 46.4 | 32.1 | -0.392 (+/- 1.053) |
| +3 min | 28 | $1.029 | $0.271 | 42.9 | 28.6 | -0.522 (+/- 1.314) |
| +5 min | 26 | $0.038 | $-0.712 | 34.6 | 26.9 | -1.898 (+/- 1.466) |
| +10 min | 25 | $-2.569 | $-3.335 | 24.0 | 8.0 | -4.471 (+/- 1.97) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

30 trades: avg gross $-1.39, avg net $-2.172, win 33.3%, target 10.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
