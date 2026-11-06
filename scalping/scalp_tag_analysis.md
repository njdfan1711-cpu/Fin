# Scalp signal analysis (fixed exits)

_242 tagged trades, 26 trading days (2026-10-01 to 2026-11-05). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 242 | 41% (35-47) | +0.22 | -1.39 | -335 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 43 | +3 | +0.07 | 199 | -338 | -1.70 | -3 |
| skip first 30 min | 2 | -8 | -4.06 | 240 | -327 | -1.36 | +8 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 143 | -236 | -1.65 | +99 |
| skip when SPY is below its VWAP | 109 | -177 | -1.62 | 133 | -159 | -1.19 | +177 |
| skip when SPY fell over the last 15 min | 87 | -129 | -1.48 | 155 | -207 | -1.33 | +129 |
| skip over-extended (30-min run in top quarter, > 0.53%) | 60 | -159 | -2.66 | 182 | -176 | -0.97 | +159 |
| skip stock not beating SPY over 15 min | 38 | -30 | -0.78 | 204 | -306 | -1.50 | +30 |
| skip afternoon entries (2:00-3:45 PM) | 53 | -218 | -4.12 | 189 | -117 | -0.62 | +218 |
| skip volume spikes above 5x average | 45 | -130 | -2.88 | 197 | -206 | -1.04 | +130 |
| skip when the stop is inside normal noise (range > stop) | 24 | +6 | +0.26 | 218 | -342 | -1.57 | -6 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.69%) | 31 | +2 | +0.05 | 211 | -337 | -1.60 | -2 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 118 | -302 | -2.56 | 124 | -33 | -0.27 | +302 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 53% (37-69) | +2.10 | +0.32 | +11 |  |
| 60-240 | 96 | 40% (30-50) | +0.10 | -1.29 | -123 |  |
| 240-375 | 69 | 30% (21-42) | -1.42 | -3.27 | -226 |  |
| 375-390 | 43 | 51% (37-65) | +1.67 | +0.07 | +3 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 66 | 33% (23-45) | -0.38 | -1.70 | -112 |  |
| > 0.2 | 77 | 43% (32-54) | +0.10 | -1.61 | -124 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 109 | 41% (32-51) | +0.07 | -1.62 | -177 |  |
| above VWAP | 133 | 41% (33-49) | +0.35 | -1.19 | -159 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 81 | 41% (31-52) | +0.18 | -1.19 | -96 |  |
| (0.136, 0.384] | 80 | 46% (36-57) | +0.62 | -0.90 | -72 |  |
| (0.384, 5.591] | 81 | 36% (26-47) | -0.12 | -2.06 | -167 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.114] | 80 | 46% (36-57) | +0.73 | -0.50 | -40 |  |
| (0.114, 0.44] | 80 | 41% (31-52) | +0.57 | -1.34 | -107 |  |
| (0.44, 4.846] | 80 | 36% (27-47) | -0.54 | -2.25 | -180 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.391] | 81 | 47% (36-58) | +0.93 | -0.91 | -73 |  |
| (-0.391, 0.378] | 80 | 42% (32-53) | +0.70 | -0.45 | -36 |  |
| (0.378, 4.204] | 81 | 33% (24-44) | -0.95 | -2.79 | -226 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 81 | 41% (31-52) | -0.18 | -1.60 | -130 |  |
| (0.056, 0.127] | 81 | 46% (35-56) | +0.68 | -0.82 | -67 |  |
| (0.127, 0.924] | 80 | 36% (27-47) | +0.17 | -1.74 | -139 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 81 | 43% (33-54) | +0.28 | -0.83 | -67 |  |
| (0.212, 0.336] | 80 | 42% (32-53) | +0.43 | -1.44 | -115 |  |
| (0.336, 2.663] | 81 | 37% (27-48) | -0.04 | -1.89 | -153 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.324] | 81 | 37% (27-48) | -0.01 | -1.52 | -123 |  |
| (2.324, 3.625] | 80 | 51% (40-62) | +1.29 | -0.36 | -28 |  |
| (3.625, 18.762] | 81 | 35% (25-45) | -0.60 | -2.27 | -184 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.1] | 81 | 47% (36-58) | +0.53 | -0.24 | -20 |  |
| (0.1, 0.154] | 80 | 38% (28-48) | -0.09 | -1.22 | -98 |  |
| (0.154, 0.76] | 81 | 38% (28-49) | +0.22 | -2.69 | -218 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.265] | 39 | 36% (23-52) | -0.54 | -1.38 | -54 |  |
| (-1.265, 0.45] | 38 | 45% (30-60) | +0.60 | +0.02 | +1 |  |
| (0.45, 5.599] | 39 | 54% (39-68) | +1.91 | +1.17 | +46 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.532] | 41 | 44% (30-59) | +0.18 | -0.43 | -18 |  |
| (0.532, 0.779] | 41 | 44% (30-59) | +0.28 | -0.47 | -19 |  |
| (0.779, 3.799] | 41 | 44% (30-59) | +0.98 | +0.13 | +6 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.837] | 41 | 41% (28-57) | -0.07 | -0.64 | -26 |  |
| (0.837, 1.475] | 41 | 46% (32-61) | +0.92 | +0.20 | +8 |  |
| (1.475, 9.058] | 41 | 44% (30-59) | +0.58 | -0.33 | -14 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.368] | 41 | 44% (30-59) | +0.41 | -0.14 | -6 |  |
| (0.368, 0.605] | 41 | 46% (32-61) | +0.56 | -0.21 | -9 |  |
| (0.605, 4.001] | 41 | 41% (28-57) | +0.46 | -0.42 | -17 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 116, target 63, time_stop 51, eod 12

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.1] | 81 | 33% | 17% | 43% |
| (0.1, 0.154] | 80 | 55% | 28% | 11% |
| (0.154, 0.76] | 81 | 56% | 33% | 9% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
