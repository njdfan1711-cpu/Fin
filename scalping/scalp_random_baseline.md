# Random-entry baseline

Generated 2026-11-19T19:31:11+00:00. 27 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.022 | $-1.721 | 37.0 | 18.5 |
| Random: A_same_symbol_day | $-0.223 (5-95%: -2.252 to 1.815) | $-0.919 | 37.9 | 22.7 |
| Random: B_within_15_min | $2.393 (5-95%: 0.18 to 4.632) | $1.696 | 54.8 | 39.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.737
- B_within_15_min: p = 0.996

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 27 | $-1.022 | $-1.721 | 37.0 | 18.5 | - |
| +1 min | 27 | $-1.67 | $-2.369 | 33.3 | 11.1 | -0.648 (+/- 1.069) |
| +2 min | 27 | $-1.819 | $-2.517 | 29.6 | 11.1 | -0.797 (+/- 1.029) |
| +3 min | 26 | $-1.408 | $-2.107 | 30.8 | 15.4 | -0.571 (+/- 1.354) |
| +5 min | 21 | $-1.162 | $-1.833 | 28.6 | 14.3 | +1.877 (+/- 1.584) |
| +10 min | 20 | $-0.15 | $-0.795 | 35.0 | 20.0 | +2.745 (+/- 1.887) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

27 trades: avg gross $2.463, avg net $1.765, win 59.3%, target 37.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
