# Scalp signal analysis (trail exits)

_291 tagged trades, 34 trading days (2026-10-01 to 2026-11-17). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 291 | 41% (35-46) | -0.83 | -2.28 | -664 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 51 | -14 | -0.27 | 240 | -651 | -2.71 | +14 |
| skip first 30 min | 4 | -17 | -4.16 | 287 | -648 | -2.26 | +17 |
| skip when SPY is down on the day | 121 | -335 | -2.76 | 170 | -330 | -1.94 | +335 |
| skip when SPY is below its VWAP | 126 | -379 | -3.01 | 165 | -285 | -1.73 | +379 |
| skip when SPY fell over the last 15 min | 101 | -227 | -2.25 | 190 | -437 | -2.30 | +227 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 72 | -245 | -3.41 | 219 | -419 | -1.91 | +245 |
| skip stock not beating SPY over 15 min | 46 | -109 | -2.38 | 245 | -555 | -2.27 | +109 |
| skip afternoon entries (2:00-3:45 PM) | 65 | -246 | -3.79 | 226 | -418 | -1.85 | +246 |
| skip volume spikes above 5x average | 60 | -219 | -3.65 | 231 | -445 | -1.93 | +219 |
| skip when the stop is inside normal noise (range > stop) | 35 | -90 | -2.56 | 256 | -575 | -2.24 | +90 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 43 | -112 | -2.61 | 248 | -552 | -2.23 | +112 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 133 | -445 | -3.35 | 158 | -219 | -1.39 | +445 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 47% (32-63) | -0.47 | -2.15 | -82 |  |
| 60-240 | 120 | 38% (30-47) | -1.23 | -2.45 | -294 |  |
| 240-375 | 82 | 38% (28-49) | -1.67 | -3.35 | -275 |  |
| 375-390 | 51 | 45% (32-59) | +1.20 | -0.27 | -14 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 70 | 39% (28-50) | -1.05 | -2.15 | -151 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 126 | 35% (27-44) | -1.46 | -3.01 | -379 |  |
| above VWAP | 165 | 45% (37-52) | -0.35 | -1.73 | -285 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 97 | 39% (30-49) | -0.37 | -1.53 | -149 |  |
| (0.133, 0.375] | 97 | 48% (39-58) | -0.49 | -1.96 | -190 |  |
| (0.375, 5.591] | 97 | 34% (25-44) | -1.63 | -3.35 | -325 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.134] | 96 | 48% (38-58) | +0.22 | -0.94 | -90 |  |
| (0.134, 0.446] | 95 | 41% (32-51) | -0.84 | -2.63 | -250 |  |
| (0.446, 4.846] | 96 | 33% (25-43) | -1.75 | -3.21 | -308 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.468] | 97 | 40% (31-50) | -1.08 | -2.64 | -256 |  |
| (-0.468, 0.373] | 97 | 46% (37-56) | +0.25 | -0.93 | -90 |  |
| (0.373, 9.926] | 97 | 35% (26-45) | -1.65 | -3.28 | -318 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0555] | 97 | 41% (32-51) | -1.14 | -2.44 | -237 |  |
| (0.0555, 0.127] | 97 | 45% (36-55) | +0.17 | -1.19 | -115 |  |
| (0.127, 0.924] | 97 | 35% (26-45) | -1.52 | -3.22 | -312 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.218] | 97 | 44% (35-54) | +0.13 | -0.90 | -87 |  |
| (0.218, 0.346] | 97 | 45% (36-55) | -0.68 | -2.36 | -229 |  |
| (0.346, 2.663] | 97 | 32% (24-42) | -1.94 | -3.58 | -348 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.377] | 98 | 40% (31-50) | -0.73 | -2.14 | -210 |  |
| (2.377, 3.634] | 96 | 47% (37-57) | +0.31 | -1.18 | -114 |  |
| (3.634, 19.488] | 97 | 35% (26-45) | -2.04 | -3.51 | -341 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 97 | 47% (38-57) | +0.22 | -0.54 | -53 |  |
| (0.104, 0.165] | 97 | 40% (31-50) | -1.23 | -2.43 | -236 |  |
| (0.165, 0.76] | 97 | 34% (25-44) | -1.47 | -3.88 | -376 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 55 | 40% (28-53) | -1.42 | -2.24 | -123 |  |
| (-0.912, 0.615] | 55 | 49% (36-62) | -0.28 | -0.85 | -47 |  |
| (0.615, 7.522] | 55 | 51% (38-64) | -0.88 | -1.61 | -89 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.552] | 58 | 47% (34-59) | -0.70 | -1.34 | -78 |  |
| (0.552, 0.837] | 57 | 53% (40-65) | -0.76 | -1.48 | -84 |  |
| (0.837, 3.799] | 57 | 40% (29-53) | -1.36 | -2.17 | -124 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.884] | 58 | 45% (33-58) | -1.49 | -2.10 | -122 |  |
| (0.884, 1.613] | 57 | 53% (40-65) | -0.21 | -0.94 | -54 |  |
| (1.613, 9.058] | 57 | 42% (30-55) | -1.10 | -1.94 | -110 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 58 | 43% (31-56) | -0.86 | -1.47 | -85 |  |
| (0.408, 0.618] | 57 | 61% (48-73) | -0.09 | -0.81 | -46 | ▲ |
| (0.618, 4.001] | 57 | 35% (24-48) | -1.86 | -2.70 | -154 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.16%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 131, trail_stop 116, time_stop 35, eod 9

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 97 | 32% | 32% | 31% |
| (0.104, 0.165] | 97 | 51% | 43% | 3% |
| (0.165, 0.76] | 97 | 53% | 44% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
