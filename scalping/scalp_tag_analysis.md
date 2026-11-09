# Scalp signal analysis (fixed exits)

_251 tagged trades, 28 trading days (2026-10-01 to 2026-11-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 251 | 41% (35-47) | +0.20 | -1.38 | -345 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 44 | -2 | -0.05 | 207 | -343 | -1.66 | +2 |
| skip first 30 min | 2 | -8 | -4.06 | 249 | -337 | -1.35 | +8 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 152 | -246 | -1.62 | +99 |
| skip when SPY is below its VWAP | 112 | -178 | -1.59 | 139 | -167 | -1.20 | +178 |
| skip when SPY fell over the last 15 min | 91 | -136 | -1.50 | 160 | -209 | -1.30 | +136 |
| skip over-extended (30-min run in top quarter, > 0.50%) | 62 | -174 | -2.80 | 189 | -171 | -0.91 | +174 |
| skip stock not beating SPY over 15 min | 42 | -40 | -0.94 | 209 | -306 | -1.46 | +40 |
| skip afternoon entries (2:00-3:45 PM) | 54 | -224 | -4.15 | 197 | -121 | -0.61 | +224 |
| skip volume spikes above 5x average | 48 | -117 | -2.44 | 203 | -228 | -1.12 | +117 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 225 | -339 | -1.50 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 33 | -12 | -0.36 | 218 | -333 | -1.53 | +12 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 122 | -312 | -2.56 | 129 | -33 | -0.25 | +312 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 53% (37-68) | +2.11 | +0.38 | +14 |  |
| 60-240 | 101 | 40% (31-49) | +0.11 | -1.24 | -125 |  |
| 240-375 | 70 | 30% (21-42) | -1.48 | -3.31 | -232 |  |
| 375-390 | 44 | 50% (36-64) | +1.54 | -0.05 | -2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 67 | 33% (23-45) | -0.43 | -1.75 | -118 |  |
| > 0.2 | 85 | 42% (32-53) | +0.11 | -1.51 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 41% (32-50) | +0.08 | -1.59 | -178 |  |
| above VWAP | 139 | 40% (33-49) | +0.31 | -1.20 | -167 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 84 | 40% (31-51) | +0.26 | -1.00 | -84 |  |
| (0.133, 0.38] | 83 | 46% (35-56) | +0.50 | -1.08 | -90 |  |
| (0.38, 5.591] | 84 | 36% (26-46) | -0.15 | -2.04 | -172 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.109] | 83 | 46% (35-56) | +0.79 | -0.41 | -34 |  |
| (0.109, 0.428] | 83 | 41% (31-52) | +0.45 | -1.42 | -118 |  |
| (0.428, 4.846] | 83 | 36% (27-47) | -0.54 | -2.23 | -185 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.375] | 84 | 45% (35-56) | +0.73 | -1.06 | -89 |  |
| (-0.375, 0.39] | 83 | 45% (34-55) | +0.90 | -0.25 | -21 |  |
| (0.39, 4.204] | 84 | 32% (23-43) | -1.01 | -2.80 | -235 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 84 | 42% (32-52) | +0.01 | -1.39 | -117 |  |
| (0.056, 0.127] | 83 | 46% (35-56) | +0.69 | -0.81 | -67 |  |
| (0.127, 0.924] | 84 | 35% (25-45) | -0.08 | -1.92 | -162 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 84 | 43% (33-54) | +0.24 | -0.85 | -71 |  |
| (0.212, 0.334] | 83 | 42% (32-53) | +0.42 | -1.41 | -117 |  |
| (0.334, 2.663] | 84 | 37% (27-48) | -0.05 | -1.87 | -157 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.293] | 84 | 36% (26-46) | -0.20 | -1.70 | -143 |  |
| (2.293, 3.625] | 83 | 51% (40-61) | +1.24 | -0.37 | -31 |  |
| (3.625, 18.762] | 84 | 36% (26-46) | -0.41 | -2.04 | -171 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 85 | 46% (36-56) | +0.39 | -0.39 | -33 |  |
| (0.102, 0.159] | 82 | 37% (27-47) | -0.22 | -1.37 | -112 |  |
| (0.159, 0.76] | 84 | 39% (30-50) | +0.43 | -2.37 | -199 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.956] | 42 | 33% (21-48) | -0.78 | -1.59 | -67 |  |
| (-0.956, 0.601] | 41 | 51% (36-66) | +1.29 | +0.68 | +28 |  |
| (0.601, 7.522] | 42 | 48% (33-62) | +1.26 | +0.52 | +22 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 45 | 42% (29-57) | -0.13 | -0.79 | -35 |  |
| (0.533, 0.834] | 43 | 44% (30-59) | +0.53 | -0.18 | -8 |  |
| (0.834, 3.799] | 44 | 43% (30-58) | +0.88 | +0.03 | +1 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.826] | 44 | 41% (28-56) | -0.11 | -0.68 | -30 |  |
| (0.826, 1.46] | 44 | 45% (32-60) | +1.00 | +0.27 | +12 |  |
| (1.46, 9.058] | 44 | 43% (30-58) | +0.37 | -0.54 | -24 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.372] | 44 | 41% (28-56) | +0.03 | -0.55 | -24 |  |
| (0.372, 0.594] | 44 | 45% (32-60) | +0.60 | -0.15 | -6 |  |
| (0.594, 4.001] | 44 | 43% (30-58) | +0.63 | -0.24 | -11 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.19%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 121, target 66, time_stop 51, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 85 | 35% | 16% | 41% |
| (0.102, 0.159] | 82 | 55% | 27% | 12% |
| (0.159, 0.76] | 84 | 55% | 36% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
