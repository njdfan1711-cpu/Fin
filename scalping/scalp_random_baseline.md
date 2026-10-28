# Random-entry baseline

Generated 2026-10-28T18:31:15+00:00. 26 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.358 | $-0.392 | 42.3 | 23.1 |
| Random: A_same_symbol_day | $-0.011 (5-95%: -2.016 to 2.083) | $-0.764 | 40.3 | 19.7 |
| Random: B_within_15_min | $2.078 (5-95%: 0.126 to 3.981) | $1.327 | 54.8 | 35.0 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.369
- B_within_15_min: p = 0.925

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 26 | $0.358 | $-0.392 | 42.3 | 23.1 | - |
| +1 min | 25 | $2.907 | $2.15 | 56.0 | 40.0 | +2.541 (+/- 1.115) |
| +2 min | 25 | $2.418 | $1.661 | 52.0 | 36.0 | +2.052 (+/- 1.272) |
| +3 min | 25 | $0.846 | $0.09 | 44.0 | 28.0 | +0.48 (+/- 1.253) |
| +5 min | 24 | $1.781 | $1.01 | 54.2 | 25.0 | +1.381 (+/- 1.653) |
| +10 min | 23 | $-1.029 | $-1.815 | 30.4 | 13.0 | -1.0 (+/- 1.873) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

26 trades: avg gross $-0.712, avg net $-1.462, win 30.8%, target 19.2%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
