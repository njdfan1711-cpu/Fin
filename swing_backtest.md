# Swing backtest: acting on Fin alerts automatically

Generated 2026-10-23T03:57:27+00:00. 1766 first-alerts of the day (2026-08-13 to 2026-10-22); 454 symbols with prices. Position $3,500, cost 0.1% round trip.

| Scenario | View | Trades | Win % | Avg net % | Avg net $ | Total net $ | $/biz day | Avg days | Max DD $ |
|---|---|---|---|---|---|---|---|---|---|
| A. take-profit +0.5 ATR, stop 1.5 ATR, inactivity stop, 7-day max | all | 1710 | 68.7 | -0.35 | -11.47 | -19620.08 | None | 2.2 | -21987.79 |
| A. take-profit +0.5 ATR, stop 1.5 ATR, inactivity stop, 7-day max | top1/day | 51 | 70.6 | -0.35 | -11.94 | -608.85 | -12.18 | 1.9 | -1200.5 |
| B. same, but full target +3 ATR | all | 1599 | 36.6 | -1.08 | -36.18 | -57846.95 | None | 4.9 | -57846.95 |
| B. same, but full target +3 ATR | top1/day | 45 | 40.0 | -1.02 | -34.04 | -1531.8 | -30.64 | 4.3 | -2760.14 |
| C. take-profit, NO inactivity stop | all | 1705 | 69.0 | -0.34 | -11.32 | -19300.39 | None | 2.2 | -21749.91 |
| C. take-profit, NO inactivity stop | top1/day | 51 | 72.5 | -0.4 | -13.55 | -690.97 | -13.82 | 2.1 | -1324.14 |
| D. take-profit, NO stop (ride dips; diagnostic of 'hold through dips') | all | 1668 | 74.9 | -0.51 | -16.8 | -28027.24 | None | 3.2 | -41769.36 |
| D. take-profit, NO stop (ride dips; diagnostic of 'hold through dips') | top1/day | 51 | 80.4 | -0.04 | -0.88 | -45.07 | -0.9 | 2.6 | -1042.0 |
| E. quick +1.0% target, stop 1.5 ATR, inactivity stop | all | 1722 | 77.5 | -0.3 | -9.97 | -17172.38 | None | 1.7 | -19741.65 |
| E. quick +1.0% target, stop 1.5 ATR, inactivity stop | top1/day | 51 | 86.3 | 0.01 | 0.41 | 20.79 | 0.42 | 1.4 | -743.01 |
| F. quick +1.0% target, NO stop | all | 1684 | 83.8 | -0.29 | -9.07 | -15275.77 | None | 2.4 | -27410.87 |
| F. quick +1.0% target, NO stop | top1/day | 51 | 90.2 | 0.35 | 12.09 | 616.34 | 12.33 | 1.8 | -650.13 |

## Exit reasons (scenario A, top1 account)

{"inactive": 2, "max_hold": 1, "stop": 9, "stop_gap": 3, "target": 32, "target_gap": 4}

## Inactivity-rule sensitivity (top1 account, in-sample -- do not tune on it)

| Days | Band (ATR) | Trades | Win % | Avg net $ |
|---|---|---|---|---|
| 2 | 0.15 | 51 | 72.5 | -8.03 |
| 2 | 0.25 | 51 | 68.6 | -10.59 |
| 2 | 0.5 | 51 | 66.7 | -8.7 |
| 3 | 0.15 | 51 | 72.5 | -10.3 |
| 3 | 0.25 | 51 | 70.6 | -11.94 |
| 3 | 0.5 | 51 | 70.6 | -12.26 |
| 5 | 0.15 | 51 | 72.5 | -13.55 |
| 5 | 0.25 | 51 | 72.5 | -14.34 |
| 5 | 0.5 | 51 | 72.5 | -14.34 |

## Your logged trades replayed under the same rules

20 trades (skipped: none). ATR = simple 14-day average true range the day before entry.

| | You (actual) | Rules A (stop + take-profit + inactivity) | Rules D (no stop) | Rules E (+1% target + stop) |
|---|---|---|---|---|
| Win rate | 100.0% | 70.0% | | 85.0% |
| Avg net % per trade | 1.55 | -0.06 | 0.95 | 0.4 |

