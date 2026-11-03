# Scalp signal analysis (fixed exits)

_215 tagged trades, 24 trading days (2026-10-01 to 2026-11-03). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 215 | 38% (31-44) | -0.22 | -1.94 | -417 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -17 | -0.47 | 180 | -401 | -2.23 | +17 |
| skip first 30 min | 2 | -8 | -4.06 | 213 | -409 | -1.92 | +8 |
| skip when SPY is down on the day | 89 | -137 | -1.54 | 126 | -280 | -2.22 | +137 |
| skip when SPY is below its VWAP | 94 | -214 | -2.27 | 121 | -204 | -1.68 | +214 |
| skip when SPY fell over the last 15 min | 78 | -134 | -1.71 | 137 | -284 | -2.07 | +134 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 53 | -193 | -3.65 | 162 | -224 | -1.38 | +193 |
| skip stock not beating SPY over 15 min | 37 | -39 | -1.06 | 178 | -378 | -2.12 | +39 |
| skip afternoon entries (2:00-3:45 PM) | 45 | -218 | -4.85 | 170 | -199 | -1.17 | +218 |
| skip volume spikes above 5x average | 40 | -177 | -4.42 | 175 | -240 | -1.37 | +177 |
| skip when the stop is inside normal noise (range > stop) | 14 | -43 | -3.08 | 201 | -374 | -1.86 | +43 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.63%) | 24 | -61 | -2.52 | 191 | -357 | -1.87 | +61 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 110 | -315 | -2.86 | 105 | -102 | -0.97 | +315 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 33 | 52% (35-67) | +1.89 | +0.09 | +3 |  |
| 60-240 | 88 | 35% (26-46) | -0.56 | -2.03 | -179 |  |
| 240-375 | 59 | 29% (19-41) | -1.79 | -3.81 | -225 |  |
| 375-390 | 35 | 46% (30-62) | +1.30 | -0.47 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 42% (28-58) | +0.35 | -1.04 | -40 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 65 | 34% (24-46) | -0.29 | -1.62 | -105 |  |
| > 0.2 | 61 | 36% (25-49) | -0.89 | -2.87 | -175 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 94 | 37% (28-47) | -0.43 | -2.27 | -214 |  |
| above VWAP | 121 | 38% (30-47) | -0.06 | -1.68 | -204 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 72 | 36% (26-48) | -0.36 | -1.70 | -122 |  |
| (0.126, 0.374] | 71 | 45% (34-57) | +0.41 | -1.34 | -95 |  |
| (0.374, 1.555] | 72 | 32% (22-43) | -0.69 | -2.78 | -200 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.122] | 71 | 42% (31-54) | +0.20 | -1.15 | -82 |  |
| (0.122, 0.415] | 71 | 39% (29-51) | +0.29 | -1.70 | -121 |  |
| (0.415, 2.453] | 71 | 32% (23-44) | -1.05 | -2.91 | -206 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.351] | 72 | 39% (28-50) | -0.03 | -2.00 | -144 |  |
| (-0.351, 0.356] | 71 | 44% (33-55) | +0.81 | -0.41 | -29 |  |
| (0.356, 2.726] | 72 | 31% (21-42) | -1.43 | -3.40 | -244 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 72 | 39% (28-50) | -0.41 | -1.93 | -139 |  |
| (0.0521, 0.122] | 71 | 44% (33-55) | +0.57 | -0.95 | -67 |  |
| (0.122, 0.678] | 72 | 31% (21-42) | -0.82 | -2.93 | -211 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.209] | 72 | 42% (31-53) | -0.06 | -1.24 | -90 |  |
| (0.209, 0.314] | 71 | 38% (28-50) | +0.02 | -1.87 | -133 |  |
| (0.314, 0.979] | 72 | 33% (24-45) | -0.62 | -2.71 | -195 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.35] | 72 | 38% (27-49) | +0.01 | -1.62 | -116 |  |
| (2.35, 3.574] | 71 | 48% (37-59) | +0.94 | -0.79 | -56 |  |
| (3.574, 18.762] | 72 | 28% (19-39) | -1.59 | -3.39 | -244 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 73 | 45% (34-57) | +0.29 | -0.48 | -35 |  |
| (0.0985, 0.149] | 70 | 37% (27-49) | +0.03 | -1.18 | -83 |  |
| (0.149, 0.392] | 72 | 31% (21-42) | -0.98 | -4.17 | -300 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.899] | 30 | 20% (10-37) | -2.98 | -3.85 | -115 | ▼ |
| (-0.899, 0.444] | 30 | 43% (27-61) | +0.65 | +0.12 | +4 |  |
| (0.444, 5.305] | 29 | 52% (34-69) | +1.54 | +0.79 | +23 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.511] | 32 | 44% (28-61) | +0.23 | -0.40 | -13 |  |
| (0.511, 0.74] | 32 | 38% (23-55) | -0.23 | -0.98 | -31 |  |
| (0.74, 1.74] | 32 | 31% (18-49) | -1.35 | -2.16 | -69 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.769] | 32 | 41% (26-58) | +0.09 | -0.43 | -14 |  |
| (0.769, 1.194] | 32 | 38% (23-55) | -0.11 | -0.85 | -27 |  |
| (1.194, 5.866] | 32 | 34% (20-52) | -1.32 | -2.27 | -73 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.346] | 32 | 38% (23-55) | -0.36 | -0.95 | -30 |  |
| (0.346, 0.554] | 32 | 41% (26-58) | -0.05 | -0.81 | -26 |  |
| (0.554, 1.659] | 32 | 34% (20-52) | -0.93 | -1.79 | -57 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 110, target 51, time_stop 47, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 73 | 36% | 16% | 44% |
| (0.0985, 0.149] | 70 | 56% | 30% | 10% |
| (0.149, 0.392] | 72 | 62% | 25% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
