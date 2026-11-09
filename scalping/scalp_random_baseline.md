# Random-entry baseline

Generated 2026-11-09T19:31:28+00:00. 33 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $2.067 | $1.261 | 51.5 | 36.4 |
| Random: A_same_symbol_day | $-0.289 (5-95%: -1.962 to 1.468) | $-1.098 | 37.5 | 20.8 |
| Random: B_within_15_min | $2.277 (5-95%: 0.387 to 4.251) | $1.467 | 53.5 | 41.0 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.022
- B_within_15_min: p = 0.566

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 33 | $2.067 | $1.261 | 51.5 | 36.4 | - |
| +1 min | 32 | $-1.193 | $-1.981 | 31.2 | 15.6 | -3.39 (+/- 1.034) |
| +2 min | 30 | $0.796 | $0.03 | 46.7 | 26.7 | -1.023 (+/- 1.084) |
| +3 min | 30 | $0.511 | $-0.255 | 43.3 | 23.3 | -1.307 (+/- 1.294) |
| +5 min | 28 | $0.25 | $-0.509 | 39.3 | 28.6 | -1.944 (+/- 1.706) |
| +10 min | 24 | $-2.727 | $-3.495 | 20.8 | 8.3 | -4.969 (+/- 2.048) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

33 trades: avg gross $-0.93, avg net $-1.736, win 36.4%, target 15.2%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
