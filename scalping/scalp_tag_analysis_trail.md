# Scalp signal analysis (trail exits)

_301 tagged trades, 35 trading days (2026-10-01 to 2026-11-18). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 301 | 42% (36-47) | -0.71 | -2.14 | -643 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 57 | +23 | +0.41 | 244 | -666 | -2.73 | -23 |
| skip first 30 min | 4 | -17 | -4.16 | 297 | -626 | -2.11 | +17 |
| skip when SPY is down on the day | 131 | -313 | -2.39 | 170 | -330 | -1.94 | +313 |
| skip when SPY is below its VWAP | 133 | -341 | -2.56 | 168 | -302 | -1.80 | +341 |
| skip when SPY fell over the last 15 min | 103 | -215 | -2.09 | 198 | -428 | -2.16 | +215 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 74 | -225 | -3.04 | 227 | -418 | -1.84 | +225 |
| skip stock not beating SPY over 15 min | 47 | -108 | -2.29 | 254 | -535 | -2.11 | +108 |
| skip afternoon entries (2:00-3:45 PM) | 66 | -245 | -3.71 | 235 | -398 | -1.69 | +245 |
| skip volume spikes above 5x average | 63 | -236 | -3.74 | 238 | -407 | -1.71 | +236 |
| skip when the stop is inside normal noise (range > stop) | 38 | -68 | -1.79 | 263 | -575 | -2.19 | +68 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 46 | -91 | -1.97 | 255 | -553 | -2.17 | +91 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 136 | -419 | -3.08 | 165 | -224 | -1.36 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 47% (32-63) | -0.47 | -2.15 | -82 |  |
| 60-240 | 123 | 37% (29-46) | -1.32 | -2.53 | -311 |  |
| 240-375 | 83 | 39% (29-49) | -1.62 | -3.30 | -274 |  |
| 375-390 | 57 | 51% (38-63) | +1.81 | +0.41 | +23 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 80 | 42% (32-53) | -0.57 | -1.62 | -129 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 133 | 38% (31-47) | -1.05 | -2.56 | -341 |  |
| above VWAP | 168 | 44% (37-52) | -0.43 | -1.80 | -302 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 101 | 40% (31-49) | -0.36 | -1.48 | -149 |  |
| (0.123, 0.374] | 100 | 49% (39-59) | -0.44 | -1.90 | -190 |  |
| (0.374, 5.591] | 100 | 36% (27-46) | -1.33 | -3.03 | -303 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.135] | 99 | 49% (40-59) | +0.33 | -0.80 | -79 |  |
| (0.135, 0.448] | 99 | 40% (31-50) | -0.91 | -2.65 | -263 |  |
| (0.448, 4.846] | 99 | 35% (27-45) | -1.43 | -2.88 | -285 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.526] | 101 | 44% (34-53) | -0.62 | -2.15 | -217 |  |
| (-0.526, 0.34] | 100 | 45% (36-55) | +0.04 | -1.11 | -111 |  |
| (0.34, 9.926] | 100 | 36% (27-46) | -1.54 | -3.15 | -315 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0558] | 101 | 43% (33-52) | -0.98 | -2.26 | -229 |  |
| (0.0558, 0.131] | 100 | 45% (36-55) | +0.08 | -1.26 | -126 |  |
| (0.131, 0.924] | 100 | 37% (28-47) | -1.22 | -2.89 | -289 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 101 | 46% (36-55) | +0.22 | -0.79 | -80 |  |
| (0.217, 0.346] | 100 | 45% (36-55) | -0.67 | -2.32 | -232 |  |
| (0.346, 2.663] | 100 | 34% (25-44) | -1.68 | -3.31 | -331 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.381] | 101 | 41% (32-50) | -0.63 | -2.02 | -204 |  |
| (2.381, 3.632] | 100 | 50% (40-60) | +0.65 | -0.81 | -81 |  |
| (3.632, 19.488] | 100 | 34% (25-44) | -2.14 | -3.57 | -357 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.105] | 101 | 47% (37-56) | +0.10 | -0.66 | -66 |  |
| (0.105, 0.166] | 101 | 44% (34-53) | -0.98 | -2.13 | -215 |  |
| (0.166, 0.76] | 99 | 34% (26-44) | -1.25 | -3.66 | -362 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 59 | 41% (29-53) | -1.40 | -2.22 | -131 |  |
| (-0.793, 0.617] | 58 | 50% (38-62) | -0.12 | -0.67 | -39 |  |
| (0.617, 7.522] | 58 | 53% (41-66) | -0.41 | -1.17 | -68 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.559] | 61 | 48% (36-60) | -0.63 | -1.26 | -77 |  |
| (0.559, 0.851] | 60 | 53% (41-65) | -0.67 | -1.38 | -83 |  |
| (0.851, 3.799] | 61 | 43% (31-55) | -0.90 | -1.72 | -105 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.9] | 61 | 46% (34-58) | -1.42 | -2.01 | -123 |  |
| (0.9, 1.638] | 60 | 52% (39-64) | -0.27 | -0.97 | -58 |  |
| (1.638, 9.058] | 61 | 46% (34-58) | -0.50 | -1.36 | -83 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 61 | 44% (33-57) | -0.77 | -1.35 | -83 |  |
| (0.408, 0.617] | 60 | 60% (47-71) | -0.13 | -0.86 | -51 | ▲ |
| (0.617, 4.001] | 61 | 39% (28-52) | -1.28 | -2.13 | -130 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 134, trail_stop 122, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.105] | 101 | 34% | 32% | 30% |
| (0.105, 0.166] | 101 | 48% | 46% | 3% |
| (0.166, 0.76] | 99 | 53% | 44% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
