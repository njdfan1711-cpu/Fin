# Scalp signal analysis (trail exits)

_200 tagged trades, 22 trading days (2026-10-01 to 2026-10-30). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 200 | 38% (32-45) | -0.79 | -2.58 | -516 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 29 | +13 | +0.45 | 171 | -530 | -3.10 | -13 |
| skip first 30 min | 1 | -6 | -6.31 | 199 | -510 | -2.56 | +6 |
| skip when SPY is down on the day | 81 | -254 | -3.13 | 119 | -263 | -2.21 | +254 |
| skip when SPY is below its VWAP | 84 | -287 | -3.42 | 116 | -229 | -1.98 | +287 |
| skip when SPY fell over the last 15 min | 76 | -178 | -2.35 | 124 | -338 | -2.73 | +178 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 50 | -204 | -4.08 | 150 | -312 | -2.08 | +204 |
| skip stock not beating SPY over 15 min | 33 | -63 | -1.91 | 167 | -453 | -2.72 | +63 |
| skip afternoon entries (2:00-3:45 PM) | 43 | -211 | -4.91 | 157 | -305 | -1.95 | +211 |
| skip volume spikes above 5x average | 38 | -180 | -4.73 | 162 | -337 | -2.08 | +180 |
| skip when the stop is inside normal noise (range > stop) | 11 | -36 | -3.25 | 189 | -481 | -2.54 | +36 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.62%) | 20 | -68 | -3.42 | 180 | -448 | -2.49 | +68 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 106 | -375 | -3.54 | 94 | -141 | -1.50 | +375 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 29 | 52% (34-69) | +0.13 | -1.85 | -54 |  |
| 60-240 | 85 | 34% (25-45) | -1.32 | -2.81 | -239 |  |
| 240-375 | 57 | 35% (24-48) | -2.11 | -4.17 | -237 |  |
| 375-390 | 29 | 45% (28-62) | +2.42 | +0.45 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 30 | 40% (25-58) | -0.78 | -2.32 | -70 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 61 | 36% (25-49) | -1.36 | -2.73 | -167 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 84 | 32% (23-43) | -1.45 | -3.42 | -287 |  |
| above VWAP | 116 | 43% (34-52) | -0.31 | -1.98 | -229 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 67 | 37% (27-49) | -0.00 | -1.40 | -94 |  |
| (0.133, 0.372] | 66 | 47% (35-59) | -0.63 | -2.43 | -160 |  |
| (0.372, 1.555] | 67 | 31% (22-43) | -1.73 | -3.92 | -263 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.116] | 67 | 42% (31-54) | +0.22 | -1.18 | -79 |  |
| (0.116, 0.403] | 66 | 41% (30-53) | -0.85 | -2.85 | -188 |  |
| (0.403, 1.281] | 66 | 33% (23-45) | -1.68 | -3.68 | -243 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.346] | 67 | 37% (27-49) | -1.26 | -3.33 | -223 |  |
| (-0.346, 0.34] | 66 | 45% (34-57) | +0.63 | -0.60 | -40 |  |
| (0.34, 2.726] | 67 | 33% (23-45) | -1.72 | -3.79 | -254 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 67 | 40% (29-52) | -1.07 | -2.64 | -177 |  |
| (0.0521, 0.122] | 66 | 41% (30-53) | +0.38 | -1.22 | -80 |  |
| (0.122, 0.678] | 67 | 34% (24-46) | -1.66 | -3.87 | -259 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.204] | 67 | 45% (33-57) | +0.26 | -0.93 | -63 |  |
| (0.204, 0.311] | 66 | 38% (27-50) | -1.00 | -2.94 | -194 |  |
| (0.311, 0.875] | 67 | 33% (23-45) | -1.63 | -3.88 | -260 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 67 | 40% (29-52) | -0.45 | -2.16 | -144 |  |
| (2.389, 3.635] | 66 | 45% (34-57) | +0.62 | -1.17 | -77 |  |
| (3.635, 18.762] | 67 | 30% (20-42) | -2.53 | -4.40 | -295 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0972] | 67 | 48% (36-60) | +0.56 | -0.19 | -12 |  |
| (0.0972, 0.145] | 67 | 42% (31-54) | -0.98 | -2.22 | -149 |  |
| (0.145, 0.392] | 66 | 26% (17-37) | -1.97 | -5.38 | -355 | ▼ |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.941000000000001, -0.719] | 25 | 32% (17-52) | -2.32 | -3.19 | -80 |  |
| (-0.719, 0.444] | 25 | 48% (30-67) | -0.63 | -1.14 | -29 |  |
| (0.444, 5.305] | 24 | 67% (47-82) | +0.61 | -0.11 | -3 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.487] | 27 | 48% (31-66) | -0.27 | -0.93 | -25 |  |
| (0.487, 0.702] | 27 | 52% (34-69) | -0.75 | -1.42 | -38 |  |
| (0.702, 1.74] | 27 | 44% (28-63) | -1.90 | -2.74 | -74 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.784] | 27 | 52% (34-69) | -0.79 | -1.25 | -34 |  |
| (0.784, 1.203] | 27 | 44% (28-63) | -0.86 | -1.66 | -45 |  |
| (1.203, 3.566] | 27 | 48% (31-66) | -1.26 | -2.19 | -59 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.342] | 27 | 44% (28-63) | -0.42 | -1.00 | -27 |  |
| (0.342, 0.551] | 27 | 56% (37-72) | -0.58 | -1.31 | -35 |  |
| (0.551, 1.21] | 27 | 44% (28-63) | -1.91 | -2.79 | -75 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.16%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 90, trail_stop 78, time_stop 29, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0972] | 67 | 31% | 30% | 36% |
| (0.0972, 0.145] | 67 | 48% | 46% | 4% |
| (0.145, 0.392] | 66 | 56% | 41% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
