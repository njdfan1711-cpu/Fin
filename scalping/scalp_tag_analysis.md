# Scalp signal analysis (fixed exits)

_189 tagged trades, 21 trading days (2026-10-01 to 2026-10-29). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 189 | 39% (32-46) | -0.04 | -1.89 | -358 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 26 | -8 | -0.31 | 163 | -350 | -2.15 | +8 |
| skip first 30 min | 1 | -6 | -6.31 | 188 | -352 | -1.87 | +6 |
| skip when SPY is down on the day | 72 | -117 | -1.62 | 117 | -241 | -2.06 | +117 |
| skip when SPY is below its VWAP | 77 | -193 | -2.51 | 112 | -165 | -1.47 | +193 |
| skip when SPY fell over the last 15 min | 69 | -131 | -1.90 | 120 | -227 | -1.89 | +131 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 47 | -160 | -3.40 | 142 | -198 | -1.39 | +160 |
| skip stock not beating SPY over 15 min | 32 | -36 | -1.12 | 157 | -322 | -2.05 | +36 |
| skip afternoon entries (2:00-3:45 PM) | 41 | -221 | -5.40 | 148 | -136 | -0.92 | +221 |
| skip volume spikes above 5x average | 35 | -147 | -4.19 | 154 | -211 | -1.37 | +147 |
| skip when the stop is inside normal noise (range > stop) | 7 | -1 | -0.20 | 182 | -356 | -1.96 | +1 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.62%) | 18 | -35 | -1.95 | 171 | -323 | -1.89 | +35 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 103 | -286 | -2.78 | 86 | -72 | -0.83 | +286 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 27 | 63% (44-78) | +3.45 | +1.40 | +38 | ▲ |
| 60-240 | 82 | 37% (27-47) | -0.31 | -1.83 | -150 |  |
| 240-375 | 54 | 26% (16-39) | -2.25 | -4.40 | -238 |  |
| 375-390 | 26 | 46% (29-65) | +1.81 | -0.31 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 48 | 42% (29-56) | +0.45 | -1.81 | -87 |  |
| 0 to 0.2 | 59 | 36% (25-48) | -0.07 | -1.46 | -86 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 77 | 36% (27-48) | -0.42 | -2.51 | -193 |  |
| above VWAP | 112 | 40% (32-49) | +0.22 | -1.47 | -165 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 63 | 38% (27-50) | +0.03 | -1.41 | -89 |  |
| (0.133, 0.369] | 63 | 43% (31-55) | +0.04 | -1.73 | -109 |  |
| (0.369, 1.555] | 63 | 35% (24-47) | -0.18 | -2.54 | -160 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.142] | 63 | 41% (30-54) | +0.20 | -1.37 | -86 |  |
| (0.142, 0.406] | 62 | 42% (30-54) | +0.71 | -1.26 | -78 |  |
| (0.406, 1.281] | 63 | 33% (23-46) | -0.92 | -2.97 | -187 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.291] | 63 | 40% (29-52) | +0.24 | -1.94 | -123 |  |
| (-0.291, 0.371] | 63 | 44% (33-57) | +0.94 | -0.30 | -19 |  |
| (0.371, 2.726] | 63 | 32% (22-44) | -1.29 | -3.44 | -216 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 63 | 40% (29-52) | -0.26 | -1.88 | -118 |  |
| (0.052, 0.121] | 63 | 46% (34-58) | +0.93 | -0.72 | -45 |  |
| (0.121, 0.678] | 63 | 30% (20-42) | -0.78 | -3.08 | -194 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.207] | 63 | 43% (31-55) | +0.05 | -1.21 | -76 |  |
| (0.207, 0.313] | 63 | 41% (30-54) | +0.57 | -1.46 | -92 |  |
| (0.313, 0.875] | 63 | 32% (22-44) | -0.74 | -3.02 | -190 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.395] | 63 | 40% (29-52) | +0.33 | -1.44 | -91 |  |
| (2.395, 3.634] | 63 | 46% (34-58) | +0.81 | -1.06 | -67 |  |
| (3.634, 18.762] | 63 | 30% (20-42) | -1.25 | -3.19 | -201 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0969] | 63 | 46% (34-58) | +0.33 | -0.42 | -27 |  |
| (0.0969, 0.145] | 64 | 36% (25-48) | -0.01 | -1.30 | -83 |  |
| (0.145, 0.392] | 62 | 34% (23-46) | -0.43 | -4.00 | -248 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.498] | 21 | 24% (11-45) | -2.11 | -3.01 | -63 |  |
| (-0.498, 0.508] | 21 | 43% (24-63) | +0.43 | -0.08 | -2 |  |
| (0.508, 5.305] | 21 | 57% (37-76) | +2.38 | +1.68 | +35 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.486] | 24 | 38% (21-57) | -0.71 | -1.41 | -34 |  |
| (0.486, 0.694] | 24 | 42% (24-61) | +0.58 | -0.12 | -3 |  |
| (0.694, 1.74] | 22 | 41% (23-61) | +0.02 | -0.80 | -18 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 24 | 50% (31-69) | +1.09 | +0.64 | +15 |  |
| (0.789, 1.2] | 23 | 30% (16-51) | -0.54 | -1.39 | -32 |  |
| (1.2, 3.566] | 23 | 39% (22-59) | -0.72 | -1.63 | -38 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.345] | 24 | 38% (21-57) | -0.23 | -0.83 | -20 |  |
| (0.345, 0.55] | 23 | 48% (29-67) | +0.85 | +0.14 | +3 |  |
| (0.55, 1.21] | 23 | 35% (19-55) | -0.72 | -1.64 | -38 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 94, target 48, time_stop 44, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0969] | 63 | 33% | 16% | 49% |
| (0.0969, 0.145] | 64 | 56% | 31% | 9% |
| (0.145, 0.392] | 62 | 60% | 29% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
