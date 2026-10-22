# Random-entry baseline

Generated 2026-10-22T16:30:58+00:00. 15 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.987 | $0.274 | 46.7 | 26.7 |
| Random: A_same_symbol_day | $-0.389 (5-95%: -2.809 to 2.212) | $-1.101 | 37.9 | 17.4 |
| Random: B_within_15_min | $1.396 (5-95%: -1.132 to 3.952) | $0.684 | 51.3 | 26.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.191
- B_within_15_min: p = 0.607

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 15 | $0.987 | $0.274 | 46.7 | 26.7 | - |
| +1 min | 14 | $1.83 | $1.107 | 57.1 | 28.6 | +0.783 (+/- 0.565) |
| +2 min | 14 | $1.573 | $0.85 | 50.0 | 28.6 | +0.527 (+/- 2.029) |
| +3 min | 14 | $1.354 | $0.632 | 50.0 | 21.4 | +0.308 (+/- 1.769) |
| +5 min | 13 | $-0.051 | $-0.797 | 30.8 | 23.1 | -1.376 (+/- 1.751) |
| +10 min | 13 | $-2.131 | $-2.877 | 15.4 | 7.7 | -3.456 (+/- 2.663) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

15 trades: avg gross $-0.829, avg net $-1.542, win 33.3%, target 13.3%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
