# Scalp signal analysis (trail exits)

_225 tagged trades, 25 trading days (2026-10-01 to 2026-11-04). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 225 | 39% (33-46) | -0.82 | -2.50 | -562 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 38 | -0 | -0.01 | 187 | -561 | -3.00 | +0 |
| skip first 30 min | 2 | -3 | -1.70 | 223 | -558 | -2.50 | +3 |
| skip when SPY is down on the day | 89 | -281 | -3.16 | 136 | -280 | -2.06 | +281 |
| skip when SPY is below its VWAP | 98 | -327 | -3.34 | 127 | -234 | -1.85 | +327 |
| skip when SPY fell over the last 15 min | 82 | -196 | -2.39 | 143 | -366 | -2.56 | +196 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 56 | -227 | -4.06 | 169 | -335 | -1.98 | +227 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 188 | -481 | -2.56 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 47 | -216 | -4.59 | 178 | -346 | -1.94 | +216 |
| skip volume spikes above 5x average | 42 | -181 | -4.30 | 183 | -381 | -2.08 | +181 |
| skip when the stop is inside normal noise (range > stop) | 15 | -37 | -2.50 | 210 | -524 | -2.50 | +37 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 27 | -69 | -2.57 | 198 | -493 | -2.49 | +69 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 112 | -406 | -3.62 | 113 | -156 | -1.38 | +406 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 91 | 35% (26-45) | -1.31 | -2.74 | -249 |  |
| 240-375 | 62 | 34% (23-46) | -2.04 | -4.00 | -248 |  |
| 375-390 | 38 | 47% (32-63) | +1.67 | -0.01 | -0 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 37% (23-53) | -1.17 | -2.57 | -98 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 70 | 46% (35-57) | +0.52 | -1.28 | -90 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 98 | 33% (24-42) | -1.55 | -3.34 | -327 |  |
| above VWAP | 127 | 44% (36-53) | -0.27 | -1.85 | -234 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 75 | 37% (27-49) | -0.30 | -1.60 | -120 |  |
| (0.133, 0.379] | 75 | 49% (38-60) | -0.46 | -2.15 | -161 |  |
| (0.379, 2.096] | 75 | 31% (21-42) | -1.72 | -3.74 | -281 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.116] | 75 | 45% (35-57) | +0.21 | -1.10 | -82 |  |
| (0.116, 0.412] | 74 | 41% (30-52) | -0.93 | -2.87 | -213 |  |
| (0.412, 2.453] | 74 | 31% (22-42) | -1.75 | -3.56 | -264 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.357] | 75 | 41% (31-53) | -1.12 | -3.02 | -227 |  |
| (-0.357, 0.371] | 75 | 44% (33-55) | +0.48 | -0.71 | -53 |  |
| (0.371, 2.726] | 75 | 32% (23-43) | -1.83 | -3.76 | -282 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.054] | 75 | 40% (30-51) | -1.15 | -2.65 | -199 |  |
| (0.054, 0.123] | 75 | 41% (31-53) | +0.13 | -1.43 | -107 |  |
| (0.123, 0.924] | 75 | 36% (26-47) | -1.45 | -3.41 | -256 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 75 | 43% (32-54) | +0.08 | -1.08 | -81 |  |
| (0.211, 0.316] | 75 | 40% (30-51) | -0.99 | -2.82 | -211 |  |
| (0.316, 2.663] | 75 | 35% (25-46) | -1.56 | -3.59 | -270 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.344] | 75 | 40% (30-51) | -0.59 | -2.16 | -162 |  |
| (2.344, 3.618] | 75 | 47% (36-58) | +0.54 | -1.15 | -86 |  |
| (3.618, 18.762] | 75 | 31% (21-42) | -2.43 | -4.18 | -313 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0986] | 75 | 45% (35-57) | +0.29 | -0.47 | -35 |  |
| (0.0986, 0.15] | 75 | 41% (31-53) | -1.31 | -2.48 | -186 |  |
| (0.15, 0.392] | 75 | 31% (21-42) | -1.45 | -4.54 | -340 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 33 | 36% (22-53) | -2.05 | -2.87 | -95 |  |
| (-0.912, 0.454] | 33 | 52% (35-67) | -0.39 | -0.92 | -30 |  |
| (0.454, 5.305] | 33 | 55% (38-70) | -0.18 | -0.94 | -31 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.518] | 37 | 49% (33-64) | -0.39 | -1.02 | -38 |  |
| (0.518, 0.748] | 34 | 44% (29-61) | -1.72 | -2.49 | -85 |  |
| (0.748, 1.75] | 35 | 49% (33-64) | -0.93 | -1.73 | -61 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 36 | 44% (30-60) | -1.52 | -2.05 | -74 |  |
| (0.789, 1.21] | 35 | 46% (30-62) | -1.00 | -1.75 | -61 |  |
| (1.21, 5.866] | 35 | 51% (36-67) | -0.46 | -1.37 | -48 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.353] | 36 | 42% (27-58) | -0.92 | -1.50 | -54 |  |
| (0.353, 0.559] | 35 | 57% (41-72) | -0.69 | -1.46 | -51 | ▲ |
| (0.559, 2.726] | 35 | 43% (28-59) | -1.39 | -2.23 | -78 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.16%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 102, trail_stop 88, time_stop 29, eod 6

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0986] | 75 | 33% | 28% | 32% |
| (0.0986, 0.15] | 75 | 51% | 44% | 4% |
| (0.15, 0.392] | 75 | 52% | 45% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
