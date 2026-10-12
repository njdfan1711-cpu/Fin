# Scalp signal analysis (trail exits)

_114 tagged trades, 7 trading days (2026-10-01 to 2026-10-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 114 | 38% (29-47) | +0.27 | -1.66 | -189 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 37 | +81 | +2.19 | 77 | -270 | -3.50 | -81 |
| skip first 30 min | 27 | +32 | +1.20 | 87 | -221 | -2.54 | -32 |
| skip when SPY is down on the day | 35 | -57 | -1.62 | 79 | -132 | -1.67 | +57 |
| skip when SPY is below its VWAP | 36 | -84 | -2.33 | 78 | -105 | -1.35 | +84 |
| skip when SPY fell over the last 15 min | 36 | -63 | -1.74 | 78 | -126 | -1.62 | +63 |
| skip over-extended (30-min run in top quarter, > 0.45%) | 22 | -99 | -4.50 | 92 | -90 | -0.98 | +99 |
| skip stock not beating SPY over 15 min | 10 | -36 | -3.59 | 104 | -153 | -1.47 | +36 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 59 | -157 | -2.66 | 55 | -32 | -0.58 | +157 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 27 | 44% (28-63) | +2.27 | +1.20 | +32 |  |
| 15-60 | 12 | 50% (25-75) | +0.57 | -2.20 | -26 |  |
| 60-240 | 40 | 28% (16-43) | -1.13 | -2.70 | -108 |  |
| 240-375 | 25 | 32% (17-52) | -2.64 | -5.42 | -135 |  |
| 375-390 | 10 | 60% (31-83) | +7.35 | +4.86 | +49 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 11 | 27% (10-57) | -1.30 | -3.13 | -34 |  |
| -0.2 to 0 | 24 | 42% (24-61) | +1.45 | -0.93 | -22 |  |
| 0 to 0.2 | 43 | 33% (20-47) | -1.01 | -2.40 | -103 |  |
| > 0.2 | 36 | 44% (30-60) | +1.49 | -0.80 | -29 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 36 | 31% (18-47) | -0.13 | -2.33 | -84 |  |
| above VWAP | 78 | 41% (31-52) | +0.45 | -1.35 | -105 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 29 | 34% (20-53) | +1.13 | -0.45 | -13 |  |
| (0.136, 0.374] | 29 | 45% (28-62) | -0.94 | -3.21 | -93 |  |
| (0.374, 1.123] | 29 | 28% (15-46) | -1.24 | -3.96 | -115 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.193] | 29 | 41% (26-59) | +1.78 | +0.21 | +6 |  |
| (0.193, 0.405] | 29 | 31% (17-49) | -1.41 | -3.83 | -111 |  |
| (0.405, 1.022] | 29 | 34% (20-53) | -1.42 | -4.00 | -116 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.089] | 38 | 34% (21-50) | -0.77 | -3.34 | -127 |  |
| (-0.089, 0.339] | 38 | 45% (30-60) | +1.81 | +0.51 | +19 |  |
| (0.339, 2.726] | 38 | 34% (21-50) | -0.23 | -2.14 | -81 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.0029, 0.0606] | 38 | 45% (30-60) | +1.10 | -0.56 | -21 |  |
| (0.0606, 0.141] | 38 | 37% (23-53) | -1.09 | -2.90 | -110 |  |
| (0.141, 0.786] | 38 | 32% (19-47) | +0.79 | -1.51 | -57 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.153, 0.22] | 38 | 50% (35-65) | +1.73 | +0.53 | +20 |  |
| (0.22, 0.422] | 38 | 26% (15-42) | -1.60 | -4.50 | -171 |  |
| (0.422, 3.871] | 38 | 37% (23-53) | +0.68 | -1.00 | -38 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.546] | 38 | 45% (30-60) | +0.05 | -2.07 | -79 |  |
| (2.546, 5.131] | 38 | 34% (21-50) | +0.44 | -1.50 | -57 |  |
| (5.131, 18.76] | 38 | 34% (21-50) | +0.32 | -1.39 | -53 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0951] | 38 | 47% (32-63) | +1.45 | +0.75 | +29 |  |
| (0.0951, 0.146] | 38 | 39% (26-55) | -0.65 | -1.95 | -74 |  |
| (0.146, 0.392] | 38 | 26% (15-42) | +0.01 | -3.77 | -143 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.17%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 16% of trades
- Reached +0.5% at some point: 6% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 52, trail_stop 44, time_stop 18

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0951] | 38 | 29% | 37% | 34% |
| (0.0951, 0.146] | 38 | 50% | 42% | 8% |
| (0.146, 0.392] | 38 | 58% | 37% | 5% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
