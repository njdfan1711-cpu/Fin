# Scalp signal analysis (trail exits)

_227 tagged trades, 25 trading days (2026-10-01 to 2026-11-04). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 227 | 40% (34-46) | -0.77 | -2.43 | -553 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 38 | -0 | -0.01 | 189 | -552 | -2.92 | +0 |
| skip first 30 min | 2 | -3 | -1.70 | 225 | -549 | -2.44 | +3 |
| skip when SPY is down on the day | 89 | -281 | -3.16 | 138 | -271 | -1.96 | +281 |
| skip when SPY is below its VWAP | 98 | -327 | -3.34 | 129 | -225 | -1.75 | +327 |
| skip when SPY fell over the last 15 min | 82 | -196 | -2.39 | 145 | -356 | -2.46 | +196 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 56 | -226 | -4.04 | 171 | -327 | -1.91 | +226 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 190 | -472 | -2.48 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 47 | -216 | -4.59 | 180 | -337 | -1.87 | +216 |
| skip volume spikes above 5x average | 43 | -172 | -3.99 | 184 | -381 | -2.07 | +172 |
| skip when the stop is inside normal noise (range > stop) | 15 | -37 | -2.50 | 212 | -515 | -2.43 | +37 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.63%) | 27 | -69 | -2.57 | 200 | -483 | -2.42 | +69 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 112 | -406 | -3.62 | 115 | -147 | -1.28 | +406 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 93 | 37% (27-47) | -1.17 | -2.58 | -240 |  |
| 240-375 | 62 | 34% (23-46) | -2.04 | -4.00 | -248 |  |
| 375-390 | 38 | 47% (32-63) | +1.67 | -0.01 | -0 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 37% (23-53) | -1.17 | -2.57 | -98 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 72 | 47% (36-59) | +0.65 | -1.12 | -81 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 98 | 33% (24-42) | -1.55 | -3.34 | -327 |  |
| above VWAP | 129 | 45% (37-54) | -0.19 | -1.75 | -225 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.134] | 76 | 37% (27-48) | -0.28 | -1.59 | -121 |  |
| (0.134, 0.376] | 75 | 51% (40-62) | -0.38 | -2.05 | -154 |  |
| (0.376, 2.096] | 76 | 32% (22-43) | -1.65 | -3.66 | -278 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.114] | 75 | 47% (36-58) | +0.41 | -0.86 | -65 |  |
| (0.114, 0.415] | 75 | 40% (30-51) | -1.00 | -2.95 | -221 |  |
| (0.415, 2.453] | 75 | 32% (23-43) | -1.71 | -3.51 | -263 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.351] | 76 | 41% (30-52) | -1.09 | -2.99 | -227 |  |
| (-0.351, 0.39] | 75 | 45% (35-57) | +0.50 | -0.68 | -51 |  |
| (0.39, 2.726] | 76 | 33% (23-44) | -1.71 | -3.61 | -275 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0541] | 76 | 41% (30-52) | -1.02 | -2.50 | -190 |  |
| (0.0541, 0.124] | 75 | 41% (31-53) | +0.13 | -1.43 | -107 |  |
| (0.124, 0.924] | 76 | 37% (27-48) | -1.42 | -3.36 | -255 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 76 | 43% (33-55) | +0.19 | -0.95 | -72 |  |
| (0.211, 0.316] | 75 | 40% (30-51) | -0.99 | -2.82 | -211 |  |
| (0.316, 2.663] | 76 | 36% (26-47) | -1.52 | -3.54 | -269 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.34] | 76 | 41% (30-52) | -0.57 | -2.13 | -162 |  |
| (2.34, 3.625] | 75 | 47% (36-58) | +0.54 | -1.15 | -86 |  |
| (3.625, 18.762] | 76 | 32% (22-43) | -2.28 | -4.01 | -304 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0987] | 76 | 46% (35-57) | +0.31 | -0.45 | -34 |  |
| (0.0987, 0.15] | 75 | 43% (32-54) | -1.12 | -2.30 | -172 |  |
| (0.15, 0.392] | 76 | 30% (21-41) | -1.51 | -4.56 | -346 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 34 | 38% (24-55) | -1.96 | -2.78 | -94 |  |
| (-0.912, 0.45] | 33 | 52% (35-67) | -0.39 | -0.92 | -30 |  |
| (0.45, 5.305] | 34 | 56% (39-71) | +0.09 | -0.66 | -22 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.518] | 37 | 49% (33-64) | -0.39 | -1.02 | -38 |  |
| (0.518, 0.747] | 35 | 49% (33-64) | -1.23 | -1.98 | -69 |  |
| (0.747, 1.75] | 36 | 47% (32-63) | -1.06 | -1.85 | -67 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 36 | 44% (30-60) | -1.52 | -2.05 | -74 |  |
| (0.789, 1.214] | 36 | 47% (32-63) | -0.73 | -1.46 | -53 |  |
| (1.214, 5.866] | 36 | 53% (37-68) | -0.42 | -1.32 | -47 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.354] | 36 | 42% (27-58) | -0.92 | -1.50 | -54 |  |
| (0.354, 0.56] | 36 | 58% (42-73) | -0.42 | -1.17 | -42 | ▲ |
| (0.56, 2.726] | 36 | 44% (30-60) | -1.32 | -2.16 | -78 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.15%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 102, trail_stop 90, time_stop 29, eod 6

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0987] | 76 | 33% | 29% | 32% |
| (0.0987, 0.15] | 75 | 49% | 45% | 4% |
| (0.15, 0.392] | 76 | 53% | 45% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
