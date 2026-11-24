# Scalp signal analysis (trail exits)

_318 tagged trades, 39 trading days (2026-10-01 to 2026-11-24). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 318 | 44% (38-49) | -0.61 | -1.99 | -633 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +29 | +0.48 | 258 | -662 | -2.57 | -29 |
| skip first 30 min | 4 | -17 | -4.16 | 314 | -617 | -1.96 | +17 |
| skip when SPY is down on the day | 147 | -306 | -2.08 | 171 | -328 | -1.92 | +306 |
| skip when SPY is below its VWAP | 140 | -327 | -2.33 | 178 | -306 | -1.72 | +327 |
| skip when SPY fell over the last 15 min | 106 | -205 | -1.93 | 212 | -429 | -2.02 | +205 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 79 | -220 | -2.78 | 239 | -413 | -1.73 | +220 |
| skip stock not beating SPY over 15 min | 49 | -114 | -2.32 | 269 | -520 | -1.93 | +114 |
| skip afternoon entries (2:00-3:45 PM) | 69 | -249 | -3.61 | 249 | -385 | -1.54 | +249 |
| skip volume spikes above 5x average | 68 | -233 | -3.42 | 250 | -401 | -1.60 | +233 |
| skip when the stop is inside normal noise (range > stop) | 44 | -58 | -1.31 | 274 | -576 | -2.10 | +58 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.73%) | 50 | -77 | -1.54 | 268 | -556 | -2.08 | +77 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 180 | -214 | -1.19 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 49% (34-64) | -0.41 | -2.04 | -80 |  |
| 60-240 | 131 | 40% (32-48) | -1.18 | -2.34 | -306 |  |
| 240-375 | 88 | 41% (31-51) | -1.52 | -3.13 | -276 |  |
| 375-390 | 60 | 53% (41-65) | +1.85 | +0.48 | +29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 91 | 47% (37-57) | -0.34 | -1.33 | -121 |  |
| -0.2 to 0 | 56 | 41% (29-54) | -1.29 | -3.30 | -185 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 102 | 48% (39-58) | +0.20 | -1.24 | -126 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 140 | 41% (34-50) | -0.87 | -2.33 | -327 |  |
| above VWAP | 178 | 46% (38-53) | -0.40 | -1.72 | -306 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 106 | 41% (32-50) | -0.41 | -1.49 | -158 |  |
| (0.129, 0.374] | 106 | 52% (42-61) | -0.25 | -1.65 | -174 |  |
| (0.374, 5.591] | 106 | 39% (30-48) | -1.17 | -2.83 | -300 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.134] | 105 | 51% (42-61) | +0.36 | -0.74 | -78 |  |
| (0.134, 0.455] | 104 | 40% (31-50) | -0.97 | -2.66 | -276 |  |
| (0.455, 4.846] | 105 | 40% (31-50) | -1.10 | -2.50 | -263 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.583] | 106 | 49% (40-58) | -0.28 | -1.65 | -175 |  |
| (-0.583, 0.325] | 106 | 43% (34-53) | -0.17 | -1.39 | -147 |  |
| (0.325, 9.926] | 106 | 39% (30-48) | -1.38 | -2.94 | -311 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0561] | 106 | 43% (34-53) | -0.97 | -2.21 | -234 |  |
| (0.0561, 0.127] | 106 | 48% (39-58) | +0.20 | -1.08 | -115 |  |
| (0.127, 0.924] | 106 | 40% (31-49) | -1.06 | -2.68 | -284 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.222] | 106 | 45% (36-55) | +0.07 | -0.93 | -98 |  |
| (0.222, 0.351] | 106 | 46% (37-56) | -0.64 | -2.30 | -244 |  |
| (0.351, 2.663] | 106 | 40% (31-49) | -1.25 | -2.75 | -291 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.38] | 106 | 44% (35-54) | -0.44 | -1.80 | -191 |  |
| (2.38, 3.634] | 106 | 51% (42-60) | +0.65 | -0.77 | -81 |  |
| (3.634, 19.488] | 106 | 36% (27-45) | -2.04 | -3.40 | -361 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 106 | 47% (38-57) | +0.09 | -0.64 | -68 |  |
| (0.104, 0.167] | 106 | 44% (35-54) | -0.98 | -2.16 | -229 |  |
| (0.167, 0.76] | 106 | 40% (31-49) | -0.95 | -3.18 | -337 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.734] | 64 | 42% (31-54) | -1.34 | -2.14 | -137 |  |
| (-0.734, 0.664] | 64 | 53% (41-65) | +0.04 | -0.51 | -33 |  |
| (0.664, 14.989] | 64 | 58% (46-69) | -0.17 | -0.91 | -58 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.552] | 67 | 48% (36-60) | -0.64 | -1.25 | -84 |  |
| (0.552, 0.884] | 66 | 56% (44-67) | -0.39 | -1.10 | -73 | ▲ |
| (0.884, 3.799] | 66 | 48% (37-60) | -0.69 | -1.48 | -98 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.925] | 67 | 51% (39-62) | -1.05 | -1.62 | -109 |  |
| (0.925, 1.669] | 66 | 48% (37-60) | -0.64 | -1.33 | -88 |  |
| (1.669, 9.058] | 66 | 53% (41-65) | -0.04 | -0.88 | -58 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 67 | 43% (32-55) | -0.99 | -1.57 | -105 |  |
| (0.409, 0.628] | 66 | 62% (50-73) | +0.01 | -0.70 | -46 | ▲ |
| (0.628, 4.001] | 66 | 47% (35-59) | -0.73 | -1.56 | -103 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.15%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 43%
- Exit mix: stop 137, trail_stop 136, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 106 | 34% | 33% | 28% |
| (0.104, 0.167] | 106 | 47% | 46% | 3% |
| (0.167, 0.76] | 106 | 48% | 49% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
