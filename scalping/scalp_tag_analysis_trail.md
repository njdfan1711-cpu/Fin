# Scalp signal analysis (trail exits)

_199 tagged trades, 22 trading days (2026-10-01 to 2026-10-30). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 199 | 38% (32-45) | -0.83 | -2.63 | -523 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 29 | +13 | +0.45 | 170 | -536 | -3.15 | -13 |
| skip first 30 min | 1 | -6 | -6.31 | 198 | -517 | -2.61 | +6 |
| skip when SPY is down on the day | 80 | -260 | -3.25 | 119 | -263 | -2.21 | +260 |
| skip when SPY is below its VWAP | 83 | -294 | -3.54 | 116 | -229 | -1.98 | +294 |
| skip when SPY fell over the last 15 min | 75 | -185 | -2.47 | 124 | -338 | -2.73 | +185 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 50 | -204 | -4.08 | 149 | -319 | -2.14 | +204 |
| skip stock not beating SPY over 15 min | 33 | -63 | -1.91 | 166 | -460 | -2.77 | +63 |
| skip afternoon entries (2:00-3:45 PM) | 43 | -211 | -4.91 | 156 | -312 | -2.00 | +211 |
| skip volume spikes above 5x average | 38 | -180 | -4.73 | 161 | -343 | -2.13 | +180 |
| skip when the stop is inside normal noise (range > stop) | 11 | -36 | -3.25 | 188 | -487 | -2.59 | +36 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.62%) | 20 | -68 | -3.42 | 179 | -455 | -2.54 | +68 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 106 | -375 | -3.54 | 93 | -148 | -1.59 | +375 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 29 | 52% (34-69) | +0.13 | -1.85 | -54 |  |
| 60-240 | 85 | 34% (25-45) | -1.32 | -2.81 | -239 |  |
| 240-375 | 56 | 34% (23-47) | -2.27 | -4.36 | -244 |  |
| 375-390 | 29 | 45% (28-62) | +2.42 | +0.45 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 29 | 38% (23-56) | -1.05 | -2.63 | -76 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 61 | 36% (25-49) | -1.36 | -2.73 | -167 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 83 | 31% (22-42) | -1.55 | -3.54 | -294 |  |
| above VWAP | 116 | 43% (34-52) | -0.31 | -1.98 | -229 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 67 | 37% (27-49) | -0.00 | -1.40 | -94 |  |
| (0.132, 0.374] | 67 | 46% (35-58) | -0.68 | -2.48 | -166 |  |
| (0.374, 1.555] | 65 | 31% (21-43) | -1.84 | -4.05 | -263 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.118] | 66 | 41% (30-53) | +0.11 | -1.30 | -86 |  |
| (0.118, 0.404] | 66 | 41% (30-53) | -0.85 | -2.85 | -188 |  |
| (0.404, 1.281] | 66 | 33% (23-45) | -1.68 | -3.68 | -243 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.348] | 67 | 37% (27-49) | -1.26 | -3.33 | -223 |  |
| (-0.348, 0.338] | 66 | 45% (34-57) | +0.63 | -0.60 | -40 |  |
| (0.338, 2.726] | 66 | 32% (22-44) | -1.85 | -3.95 | -260 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 67 | 40% (29-52) | -1.07 | -2.64 | -177 |  |
| (0.0521, 0.122] | 66 | 39% (29-51) | +0.18 | -1.42 | -93 |  |
| (0.122, 0.678] | 66 | 35% (24-47) | -1.59 | -3.83 | -253 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.206] | 67 | 43% (32-55) | +0.18 | -1.04 | -70 |  |
| (0.206, 0.312] | 66 | 38% (27-50) | -0.99 | -2.97 | -196 |  |
| (0.312, 0.875] | 66 | 33% (23-45) | -1.69 | -3.90 | -257 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 67 | 40% (29-52) | -0.54 | -2.24 | -150 |  |
| (2.39, 3.637] | 66 | 45% (34-57) | +0.65 | -1.15 | -76 |  |
| (3.637, 18.762] | 66 | 29% (19-41) | -2.60 | -4.49 | -297 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0971] | 67 | 48% (36-60) | +0.56 | -0.19 | -12 |  |
| (0.0971, 0.145] | 66 | 41% (30-53) | -1.10 | -2.36 | -156 |  |
| (0.145, 0.392] | 66 | 26% (17-37) | -1.97 | -5.38 | -355 | ▼ |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.941000000000001, -0.633] | 25 | 28% (14-48) | -2.83 | -3.71 | -93 |  |
| (-0.633, 0.444] | 24 | 50% (31-69) | -0.40 | -0.93 | -22 |  |
| (0.444, 5.305] | 24 | 67% (47-82) | +0.61 | -0.11 | -3 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.486] | 27 | 48% (31-66) | -0.27 | -0.93 | -25 |  |
| (0.486, 0.709] | 26 | 50% (32-68) | -1.04 | -1.73 | -45 |  |
| (0.709, 1.74] | 27 | 44% (28-63) | -1.90 | -2.74 | -74 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 27 | 52% (34-69) | -0.79 | -1.25 | -34 |  |
| (0.779, 1.206] | 26 | 42% (26-61) | -1.17 | -1.97 | -51 |  |
| (1.206, 3.566] | 27 | 48% (31-66) | -1.26 | -2.19 | -59 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.348] | 27 | 41% (25-59) | -0.90 | -1.49 | -40 |  |
| (0.348, 0.552] | 26 | 58% (39-74) | -0.37 | -1.11 | -29 | ▲ |
| (0.552, 1.21] | 27 | 44% (28-63) | -1.91 | -2.79 | -75 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.16%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 90, trail_stop 77, time_stop 29, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0971] | 67 | 31% | 30% | 36% |
| (0.0971, 0.145] | 66 | 48% | 45% | 5% |
| (0.145, 0.392] | 66 | 56% | 41% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
