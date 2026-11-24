# Random-entry baseline

Generated 2026-11-24T20:31:07+00:00. 37 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.567 | $-1.153 | 35.1 | 21.6 |
| Random: A_same_symbol_day | $-0.342 (5-95%: -2.156 to 1.393) | $-0.926 | 36.7 | 24.2 |
| Random: B_within_15_min | $1.841 (5-95%: 0.072 to 3.627) | $1.257 | 51.9 | 38.3 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.576
- B_within_15_min: p = 0.993

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 37 | $-0.567 | $-1.153 | 35.1 | 21.6 | - |
| +1 min | 37 | $-2.253 | $-2.839 | 24.3 | 5.4 | -1.686 (+/- 0.798) |
| +2 min | 37 | $-2.099 | $-2.684 | 29.7 | 5.4 | -1.531 (+/- 0.701) |
| +3 min | 36 | $-2.157 | $-2.715 | 33.3 | 2.8 | -1.285 (+/- 0.952) |
| +5 min | 28 | $-0.794 | $-1.327 | 35.7 | 17.9 | +1.834 (+/- 1.361) |
| +10 min | 28 | $0.312 | $-0.22 | 42.9 | 21.4 | +2.939 (+/- 1.573) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

37 trades: avg gross $1.371, avg net $0.786, win 48.6%, target 35.1%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
