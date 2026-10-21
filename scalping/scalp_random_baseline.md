# Random-entry baseline

Generated 2026-10-21T17:31:01+00:00. 18 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.106 | $-0.578 | 38.9 | 22.2 |
| Random: A_same_symbol_day | $-0.391 (5-95%: -2.655 to 2.039) | $-1.073 | 38.2 | 16.3 |
| Random: B_within_15_min | $1.356 (5-95%: -0.913 to 3.82) | $0.673 | 50.4 | 26.8 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.347
- B_within_15_min: p = 0.807

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
