# Scalp signal analysis (trail exits)

_201 tagged trades, 22 trading days (2026-10-01 to 2026-10-30). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 201 | 38% (32-45) | -0.78 | -2.57 | -517 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 29 | +13 | +0.45 | 172 | -530 | -3.08 | -13 |
| skip first 30 min | 1 | -6 | -6.31 | 200 | -510 | -2.55 | +6 |
| skip when SPY is down on the day | 82 | -254 | -3.10 | 119 | -263 | -2.21 | +254 |
| skip when SPY is below its VWAP | 85 | -287 | -3.38 | 116 | -229 | -1.98 | +287 |
| skip when SPY fell over the last 15 min | 77 | -179 | -2.32 | 124 | -338 | -2.73 | +179 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 50 | -198 | -3.96 | 151 | -319 | -2.11 | +198 |
| skip stock not beating SPY over 15 min | 33 | -63 | -1.91 | 168 | -454 | -2.70 | +63 |
| skip afternoon entries (2:00-3:45 PM) | 44 | -211 | -4.80 | 157 | -305 | -1.95 | +211 |
| skip volume spikes above 5x average | 38 | -180 | -4.73 | 163 | -337 | -2.07 | +180 |
| skip when the stop is inside normal noise (range > stop) | 11 | -36 | -3.25 | 190 | -481 | -2.53 | +36 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.62%) | 21 | -69 | -3.27 | 180 | -448 | -2.49 | +69 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 107 | -376 | -3.51 | 94 | -141 | -1.50 | +376 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 29 | 52% (34-69) | +0.13 | -1.85 | -54 |  |
| 60-240 | 85 | 34% (25-45) | -1.32 | -2.81 | -239 |  |
| 240-375 | 58 | 34% (24-47) | -2.06 | -4.10 | -238 |  |
| 375-390 | 29 | 45% (28-62) | +2.42 | +0.45 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 31 | 39% (24-56) | -0.73 | -2.26 | -70 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 61 | 36% (25-49) | -1.36 | -2.73 | -167 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 85 | 32% (23-42) | -1.43 | -3.38 | -287 |  |
| above VWAP | 116 | 43% (34-52) | -0.31 | -1.98 | -229 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 67 | 37% (27-49) | -0.00 | -1.40 | -94 |  |
| (0.133, 0.374] | 68 | 47% (36-59) | -0.56 | -2.35 | -160 |  |
| (0.374, 1.555] | 66 | 30% (21-42) | -1.80 | -3.99 | -264 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.117] | 67 | 42% (31-54) | +0.22 | -1.18 | -79 |  |
| (0.117, 0.404] | 66 | 41% (30-53) | -0.85 | -2.85 | -188 |  |
| (0.404, 1.281] | 67 | 33% (23-45) | -1.64 | -3.63 | -243 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.345] | 67 | 37% (27-49) | -1.26 | -3.33 | -223 |  |
| (-0.345, 0.339] | 67 | 45% (33-57) | +0.63 | -0.60 | -40 |  |
| (0.339, 2.726] | 67 | 33% (23-45) | -1.72 | -3.79 | -254 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 67 | 39% (28-51) | -1.08 | -2.65 | -177 |  |
| (0.052, 0.121] | 67 | 42% (31-54) | +0.39 | -1.20 | -80 |  |
| (0.121, 0.678] | 67 | 34% (24-46) | -1.66 | -3.87 | -259 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.205] | 67 | 45% (33-57) | +0.26 | -0.93 | -63 |  |
| (0.205, 0.313] | 67 | 37% (27-49) | -0.95 | -2.93 | -197 |  |
| (0.313, 0.875] | 67 | 33% (23-45) | -1.66 | -3.85 | -258 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.382] | 67 | 39% (28-51) | -0.46 | -2.17 | -145 |  |
| (2.382, 3.634] | 67 | 46% (35-58) | +0.64 | -1.14 | -77 |  |
| (3.634, 18.762] | 67 | 30% (20-42) | -2.53 | -4.40 | -295 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0973] | 67 | 48% (36-60) | +0.56 | -0.19 | -12 |  |
| (0.0973, 0.146] | 67 | 42% (31-54) | -0.98 | -2.22 | -149 |  |
| (0.146, 0.392] | 67 | 25% (16-37) | -1.93 | -5.30 | -355 | ▼ |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-8.533999999999999, -0.8] | 25 | 32% (17-52) | -2.17 | -3.08 | -77 |  |
| (-0.8, 0.444] | 26 | 46% (29-65) | -0.71 | -1.22 | -32 |  |
| (0.444, 5.305] | 24 | 67% (47-82) | +0.61 | -0.11 | -3 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.487] | 28 | 46% (30-64) | -0.27 | -0.93 | -26 |  |
| (0.487, 0.717] | 27 | 52% (34-69) | -0.94 | -1.64 | -44 |  |
| (0.717, 1.74] | 27 | 44% (28-63) | -1.65 | -2.50 | -68 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 28 | 50% (33-67) | -0.97 | -1.43 | -40 |  |
| (0.789, 1.21] | 27 | 44% (28-63) | -0.86 | -1.66 | -45 |  |
| (1.21, 3.566] | 27 | 48% (31-66) | -1.01 | -1.96 | -53 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.345] | 28 | 43% (27-61) | -0.62 | -1.20 | -34 |  |
| (0.345, 0.552] | 27 | 59% (41-75) | -0.21 | -0.95 | -26 | ▲ |
| (0.552, 1.21] | 27 | 41% (25-59) | -2.03 | -2.91 | -79 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.15%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 90, trail_stop 79, time_stop 29, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0973] | 67 | 31% | 30% | 36% |
| (0.0973, 0.146] | 67 | 48% | 46% | 4% |
| (0.146, 0.392] | 67 | 55% | 42% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
