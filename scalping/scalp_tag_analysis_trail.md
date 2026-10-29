# Scalp signal analysis (trail exits)

_189 tagged trades, 21 trading days (2026-10-01 to 2026-10-29). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 189 | 38% (31-45) | -0.81 | -2.66 | -503 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 26 | +16 | +0.60 | 163 | -519 | -3.18 | -16 |
| skip first 30 min | 1 | -6 | -6.31 | 188 | -497 | -2.64 | +6 |
| skip when SPY is down on the day | 72 | -246 | -3.41 | 117 | -258 | -2.20 | +246 |
| skip when SPY is below its VWAP | 77 | -292 | -3.79 | 112 | -211 | -1.89 | +292 |
| skip when SPY fell over the last 15 min | 69 | -175 | -2.53 | 120 | -329 | -2.74 | +175 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 47 | -192 | -4.09 | 142 | -311 | -2.19 | +192 |
| skip stock not beating SPY over 15 min | 32 | -70 | -2.19 | 157 | -433 | -2.76 | +70 |
| skip afternoon entries (2:00-3:45 PM) | 41 | -220 | -5.37 | 148 | -283 | -1.91 | +220 |
| skip volume spikes above 5x average | 35 | -159 | -4.55 | 154 | -344 | -2.24 | +159 |
| skip when the stop is inside normal noise (range > stop) | 7 | -9 | -1.25 | 182 | -495 | -2.72 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.62%) | 18 | -63 | -3.52 | 171 | -440 | -2.57 | +63 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 103 | -363 | -3.52 | 86 | -140 | -1.63 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 27 | 56% (37-72) | +0.58 | -1.48 | -40 |  |
| 60-240 | 82 | 34% (25-45) | -1.24 | -2.75 | -226 |  |
| 240-375 | 54 | 31% (21-45) | -2.55 | -4.69 | -253 |  |
| 375-390 | 26 | 42% (26-61) | +2.71 | +0.60 | +16 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 48 | 38% (25-52) | -1.35 | -3.61 | -173 |  |
| 0 to 0.2 | 59 | 36% (25-48) | -1.35 | -2.74 | -162 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 77 | 29% (20-39) | -1.71 | -3.79 | -292 |  |
| above VWAP | 112 | 44% (35-53) | -0.19 | -1.89 | -211 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 63 | 37% (26-49) | +0.01 | -1.43 | -90 |  |
| (0.133, 0.369] | 63 | 48% (36-60) | -0.59 | -2.36 | -149 |  |
| (0.369, 1.555] | 63 | 29% (19-41) | -1.85 | -4.21 | -265 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.142] | 63 | 41% (30-54) | +0.20 | -1.37 | -86 |  |
| (0.142, 0.406] | 62 | 40% (29-53) | -0.77 | -2.74 | -170 |  |
| (0.406, 1.281] | 63 | 32% (22-44) | -1.78 | -3.82 | -241 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.291] | 63 | 37% (26-49) | -1.16 | -3.34 | -211 |  |
| (-0.291, 0.371] | 63 | 46% (34-58) | +0.79 | -0.45 | -28 |  |
| (0.371, 2.726] | 63 | 30% (20-42) | -2.05 | -4.20 | -265 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 63 | 38% (27-50) | -1.20 | -2.82 | -178 |  |
| (0.052, 0.121] | 63 | 41% (30-54) | +0.44 | -1.21 | -76 |  |
| (0.121, 0.678] | 63 | 33% (23-46) | -1.66 | -3.96 | -250 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.207] | 63 | 43% (31-55) | +0.21 | -1.05 | -66 |  |
| (0.207, 0.313] | 63 | 40% (29-52) | -0.76 | -2.79 | -176 |  |
| (0.313, 0.875] | 63 | 30% (20-42) | -1.87 | -4.15 | -261 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.395] | 63 | 40% (29-52) | -0.55 | -2.32 | -146 |  |
| (2.395, 3.634] | 63 | 43% (31-55) | +0.58 | -1.29 | -81 |  |
| (3.634, 18.762] | 63 | 30% (20-42) | -2.45 | -4.38 | -276 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0969] | 63 | 46% (34-58) | +0.48 | -0.27 | -17 |  |
| (0.0969, 0.145] | 64 | 39% (28-51) | -1.19 | -2.47 | -158 |  |
| (0.145, 0.392] | 62 | 27% (18-40) | -1.72 | -5.29 | -328 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.498] | 21 | 33% (17-55) | -2.26 | -3.16 | -66 |  |
| (-0.498, 0.508] | 21 | 48% (28-68) | -0.37 | -0.89 | -19 |  |
| (0.508, 5.305] | 21 | 62% (41-79) | +0.09 | -0.62 | -13 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.486] | 24 | 42% (24-61) | -0.85 | -1.54 | -37 |  |
| (0.486, 0.694] | 24 | 50% (31-69) | -0.93 | -1.63 | -39 |  |
| (0.694, 1.74] | 22 | 50% (31-69) | -1.39 | -2.21 | -49 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 24 | 50% (31-69) | -0.79 | -1.24 | -30 |  |
| (0.789, 1.2] | 23 | 39% (22-59) | -1.52 | -2.37 | -54 |  |
| (1.2, 3.566] | 23 | 52% (33-71) | -0.84 | -1.76 | -40 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.345] | 24 | 38% (21-57) | -1.21 | -1.81 | -43 |  |
| (0.345, 0.55] | 23 | 65% (45-81) | +0.34 | -0.36 | -8 | ▲ |
| (0.55, 1.21] | 23 | 39% (22-59) | -2.25 | -3.17 | -73 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.15%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 8% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 85, trail_stop 73, time_stop 29, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0969] | 63 | 32% | 29% | 38% |
| (0.0969, 0.145] | 64 | 50% | 44% | 5% |
| (0.145, 0.392] | 62 | 53% | 44% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
