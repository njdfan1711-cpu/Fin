# Scalp signal analysis (trail exits)

_302 tagged trades, 35 trading days (2026-10-01 to 2026-11-18). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 302 | 41% (36-47) | -0.72 | -2.15 | -649 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 57 | +23 | +0.41 | 245 | -673 | -2.75 | -23 |
| skip first 30 min | 4 | -17 | -4.16 | 298 | -633 | -2.12 | +17 |
| skip when SPY is down on the day | 132 | -320 | -2.42 | 170 | -330 | -1.94 | +320 |
| skip when SPY is below its VWAP | 133 | -341 | -2.56 | 169 | -308 | -1.82 | +341 |
| skip when SPY fell over the last 15 min | 103 | -215 | -2.09 | 199 | -435 | -2.18 | +215 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 75 | -224 | -2.98 | 227 | -426 | -1.88 | +224 |
| skip stock not beating SPY over 15 min | 47 | -108 | -2.29 | 255 | -542 | -2.12 | +108 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -252 | -3.75 | 235 | -398 | -1.69 | +252 |
| skip volume spikes above 5x average | 63 | -236 | -3.74 | 239 | -414 | -1.73 | +236 |
| skip when the stop is inside normal noise (range > stop) | 38 | -68 | -1.79 | 264 | -582 | -2.20 | +68 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 46 | -91 | -1.97 | 256 | -559 | -2.18 | +91 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 136 | -419 | -3.08 | 166 | -230 | -1.39 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 47% (32-63) | -0.47 | -2.15 | -82 |  |
| 60-240 | 123 | 37% (29-46) | -1.32 | -2.53 | -311 |  |
| 240-375 | 84 | 38% (28-49) | -1.68 | -3.33 | -280 |  |
| 375-390 | 57 | 51% (38-63) | +1.81 | +0.41 | +23 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 81 | 42% (32-53) | -0.64 | -1.67 | -136 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 133 | 38% (31-47) | -1.05 | -2.56 | -341 |  |
| above VWAP | 169 | 44% (37-51) | -0.47 | -1.82 | -308 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 101 | 40% (31-49) | -0.36 | -1.48 | -149 |  |
| (0.126, 0.374] | 100 | 49% (39-59) | -0.44 | -1.89 | -189 |  |
| (0.374, 5.591] | 101 | 36% (27-45) | -1.37 | -3.08 | -311 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.133] | 100 | 49% (39-59) | +0.27 | -0.85 | -85 |  |
| (0.133, 0.446] | 99 | 40% (31-50) | -0.91 | -2.65 | -263 |  |
| (0.446, 4.846] | 99 | 35% (27-45) | -1.43 | -2.88 | -285 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.516] | 101 | 44% (34-53) | -0.62 | -2.15 | -217 |  |
| (-0.516, 0.356] | 100 | 45% (36-55) | +0.04 | -1.11 | -111 |  |
| (0.356, 9.926] | 101 | 36% (27-45) | -1.59 | -3.18 | -321 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0557] | 101 | 42% (32-51) | -1.10 | -2.38 | -240 |  |
| (0.0557, 0.13] | 100 | 45% (36-55) | +0.12 | -1.22 | -122 |  |
| (0.13, 0.924] | 101 | 38% (29-47) | -1.18 | -2.85 | -288 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.216] | 101 | 45% (35-54) | +0.10 | -0.91 | -91 |  |
| (0.216, 0.346] | 100 | 46% (37-56) | -0.62 | -2.27 | -227 |  |
| (0.346, 2.663] | 101 | 34% (25-43) | -1.66 | -3.28 | -331 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.384] | 101 | 41% (32-50) | -0.63 | -2.02 | -204 |  |
| (2.384, 3.625] | 100 | 50% (40-60) | +0.65 | -0.81 | -81 |  |
| (3.625, 19.488] | 101 | 34% (25-43) | -2.18 | -3.61 | -364 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 101 | 47% (37-56) | +0.11 | -0.64 | -64 |  |
| (0.104, 0.166] | 100 | 42% (33-52) | -1.09 | -2.27 | -227 |  |
| (0.166, 0.76] | 101 | 36% (27-45) | -1.19 | -3.55 | -358 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 60 | 40% (29-53) | -1.48 | -2.29 | -137 |  |
| (-0.793, 0.616] | 57 | 51% (38-63) | -0.08 | -0.62 | -36 |  |
| (0.616, 7.522] | 59 | 53% (40-65) | -0.45 | -1.21 | -71 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.554] | 61 | 46% (34-58) | -0.74 | -1.36 | -83 |  |
| (0.554, 0.847] | 61 | 54% (42-66) | -0.64 | -1.35 | -83 | ▲ |
| (0.847, 3.799] | 61 | 43% (31-55) | -0.90 | -1.72 | -105 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.909] | 61 | 46% (34-58) | -1.42 | -2.01 | -123 |  |
| (0.909, 1.631] | 61 | 51% (39-63) | -0.36 | -1.06 | -65 |  |
| (1.631, 9.058] | 61 | 46% (34-58) | -0.50 | -1.36 | -83 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.404] | 61 | 44% (33-57) | -0.77 | -1.35 | -82 |  |
| (0.404, 0.616] | 61 | 59% (46-70) | -0.23 | -0.95 | -58 | ▲ |
| (0.616, 4.001] | 61 | 39% (28-52) | -1.28 | -2.13 | -130 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.16%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 135, trail_stop 122, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 101 | 34% | 32% | 30% |
| (0.104, 0.166] | 100 | 49% | 44% | 3% |
| (0.166, 0.76] | 101 | 51% | 46% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
