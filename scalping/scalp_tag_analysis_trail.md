# Scalp signal analysis (trail exits)

_193 tagged trades, 21 trading days (2026-10-01 to 2026-10-29). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 193 | 38% (31-45) | -0.83 | -2.66 | -513 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 28 | +11 | +0.38 | 165 | -523 | -3.17 | -11 |
| skip first 30 min | 1 | -6 | -6.31 | 192 | -506 | -2.64 | +6 |
| skip when SPY is down on the day | 74 | -250 | -3.38 | 119 | -263 | -2.21 | +250 |
| skip when SPY is below its VWAP | 78 | -290 | -3.72 | 115 | -223 | -1.94 | +290 |
| skip when SPY fell over the last 15 min | 71 | -179 | -2.52 | 122 | -334 | -2.74 | +179 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 48 | -191 | -3.98 | 145 | -322 | -2.22 | +191 |
| skip stock not beating SPY over 15 min | 32 | -70 | -2.19 | 161 | -442 | -2.75 | +70 |
| skip afternoon entries (2:00-3:45 PM) | 42 | -218 | -5.19 | 151 | -295 | -1.95 | +218 |
| skip volume spikes above 5x average | 35 | -159 | -4.55 | 158 | -354 | -2.24 | +159 |
| skip when the stop is inside normal noise (range > stop) | 8 | -15 | -1.91 | 185 | -497 | -2.69 | +15 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.63%) | 19 | -71 | -3.71 | 174 | -442 | -2.54 | +71 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 104 | -362 | -3.48 | 89 | -151 | -1.70 | +362 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 27 | 56% (37-72) | +0.58 | -1.48 | -40 |  |
| 60-240 | 83 | 34% (24-44) | -1.29 | -2.80 | -232 |  |
| 240-375 | 55 | 33% (22-46) | -2.45 | -4.57 | -251 |  |
| 375-390 | 28 | 43% (27-61) | +2.40 | +0.38 | +11 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 25 | 36% (20-55) | -1.11 | -2.81 | -70 |  |
| -0.2 to 0 | 49 | 37% (25-51) | -1.45 | -3.67 | -180 |  |
| 0 to 0.2 | 61 | 36% (25-49) | -1.36 | -2.73 | -167 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 78 | 29% (21-40) | -1.65 | -3.72 | -290 |  |
| above VWAP | 115 | 43% (35-53) | -0.27 | -1.94 | -223 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 65 | 35% (25-48) | -0.07 | -1.49 | -97 |  |
| (0.133, 0.374] | 65 | 48% (36-60) | -0.62 | -2.45 | -159 |  |
| (0.374, 1.555] | 63 | 30% (20-42) | -1.82 | -4.08 | -257 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.139] | 64 | 41% (29-53) | +0.11 | -1.32 | -85 |  |
| (0.139, 0.405] | 64 | 41% (29-53) | -0.80 | -2.85 | -183 |  |
| (0.405, 1.281] | 64 | 33% (23-45) | -1.71 | -3.74 | -239 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.292] | 65 | 37% (26-49) | -1.18 | -3.32 | -216 |  |
| (-0.292, 0.364] | 64 | 45% (34-57) | +0.65 | -0.58 | -37 |  |
| (0.364, 2.726] | 64 | 31% (21-43) | -1.94 | -4.06 | -260 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0522] | 65 | 38% (28-51) | -1.24 | -2.85 | -185 |  |
| (0.0522, 0.123] | 64 | 39% (28-51) | +0.23 | -1.50 | -96 |  |
| (0.123, 0.678] | 64 | 36% (25-48) | -1.46 | -3.61 | -231 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.207] | 65 | 42% (30-54) | +0.02 | -1.22 | -79 |  |
| (0.207, 0.314] | 64 | 39% (28-51) | -0.84 | -2.85 | -182 |  |
| (0.314, 0.875] | 64 | 33% (23-45) | -1.67 | -3.92 | -251 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 65 | 38% (28-51) | -0.69 | -2.43 | -158 |  |
| (2.389, 3.632] | 64 | 44% (32-56) | +0.58 | -1.26 | -80 |  |
| (3.632, 18.762] | 64 | 31% (21-43) | -2.37 | -4.28 | -274 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0971] | 65 | 46% (35-58) | +0.42 | -0.34 | -22 |  |
| (0.0971, 0.145] | 65 | 40% (29-52) | -1.13 | -2.40 | -156 |  |
| (0.145, 0.392] | 63 | 27% (18-39) | -1.79 | -5.31 | -335 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.53] | 23 | 30% (16-51) | -2.58 | -3.44 | -79 |  |
| (-0.53, 0.474] | 22 | 50% (31-69) | -0.24 | -0.75 | -17 |  |
| (0.474, 5.305] | 22 | 64% (43-80) | +0.20 | -0.52 | -11 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.486] | 25 | 44% (27-63) | -0.71 | -1.39 | -35 |  |
| (0.486, 0.694] | 25 | 48% (30-67) | -1.13 | -1.82 | -45 |  |
| (0.694, 1.74] | 24 | 50% (31-69) | -1.41 | -2.23 | -54 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 25 | 52% (33-70) | -0.65 | -1.11 | -28 |  |
| (0.779, 1.206] | 24 | 38% (21-57) | -1.71 | -2.54 | -61 |  |
| (1.206, 3.566] | 25 | 52% (33-70) | -0.90 | -1.81 | -45 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.348] | 25 | 36% (20-55) | -1.40 | -1.99 | -50 |  |
| (0.348, 0.557] | 24 | 67% (47-82) | +0.49 | -0.22 | -5 | ▲ |
| (0.557, 1.21] | 25 | 40% (23-59) | -2.26 | -3.15 | -79 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.15%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 8% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 87, trail_stop 75, time_stop 29, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0971] | 65 | 32% | 29% | 37% |
| (0.0971, 0.145] | 65 | 49% | 45% | 5% |
| (0.145, 0.392] | 63 | 54% | 43% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
