# Swing backtest: acting on Fin alerts automatically

Generated 2026-10-22T18:08:04+00:00. 1765 first-alerts of the day (2026-08-13 to 2026-10-22); 453 symbols with prices. Position $3,500, cost 0.1% round trip.

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

Cost sensitivity (avg net $ per trade, top1): {"0.05%": -3.55, "0.1%": -5.26, "0.25%": -10.39}

Conventions: stop counts first if a day touches both stop and target; gaps fill at the open; pre-open and after-close alerts fill at the next open; exits start the day after a regular-session alert. In-sample, about two months, one market regime.
