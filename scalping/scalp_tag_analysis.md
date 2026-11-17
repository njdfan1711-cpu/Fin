# Scalp signal analysis (fixed exits)

_291 tagged trades, 34 trading days (2026-10-01 to 2026-11-17). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 291 | 38% (33-44) | -0.15 | -1.61 | -468 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 51 | -27 | -0.53 | 240 | -441 | -1.84 | +27 |
| skip first 30 min | 4 | -21 | -5.34 | 287 | -447 | -1.56 | +21 |
| skip when SPY is down on the day | 121 | -193 | -1.60 | 170 | -275 | -1.62 | +193 |
| skip when SPY is below its VWAP | 126 | -222 | -1.76 | 165 | -247 | -1.50 | +222 |
| skip when SPY fell over the last 15 min | 100 | -147 | -1.47 | 191 | -321 | -1.68 | +147 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 72 | -195 | -2.71 | 219 | -273 | -1.25 | +195 |
| skip stock not beating SPY over 15 min | 46 | -63 | -1.38 | 245 | -405 | -1.65 | +63 |
| skip afternoon entries (2:00-3:45 PM) | 65 | -231 | -3.56 | 226 | -237 | -1.05 | +231 |
| skip volume spikes above 5x average | 60 | -156 | -2.59 | 231 | -313 | -1.35 | +156 |
| skip when the stop is inside normal noise (range > stop) | 35 | -64 | -1.82 | 256 | -404 | -1.58 | +64 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 43 | -75 | -1.74 | 248 | -393 | -1.59 | +75 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 133 | -377 | -2.84 | 158 | -91 | -0.57 | +377 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 50% (35-65) | +1.69 | +0.01 | +0 |  |
| 60-240 | 120 | 37% (29-46) | -0.41 | -1.63 | -196 |  |
| 240-375 | 82 | 32% (23-42) | -1.31 | -2.99 | -245 |  |
| 375-390 | 51 | 45% (32-59) | +0.93 | -0.53 | -27 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 70 | 37% (27-49) | -0.27 | -1.37 | -96 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 126 | 39% (31-48) | -0.21 | -1.76 | -222 |  |
| above VWAP | 165 | 38% (31-46) | -0.11 | -1.50 | -247 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 97 | 38% (29-48) | -0.11 | -1.28 | -124 |  |
| (0.133, 0.375] | 97 | 41% (32-51) | -0.07 | -1.55 | -150 |  |
| (0.375, 5.591] | 97 | 36% (27-46) | -0.28 | -2.00 | -194 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.134] | 96 | 46% (36-56) | +0.65 | -0.50 | -48 |  |
| (0.134, 0.446] | 95 | 40% (31-50) | +0.31 | -1.47 | -140 |  |
| (0.446, 4.846] | 96 | 31% (23-41) | -1.23 | -2.70 | -259 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.468] | 97 | 40% (31-50) | -0.12 | -1.68 | -163 |  |
| (-0.468, 0.373] | 97 | 41% (32-51) | +0.53 | -0.65 | -63 |  |
| (0.373, 9.926] | 97 | 34% (25-44) | -0.87 | -2.50 | -242 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0555] | 97 | 38% (29-48) | -0.51 | -1.81 | -176 |  |
| (0.0555, 0.127] | 97 | 44% (35-54) | +0.55 | -0.81 | -78 |  |
| (0.127, 0.924] | 97 | 33% (24-43) | -0.50 | -2.20 | -214 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.218] | 97 | 43% (34-53) | +0.35 | -0.69 | -67 |  |
| (0.218, 0.346] | 97 | 40% (31-50) | +0.12 | -1.56 | -151 |  |
| (0.346, 2.663] | 97 | 32% (24-42) | -0.93 | -2.58 | -250 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.377] | 98 | 36% (27-46) | -0.32 | -1.73 | -170 |  |
| (2.377, 3.634] | 96 | 45% (35-55) | +0.49 | -1.00 | -96 |  |
| (3.634, 19.488] | 97 | 35% (26-45) | -0.62 | -2.09 | -202 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 97 | 46% (37-56) | +0.44 | -0.32 | -31 |  |
| (0.104, 0.165] | 97 | 34% (25-44) | -0.59 | -1.80 | -174 |  |
| (0.165, 0.76] | 97 | 35% (26-45) | -0.31 | -2.71 | -263 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 55 | 33% (22-46) | -1.01 | -1.84 | -101 |  |
| (-0.912, 0.615] | 55 | 45% (33-58) | +0.71 | +0.14 | +8 |  |
| (0.615, 7.522] | 55 | 40% (28-53) | -0.10 | -0.84 | -46 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.552] | 58 | 43% (31-56) | -0.04 | -0.68 | -39 |  |
| (0.552, 0.837] | 57 | 40% (29-53) | -0.04 | -0.76 | -43 |  |
| (0.837, 3.799] | 57 | 33% (22-46) | -0.63 | -1.44 | -82 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.884] | 58 | 40% (28-53) | -0.24 | -0.85 | -49 |  |
| (0.884, 1.613] | 57 | 47% (35-60) | +0.92 | +0.19 | +11 |  |
| (1.613, 9.058] | 57 | 30% (20-43) | -1.38 | -2.22 | -127 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 58 | 38% (27-51) | -0.30 | -0.90 | -52 |  |
| (0.408, 0.618] | 57 | 49% (37-62) | +0.88 | +0.15 | +9 |  |
| (0.618, 4.001] | 57 | 30% (20-43) | -1.28 | -2.12 | -121 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 3% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 148, target 70, time_stop 59, eod 14

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 97 | 35% | 16% | 42% |
| (0.104, 0.165] | 97 | 58% | 25% | 11% |
| (0.165, 0.76] | 97 | 60% | 31% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
