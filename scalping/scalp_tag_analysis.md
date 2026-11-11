# Scalp signal analysis (fixed exits)

_257 tagged trades, 29 trading days (2026-10-01 to 2026-11-10). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 257 | 40% (35-47) | +0.17 | -1.39 | -357 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 46 | -15 | -0.32 | 211 | -342 | -1.62 | +15 |
| skip first 30 min | 2 | -8 | -4.06 | 255 | -349 | -1.37 | +8 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 158 | -258 | -1.63 | +99 |
| skip when SPY is below its VWAP | 112 | -178 | -1.59 | 145 | -179 | -1.24 | +178 |
| skip when SPY fell over the last 15 min | 93 | -134 | -1.44 | 164 | -223 | -1.36 | +134 |
| skip over-extended (30-min run in top quarter, > 0.53%) | 64 | -173 | -2.71 | 193 | -184 | -0.95 | +173 |
| skip stock not beating SPY over 15 min | 42 | -40 | -0.94 | 215 | -318 | -1.48 | +40 |
| skip afternoon entries (2:00-3:45 PM) | 57 | -217 | -3.81 | 200 | -140 | -0.70 | +217 |
| skip volume spikes above 5x average | 48 | -117 | -2.44 | 209 | -240 | -1.15 | +117 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 231 | -351 | -1.52 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 35 | -25 | -0.70 | 222 | -333 | -1.50 | +25 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 123 | -319 | -2.60 | 134 | -38 | -0.28 | +319 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 53% (37-68) | +2.11 | +0.38 | +14 |  |
| 60-240 | 102 | 39% (30-49) | +0.05 | -1.29 | -131 |  |
| 240-375 | 73 | 32% (22-43) | -1.29 | -3.08 | -225 |  |
| 375-390 | 46 | 48% (34-62) | +1.22 | -0.32 | -15 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 67 | 33% (23-45) | -0.43 | -1.75 | -118 |  |
| > 0.2 | 91 | 42% (32-52) | +0.01 | -1.54 | -140 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 41% (32-50) | +0.08 | -1.59 | -178 |  |
| above VWAP | 145 | 40% (32-48) | +0.24 | -1.24 | -179 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 86 | 41% (31-51) | +0.22 | -1.12 | -96 |  |
| (0.136, 0.382] | 85 | 46% (36-56) | +0.60 | -0.87 | -74 |  |
| (0.382, 5.591] | 86 | 35% (26-45) | -0.31 | -2.18 | -187 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.118] | 85 | 46% (36-56) | +0.73 | -0.48 | -41 |  |
| (0.118, 0.44] | 85 | 41% (31-52) | +0.57 | -1.26 | -107 |  |
| (0.44, 4.846] | 85 | 35% (26-46) | -0.71 | -2.37 | -201 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.375] | 86 | 44% (34-55) | +0.58 | -1.18 | -101 |  |
| (-0.375, 0.391] | 85 | 45% (35-55) | +0.88 | -0.26 | -22 |  |
| (0.391, 5.005] | 86 | 33% (24-43) | -0.95 | -2.72 | -234 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 86 | 42% (32-52) | +0.00 | -1.37 | -118 |  |
| (0.056, 0.127] | 85 | 46% (36-56) | +0.71 | -0.76 | -65 |  |
| (0.127, 0.924] | 86 | 34% (25-44) | -0.21 | -2.03 | -174 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.213] | 86 | 43% (33-54) | +0.28 | -0.80 | -69 |  |
| (0.213, 0.334] | 85 | 42% (32-53) | +0.41 | -1.39 | -118 |  |
| (0.334, 2.663] | 86 | 36% (27-47) | -0.19 | -1.98 | -170 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.324] | 86 | 36% (27-47) | -0.14 | -1.62 | -140 |  |
| (2.324, 3.574] | 85 | 49% (39-60) | +1.09 | -0.50 | -42 |  |
| (3.574, 18.762] | 86 | 36% (27-47) | -0.44 | -2.04 | -175 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 87 | 47% (37-58) | +0.55 | -0.23 | -20 |  |
| (0.102, 0.161] | 84 | 37% (27-48) | -0.16 | -1.35 | -113 |  |
| (0.161, 0.76] | 86 | 37% (28-48) | +0.10 | -2.61 | -224 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.043] | 44 | 34% (22-49) | -0.74 | -1.54 | -68 |  |
| (-1.043, 0.575] | 43 | 49% (35-63) | +1.12 | +0.51 | +22 |  |
| (0.575, 7.522] | 44 | 48% (34-62) | +1.12 | +0.39 | +17 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 47 | 45% (31-59) | +0.20 | -0.46 | -22 |  |
| (0.533, 0.834] | 45 | 42% (29-57) | +0.24 | -0.45 | -20 |  |
| (0.834, 3.799] | 46 | 41% (28-56) | +0.59 | -0.25 | -11 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.826] | 46 | 43% (30-58) | +0.23 | -0.35 | -16 |  |
| (0.826, 1.475] | 46 | 46% (32-60) | +0.88 | +0.16 | +7 |  |
| (1.475, 9.058] | 46 | 39% (26-54) | -0.08 | -0.97 | -45 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.372] | 46 | 41% (28-56) | +0.10 | -0.48 | -22 |  |
| (0.372, 0.596] | 46 | 48% (34-62) | +0.90 | +0.15 | +7 |  |
| (0.596, 4.001] | 46 | 39% (26-54) | +0.03 | -0.83 | -38 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 125, target 67, time_stop 52, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 87 | 34% | 17% | 41% |
| (0.102, 0.161] | 84 | 55% | 27% | 12% |
| (0.161, 0.76] | 86 | 57% | 34% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
