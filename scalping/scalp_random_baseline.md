# Random-entry baseline

Generated 2026-10-21T14:31:17+00:00. 17 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.459 | $-0.239 | 41.2 | 23.5 |
| Random: A_same_symbol_day | $-0.425 (5-95%: -2.725 to 1.84) | $-1.122 | 37.9 | 15.5 |
| Random: B_within_15_min | $1.624 (5-95%: -0.658 to 4.001) | $0.927 | 52.2 | 28.5 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.264
- B_within_15_min: p = 0.799

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
