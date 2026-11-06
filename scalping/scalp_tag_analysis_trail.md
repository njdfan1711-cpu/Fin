# Scalp signal analysis (trail exits)

_242 tagged trades, 26 trading days (2026-10-01 to 2026-11-05). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 242 | 42% (36-48) | -0.61 | -2.22 | -538 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 43 | +2 | +0.05 | 199 | -540 | -2.71 | -2 |
| skip first 30 min | 2 | -3 | -1.70 | 240 | -535 | -2.23 | +3 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 143 | -270 | -1.89 | +268 |
| skip when SPY is below its VWAP | 109 | -317 | -2.91 | 133 | -221 | -1.66 | +317 |
| skip when SPY fell over the last 15 min | 88 | -187 | -2.12 | 154 | -351 | -2.28 | +187 |
| skip over-extended (30-min run in top quarter, > 0.53%) | 60 | -218 | -3.63 | 182 | -320 | -1.76 | +218 |
| skip stock not beating SPY over 15 min | 38 | -76 | -1.99 | 204 | -462 | -2.27 | +76 |
| skip afternoon entries (2:00-3:45 PM) | 53 | -222 | -4.19 | 189 | -316 | -1.67 | +222 |
| skip volume spikes above 5x average | 45 | -166 | -3.68 | 197 | -372 | -1.89 | +166 |
| skip when the stop is inside normal noise (range > stop) | 24 | -28 | -1.17 | 218 | -510 | -2.34 | +28 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.69%) | 31 | -42 | -1.36 | 211 | -496 | -2.35 | +42 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 118 | -403 | -3.42 | 124 | -135 | -1.09 | +403 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 96 | 39% (29-49) | -0.97 | -2.36 | -226 |  |
| 240-375 | 69 | 38% (27-49) | -1.77 | -3.62 | -250 |  |
| 375-390 | 43 | 49% (35-63) | +1.65 | +0.05 | +2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 77 | 48% (37-59) | +0.68 | -1.03 | -79 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 109 | 37% (28-46) | -1.21 | -2.91 | -317 |  |
| above VWAP | 133 | 46% (38-54) | -0.12 | -1.66 | -221 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 81 | 40% (30-50) | -0.08 | -1.45 | -117 |  |
| (0.136, 0.384] | 80 | 52% (42-63) | -0.18 | -1.70 | -136 |  |
| (0.384, 5.591] | 81 | 33% (24-44) | -1.57 | -3.51 | -284 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.114] | 80 | 49% (38-60) | +0.56 | -0.67 | -53 |  |
| (0.114, 0.44] | 80 | 41% (31-52) | -0.88 | -2.79 | -224 |  |
| (0.44, 4.846] | 80 | 35% (25-46) | -1.51 | -3.22 | -258 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.391] | 81 | 47% (36-58) | -0.65 | -2.48 | -201 |  |
| (-0.391, 0.378] | 80 | 44% (33-55) | +0.40 | -0.76 | -61 |  |
| (0.378, 4.204] | 81 | 35% (25-45) | -1.58 | -3.41 | -276 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 81 | 42% (32-53) | -0.98 | -2.40 | -194 |  |
| (0.056, 0.127] | 81 | 46% (35-56) | +0.39 | -1.12 | -90 |  |
| (0.127, 0.924] | 80 | 38% (28-48) | -1.26 | -3.17 | -253 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 81 | 44% (34-55) | +0.27 | -0.84 | -68 |  |
| (0.212, 0.336] | 80 | 44% (33-55) | -0.78 | -2.65 | -212 |  |
| (0.336, 2.663] | 81 | 37% (27-48) | -1.33 | -3.19 | -258 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.324] | 81 | 42% (32-53) | -0.49 | -2.00 | -162 |  |
| (2.324, 3.625] | 80 | 49% (38-60) | +0.63 | -1.02 | -81 |  |
| (3.625, 18.762] | 81 | 35% (25-45) | -1.97 | -3.64 | -295 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.1] | 81 | 48% (38-59) | +0.38 | -0.40 | -32 |  |
| (0.1, 0.154] | 80 | 42% (32-53) | -1.14 | -2.27 | -182 |  |
| (0.154, 0.76] | 81 | 35% (25-45) | -1.09 | -4.00 | -324 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.265] | 39 | 44% (29-59) | -1.42 | -2.26 | -88 |  |
| (-1.265, 0.45] | 38 | 50% (35-65) | -0.32 | -0.91 | -34 |  |
| (0.45, 5.599] | 39 | 62% (46-75) | +0.47 | -0.26 | -10 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.532] | 41 | 49% (34-64) | -0.47 | -1.09 | -45 |  |
| (0.532, 0.779] | 41 | 54% (39-68) | -0.89 | -1.64 | -67 |  |
| (0.779, 3.799] | 41 | 51% (36-66) | -0.32 | -1.16 | -48 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.837] | 41 | 46% (32-61) | -1.40 | -1.97 | -81 |  |
| (0.837, 1.475] | 41 | 56% (41-70) | +0.05 | -0.68 | -28 |  |
| (1.475, 9.058] | 41 | 51% (36-66) | -0.33 | -1.24 | -51 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.368] | 41 | 49% (34-64) | -0.37 | -0.92 | -38 |  |
| (0.368, 0.605] | 41 | 61% (46-74) | -0.30 | -1.07 | -44 | ▲ |
| (0.605, 4.001] | 41 | 44% (30-59) | -1.01 | -1.90 | -78 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 105, trail_stop 101, time_stop 29, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.1] | 81 | 31% | 32% | 31% |
| (0.1, 0.154] | 80 | 50% | 46% | 2% |
| (0.154, 0.76] | 81 | 49% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
