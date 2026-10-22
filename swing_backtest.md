# Swing backtest: acting on Fin alerts automatically

Generated 2026-10-22T18:42:11+00:00. 1765 first-alerts of the day (2026-08-13 to 2026-10-22); 453 symbols with prices. Position $3,500, cost 0.1% round trip.

| Scenario | View | Trades | Win % | Avg net % | Avg net $ | Total net $ | $/biz day | Avg days | Max DD $ |
|---|---|---|---|---|---|---|---|---|---|
| A. take-profit +0.5 ATR, stop 1.5 ATR, inactivity stop, 7-day max | all | 1671 | 69.1 | -0.31 | -10.25 | -17128.89 | None | 2.2 | -21025.0 |
| A. take-profit +0.5 ATR, stop 1.5 ATR, inactivity stop, 7-day max | top1/day | 50 | 74.0 | -0.16 | -5.26 | -263.14 | -5.37 | 1.9 | -1051.3 |
| B. same, but full target +3 ATR | all | 1567 | 36.9 | -1.05 | -35.17 | -55118.24 | None | 4.9 | -56423.56 |
| B. same, but full target +3 ATR | top1/day | 45 | 42.2 | 0.03 | 2.13 | 95.63 | 1.95 | 4.3 | -1867.51 |
| C. take-profit, NO inactivity stop | all | 1669 | 69.4 | -0.31 | -10.06 | -16797.07 | None | 2.2 | -20787.12 |
| C. take-profit, NO inactivity stop | top1/day | 50 | 76.0 | -0.2 | -6.91 | -345.26 | -7.05 | 2.1 | -1174.94 |
| D. take-profit, NO stop (ride dips; diagnostic of 'hold through dips') | all | 1623 | 75.7 | -0.34 | -11.04 | -17917.09 | None | 3.1 | -32330.9 |
| D. take-profit, NO stop (ride dips; diagnostic of 'hold through dips') | top1/day | 50 | 82.0 | 0.37 | 12.89 | 644.38 | 13.15 | 2.5 | -1042.0 |

## Exit reasons (scenario A, top1 account)

{"inactive": 2, "max_hold": 1, "stop": 7, "stop_gap": 3, "target": 33, "target_gap": 4}

## Inactivity-rule sensitivity (top1 account, in-sample -- do not tune on it)

| Days | Band (ATR) | Trades | Win % | Avg net $ |
|---|---|---|---|---|
| 2 | 0.15 | 50 | 76.0 | -1.27 |
| 2 | 0.25 | 50 | 72.0 | -4.23 |
| 2 | 0.5 | 50 | 70.0 | -2.51 |
| 3 | 0.15 | 50 | 76.0 | -3.59 |
| 3 | 0.25 | 50 | 74.0 | -5.26 |
| 3 | 0.5 | 50 | 74.0 | -5.59 |
| 5 | 0.15 | 50 | 76.0 | -6.91 |
| 5 | 0.25 | 50 | 76.0 | -7.72 |
| 5 | 0.5 | 50 | 76.0 | -7.72 |

## Your logged trades replayed under the same rules

19 trades (skipped: SEZL: not enough price history for ATR). ATR = simple 14-day average true range the day before entry.

| | You (actual) | Rules A (stop + take-profit + inactivity) | Rules D (no stop) |
|---|---|---|---|
| Win rate | 100.0% | 73.7% | |
| Avg net % per trade | 1.59 | -0.06 | 0.95 |

- Fin's stop level was reached while you held: PSIX, CDNA, SLDE. Under rules A, 4 of 19 would have been stopped out.
- Your picks had a Fin alert that day for 17 of 19 trades (median Fin rank 8, 1 = top).
- Fin's top pick on your entry days, under rules A: avg -1.19% per trade.

| Symbol | Entry | You: net % / days / worst dip | Rules A | Rules D | Fin rank that day |
|---|---|---|---|---|---|
| PSIX | 2026-08-13 @ 41.03 | 0.66% / 18d / -15.5% (Fin stop hit) | stop -11.77% | max_hold -14.87% | 4 of 26 |
| SSRM | 2026-08-26 @ 38.28 | 1.13% / 1d / -0.5% | target_gap 2.46% | target_gap 2.46% | 10 of 19 |
| CHYM | 2026-08-24 @ 32.92 | 0.51% / 2d / -1.6% | target 2.774% | target 2.774% | 21 of 30 |
| B | 2026-08-20 @ 46.15 | 4.04% / 2d / 0.3% | target_gap 2.609% | target_gap 2.609% | 2 of 28 |
| ETOR | 2026-08-18 @ 27.57 | 3.96% / 1d / 0.7% | target 2.696% | target 2.696% | 29 of 33 |
| A | 2026-08-19 @ 154.71 | 2.3% / 1d / 0.5% | target 0.879% | target 0.879% | 4 of 34 |
| CDNA | 2026-08-28 @ 51.38 | 0.54% / 11d / -9.1% (Fin stop hit) | stop -6.391% | max_hold -2.727% | no alert |
| A | 2026-09-08 @ 147.53 | 1.91% / 5d / -4.3% | target 1.654% | target 1.654% | 8 of 30 |
| SLDE | 2026-09-14 @ 26.09 | 0.21% / 23d / -14.7% (Fin stop hit) | target 1.221% | target 1.221% | 12 of 24 |
| STNG | 2026-09-15 @ 85.72 | 3.06% / 2d / -0.5% | target 1.215% | target 1.215% | 3 of 30 |
| PINS | 2026-09-18 @ 18.39 | 2.24% / 1d / 1.1% | target 2.281% | target 2.281% | no alert |
| HPE | 2026-09-23 @ 61.99 | 1.27% / 1d / 0.5% | target 3.303% | target 3.303% | 31 of 52 |
| S | 2026-09-24 @ 23.94 | 1.19% / 0d / 0.2% | stop -6.939% | target 2.18% | 1 of 37 |
| AVT | 2026-09-25 @ 103.41 | 2.69% / 5d / -4.7% | target 1.747% | target 1.747% | 10 of 33 |
| NAT | 2026-10-05 @ 8.41 | 0.14% / 2d / -3.3% | target 1.904% | target 1.904% | 3 of 35 |
| INSW | 2026-10-07 @ 118.44 | 2.15% / 1d / -1.3% | target 1.964% | target 1.964% | 23 of 36 |
| PENG | 2026-10-09 @ 72.84 | 0.75% / 0d / 4.7% | target_gap 3.826% | target_gap 3.826% | 7 of 41 |
| PAYS | 2026-10-12 @ 15.38 | 1.01% / 1d / -1.4% | stop -6.6% | target 2.067% | 6 of 34 |
| PBR | 2026-10-14 @ 25.8 | 0.48% / 5d / -2.7% | unresolved None% | unresolved None% | 10 of 37 |

Cost sensitivity (avg net $ per trade, top1): {"0.05%": -3.55, "0.1%": -5.26, "0.25%": -10.39}

Conventions: stop counts first if a day touches both stop and target; gaps fill at the open; pre-open and after-close alerts fill at the next open; exits start the day after a regular-session alert. In-sample, about two months, one market regime.
