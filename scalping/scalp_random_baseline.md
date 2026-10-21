# Random-entry baseline

Generated 2026-10-21T18:31:20+00:00. 13 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.67 | $-2.296 | 30.8 | 0.0 |
| Random: A_same_symbol_day | $-0.145 (5-95%: -2.671 to 2.493) | $-0.774 | 40.8 | 13.7 |
| Random: B_within_15_min | $2.125 (5-95%: -0.624 to 4.879) | $1.499 | 53.3 | 30.6 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.839
- B_within_15_min: p = 0.99

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
