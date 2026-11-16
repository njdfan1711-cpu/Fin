# Random-entry baseline

Generated 2026-11-16T20:31:28+00:00. 22 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.49 | $-1.243 | 40.9 | 18.2 |
| Random: A_same_symbol_day | $-0.164 (5-95%: -2.229 to 2.029) | $-0.917 | 40.2 | 17.0 |
| Random: B_within_15_min | $2.283 (5-95%: 0.084 to 4.634) | $1.53 | 55.4 | 35.0 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.601
- B_within_15_min: p = 0.976

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 22 | $-0.49 | $-1.243 | 40.9 | 18.2 | - |
| +1 min | 22 | $-0.594 | $-1.347 | 40.9 | 18.2 | -0.105 (+/- 1.163) |
| +2 min | 22 | $-0.319 | $-1.072 | 40.9 | 18.2 | +0.171 (+/- 1.393) |
| +3 min | 21 | $0.305 | $-0.451 | 38.1 | 23.8 | +0.54 (+/- 1.813) |
| +5 min | 21 | $-0.175 | $-0.931 | 33.3 | 14.3 | +0.06 (+/- 1.874) |
| +10 min | 20 | $-2.46 | $-3.195 | 25.0 | 5.0 | -2.511 (+/- 1.889) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

22 trades: avg gross $0.495, avg net $-0.258, win 50.0%, target 22.7%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
