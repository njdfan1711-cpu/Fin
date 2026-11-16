# Scalp signal analysis (trail exits)

_278 tagged trades, 32 trading days (2026-10-01 to 2026-11-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 278 | 42% (36-48) | -0.72 | -2.21 | -616 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 49 | -19 | -0.39 | 229 | -596 | -2.60 | +19 |
| skip first 30 min | 3 | -10 | -3.32 | 275 | -606 | -2.20 | +10 |
| skip when SPY is down on the day | 109 | -292 | -2.68 | 169 | -323 | -1.91 | +292 |
| skip when SPY is below its VWAP | 120 | -362 | -3.01 | 158 | -254 | -1.61 | +362 |
| skip when SPY fell over the last 15 min | 101 | -227 | -2.25 | 177 | -388 | -2.19 | +227 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 69 | -240 | -3.47 | 209 | -376 | -1.80 | +240 |
| skip stock not beating SPY over 15 min | 45 | -103 | -2.30 | 233 | -512 | -2.20 | +103 |
| skip afternoon entries (2:00-3:45 PM) | 62 | -230 | -3.71 | 216 | -386 | -1.79 | +230 |
| skip volume spikes above 5x average | 57 | -200 | -3.50 | 221 | -416 | -1.88 | +200 |
| skip when the stop is inside normal noise (range > stop) | 30 | -58 | -1.93 | 248 | -558 | -2.25 | +58 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.69%) | 40 | -79 | -1.97 | 238 | -537 | -2.26 | +79 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 130 | -425 | -3.27 | 148 | -191 | -1.29 | +425 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 49% (33-64) | -0.33 | -2.03 | -75 |  |
| 60-240 | 113 | 40% (31-49) | -1.06 | -2.33 | -263 |  |
| 240-375 | 79 | 39% (29-50) | -1.55 | -3.27 | -258 |  |
| 375-390 | 49 | 45% (32-59) | +1.10 | -0.39 | -19 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 58 | 43% (31-56) | -0.67 | -1.87 | -108 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 68 | 35% (25-47) | -1.54 | -2.86 | -195 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 120 | 36% (28-45) | -1.42 | -3.01 | -362 |  |
| above VWAP | 158 | 46% (39-54) | -0.19 | -1.61 | -254 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 93 | 40% (30-50) | -0.32 | -1.52 | -141 |  |
| (0.133, 0.374] | 92 | 51% (41-61) | -0.24 | -1.75 | -161 |  |
| (0.374, 5.591] | 93 | 34% (26-45) | -1.59 | -3.37 | -313 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.118] | 92 | 47% (37-57) | +0.20 | -0.97 | -90 |  |
| (0.118, 0.442] | 91 | 43% (33-53) | -0.82 | -2.66 | -242 |  |
| (0.442, 4.846] | 92 | 36% (27-46) | -1.47 | -2.98 | -274 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.395] | 93 | 46% (36-56) | -0.64 | -2.36 | -219 |  |
| (-0.395, 0.398] | 92 | 46% (36-56) | +0.26 | -0.83 | -76 |  |
| (0.398, 9.926] | 93 | 33% (25-43) | -1.77 | -3.45 | -320 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 93 | 43% (33-53) | -0.95 | -2.27 | -212 |  |
| (0.0559, 0.127] | 93 | 45% (35-55) | +0.11 | -1.28 | -119 |  |
| (0.127, 0.924] | 92 | 37% (28-47) | -1.33 | -3.10 | -285 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 93 | 45% (35-55) | +0.15 | -0.90 | -84 |  |
| (0.217, 0.342] | 92 | 46% (36-56) | -0.68 | -2.40 | -221 |  |
| (0.342, 2.663] | 93 | 34% (26-45) | -1.64 | -3.34 | -311 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.36] | 93 | 41% (31-51) | -0.61 | -2.06 | -192 |  |
| (2.36, 3.625] | 92 | 49% (39-59) | +0.48 | -1.04 | -95 |  |
| (3.625, 19.488] | 93 | 35% (27-46) | -2.02 | -3.53 | -329 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 93 | 48% (38-58) | +0.32 | -0.45 | -42 |  |
| (0.104, 0.165] | 93 | 41% (31-51) | -1.24 | -2.47 | -229 |  |
| (0.165, 0.76] | 92 | 36% (27-46) | -1.24 | -3.74 | -344 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.193] | 51 | 41% (29-55) | -1.41 | -2.24 | -114 |  |
| (-1.193, 0.616] | 50 | 52% (39-65) | -0.01 | -0.61 | -30 |  |
| (0.616, 7.522] | 51 | 55% (41-68) | -0.56 | -1.29 | -66 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.544] | 53 | 51% (38-64) | -0.27 | -0.92 | -49 |  |
| (0.544, 0.837] | 54 | 52% (39-65) | -1.05 | -1.78 | -96 |  |
| (0.837, 3.799] | 52 | 44% (32-58) | -0.95 | -1.77 | -92 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.876] | 53 | 47% (34-60) | -1.36 | -1.95 | -103 |  |
| (0.876, 1.556] | 53 | 53% (40-66) | -0.33 | -1.05 | -56 |  |
| (1.556, 9.058] | 53 | 47% (34-60) | -0.58 | -1.46 | -77 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.384] | 53 | 45% (33-59) | -0.77 | -1.36 | -72 |  |
| (0.384, 0.605] | 53 | 62% (49-74) | -0.09 | -0.84 | -45 | ▲ |
| (0.605, 4.001] | 53 | 40% (28-53) | -1.41 | -2.26 | -120 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 122, trail_stop 115, time_stop 33, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 93 | 31% | 32% | 31% |
| (0.104, 0.165] | 93 | 51% | 45% | 2% |
| (0.165, 0.76] | 92 | 50% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
