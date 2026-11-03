# Scalp signal analysis (fixed exits)

_213 tagged trades, 24 trading days (2026-10-01 to 2026-11-03). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 213 | 38% (32-45) | -0.17 | -1.89 | -404 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -17 | -0.47 | 178 | -387 | -2.17 | +17 |
| skip first 30 min | 2 | -8 | -4.06 | 211 | -395 | -1.87 | +8 |
| skip when SPY is down on the day | 89 | -137 | -1.54 | 124 | -266 | -2.15 | +137 |
| skip when SPY is below its VWAP | 94 | -214 | -2.27 | 119 | -190 | -1.60 | +214 |
| skip when SPY fell over the last 15 min | 78 | -134 | -1.71 | 135 | -270 | -2.00 | +134 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 53 | -187 | -3.53 | 160 | -217 | -1.35 | +187 |
| skip stock not beating SPY over 15 min | 37 | -39 | -1.06 | 176 | -365 | -2.07 | +39 |
| skip afternoon entries (2:00-3:45 PM) | 45 | -218 | -4.85 | 168 | -185 | -1.10 | +218 |
| skip volume spikes above 5x average | 40 | -177 | -4.42 | 173 | -227 | -1.31 | +177 |
| skip when the stop is inside normal noise (range > stop) | 14 | -43 | -3.08 | 199 | -360 | -1.81 | +43 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 24 | -61 | -2.52 | 189 | -343 | -1.81 | +61 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 109 | -308 | -2.82 | 104 | -96 | -0.92 | +308 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 32 | 53% (36-69) | +2.13 | +0.29 | +9 |  |
| 60-240 | 87 | 36% (26-46) | -0.50 | -1.97 | -172 |  |
| 240-375 | 59 | 29% (19-41) | -1.79 | -3.81 | -225 |  |
| 375-390 | 35 | 46% (30-62) | +1.30 | -0.47 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 42% (28-58) | +0.35 | -1.04 | -40 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 65 | 34% (24-46) | -0.29 | -1.62 | -105 |  |
| > 0.2 | 59 | 37% (26-50) | -0.72 | -2.73 | -161 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 94 | 37% (28-47) | -0.43 | -2.27 | -214 |  |
| above VWAP | 119 | 39% (30-48) | +0.04 | -1.60 | -190 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 71 | 35% (25-47) | -0.52 | -1.75 | -124 |  |
| (0.122, 0.374] | 71 | 45% (34-57) | +0.41 | -1.45 | -103 |  |
| (0.374, 1.555] | 71 | 34% (24-45) | -0.40 | -2.49 | -177 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.119] | 71 | 42% (31-54) | +0.20 | -1.15 | -82 |  |
| (0.119, 0.412] | 70 | 40% (29-52) | +0.37 | -1.63 | -114 |  |
| (0.412, 2.453] | 70 | 33% (23-44) | -0.98 | -2.85 | -199 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.357] | 71 | 38% (28-50) | -0.17 | -2.15 | -153 |  |
| (-0.357, 0.339] | 71 | 44% (33-55) | +0.80 | -0.40 | -28 |  |
| (0.339, 2.726] | 71 | 32% (23-44) | -1.13 | -3.13 | -223 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.054] | 71 | 39% (29-51) | -0.33 | -1.87 | -133 |  |
| (0.054, 0.123] | 71 | 44% (33-55) | +0.57 | -1.04 | -74 |  |
| (0.123, 0.678] | 71 | 31% (21-42) | -0.74 | -2.77 | -196 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.21] | 71 | 42% (31-54) | +0.01 | -1.17 | -83 |  |
| (0.21, 0.314] | 71 | 38% (28-50) | +0.02 | -1.87 | -133 |  |
| (0.314, 0.979] | 71 | 34% (24-45) | -0.54 | -2.65 | -188 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.353] | 71 | 38% (28-50) | +0.10 | -1.54 | -109 |  |
| (2.353, 3.617] | 71 | 48% (37-59) | +0.93 | -0.79 | -56 |  |
| (3.617, 18.762] | 71 | 28% (19-40) | -1.53 | -3.35 | -238 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 71 | 46% (35-58) | +0.46 | -0.28 | -20 |  |
| (0.0985, 0.15] | 71 | 37% (26-48) | -0.05 | -1.27 | -90 |  |
| (0.15, 0.392] | 71 | 31% (21-42) | -0.91 | -4.13 | -293 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.887] | 29 | 21% (10-38) | -2.89 | -3.75 | -109 |  |
| (-0.887, 0.444] | 30 | 43% (27-61) | +0.65 | +0.12 | +4 |  |
| (0.444, 5.305] | 28 | 54% (36-70) | +1.80 | +1.08 | +30 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.507] | 32 | 44% (28-61) | +0.23 | -0.40 | -13 |  |
| (0.507, 0.747] | 31 | 39% (24-56) | -0.04 | -0.79 | -24 |  |
| (0.747, 1.74] | 31 | 32% (19-50) | -1.21 | -2.02 | -63 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.775] | 32 | 44% (28-61) | +0.35 | -0.15 | -5 |  |
| (0.775, 1.2] | 31 | 35% (21-53) | -0.18 | -0.95 | -29 |  |
| (1.2, 5.866] | 31 | 35% (21-53) | -1.19 | -2.12 | -66 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.347] | 32 | 38% (23-55) | -0.36 | -0.94 | -30 |  |
| (0.347, 0.559] | 31 | 45% (29-62) | +0.65 | -0.11 | -4 |  |
| (0.559, 1.659] | 31 | 32% (19-50) | -1.29 | -2.14 | -66 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 108, target 51, time_stop 47, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 71 | 34% | 17% | 45% |
| (0.0985, 0.15] | 71 | 56% | 30% | 10% |
| (0.15, 0.392] | 71 | 62% | 25% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
