# Scalp signal analysis (trail exits)

_317 tagged trades, 38 trading days (2026-10-01 to 2026-11-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 317 | 44% (38-49) | -0.62 | -2.00 | -635 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +29 | +0.48 | 257 | -664 | -2.58 | -29 |
| skip first 30 min | 4 | -17 | -4.16 | 313 | -619 | -1.98 | +17 |
| skip when SPY is down on the day | 147 | -306 | -2.08 | 170 | -330 | -1.94 | +306 |
| skip when SPY is below its VWAP | 140 | -327 | -2.33 | 177 | -309 | -1.74 | +327 |
| skip when SPY fell over the last 15 min | 105 | -207 | -1.97 | 212 | -429 | -2.02 | +207 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 78 | -214 | -2.74 | 239 | -422 | -1.76 | +214 |
| skip stock not beating SPY over 15 min | 49 | -114 | -2.32 | 268 | -522 | -1.95 | +114 |
| skip afternoon entries (2:00-3:45 PM) | 69 | -249 | -3.61 | 248 | -387 | -1.56 | +249 |
| skip volume spikes above 5x average | 68 | -233 | -3.42 | 249 | -403 | -1.62 | +233 |
| skip when the stop is inside normal noise (range > stop) | 43 | -60 | -1.39 | 274 | -576 | -2.10 | +60 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 50 | -75 | -1.50 | 267 | -560 | -2.10 | +75 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 179 | -216 | -1.21 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 49% (34-64) | -0.41 | -2.04 | -80 |  |
| 60-240 | 130 | 39% (31-48) | -1.21 | -2.37 | -309 |  |
| 240-375 | 88 | 41% (31-51) | -1.52 | -3.13 | -276 |  |
| 375-390 | 60 | 53% (41-65) | +1.85 | +0.48 | +29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 91 | 47% (37-57) | -0.34 | -1.33 | -121 |  |
| -0.2 to 0 | 56 | 41% (29-54) | -1.29 | -3.30 | -185 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 140 | 41% (34-50) | -0.87 | -2.33 | -327 |  |
| above VWAP | 177 | 45% (38-53) | -0.42 | -1.74 | -309 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 106 | 41% (32-50) | -0.41 | -1.49 | -158 |  |
| (0.126, 0.374] | 105 | 51% (42-61) | -0.28 | -1.68 | -177 |  |
| (0.374, 5.591] | 106 | 39% (30-48) | -1.17 | -2.83 | -300 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.135] | 105 | 51% (42-61) | +0.38 | -0.72 | -76 |  |
| (0.135, 0.458] | 104 | 39% (31-49) | -1.05 | -2.72 | -283 |  |
| (0.458, 4.846] | 104 | 40% (31-50) | -1.09 | -2.50 | -260 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.585] | 106 | 49% (40-58) | -0.28 | -1.65 | -175 |  |
| (-0.585, 0.308] | 105 | 43% (34-52) | -0.21 | -1.43 | -151 |  |
| (0.308, 9.926] | 106 | 39% (30-48) | -1.37 | -2.93 | -310 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.056] | 106 | 43% (34-53) | -0.97 | -2.21 | -234 |  |
| (0.056, 0.127] | 106 | 48% (39-58) | +0.20 | -1.08 | -115 |  |
| (0.127, 0.924] | 105 | 39% (30-49) | -1.09 | -2.73 | -287 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.222] | 106 | 45% (36-55) | +0.07 | -0.93 | -98 |  |
| (0.222, 0.35] | 105 | 47% (37-56) | -0.59 | -2.18 | -229 |  |
| (0.35, 2.663] | 106 | 39% (30-48) | -1.34 | -2.90 | -308 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.384] | 106 | 43% (34-53) | -0.52 | -1.89 | -200 |  |
| (2.384, 3.635] | 105 | 51% (42-61) | +0.71 | -0.71 | -75 |  |
| (3.635, 19.488] | 106 | 36% (27-45) | -2.04 | -3.40 | -361 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 106 | 47% (38-57) | +0.09 | -0.64 | -68 |  |
| (0.104, 0.167] | 105 | 44% (35-53) | -1.01 | -2.20 | -231 |  |
| (0.167, 0.76] | 106 | 40% (31-49) | -0.95 | -3.18 | -337 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.711] | 64 | 41% (29-53) | -1.48 | -2.27 | -145 |  |
| (-0.711, 0.669] | 63 | 54% (42-66) | +0.13 | -0.42 | -26 |  |
| (0.669, 14.989] | 64 | 58% (46-69) | -0.17 | -0.91 | -58 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.55] | 66 | 48% (37-60) | -0.56 | -1.17 | -78 |  |
| (0.55, 0.871] | 66 | 55% (43-66) | -0.50 | -1.20 | -79 |  |
| (0.871, 3.799] | 66 | 48% (37-60) | -0.72 | -1.51 | -100 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.923] | 66 | 50% (38-62) | -1.09 | -1.67 | -110 |  |
| (0.923, 1.652] | 66 | 50% (38-62) | -0.52 | -1.21 | -80 |  |
| (1.652, 9.058] | 66 | 52% (40-63) | -0.17 | -1.01 | -67 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 66 | 44% (33-56) | -0.92 | -1.49 | -98 |  |
| (0.409, 0.625] | 66 | 62% (50-73) | +0.00 | -0.71 | -47 | ▲ |
| (0.625, 4.001] | 66 | 45% (34-57) | -0.86 | -1.69 | -111 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.15%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 137, trail_stop 135, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 106 | 34% | 33% | 28% |
| (0.104, 0.167] | 105 | 48% | 46% | 3% |
| (0.167, 0.76] | 106 | 48% | 49% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
