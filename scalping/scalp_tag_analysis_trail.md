# Scalp signal analysis (trail exits)

_303 tagged trades, 35 trading days (2026-10-01 to 2026-11-18). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 303 | 42% (36-47) | -0.70 | -2.13 | -645 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 58 | +28 | +0.48 | 245 | -673 | -2.75 | -28 |
| skip first 30 min | 4 | -17 | -4.16 | 299 | -628 | -2.10 | +17 |
| skip when SPY is down on the day | 133 | -315 | -2.37 | 170 | -330 | -1.94 | +315 |
| skip when SPY is below its VWAP | 133 | -341 | -2.56 | 170 | -304 | -1.79 | +341 |
| skip when SPY fell over the last 15 min | 103 | -215 | -2.09 | 200 | -430 | -2.15 | +215 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 75 | -224 | -2.98 | 228 | -421 | -1.85 | +224 |
| skip stock not beating SPY over 15 min | 47 | -108 | -2.29 | 256 | -537 | -2.10 | +108 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -252 | -3.75 | 236 | -393 | -1.67 | +252 |
| skip volume spikes above 5x average | 63 | -236 | -3.74 | 240 | -409 | -1.70 | +236 |
| skip when the stop is inside normal noise (range > stop) | 38 | -68 | -1.79 | 265 | -577 | -2.18 | +68 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 46 | -91 | -1.97 | 257 | -554 | -2.16 | +91 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 136 | -419 | -3.08 | 167 | -225 | -1.35 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 47% (32-63) | -0.47 | -2.15 | -82 |  |
| 60-240 | 123 | 37% (29-46) | -1.32 | -2.53 | -311 |  |
| 240-375 | 84 | 38% (28-49) | -1.68 | -3.33 | -280 |  |
| 375-390 | 58 | 52% (39-64) | +1.87 | +0.48 | +28 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 82 | 43% (33-53) | -0.56 | -1.60 | -131 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 133 | 38% (31-47) | -1.05 | -2.56 | -341 |  |
| above VWAP | 170 | 44% (37-52) | -0.43 | -1.79 | -304 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 101 | 40% (31-49) | -0.36 | -1.48 | -149 |  |
| (0.129, 0.374] | 101 | 50% (40-59) | -0.38 | -1.82 | -184 |  |
| (0.374, 5.591] | 101 | 36% (27-45) | -1.37 | -3.08 | -311 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.134] | 100 | 49% (39-59) | +0.27 | -0.85 | -85 |  |
| (0.134, 0.449] | 99 | 40% (31-50) | -0.91 | -2.65 | -263 |  |
| (0.449, 4.846] | 100 | 36% (27-46) | -1.36 | -2.80 | -280 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.53] | 101 | 45% (35-54) | -0.57 | -2.06 | -208 |  |
| (-0.53, 0.348] | 101 | 45% (35-54) | +0.05 | -1.15 | -116 |  |
| (0.348, 9.926] | 101 | 36% (27-45) | -1.59 | -3.18 | -321 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0558] | 101 | 42% (32-51) | -1.10 | -2.38 | -240 |  |
| (0.0558, 0.129] | 101 | 46% (36-55) | +0.17 | -1.16 | -117 |  |
| (0.129, 0.924] | 101 | 38% (29-47) | -1.18 | -2.85 | -288 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 101 | 45% (35-54) | +0.10 | -0.91 | -91 |  |
| (0.217, 0.347] | 101 | 46% (36-55) | -0.60 | -2.25 | -227 |  |
| (0.347, 2.663] | 101 | 35% (26-44) | -1.61 | -3.23 | -326 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.386] | 101 | 41% (32-50) | -0.63 | -2.02 | -204 |  |
| (2.386, 3.618] | 101 | 50% (41-60) | +0.69 | -0.75 | -76 |  |
| (3.618, 19.488] | 101 | 34% (25-43) | -2.18 | -3.61 | -364 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 101 | 48% (38-57) | +0.22 | -0.53 | -54 |  |
| (0.104, 0.166] | 101 | 42% (32-51) | -1.14 | -2.31 | -233 |  |
| (0.166, 0.76] | 101 | 36% (27-45) | -1.19 | -3.55 | -358 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 60 | 40% (29-53) | -1.48 | -2.29 | -137 |  |
| (-0.793, 0.616] | 58 | 52% (39-64) | +0.02 | -0.53 | -31 |  |
| (0.616, 7.522] | 59 | 53% (40-65) | -0.45 | -1.21 | -71 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.552] | 62 | 47% (35-59) | -0.64 | -1.26 | -78 |  |
| (0.552, 0.843] | 61 | 54% (42-66) | -0.64 | -1.35 | -83 | ▲ |
| (0.843, 3.799] | 61 | 43% (31-55) | -0.90 | -1.72 | -105 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.891] | 62 | 47% (35-59) | -1.30 | -1.90 | -118 |  |
| (0.891, 1.624] | 61 | 51% (39-63) | -0.36 | -1.06 | -65 |  |
| (1.624, 9.058] | 61 | 46% (34-58) | -0.50 | -1.36 | -83 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 62 | 44% (32-56) | -0.86 | -1.44 | -89 |  |
| (0.408, 0.616] | 61 | 61% (48-72) | -0.04 | -0.76 | -47 | ▲ |
| (0.616, 4.001] | 61 | 39% (28-52) | -1.28 | -2.13 | -130 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.16%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 135, trail_stop 123, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 101 | 33% | 33% | 30% |
| (0.104, 0.166] | 101 | 50% | 44% | 3% |
| (0.166, 0.76] | 101 | 51% | 46% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
