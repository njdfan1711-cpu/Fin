# Scalp signal analysis (fixed exits)

_238 tagged trades, 26 trading days (2026-10-01 to 2026-11-05). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 238 | 41% (35-47) | +0.22 | -1.40 | -333 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 42 | +1 | +0.03 | 196 | -334 | -1.71 | -1 |
| skip first 30 min | 2 | -8 | -4.06 | 236 | -325 | -1.38 | +8 |
| skip when SPY is down on the day | 95 | -97 | -1.02 | 143 | -236 | -1.65 | +97 |
| skip when SPY is below its VWAP | 105 | -174 | -1.66 | 133 | -159 | -1.19 | +174 |
| skip when SPY fell over the last 15 min | 86 | -122 | -1.42 | 152 | -211 | -1.39 | +122 |
| skip over-extended (30-min run in top quarter, > 0.50%) | 59 | -171 | -2.90 | 179 | -162 | -0.91 | +171 |
| skip stock not beating SPY over 15 min | 38 | -30 | -0.78 | 200 | -303 | -1.52 | +30 |
| skip afternoon entries (2:00-3:45 PM) | 50 | -214 | -4.28 | 188 | -119 | -0.63 | +214 |
| skip volume spikes above 5x average | 45 | -130 | -2.88 | 193 | -203 | -1.05 | +130 |
| skip when the stop is inside normal noise (range > stop) | 22 | +4 | +0.18 | 216 | -337 | -1.56 | -4 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 30 | -16 | -0.53 | 208 | -317 | -1.52 | +16 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 117 | -311 | -2.66 | 121 | -22 | -0.18 | +311 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 53% (37-69) | +2.10 | +0.32 | +11 |  |
| 60-240 | 96 | 40% (30-50) | +0.10 | -1.29 | -123 |  |
| 240-375 | 66 | 30% (21-42) | -1.46 | -3.36 | -222 |  |
| 375-390 | 42 | 50% (36-64) | +1.66 | +0.03 | +1 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 44 | 48% (34-62) | +1.32 | +0.01 | +1 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 66 | 33% (23-45) | -0.38 | -1.70 | -112 |  |
| > 0.2 | 77 | 43% (32-54) | +0.10 | -1.61 | -124 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 105 | 41% (32-51) | +0.07 | -1.66 | -174 |  |
| above VWAP | 133 | 41% (33-49) | +0.35 | -1.19 | -159 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 80 | 41% (31-52) | +0.25 | -1.12 | -90 |  |
| (0.136, 0.382] | 79 | 47% (36-58) | +0.70 | -0.84 | -66 |  |
| (0.382, 5.591] | 79 | 34% (25-45) | -0.28 | -2.24 | -177 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.112] | 79 | 47% (36-58) | +0.82 | -0.42 | -33 |  |
| (0.112, 0.433] | 78 | 41% (31-52) | +0.54 | -1.40 | -109 |  |
| (0.433, 4.846] | 79 | 35% (26-46) | -0.58 | -2.31 | -182 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.039000000000001, -0.367] | 80 | 45% (35-56) | +0.82 | -1.02 | -82 |  |
| (-0.367, 0.394] | 79 | 46% (35-57) | +0.99 | -0.17 | -14 |  |
| (0.394, 4.204] | 79 | 32% (22-43) | -1.13 | -3.01 | -238 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 80 | 41% (31-52) | -0.11 | -1.54 | -123 |  |
| (0.056, 0.127] | 80 | 45% (35-56) | +0.66 | -0.86 | -69 |  |
| (0.127, 0.924] | 78 | 36% (26-47) | +0.12 | -1.81 | -141 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 80 | 44% (33-55) | +0.36 | -0.76 | -61 |  |
| (0.212, 0.331] | 79 | 43% (33-54) | +0.51 | -1.27 | -100 |  |
| (0.331, 2.663] | 79 | 35% (26-46) | -0.20 | -2.18 | -172 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.318] | 80 | 38% (28-48) | +0.07 | -1.46 | -117 |  |
| (2.318, 3.637] | 79 | 51% (40-61) | +1.18 | -0.47 | -37 |  |
| (3.637, 18.762] | 79 | 34% (25-45) | -0.57 | -2.26 | -179 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0997] | 81 | 47% (36-58) | +0.53 | -0.24 | -20 |  |
| (0.0997, 0.154] | 78 | 37% (27-48) | -0.04 | -1.20 | -93 |  |
| (0.154, 0.76] | 79 | 38% (28-49) | +0.17 | -2.79 | -220 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.078] | 38 | 34% (21-50) | -0.68 | -1.49 | -57 |  |
| (-1.078, 0.444] | 37 | 46% (31-62) | +0.63 | +0.05 | +2 |  |
| (0.444, 5.599] | 37 | 54% (38-69) | +2.11 | +1.36 | +50 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.523] | 40 | 45% (31-60) | +0.33 | -0.28 | -11 |  |
| (0.523, 0.775] | 39 | 41% (27-57) | +0.09 | -0.68 | -27 |  |
| (0.775, 3.799] | 40 | 45% (31-60) | +1.03 | +0.21 | +8 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.824] | 40 | 40% (26-55) | -0.31 | -0.86 | -34 |  |
| (0.824, 1.432] | 39 | 46% (32-61) | +1.01 | +0.26 | +10 |  |
| (1.432, 7.752] | 40 | 45% (31-60) | +0.77 | -0.13 | -5 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.362] | 40 | 45% (31-60) | +0.57 | +0.01 | +0 |  |
| (0.362, 0.594] | 39 | 44% (29-59) | +0.22 | -0.56 | -22 |  |
| (0.594, 4.001] | 40 | 42% (29-58) | +0.67 | -0.20 | -8 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.19%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 114, target 62, time_stop 51, eod 11

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0997] | 81 | 33% | 17% | 43% |
| (0.0997, 0.154] | 78 | 55% | 28% | 12% |
| (0.154, 0.76] | 79 | 56% | 33% | 9% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
