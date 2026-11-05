# Scalp signal analysis (fixed exits)

_233 tagged trades, 26 trading days (2026-10-01 to 2026-11-05). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 233 | 40% (34-46) | +0.08 | -1.56 | -364 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 40 | -2 | -0.05 | 193 | -362 | -1.88 | +2 |
| skip first 30 min | 2 | -8 | -4.06 | 231 | -356 | -1.54 | +8 |
| skip when SPY is down on the day | 90 | -128 | -1.42 | 143 | -236 | -1.65 | +128 |
| skip when SPY is below its VWAP | 100 | -205 | -2.05 | 133 | -159 | -1.19 | +205 |
| skip when SPY fell over the last 15 min | 84 | -126 | -1.50 | 149 | -238 | -1.60 | +126 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 58 | -185 | -3.18 | 175 | -180 | -1.03 | +185 |
| skip stock not beating SPY over 15 min | 37 | -39 | -1.06 | 196 | -325 | -1.66 | +39 |
| skip afternoon entries (2:00-3:45 PM) | 49 | -224 | -4.56 | 184 | -141 | -0.76 | +224 |
| skip volume spikes above 5x average | 44 | -139 | -3.15 | 189 | -225 | -1.19 | +139 |
| skip when the stop is inside normal noise (range > stop) | 18 | -18 | -1.00 | 215 | -346 | -1.61 | +18 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.67%) | 29 | -26 | -0.89 | 204 | -338 | -1.66 | +26 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 115 | -329 | -2.86 | 118 | -35 | -0.30 | +329 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 53% (37-69) | +2.10 | +0.32 | +11 |  |
| 60-240 | 94 | 38% (29-48) | -0.12 | -1.51 | -142 |  |
| 240-375 | 65 | 29% (20-41) | -1.65 | -3.56 | -231 |  |
| 375-390 | 40 | 50% (35-65) | +1.62 | -0.05 | -2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 39 | 44% (29-59) | +0.58 | -0.78 | -31 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 66 | 33% (23-45) | -0.38 | -1.70 | -112 |  |
| > 0.2 | 77 | 43% (32-54) | +0.10 | -1.61 | -124 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 100 | 39% (30-49) | -0.28 | -2.05 | -205 |  |
| above VWAP | 133 | 41% (33-49) | +0.35 | -1.19 | -159 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 78 | 40% (30-51) | -0.01 | -1.40 | -109 |  |
| (0.136, 0.38] | 77 | 45% (35-57) | +0.47 | -1.08 | -83 |  |
| (0.38, 2.096] | 78 | 35% (25-46) | -0.23 | -2.20 | -172 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.109] | 77 | 45% (35-57) | +0.68 | -0.58 | -45 |  |
| (0.109, 0.422] | 77 | 42% (31-53) | +0.44 | -1.49 | -115 |  |
| (0.422, 2.453] | 77 | 34% (24-45) | -0.79 | -2.56 | -197 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.349] | 78 | 42% (32-53) | +0.36 | -1.50 | -117 |  |
| (-0.349, 0.401] | 77 | 47% (36-58) | +1.17 | +0.01 | +0 |  |
| (0.401, 4.204] | 78 | 31% (22-42) | -1.28 | -3.17 | -247 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0559] | 78 | 41% (31-52) | -0.08 | -1.53 | -120 |  |
| (0.0559, 0.124] | 77 | 45% (35-57) | +0.71 | -0.84 | -65 |  |
| (0.124, 0.924] | 78 | 33% (24-44) | -0.39 | -2.31 | -180 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 78 | 44% (33-55) | +0.24 | -0.89 | -69 |  |
| (0.211, 0.323] | 77 | 42% (31-53) | +0.43 | -1.36 | -105 |  |
| (0.323, 2.663] | 78 | 35% (25-46) | -0.43 | -2.44 | -190 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.34] | 78 | 37% (27-48) | -0.10 | -1.64 | -128 |  |
| (2.34, 3.635] | 77 | 49% (38-60) | +1.15 | -0.54 | -41 |  |
| (3.635, 18.762] | 78 | 33% (24-44) | -0.81 | -2.50 | -195 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0987] | 78 | 47% (37-58) | +0.56 | -0.19 | -14 |  |
| (0.0987, 0.15] | 77 | 36% (27-48) | -0.25 | -1.41 | -109 |  |
| (0.15, 0.392] | 78 | 36% (26-47) | -0.09 | -3.09 | -241 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.918] | 36 | 31% (18-47) | -1.48 | -2.31 | -83 |  |
| (-0.918, 0.45] | 35 | 46% (30-62) | +0.73 | +0.17 | +6 |  |
| (0.45, 5.599] | 36 | 53% (37-68) | +1.88 | +1.15 | +41 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.518] | 39 | 46% (32-61) | +0.48 | -0.13 | -5 |  |
| (0.518, 0.748] | 37 | 38% (24-54) | -0.47 | -1.23 | -45 |  |
| (0.748, 1.75] | 38 | 42% (28-58) | +0.54 | -0.26 | -10 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.811] | 38 | 42% (28-58) | -0.02 | -0.55 | -21 |  |
| (0.811, 1.266] | 38 | 42% (28-58) | +0.36 | -0.37 | -14 |  |
| (1.266, 5.866] | 38 | 42% (28-58) | +0.25 | -0.67 | -25 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.354] | 38 | 42% (28-58) | +0.17 | -0.40 | -15 |  |
| (0.354, 0.566] | 38 | 47% (32-63) | +0.62 | -0.12 | -4 |  |
| (0.566, 2.726] | 38 | 37% (23-53) | -0.21 | -1.08 | -41 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.19%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 113, target 58, time_stop 51, eod 11

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0987] | 78 | 33% | 17% | 44% |
| (0.0987, 0.15] | 77 | 56% | 27% | 12% |
| (0.15, 0.392] | 78 | 56% | 31% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
