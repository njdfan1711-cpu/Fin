# Scalp signal analysis (trail exits)

_257 tagged trades, 29 trading days (2026-10-01 to 2026-11-10). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 257 | 42% (36-48) | -0.65 | -2.21 | -567 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 46 | -6 | -0.13 | 211 | -561 | -2.66 | +6 |
| skip first 30 min | 2 | -3 | -1.70 | 255 | -564 | -2.21 | +3 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 158 | -299 | -1.89 | +268 |
| skip when SPY is below its VWAP | 112 | -326 | -2.91 | 145 | -241 | -1.66 | +326 |
| skip when SPY fell over the last 15 min | 94 | -207 | -2.20 | 163 | -360 | -2.21 | +207 |
| skip over-extended (30-min run in top quarter, > 0.53%) | 64 | -222 | -3.47 | 193 | -345 | -1.79 | +222 |
| skip stock not beating SPY over 15 min | 42 | -93 | -2.20 | 215 | -475 | -2.21 | +93 |
| skip afternoon entries (2:00-3:45 PM) | 57 | -217 | -3.80 | 200 | -350 | -1.75 | +217 |
| skip volume spikes above 5x average | 48 | -167 | -3.48 | 209 | -400 | -1.91 | +167 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 231 | -526 | -2.28 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 35 | -50 | -1.44 | 222 | -517 | -2.33 | +50 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 123 | -417 | -3.39 | 134 | -150 | -1.12 | +417 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 50% (34-66) | -0.17 | -1.90 | -68 |  |
| 60-240 | 102 | 38% (29-48) | -1.09 | -2.43 | -248 |  |
| 240-375 | 73 | 40% (29-51) | -1.57 | -3.35 | -245 |  |
| 375-390 | 46 | 48% (34-62) | +1.41 | -0.13 | -6 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 67 | 34% (24-46) | -1.60 | -2.92 | -196 |  |
| > 0.2 | 91 | 48% (38-58) | +0.42 | -1.13 | -103 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 37% (28-46) | -1.25 | -2.91 | -326 |  |
| above VWAP | 145 | 46% (38-54) | -0.19 | -1.66 | -241 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 86 | 40% (30-50) | -0.20 | -1.54 | -132 |  |
| (0.136, 0.382] | 85 | 54% (44-64) | -0.07 | -1.53 | -130 | ▲ |
| (0.382, 5.591] | 86 | 33% (24-43) | -1.68 | -3.54 | -304 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.118] | 85 | 48% (38-59) | +0.40 | -0.81 | -69 |  |
| (0.118, 0.44] | 85 | 41% (31-52) | -0.96 | -2.79 | -237 |  |
| (0.44, 4.846] | 85 | 36% (27-47) | -1.38 | -3.04 | -258 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.375] | 86 | 44% (34-55) | -0.90 | -2.66 | -229 |  |
| (-0.375, 0.391] | 85 | 47% (37-58) | +0.55 | -0.59 | -50 |  |
| (0.391, 5.005] | 86 | 35% (26-45) | -1.58 | -3.35 | -288 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 86 | 43% (33-54) | -0.92 | -2.30 | -197 |  |
| (0.056, 0.127] | 85 | 45% (35-55) | +0.25 | -1.23 | -104 |  |
| (0.127, 0.924] | 86 | 38% (29-49) | -1.27 | -3.09 | -265 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.213] | 86 | 44% (34-55) | +0.11 | -0.96 | -83 |  |
| (0.213, 0.334] | 85 | 45% (35-55) | -0.71 | -2.51 | -213 |  |
| (0.334, 2.663] | 86 | 37% (28-48) | -1.36 | -3.15 | -271 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.324] | 86 | 41% (31-51) | -0.67 | -2.16 | -185 |  |
| (2.324, 3.574] | 85 | 49% (39-60) | +0.65 | -0.94 | -80 |  |
| (3.574, 18.762] | 86 | 36% (27-47) | -1.91 | -3.51 | -302 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 87 | 48% (38-59) | +0.36 | -0.42 | -37 |  |
| (0.102, 0.161] | 84 | 42% (32-52) | -1.13 | -2.32 | -195 |  |
| (0.161, 0.76] | 86 | 36% (27-47) | -1.20 | -3.91 | -336 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.043] | 44 | 43% (30-58) | -1.30 | -2.10 | -92 |  |
| (-1.043, 0.575] | 43 | 53% (39-67) | -0.04 | -0.65 | -28 |  |
| (0.575, 7.522] | 44 | 57% (42-70) | -0.21 | -0.94 | -42 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 47 | 49% (35-63) | -0.54 | -1.20 | -56 |  |
| (0.533, 0.834] | 45 | 53% (39-67) | -0.91 | -1.61 | -72 |  |
| (0.834, 3.799] | 46 | 50% (36-64) | -0.46 | -1.30 | -60 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.826] | 46 | 48% (34-62) | -1.24 | -1.82 | -84 |  |
| (0.826, 1.475] | 46 | 54% (40-68) | -0.22 | -0.94 | -43 |  |
| (1.475, 9.058] | 46 | 50% (36-64) | -0.44 | -1.34 | -61 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.372] | 46 | 46% (32-60) | -0.74 | -1.32 | -61 |  |
| (0.372, 0.596] | 46 | 61% (46-74) | -0.23 | -0.98 | -45 | ▲ |
| (0.596, 4.001] | 46 | 46% (32-60) | -0.94 | -1.80 | -83 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 112, trail_stop 107, time_stop 30, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 87 | 31% | 33% | 30% |
| (0.102, 0.161] | 84 | 50% | 45% | 2% |
| (0.161, 0.76] | 86 | 50% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
