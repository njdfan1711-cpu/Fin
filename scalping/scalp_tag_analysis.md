# Scalp signal analysis (fixed exits)

_235 tagged trades, 26 trading days (2026-10-01 to 2026-11-05). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 235 | 40% (34-47) | +0.16 | -1.47 | -345 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 40 | -2 | -0.05 | 195 | -344 | -1.76 | +2 |
| skip first 30 min | 2 | -8 | -4.06 | 233 | -337 | -1.45 | +8 |
| skip when SPY is down on the day | 92 | -109 | -1.19 | 143 | -236 | -1.65 | +109 |
| skip when SPY is below its VWAP | 102 | -187 | -1.83 | 133 | -159 | -1.19 | +187 |
| skip when SPY fell over the last 15 min | 85 | -116 | -1.37 | 150 | -229 | -1.53 | +116 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 58 | -172 | -2.97 | 177 | -173 | -0.98 | +172 |
| skip stock not beating SPY over 15 min | 37 | -39 | -1.06 | 198 | -306 | -1.55 | +39 |
| skip afternoon entries (2:00-3:45 PM) | 49 | -224 | -4.56 | 186 | -122 | -0.66 | +224 |
| skip volume spikes above 5x average | 45 | -130 | -2.88 | 190 | -216 | -1.13 | +130 |
| skip when the stop is inside normal noise (range > stop) | 20 | +1 | +0.04 | 215 | -346 | -1.61 | -1 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 29 | -10 | -0.34 | 206 | -336 | -1.63 | +10 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 116 | -320 | -2.76 | 119 | -25 | -0.21 | +320 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 53% (37-69) | +2.10 | +0.32 | +11 |  |
| 60-240 | 96 | 40% (30-50) | +0.10 | -1.29 | -123 |  |
| 240-375 | 65 | 29% (20-41) | -1.65 | -3.56 | -231 |  |
| 375-390 | 40 | 50% (35-65) | +1.62 | -0.05 | -2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 41 | 46% (32-61) | +1.04 | -0.29 | -12 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 66 | 33% (23-45) | -0.38 | -1.70 | -112 |  |
| > 0.2 | 77 | 43% (32-54) | +0.10 | -1.61 | -124 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 102 | 40% (31-50) | -0.08 | -1.83 | -187 |  |
| above VWAP | 133 | 41% (33-49) | +0.35 | -1.19 | -159 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 79 | 41% (30-52) | +0.13 | -1.25 | -99 |  |
| (0.136, 0.382] | 78 | 46% (36-57) | +0.57 | -0.96 | -75 |  |
| (0.382, 5.591] | 78 | 35% (25-46) | -0.21 | -2.19 | -171 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.108] | 78 | 46% (36-57) | +0.80 | -0.45 | -35 |  |
| (0.108, 0.422] | 77 | 42% (31-53) | +0.44 | -1.49 | -115 |  |
| (0.422, 4.846] | 78 | 35% (25-46) | -0.65 | -2.41 | -188 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.0920000000000005, -0.352] | 79 | 44% (34-55) | +0.68 | -1.16 | -92 |  |
| (-0.352, 0.4] | 78 | 46% (36-57) | +1.08 | -0.08 | -6 |  |
| (0.4, 4.204] | 78 | 31% (22-42) | -1.28 | -3.17 | -247 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 79 | 42% (32-53) | -0.04 | -1.48 | -117 |  |
| (0.056, 0.126] | 78 | 46% (36-57) | +0.79 | -0.75 | -59 |  |
| (0.126, 0.924] | 78 | 33% (24-44) | -0.26 | -2.17 | -169 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 79 | 43% (33-54) | +0.23 | -0.89 | -70 |  |
| (0.212, 0.329] | 78 | 42% (32-53) | +0.39 | -1.39 | -108 |  |
| (0.329, 2.663] | 78 | 36% (26-47) | -0.13 | -2.14 | -167 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.337] | 79 | 38% (28-49) | +0.03 | -1.50 | -118 |  |
| (2.337, 3.637] | 78 | 50% (39-61) | +1.17 | -0.50 | -39 |  |
| (3.637, 18.762] | 78 | 33% (24-44) | -0.71 | -2.41 | -188 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0988] | 79 | 47% (36-58) | +0.48 | -0.28 | -22 |  |
| (0.0988, 0.152] | 78 | 36% (26-47) | -0.23 | -1.41 | -110 |  |
| (0.152, 0.76] | 78 | 38% (28-50) | +0.24 | -2.74 | -214 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.974] | 37 | 32% (20-49) | -0.99 | -1.80 | -67 |  |
| (-0.974, 0.444] | 36 | 47% (32-63) | +0.81 | +0.23 | +8 |  |
| (0.444, 5.599] | 36 | 53% (37-68) | +1.88 | +1.15 | +41 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.519] | 39 | 46% (32-61) | +0.48 | -0.13 | -5 |  |
| (0.519, 0.762] | 38 | 37% (23-53) | -0.59 | -1.35 | -51 |  |
| (0.762, 3.799] | 39 | 46% (32-61) | +1.18 | +0.38 | +15 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.822] | 39 | 41% (27-57) | -0.17 | -0.71 | -28 |  |
| (0.822, 1.378] | 38 | 42% (28-58) | +0.36 | -0.38 | -15 |  |
| (1.378, 7.752] | 39 | 46% (32-61) | +0.91 | +0.01 | +0 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.355] | 39 | 44% (29-59) | +0.42 | -0.14 | -6 |  |
| (0.355, 0.585] | 38 | 45% (30-60) | +0.21 | -0.55 | -21 |  |
| (0.585, 4.001] | 39 | 41% (27-57) | +0.47 | -0.39 | -15 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.19%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 113, target 60, time_stop 51, eod 11

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0988] | 79 | 34% | 16% | 43% |
| (0.0988, 0.152] | 78 | 55% | 27% | 13% |
| (0.152, 0.76] | 78 | 55% | 33% | 9% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
