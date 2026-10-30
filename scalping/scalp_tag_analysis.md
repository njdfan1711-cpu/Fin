# Scalp signal analysis (fixed exits)

_193 tagged trades, 21 trading days (2026-10-01 to 2026-10-29). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 193 | 39% (32-46) | -0.01 | -1.84 | -355 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 28 | -5 | -0.19 | 165 | -350 | -2.12 | +5 |
| skip first 30 min | 1 | -6 | -6.31 | 192 | -349 | -1.82 | +6 |
| skip when SPY is down on the day | 74 | -117 | -1.58 | 119 | -238 | -2.00 | +117 |
| skip when SPY is below its VWAP | 78 | -187 | -2.39 | 115 | -169 | -1.47 | +187 |
| skip when SPY fell over the last 15 min | 71 | -131 | -1.85 | 122 | -224 | -1.84 | +131 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 48 | -151 | -3.14 | 145 | -204 | -1.41 | +151 |
| skip stock not beating SPY over 15 min | 32 | -36 | -1.12 | 161 | -319 | -1.98 | +36 |
| skip afternoon entries (2:00-3:45 PM) | 42 | -215 | -5.12 | 151 | -140 | -0.93 | +215 |
| skip volume spikes above 5x average | 35 | -147 | -4.19 | 158 | -209 | -1.32 | +147 |
| skip when the stop is inside normal noise (range > stop) | 8 | -8 | -0.99 | 185 | -347 | -1.88 | +8 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.63%) | 19 | -42 | -2.20 | 174 | -313 | -1.80 | +42 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 104 | -277 | -2.66 | 89 | -78 | -0.88 | +277 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 27 | 63% (44-78) | +3.45 | +1.40 | +38 | ▲ |
| 60-240 | 83 | 36% (27-47) | -0.38 | -1.89 | -157 |  |
| 240-375 | 55 | 27% (17-40) | -2.09 | -4.20 | -231 |  |
| 375-390 | 28 | 46% (30-64) | +1.83 | -0.19 | -5 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 25 | 44% (27-63) | +0.76 | -0.94 | -23 |  |
| -0.2 to 0 | 49 | 41% (28-55) | +0.32 | -1.90 | -93 |  |
| 0 to 0.2 | 61 | 36% (25-49) | +0.00 | -1.37 | -84 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 78 | 37% (27-48) | -0.32 | -2.39 | -187 |  |
| above VWAP | 115 | 40% (32-49) | +0.21 | -1.47 | -169 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 65 | 38% (28-51) | -0.01 | -1.44 | -93 |  |
| (0.133, 0.374] | 65 | 43% (32-55) | +0.10 | -1.72 | -112 |  |
| (0.374, 1.555] | 63 | 35% (24-47) | -0.12 | -2.38 | -150 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.139] | 64 | 41% (29-53) | +0.11 | -1.32 | -85 |  |
| (0.139, 0.405] | 64 | 42% (31-54) | +0.71 | -1.35 | -86 |  |
| (0.405, 1.281] | 64 | 34% (24-47) | -0.75 | -2.78 | -178 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.292] | 65 | 40% (29-52) | +0.30 | -1.84 | -120 |  |
| (-0.292, 0.364] | 64 | 44% (32-56) | +0.86 | -0.37 | -24 |  |
| (0.364, 2.726] | 64 | 33% (23-45) | -1.19 | -3.31 | -212 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0522] | 65 | 38% (28-51) | -0.44 | -2.05 | -133 |  |
| (0.0522, 0.123] | 64 | 45% (34-57) | +0.82 | -0.91 | -58 |  |
| (0.123, 0.678] | 64 | 33% (23-45) | -0.41 | -2.56 | -164 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.207] | 65 | 42% (30-54) | -0.13 | -1.37 | -89 |  |
| (0.207, 0.314] | 64 | 41% (29-53) | +0.47 | -1.53 | -98 |  |
| (0.314, 0.875] | 64 | 34% (24-47) | -0.37 | -2.62 | -168 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 65 | 38% (28-51) | +0.15 | -1.60 | -104 |  |
| (2.389, 3.632] | 64 | 47% (35-59) | +0.95 | -0.89 | -57 |  |
| (3.632, 18.762] | 64 | 31% (21-43) | -1.12 | -3.03 | -194 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0971] | 65 | 46% (35-58) | +0.34 | -0.42 | -27 |  |
| (0.0971, 0.145] | 65 | 37% (26-49) | +0.14 | -1.13 | -73 |  |
| (0.145, 0.392] | 63 | 33% (23-46) | -0.52 | -4.04 | -255 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.53] | 23 | 22% (10-42) | -2.44 | -3.30 | -76 |  |
| (-0.53, 0.474] | 22 | 45% (27-65) | +0.73 | +0.22 | +5 |  |
| (0.474, 5.305] | 22 | 59% (39-77) | +2.74 | +2.02 | +44 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.486] | 25 | 40% (23-59) | -0.41 | -1.09 | -27 |  |
| (0.486, 0.694] | 25 | 40% (23-59) | +0.32 | -0.37 | -9 |  |
| (0.694, 1.74] | 24 | 42% (24-61) | +0.20 | -0.63 | -15 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 25 | 52% (33-70) | +1.32 | +0.87 | +22 |  |
| (0.779, 1.206] | 24 | 29% (15-49) | -0.76 | -1.60 | -38 |  |
| (1.206, 3.566] | 25 | 40% (23-59) | -0.48 | -1.39 | -35 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.348] | 25 | 36% (20-55) | -0.46 | -1.05 | -26 |  |
| (0.348, 0.557] | 24 | 50% (31-69) | +1.21 | +0.50 | +12 |  |
| (0.557, 1.21] | 25 | 36% (20-55) | -0.59 | -1.48 | -37 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 96, target 49, time_stop 45, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0971] | 65 | 34% | 15% | 49% |
| (0.0971, 0.145] | 65 | 55% | 32% | 9% |
| (0.145, 0.392] | 63 | 60% | 29% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
