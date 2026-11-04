# Scalp signal analysis (fixed exits)

_227 tagged trades, 25 trading days (2026-10-01 to 2026-11-04). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 227 | 40% (34-46) | +0.00 | -1.66 | -377 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 38 | -8 | -0.21 | 189 | -369 | -1.95 | +8 |
| skip first 30 min | 2 | -8 | -4.06 | 225 | -369 | -1.64 | +8 |
| skip when SPY is down on the day | 89 | -137 | -1.54 | 138 | -240 | -1.74 | +137 |
| skip when SPY is below its VWAP | 98 | -212 | -2.16 | 129 | -165 | -1.28 | +212 |
| skip when SPY fell over the last 15 min | 81 | -137 | -1.70 | 146 | -239 | -1.64 | +137 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 56 | -194 | -3.46 | 171 | -183 | -1.07 | +194 |
| skip stock not beating SPY over 15 min | 37 | -39 | -1.06 | 190 | -338 | -1.78 | +39 |
| skip afternoon entries (2:00-3:45 PM) | 47 | -216 | -4.59 | 180 | -161 | -0.89 | +216 |
| skip volume spikes above 5x average | 43 | -148 | -3.44 | 184 | -229 | -1.24 | +148 |
| skip when the stop is inside normal noise (range > stop) | 15 | -33 | -2.22 | 212 | -343 | -1.62 | +33 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.63%) | 27 | -47 | -1.75 | 200 | -329 | -1.65 | +47 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 112 | -328 | -2.93 | 115 | -49 | -0.42 | +328 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 53% (37-69) | +2.10 | +0.32 | +11 |  |
| 60-240 | 93 | 38% (28-48) | -0.22 | -1.63 | -151 |  |
| 240-375 | 62 | 29% (19-41) | -1.72 | -3.68 | -228 |  |
| 375-390 | 38 | 50% (35-65) | +1.47 | -0.21 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 42% (28-58) | +0.35 | -1.04 | -40 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 66 | 33% (23-45) | -0.38 | -1.70 | -112 |  |
| > 0.2 | 72 | 43% (32-55) | -0.00 | -1.77 | -127 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 98 | 39% (30-49) | -0.37 | -2.16 | -212 |  |
| above VWAP | 129 | 40% (32-49) | +0.28 | -1.28 | -165 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.134] | 76 | 39% (29-51) | +0.00 | -1.30 | -99 |  |
| (0.134, 0.376] | 75 | 45% (35-57) | +0.35 | -1.33 | -100 |  |
| (0.376, 2.096] | 76 | 34% (25-45) | -0.34 | -2.34 | -178 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.114] | 75 | 47% (36-58) | +0.67 | -0.60 | -45 |  |
| (0.114, 0.415] | 75 | 40% (30-51) | +0.28 | -1.67 | -125 |  |
| (0.415, 2.453] | 75 | 33% (24-45) | -0.85 | -2.65 | -199 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.351] | 76 | 42% (32-53) | +0.32 | -1.58 | -120 |  |
| (-0.351, 0.39] | 75 | 44% (33-55) | +0.72 | -0.46 | -34 |  |
| (0.39, 2.726] | 76 | 33% (23-44) | -1.02 | -2.93 | -222 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0541] | 76 | 41% (30-52) | -0.14 | -1.61 | -123 |  |
| (0.0541, 0.124] | 75 | 45% (35-57) | +0.66 | -0.91 | -68 |  |
| (0.124, 0.924] | 76 | 33% (23-44) | -0.51 | -2.45 | -186 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 76 | 43% (33-55) | +0.18 | -0.97 | -74 |  |
| (0.211, 0.316] | 75 | 41% (31-53) | +0.39 | -1.43 | -107 |  |
| (0.316, 2.663] | 76 | 34% (25-45) | -0.56 | -2.58 | -196 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.34] | 76 | 38% (28-49) | -0.02 | -1.58 | -120 |  |
| (2.34, 3.625] | 75 | 49% (38-60) | +1.12 | -0.57 | -43 |  |
| (3.625, 18.762] | 76 | 32% (22-43) | -1.08 | -2.81 | -213 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0987] | 76 | 47% (37-58) | +0.51 | -0.25 | -19 |  |
| (0.0987, 0.15] | 75 | 37% (27-49) | -0.10 | -1.28 | -96 |  |
| (0.15, 0.392] | 76 | 34% (25-45) | -0.40 | -3.45 | -262 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 34 | 29% (17-46) | -1.79 | -2.61 | -89 |  |
| (-0.912, 0.45] | 33 | 45% (30-62) | +0.64 | +0.10 | +3 |  |
| (0.45, 5.305] | 34 | 53% (37-69) | +1.84 | +1.09 | +37 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.518] | 37 | 46% (31-62) | +0.37 | -0.25 | -9 |  |
| (0.518, 0.747] | 35 | 40% (26-56) | -0.17 | -0.92 | -32 |  |
| (0.747, 1.75] | 36 | 39% (25-55) | -0.08 | -0.88 | -32 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 36 | 42% (27-58) | -0.11 | -0.64 | -23 |  |
| (0.789, 1.214] | 36 | 42% (27-58) | +0.25 | -0.49 | -18 |  |
| (1.214, 5.866] | 36 | 42% (27-58) | -0.00 | -0.90 | -32 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.354] | 36 | 42% (27-58) | +0.04 | -0.54 | -19 |  |
| (0.354, 0.56] | 36 | 47% (32-63) | +0.62 | -0.13 | -5 |  |
| (0.56, 2.726] | 36 | 36% (22-52) | -0.53 | -1.36 | -49 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 112, target 56, time_stop 49, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0987] | 76 | 34% | 17% | 42% |
| (0.0987, 0.15] | 75 | 55% | 28% | 12% |
| (0.15, 0.392] | 76 | 59% | 29% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
