# Scalp signal analysis (fixed exits)

_191 tagged trades, 21 trading days (2026-10-01 to 2026-10-29). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 191 | 39% (32-46) | -0.03 | -1.87 | -358 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 26 | -8 | -0.31 | 165 | -350 | -2.12 | +8 |
| skip first 30 min | 1 | -6 | -6.31 | 190 | -352 | -1.85 | +6 |
| skip when SPY is down on the day | 74 | -117 | -1.58 | 117 | -241 | -2.06 | +117 |
| skip when SPY is below its VWAP | 78 | -187 | -2.39 | 113 | -171 | -1.52 | +187 |
| skip when SPY fell over the last 15 min | 71 | -131 | -1.85 | 120 | -227 | -1.89 | +131 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 48 | -166 | -3.47 | 143 | -192 | -1.34 | +166 |
| skip stock not beating SPY over 15 min | 32 | -36 | -1.12 | 159 | -322 | -2.02 | +36 |
| skip afternoon entries (2:00-3:45 PM) | 42 | -215 | -5.12 | 149 | -143 | -0.96 | +215 |
| skip volume spikes above 5x average | 35 | -147 | -4.19 | 156 | -211 | -1.35 | +147 |
| skip when the stop is inside normal noise (range > stop) | 8 | -8 | -0.99 | 183 | -350 | -1.91 | +8 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.62%) | 18 | -51 | -2.83 | 173 | -307 | -1.77 | +51 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 103 | -286 | -2.78 | 88 | -72 | -0.81 | +286 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 27 | 63% (44-78) | +3.45 | +1.40 | +38 | ▲ |
| 60-240 | 83 | 36% (27-47) | -0.38 | -1.89 | -157 |  |
| 240-375 | 55 | 27% (17-40) | -2.09 | -4.20 | -231 |  |
| 375-390 | 26 | 46% (29-65) | +1.81 | -0.31 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 25 | 44% (27-63) | +0.76 | -0.94 | -23 |  |
| -0.2 to 0 | 49 | 41% (28-55) | +0.32 | -1.90 | -93 |  |
| 0 to 0.2 | 59 | 36% (25-48) | -0.07 | -1.46 | -86 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 78 | 37% (27-48) | -0.32 | -2.39 | -187 |  |
| above VWAP | 113 | 40% (31-49) | +0.17 | -1.52 | -171 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.134] | 64 | 39% (28-51) | +0.08 | -1.36 | -87 |  |
| (0.134, 0.372] | 63 | 41% (30-54) | -0.11 | -1.94 | -122 |  |
| (0.372, 1.555] | 64 | 36% (25-48) | -0.06 | -2.32 | -149 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.141] | 64 | 41% (29-53) | +0.11 | -1.45 | -93 |  |
| (0.141, 0.405] | 63 | 43% (31-55) | +0.81 | -1.14 | -72 |  |
| (0.405, 1.281] | 63 | 33% (23-46) | -0.92 | -2.97 | -187 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.29] | 64 | 39% (28-51) | +0.14 | -2.01 | -129 |  |
| (-0.29, 0.364] | 63 | 44% (33-57) | +0.97 | -0.28 | -17 |  |
| (0.364, 2.726] | 64 | 33% (23-45) | -1.19 | -3.31 | -212 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 64 | 39% (28-51) | -0.35 | -1.96 | -125 |  |
| (0.0521, 0.122] | 63 | 46% (34-58) | +0.93 | -0.71 | -45 |  |
| (0.122, 0.678] | 64 | 31% (21-43) | -0.66 | -2.94 | -188 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.207] | 64 | 42% (31-54) | -0.04 | -1.30 | -83 |  |
| (0.207, 0.313] | 63 | 41% (30-54) | +0.57 | -1.45 | -91 |  |
| (0.313, 0.875] | 64 | 33% (23-45) | -0.62 | -2.87 | -184 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.392] | 64 | 39% (28-51) | +0.24 | -1.52 | -97 |  |
| (2.392, 3.635] | 63 | 46% (34-58) | +0.81 | -1.06 | -67 |  |
| (3.635, 18.762] | 64 | 31% (21-43) | -1.12 | -3.03 | -194 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0968] | 64 | 47% (35-59) | +0.43 | -0.32 | -20 |  |
| (0.0968, 0.145] | 64 | 36% (25-48) | -0.01 | -1.30 | -83 |  |
| (0.145, 0.392] | 63 | 33% (23-46) | -0.52 | -4.04 | -255 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.514] | 22 | 23% (10-43) | -2.28 | -3.17 | -70 |  |
| (-0.514, 0.464] | 21 | 43% (24-63) | +0.42 | -0.08 | -2 |  |
| (0.464, 5.305] | 22 | 59% (39-77) | +2.60 | +1.90 | +42 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.485] | 24 | 42% (24-61) | -0.18 | -0.84 | -20 |  |
| (0.485, 0.694] | 25 | 40% (23-59) | +0.33 | -0.39 | -10 |  |
| (0.694, 1.74] | 23 | 39% (22-59) | -0.24 | -1.05 | -24 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.769] | 24 | 50% (31-69) | +1.27 | +0.83 | +20 |  |
| (0.769, 1.192] | 24 | 33% (18-53) | -0.43 | -1.23 | -30 |  |
| (1.192, 3.566] | 24 | 38% (21-57) | -0.91 | -1.85 | -44 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.35] | 24 | 38% (21-57) | -0.23 | -0.83 | -20 |  |
| (0.35, 0.554] | 24 | 50% (31-69) | +1.21 | +0.50 | +12 |  |
| (0.554, 1.21] | 24 | 33% (18-53) | -1.05 | -1.92 | -46 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 95, target 48, time_stop 45, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0968] | 64 | 33% | 16% | 50% |
| (0.0968, 0.145] | 64 | 56% | 31% | 9% |
| (0.145, 0.392] | 63 | 60% | 29% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
