# Random-entry baseline

Generated 2026-11-13T16:31:02+00:00. 22 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.815 | $1.122 | 54.5 | 36.4 |
| Random: A_same_symbol_day | $-0.207 (5-95%: -2.357 to 2.083) | $-0.9 | 39.4 | 19.6 |
| Random: B_within_15_min | $2.128 (5-95%: -0.253 to 4.478) | $1.436 | 54.5 | 37.8 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.082
- B_within_15_min: p = 0.576

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 22 | $1.815 | $1.122 | 54.5 | 36.4 | - |
| +1 min | 22 | $0.404 | $-0.289 | 45.5 | 27.3 | -1.412 (+/- 1.509) |
| +2 min | 22 | $1.863 | $1.171 | 54.5 | 31.8 | +0.048 (+/- 1.611) |
| +3 min | 21 | $1.54 | $0.847 | 52.4 | 28.6 | -0.64 (+/- 1.855) |
| +5 min | 20 | $-0.106 | $-0.806 | 40.0 | 15.0 | -2.671 (+/- 2.041) |
| +10 min | 20 | $-1.686 | $-2.386 | 30.0 | 10.0 | -4.251 (+/- 2.042) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

22 trades: avg gross $-1.12, avg net $-1.813, win 36.4%, target 18.2%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
