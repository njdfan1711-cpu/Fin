# Scalp signal analysis (fixed exits)

_168 tagged trades, 19 trading days (2026-10-01 to 2026-10-27). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 168 | 39% (32-46) | -0.13 | -2.12 | -356 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | -17 | -0.68 | 143 | -339 | -2.37 | +17 |
| skip first 30 min | 1 | -6 | -6.31 | 167 | -349 | -2.09 | +6 |
| skip when SPY is down on the day | 63 | -136 | -2.16 | 105 | -220 | -2.09 | +136 |
| skip when SPY is below its VWAP | 71 | -187 | -2.63 | 97 | -169 | -1.74 | +187 |
| skip when SPY fell over the last 15 min | 65 | -140 | -2.16 | 103 | -215 | -2.09 | +140 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 42 | -158 | -3.76 | 126 | -198 | -1.57 | +158 |
| skip stock not beating SPY over 15 min | 27 | -10 | -0.39 | 141 | -345 | -2.45 | +10 |
| skip afternoon entries (2:00-3:45 PM) | 37 | -195 | -5.26 | 131 | -161 | -1.23 | +195 |
| skip volume spikes above 5x average | 30 | -137 | -4.58 | 138 | -218 | -1.58 | +137 |
| skip when the stop is inside normal noise (range > stop) | 7 | -1 | -0.20 | 161 | -354 | -2.20 | +1 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.57%) | 12 | -27 | -2.23 | 156 | -329 | -2.11 | +27 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 95 | -294 | -3.09 | 73 | -62 | -0.85 | +294 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 24 | 62% (43-79) | +3.42 | +1.17 | +28 | ▲ |
| 60-240 | 70 | 37% (27-49) | -0.46 | -2.10 | -147 |  |
| 240-375 | 49 | 27% (16-40) | -2.21 | -4.50 | -220 |  |
| 375-390 | 25 | 44% (27-63) | +1.47 | -0.68 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 39 | 38% (25-54) | -0.16 | -2.72 | -106 |  |
| 0 to 0.2 | 47 | 38% (26-53) | +0.19 | -1.38 | -65 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 71 | 37% (26-48) | -0.42 | -2.63 | -187 |  |
| above VWAP | 97 | 40% (31-50) | +0.08 | -1.74 | -169 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 56 | 39% (28-52) | +0.07 | -1.47 | -82 |  |
| (0.129, 0.369] | 56 | 43% (31-56) | -0.13 | -2.02 | -113 |  |
| (0.369, 1.555] | 56 | 34% (23-47) | -0.33 | -2.86 | -160 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 56 | 41% (29-54) | -0.02 | -1.72 | -97 |  |
| (0.147, 0.406] | 55 | 44% (31-57) | +0.92 | -1.20 | -66 |  |
| (0.406, 1.281] | 56 | 32% (21-45) | -1.17 | -3.34 | -187 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.242] | 56 | 38% (26-51) | -0.15 | -2.48 | -139 |  |
| (-0.242, 0.397] | 56 | 46% (34-59) | +0.95 | -0.36 | -20 |  |
| (0.397, 2.726] | 56 | 32% (21-45) | -1.20 | -3.52 | -197 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 56 | 39% (28-52) | -0.48 | -2.21 | -124 |  |
| (0.052, 0.12] | 56 | 46% (34-59) | +0.80 | -0.95 | -53 |  |
| (0.12, 0.678] | 56 | 30% (20-43) | -0.71 | -3.20 | -179 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.199] | 56 | 45% (32-58) | +0.02 | -1.28 | -72 |  |
| (0.199, 0.301] | 56 | 39% (28-52) | +0.23 | -1.90 | -106 |  |
| (0.301, 0.875] | 56 | 32% (21-45) | -0.64 | -3.18 | -178 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.363] | 56 | 38% (26-51) | -0.05 | -1.92 | -108 |  |
| (2.363, 3.448] | 56 | 48% (36-61) | +1.04 | -0.95 | -53 |  |
| (3.448, 18.762] | 56 | 30% (20-43) | -1.38 | -3.47 | -195 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0969] | 56 | 46% (34-59) | +0.11 | -0.65 | -37 |  |
| (0.0969, 0.147] | 56 | 34% (23-47) | -0.32 | -1.65 | -92 |  |
| (0.147, 0.392] | 56 | 36% (24-49) | -0.18 | -4.05 | -227 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.912] | 14 | 29% (12-55) | -1.79 | -2.75 | -38 |  |
| (-0.912, 0.215] | 14 | 21% (8-48) | -2.48 | -3.02 | -42 |  |
| (0.215, 5.305] | 14 | 79% (52-92) | +4.28 | +3.81 | +53 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.486] | 17 | 35% (17-59) | -1.86 | -2.57 | -44 |  |
| (0.486, 0.61] | 16 | 38% (18-61) | -0.20 | -0.76 | -12 |  |
| (0.61, 1.74] | 16 | 50% (28-72) | +1.07 | +0.24 | +4 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.775] | 17 | 53% (31-74) | +1.13 | +0.72 | +12 |  |
| (0.775, 1.178] | 16 | 38% (18-61) | +0.31 | -0.48 | -8 |  |
| (1.178, 3.566] | 16 | 31% (14-56) | -2.61 | -3.54 | -57 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 17 | 29% (13-53) | -1.60 | -2.23 | -38 |  |
| (0.315, 0.527] | 16 | 56% (33-77) | +1.07 | +0.50 | +8 |  |
| (0.527, 1.14] | 16 | 38% (18-61) | -0.46 | -1.39 | -22 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 85, target 41, time_stop 39, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0969] | 56 | 36% | 14% | 48% |
| (0.0969, 0.147] | 56 | 57% | 29% | 11% |
| (0.147, 0.392] | 56 | 59% | 30% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
