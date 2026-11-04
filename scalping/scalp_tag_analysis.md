# Scalp signal analysis (fixed exits)

_230 tagged trades, 25 trading days (2026-10-01 to 2026-11-04). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 230 | 40% (33-46) | -0.00 | -1.65 | -380 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 38 | -8 | -0.21 | 192 | -372 | -1.94 | +8 |
| skip first 30 min | 2 | -8 | -4.06 | 228 | -371 | -1.63 | +8 |
| skip when SPY is down on the day | 89 | -137 | -1.54 | 141 | -242 | -1.72 | +137 |
| skip when SPY is below its VWAP | 98 | -212 | -2.16 | 132 | -167 | -1.27 | +212 |
| skip when SPY fell over the last 15 min | 82 | -132 | -1.61 | 148 | -247 | -1.67 | +132 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 57 | -201 | -3.52 | 173 | -179 | -1.03 | +201 |
| skip stock not beating SPY over 15 min | 37 | -39 | -1.06 | 193 | -340 | -1.76 | +39 |
| skip afternoon entries (2:00-3:45 PM) | 49 | -224 | -4.56 | 181 | -156 | -0.86 | +224 |
| skip volume spikes above 5x average | 43 | -148 | -3.44 | 187 | -232 | -1.24 | +148 |
| skip when the stop is inside normal noise (range > stop) | 15 | -33 | -2.22 | 215 | -346 | -1.61 | +33 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 28 | -54 | -1.94 | 202 | -325 | -1.61 | +54 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 113 | -335 | -2.97 | 117 | -44 | -0.38 | +335 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 53% (37-69) | +2.10 | +0.32 | +11 |  |
| 60-240 | 93 | 38% (28-48) | -0.22 | -1.63 | -151 |  |
| 240-375 | 65 | 29% (20-41) | -1.65 | -3.56 | -231 |  |
| 375-390 | 38 | 50% (35-65) | +1.47 | -0.21 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 42% (28-58) | +0.35 | -1.04 | -40 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 66 | 33% (23-45) | -0.38 | -1.70 | -112 |  |
| > 0.2 | 75 | 43% (32-54) | -0.01 | -1.73 | -130 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 98 | 39% (30-49) | -0.37 | -2.16 | -212 |  |
| above VWAP | 132 | 40% (32-49) | +0.27 | -1.27 | -167 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.134] | 77 | 40% (30-51) | +0.07 | -1.22 | -94 |  |
| (0.134, 0.376] | 76 | 45% (34-56) | +0.34 | -1.32 | -101 |  |
| (0.376, 2.096] | 77 | 34% (24-45) | -0.41 | -2.40 | -185 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.109] | 76 | 46% (35-57) | +0.70 | -0.55 | -42 |  |
| (0.109, 0.415] | 76 | 41% (30-52) | +0.31 | -1.63 | -124 |  |
| (0.415, 2.453] | 76 | 33% (23-44) | -0.92 | -2.71 | -206 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.349] | 77 | 42% (31-53) | +0.24 | -1.64 | -126 |  |
| (-0.349, 0.401] | 76 | 46% (35-57) | +1.05 | -0.11 | -8 |  |
| (0.401, 4.204] | 77 | 31% (22-42) | -1.28 | -3.18 | -245 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0552] | 77 | 40% (30-51) | -0.21 | -1.67 | -129 |  |
| (0.0552, 0.122] | 76 | 46% (35-57) | +0.80 | -0.65 | -50 |  |
| (0.122, 0.924] | 77 | 32% (23-44) | -0.58 | -2.61 | -201 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.209] | 77 | 44% (34-55) | +0.32 | -0.81 | -63 |  |
| (0.209, 0.316] | 76 | 41% (30-52) | +0.31 | -1.50 | -114 |  |
| (0.316, 2.663] | 77 | 34% (24-45) | -0.63 | -2.64 | -203 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.299] | 77 | 36% (27-48) | -0.13 | -1.69 | -130 |  |
| (2.299, 3.625] | 76 | 50% (39-61) | +1.14 | -0.54 | -41 |  |
| (3.625, 18.762] | 77 | 32% (23-44) | -0.99 | -2.71 | -208 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 77 | 47% (36-58) | +0.44 | -0.32 | -24 |  |
| (0.0985, 0.149] | 76 | 38% (28-49) | +0.03 | -1.14 | -86 |  |
| (0.149, 0.392] | 77 | 34% (24-45) | -0.47 | -3.49 | -269 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 35 | 29% (16-45) | -1.91 | -2.74 | -96 |  |
| (-0.912, 0.466] | 34 | 47% (31-63) | +0.91 | +0.38 | +13 |  |
| (0.466, 5.599] | 35 | 51% (36-67) | +1.65 | +0.90 | +32 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.516] | 37 | 46% (31-62) | +0.39 | -0.23 | -8 |  |
| (0.516, 0.741] | 37 | 41% (26-57) | -0.04 | -0.79 | -29 |  |
| (0.741, 1.75] | 37 | 38% (24-54) | -0.23 | -1.03 | -38 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 37 | 43% (29-59) | +0.04 | -0.49 | -18 |  |
| (0.789, 1.214] | 37 | 41% (26-57) | +0.23 | -0.49 | -18 |  |
| (1.214, 5.866] | 37 | 41% (26-57) | -0.16 | -1.07 | -40 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.351] | 37 | 41% (26-57) | -0.10 | -0.68 | -25 |  |
| (0.351, 0.56] | 37 | 49% (33-64) | +0.88 | +0.14 | +5 |  |
| (0.56, 2.726] | 37 | 35% (22-51) | -0.67 | -1.52 | -56 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 113, target 56, time_stop 51, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 77 | 34% | 16% | 44% |
| (0.0985, 0.149] | 76 | 54% | 29% | 12% |
| (0.149, 0.392] | 77 | 60% | 29% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
