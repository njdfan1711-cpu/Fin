# Random-entry baseline

Generated 2026-10-21T13:31:22+00:00. 11 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-2.049 | $-2.702 | 27.3 | 0.0 |
| Random: A_same_symbol_day | $-0.059 (5-95%: -2.842 to 2.875) | $-0.715 | 41.5 | 13.9 |
| Random: B_within_15_min | $2.043 (5-95%: -0.646 to 4.616) | $1.39 | 54.1 | 27.0 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.875
- B_within_15_min: p = 0.997

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
