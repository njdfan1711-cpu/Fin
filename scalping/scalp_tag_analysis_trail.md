# Scalp signal analysis (trail exits)

_327 tagged trades, 40 trading days (2026-10-01 to 2026-11-25). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 327 | 44% (39-49) | -0.62 | -1.98 | -646 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +24 | +0.39 | 265 | -670 | -2.53 | -24 |
| skip first 30 min | 4 | -17 | -4.16 | 323 | -630 | -1.95 | +17 |
| skip when SPY is down on the day | 150 | -309 | -2.06 | 177 | -337 | -1.90 | +309 |
| skip when SPY is below its VWAP | 141 | -326 | -2.31 | 186 | -320 | -1.72 | +326 |
| skip when SPY fell over the last 15 min | 108 | -208 | -1.93 | 219 | -438 | -2.00 | +208 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 81 | -213 | -2.62 | 246 | -434 | -1.76 | +213 |
| skip stock not beating SPY over 15 min | 51 | -118 | -2.31 | 276 | -528 | -1.91 | +118 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -251 | -3.58 | 257 | -395 | -1.54 | +251 |
| skip volume spikes above 5x average | 70 | -236 | -3.38 | 257 | -410 | -1.59 | +236 |
| skip when the stop is inside normal noise (range > stop) | 47 | -59 | -1.26 | 280 | -587 | -2.10 | +59 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 52 | -79 | -1.52 | 275 | -567 | -2.06 | +79 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 189 | -227 | -1.20 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 40 | 48% (33-63) | -0.54 | -2.15 | -86 |  |
| 60-240 | 136 | 41% (33-50) | -1.12 | -2.25 | -307 |  |
| 240-375 | 89 | 40% (31-51) | -1.52 | -3.12 | -278 |  |
| 375-390 | 62 | 53% (41-65) | +1.74 | +0.39 | +24 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 93 | 47% (37-57) | -0.38 | -1.36 | -126 |  |
| -0.2 to 0 | 57 | 42% (30-55) | -1.23 | -3.21 | -183 |  |
| 0 to 0.2 | 70 | 36% (26-47) | -1.54 | -2.84 | -199 |  |
| > 0.2 | 107 | 48% (38-57) | +0.10 | -1.29 | -138 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 141 | 42% (34-50) | -0.86 | -2.31 | -326 |  |
| above VWAP | 186 | 46% (39-53) | -0.44 | -1.72 | -320 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.119] | 109 | 41% (32-51) | -0.53 | -1.53 | -166 |  |
| (0.119, 0.37] | 109 | 52% (43-61) | -0.16 | -1.60 | -174 |  |
| (0.37, 5.591] | 109 | 39% (30-48) | -1.15 | -2.81 | -306 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.137] | 108 | 52% (43-61) | +0.39 | -0.69 | -75 |  |
| (0.137, 0.446] | 107 | 41% (32-51) | -0.98 | -2.62 | -280 |  |
| (0.446, 4.846] | 108 | 40% (31-49) | -1.16 | -2.54 | -274 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.583] | 109 | 49% (39-58) | -0.36 | -1.70 | -185 |  |
| (-0.583, 0.3] | 109 | 44% (35-53) | -0.19 | -1.39 | -152 |  |
| (0.3, 9.926] | 109 | 39% (31-49) | -1.31 | -2.84 | -309 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 109 | 42% (33-52) | -1.06 | -2.29 | -249 |  |
| (0.0559, 0.126] | 109 | 49% (39-58) | +0.14 | -1.12 | -122 |  |
| (0.126, 0.924] | 109 | 41% (32-51) | -0.93 | -2.52 | -275 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.224] | 109 | 44% (35-53) | -0.10 | -1.08 | -118 |  |
| (0.224, 0.351] | 109 | 48% (39-57) | -0.52 | -2.15 | -234 |  |
| (0.351, 2.663] | 109 | 40% (32-50) | -1.23 | -2.70 | -294 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.386] | 109 | 43% (34-52) | -0.55 | -1.89 | -206 |  |
| (2.386, 3.618] | 109 | 53% (44-62) | +0.76 | -0.63 | -69 |  |
| (3.618, 19.488] | 109 | 36% (27-45) | -2.06 | -3.41 | -372 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 109 | 47% (38-56) | +0.04 | -0.69 | -75 |  |
| (0.104, 0.167] | 109 | 45% (36-54) | -0.97 | -2.13 | -232 |  |
| (0.167, 0.76] | 109 | 40% (32-50) | -0.92 | -3.11 | -339 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.887] | 67 | 43% (32-55) | -1.31 | -2.09 | -140 |  |
| (-0.887, 0.644] | 67 | 52% (40-64) | -0.11 | -0.67 | -45 |  |
| (0.644, 14.989] | 67 | 58% (46-69) | -0.12 | -0.84 | -56 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.547] | 70 | 49% (37-60) | -0.57 | -1.19 | -83 |  |
| (0.547, 0.884] | 69 | 55% (43-66) | -0.52 | -1.23 | -85 |  |
| (0.884, 3.799] | 69 | 49% (38-61) | -0.67 | -1.44 | -100 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.952] | 70 | 51% (40-63) | -0.96 | -1.53 | -107 |  |
| (0.952, 1.669] | 69 | 48% (36-59) | -0.76 | -1.46 | -100 |  |
| (1.669, 9.058] | 69 | 54% (42-65) | -0.04 | -0.86 | -60 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 70 | 44% (33-56) | -0.91 | -1.49 | -105 |  |
| (0.409, 0.624] | 69 | 62% (51-73) | -0.03 | -0.72 | -50 | ▲ |
| (0.624, 4.001] | 69 | 46% (35-58) | -0.82 | -1.64 | -113 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.15%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 43%
- Exit mix: trail_stop 141, stop 140, time_stop 36, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 109 | 34% | 33% | 28% |
| (0.104, 0.167] | 109 | 47% | 47% | 3% |
| (0.167, 0.76] | 109 | 48% | 50% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
