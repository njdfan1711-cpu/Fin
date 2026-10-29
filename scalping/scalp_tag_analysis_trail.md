# Scalp signal analysis (trail exits)

_191 tagged trades, 21 trading days (2026-10-01 to 2026-10-29). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 191 | 38% (31-45) | -0.82 | -2.66 | -508 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 26 | +16 | +0.60 | 165 | -523 | -3.17 | -16 |
| skip first 30 min | 1 | -6 | -6.31 | 190 | -501 | -2.64 | +6 |
| skip when SPY is down on the day | 74 | -250 | -3.38 | 117 | -258 | -2.20 | +250 |
| skip when SPY is below its VWAP | 78 | -290 | -3.72 | 113 | -218 | -1.93 | +290 |
| skip when SPY fell over the last 15 min | 71 | -179 | -2.52 | 120 | -329 | -2.74 | +179 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 48 | -199 | -4.14 | 143 | -309 | -2.16 | +199 |
| skip stock not beating SPY over 15 min | 32 | -70 | -2.19 | 159 | -438 | -2.75 | +70 |
| skip afternoon entries (2:00-3:45 PM) | 42 | -218 | -5.19 | 149 | -290 | -1.94 | +218 |
| skip volume spikes above 5x average | 35 | -159 | -4.55 | 156 | -349 | -2.23 | +159 |
| skip when the stop is inside normal noise (range > stop) | 8 | -15 | -1.91 | 183 | -493 | -2.69 | +15 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.62%) | 18 | -72 | -4.00 | 173 | -436 | -2.52 | +72 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 103 | -363 | -3.52 | 88 | -145 | -1.65 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 27 | 56% (37-72) | +0.58 | -1.48 | -40 |  |
| 60-240 | 83 | 34% (24-44) | -1.29 | -2.80 | -232 |  |
| 240-375 | 55 | 33% (22-46) | -2.45 | -4.57 | -251 |  |
| 375-390 | 26 | 42% (26-61) | +2.71 | +0.60 | +16 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 25 | 36% (20-55) | -1.11 | -2.81 | -70 |  |
| -0.2 to 0 | 49 | 37% (25-51) | -1.45 | -3.67 | -180 |  |
| 0 to 0.2 | 59 | 36% (25-48) | -1.35 | -2.74 | -162 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 78 | 29% (21-40) | -1.65 | -3.72 | -290 |  |
| above VWAP | 113 | 43% (35-53) | -0.24 | -1.93 | -218 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.134] | 64 | 36% (25-48) | +0.03 | -1.41 | -90 |  |
| (0.134, 0.372] | 63 | 48% (36-60) | -0.70 | -2.53 | -160 |  |
| (0.372, 1.555] | 64 | 30% (20-42) | -1.78 | -4.03 | -258 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.141] | 64 | 41% (29-53) | +0.11 | -1.45 | -93 |  |
| (0.141, 0.405] | 63 | 41% (30-54) | -0.71 | -2.67 | -168 |  |
| (0.405, 1.281] | 63 | 32% (22-44) | -1.78 | -3.82 | -241 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.29] | 64 | 36% (25-48) | -1.23 | -3.39 | -217 |  |
| (-0.29, 0.364] | 63 | 46% (34-58) | +0.75 | -0.49 | -31 |  |
| (0.364, 2.726] | 64 | 31% (21-43) | -1.94 | -4.06 | -260 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 64 | 39% (28-51) | -1.17 | -2.77 | -178 |  |
| (0.0521, 0.122] | 63 | 40% (29-52) | +0.33 | -1.31 | -83 |  |
| (0.122, 0.678] | 64 | 34% (24-47) | -1.59 | -3.87 | -248 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.207] | 64 | 42% (31-54) | +0.11 | -1.14 | -73 |  |
| (0.207, 0.313] | 63 | 40% (29-52) | -0.76 | -2.78 | -175 |  |
| (0.313, 0.875] | 64 | 31% (21-43) | -1.80 | -4.05 | -259 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.392] | 64 | 39% (28-51) | -0.63 | -2.39 | -153 |  |
| (2.392, 3.635] | 63 | 43% (31-55) | +0.58 | -1.29 | -81 |  |
| (3.635, 18.762] | 64 | 31% (21-43) | -2.37 | -4.28 | -274 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0968] | 64 | 47% (35-59) | +0.51 | -0.23 | -15 |  |
| (0.0968, 0.145] | 64 | 39% (28-51) | -1.19 | -2.47 | -158 |  |
| (0.145, 0.392] | 63 | 27% (18-39) | -1.79 | -5.31 | -335 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.514] | 22 | 32% (16-53) | -2.43 | -3.31 | -73 |  |
| (-0.514, 0.464] | 21 | 48% (28-68) | -0.60 | -1.10 | -23 |  |
| (0.464, 5.305] | 22 | 64% (43-80) | +0.41 | -0.29 | -6 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.485] | 24 | 46% (28-65) | -0.49 | -1.16 | -28 |  |
| (0.485, 0.694] | 25 | 48% (30-67) | -1.12 | -1.84 | -46 |  |
| (0.694, 1.74] | 23 | 48% (29-67) | -1.58 | -2.39 | -55 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.769] | 24 | 50% (31-69) | -0.78 | -1.23 | -30 |  |
| (0.769, 1.192] | 24 | 42% (24-61) | -1.37 | -2.17 | -52 |  |
| (1.192, 3.566] | 24 | 50% (31-69) | -1.03 | -1.97 | -47 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.35] | 24 | 38% (21-57) | -1.21 | -1.81 | -43 |  |
| (0.35, 0.554] | 24 | 67% (47-82) | +0.49 | -0.22 | -5 | ▲ |
| (0.554, 1.21] | 24 | 38% (21-57) | -2.46 | -3.34 | -80 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.15%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 8% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 86, trail_stop 74, time_stop 29, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0968] | 64 | 31% | 30% | 38% |
| (0.0968, 0.145] | 64 | 50% | 44% | 5% |
| (0.145, 0.392] | 63 | 54% | 43% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
