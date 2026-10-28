# Random-entry baseline

Generated 2026-10-28T16:31:26+00:00. 21 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.306 | $-0.448 | 42.9 | 19.0 |
| Random: A_same_symbol_day | $-0.076 (5-95%: -2.276 to 2.089) | $-0.83 | 40.9 | 17.6 |
| Random: B_within_15_min | $2.34 (5-95%: 0.274 to 4.392) | $1.586 | 57.8 | 34.0 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.399
- B_within_15_min: p = 0.947

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 21 | $0.306 | $-0.448 | 42.9 | 19.0 | - |
| +1 min | 20 | $2.434 | $1.671 | 55.0 | 35.0 | +2.121 (+/- 1.187) |
| +2 min | 20 | $2.736 | $1.974 | 55.0 | 35.0 | +2.423 (+/- 1.581) |
| +3 min | 20 | $0.912 | $0.149 | 45.0 | 25.0 | +0.599 (+/- 1.573) |
| +5 min | 19 | $2.106 | $1.327 | 57.9 | 21.1 | +1.752 (+/- 2.092) |
| +10 min | 18 | $0.318 | $-0.48 | 38.9 | 16.7 | +0.516 (+/- 2.043) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

21 trades: avg gross $-0.86, avg net $-1.614, win 28.6%, target 19.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