- Fin's stop level was reached while you held: PSIX, CDNA, SLDE. Under rules A, 4 of 20 would have been stopped out.
- Your picks had a Fin alert that day for 18 of 20 trades (median Fin rank 10, 1 = top).
- Fin's top pick on your entry days, under rules A: avg -1.19% per trade.

| Symbol | Entry | You: net % / days / worst dip | Rules A | Rules D | Rules E | Fin rank that day |
|---|---|---|---|---|---|---|
| PSIX | 2026-08-13 @ 41.03 | 0.66% / 18d / -15.5% (Fin stop hit) | stop -11.77% | max_hold -14.87% | target 0.9% | 4 of 26 |
| SSRM | 2026-08-26 @ 38.28 | 1.13% / 1d / -0.5% | target_gap 2.46% | target_gap 2.46% | target 0.9% | 10 of 19 |
| CHYM | 2026-08-24 @ 32.92 | 0.51% / 2d / -1.6% | target 2.774% | target 2.774% | target 0.9% | 21 of 30 |
| B | 2026-08-20 @ 46.15 | 4.04% / 2d / 0.3% | target_gap 2.609% | target_gap 2.609% | target_gap 2.609% | 2 of 28 |
| ETOR | 2026-08-18 @ 27.57 | 3.96% / 1d / 0.7% | target 2.696% | target 2.696% | target 0.9% | 29 of 33 |
| A | 2026-08-19 @ 154.71 | 2.3% / 1d / 0.5% | target 0.879% | target 0.879% | target 0.9% | 4 of 34 |
| CDNA | 2026-08-28 @ 51.38 | 0.54% / 11d / -9.1% (Fin stop hit) | stop -6.391% | max_hold -2.727% | stop -6.391% | no alert |
| A | 2026-09-08 @ 147.53 | 1.91% / 5d / -4.3% | target 1.654% | target 1.654% | target 0.9% | 8 of 30 |
| SLDE | 2026-09-14 @ 26.09 | 0.21% / 23d / -14.7% (Fin stop hit) | target 1.221% | target 1.221% | target 0.9% | 12 of 24 |
| STNG | 2026-09-15 @ 85.72 | 3.06% / 2d / -0.5% | target 1.215% | target 1.215% | target 0.9% | 3 of 30 |
| PINS | 2026-09-18 @ 18.39 | 2.24% / 1d / 1.1% | target 2.281% | target 2.281% | target_gap 1.858% | no alert |
| HPE | 2026-09-23 @ 61.99 | 1.27% / 1d / 0.5% | target 3.303% | target 3.303% | target 0.9% | 31 of 52 |
| S | 2026-09-24 @ 23.94 | 1.19% / 0d / 0.2% | stop -6.939% | target 2.18% | stop -6.939% | 1 of 37 |
| AVT | 2026-09-25 @ 103.41 | 2.69% / 5d / -4.7% | target 1.747% | target 1.747% | target 0.9% | 10 of 33 |
| NAT | 2026-10-05 @ 8.41 | 0.14% / 2d / -3.3% | target 1.904% | target 1.904% | target 0.9% | 3 of 35 |
| INSW | 2026-10-07 @ 118.44 | 2.15% / 1d / -1.3% | target 1.964% | target 1.964% | target 0.9% | 23 of 36 |
| PENG | 2026-10-09 @ 72.84 | 0.75% / 0d / 4.7% | target_gap 3.826% | target_gap 3.826% | target_gap 3.826% | 7 of 41 |
| PAYS | 2026-10-12 @ 15.38 | 1.01% / 1d / -1.4% | stop -6.6% | target 2.067% | target 0.9% | 6 of 34 |
| PBR | 2026-10-14 @ 25.8 | 0.48% / 5d / -2.7% | unresolved None% | unresolved None% | target 0.9% | 10 of 37 |
| SEZL | 2026-10-22 @ 136.0 | 0.72% / 0d / 2.4% | unresolved None% | unresolved None% | unresolved None% | 22 of 34 |

Quick-target break-even: with a +1.0% target and the median stop of -5.78%, the win rate must exceed 86.7% to break even after costs.

Cost sensitivity (avg net $ per trade, top1): {"0.05%": -10.23, "0.1%": -11.94, "0.25%": -17.06}

Conventions: stop counts first if a day touches both stop and target; gaps fill at the open; pre-open and after-close alerts fill at the next open; exits start the day after a regular-session alert. In-sample, about two months, one market regime.
