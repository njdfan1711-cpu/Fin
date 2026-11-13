# Scalp signal analysis (trail exits)

_269 tagged trades, 32 trading days (2026-10-01 to 2026-11-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 269 | 42% (36-48) | -0.71 | -2.22 | -598 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 48 | -19 | -0.40 | 221 | -579 | -2.62 | +19 |
| skip first 30 min | 3 | -10 | -3.32 | 266 | -588 | -2.21 | +10 |
| skip when SPY is down on the day | 100 | -275 | -2.75 | 169 | -323 | -1.91 | +275 |
| skip when SPY is below its VWAP | 117 | -351 | -3.00 | 152 | -247 | -1.63 | +351 |
| skip when SPY fell over the last 15 min | 100 | -230 | -2.30 | 169 | -368 | -2.18 | +230 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 67 | -240 | -3.59 | 202 | -358 | -1.77 | +240 |
| skip stock not beating SPY over 15 min | 43 | -99 | -2.30 | 226 | -499 | -2.21 | +99 |
| skip afternoon entries (2:00-3:45 PM) | 60 | -227 | -3.79 | 209 | -371 | -1.77 | +227 |
| skip volume spikes above 5x average | 54 | -189 | -3.50 | 215 | -409 | -1.90 | +189 |
| skip when the stop is inside normal noise (range > stop) | 27 | -47 | -1.74 | 242 | -551 | -2.28 | +47 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 38 | -70 | -1.84 | 231 | -528 | -2.29 | +70 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -416 | -3.35 | 145 | -183 | -1.26 | +416 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 49% (33-64) | -0.33 | -2.03 | -75 |  |
| 60-240 | 108 | 40% (31-49) | -1.01 | -2.31 | -249 |  |
| 240-375 | 76 | 39% (29-51) | -1.62 | -3.36 | -255 |  |
| 375-390 | 48 | 46% (33-60) | +1.11 | -0.40 | -19 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 49 | 45% (32-59) | -0.61 | -1.86 | -91 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 68 | 35% (25-47) | -1.54 | -2.86 | -195 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 117 | 36% (28-45) | -1.38 | -3.00 | -351 |  |
| above VWAP | 152 | 47% (39-55) | -0.20 | -1.63 | -247 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 90 | 40% (30-50) | -0.33 | -1.53 | -138 |  |
| (0.133, 0.38] | 89 | 53% (43-63) | -0.16 | -1.68 | -150 | ▲ |
| (0.38, 5.591] | 90 | 33% (24-44) | -1.64 | -3.45 | -310 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.118] | 89 | 48% (38-59) | +0.32 | -0.86 | -76 |  |
| (0.118, 0.442] | 88 | 42% (32-52) | -0.90 | -2.77 | -244 |  |
| (0.442, 4.846] | 89 | 36% (27-46) | -1.49 | -3.01 | -268 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 90 | 46% (36-56) | -0.80 | -2.50 | -225 |  |
| (-0.367, 0.418] | 89 | 48% (38-59) | +0.57 | -0.54 | -48 |  |
| (0.418, 9.926] | 90 | 32% (23-42) | -1.90 | -3.61 | -325 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 90 | 42% (33-53) | -1.00 | -2.34 | -211 |  |
| (0.0559, 0.127] | 89 | 45% (35-55) | +0.18 | -1.26 | -112 |  |
| (0.127, 0.924] | 90 | 39% (29-49) | -1.30 | -3.06 | -276 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.216] | 90 | 44% (35-55) | +0.07 | -0.99 | -89 |  |
| (0.216, 0.339] | 89 | 46% (36-56) | -0.64 | -2.39 | -213 |  |
| (0.339, 2.663] | 90 | 36% (26-46) | -1.57 | -3.29 | -296 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.36] | 90 | 42% (33-53) | -0.54 | -2.00 | -180 |  |
| (2.36, 3.625] | 89 | 48% (38-59) | +0.40 | -1.12 | -100 |  |
| (3.625, 19.488] | 90 | 36% (26-46) | -1.98 | -3.53 | -318 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 91 | 48% (38-58) | +0.31 | -0.46 | -42 |  |
| (0.104, 0.163] | 88 | 41% (31-51) | -1.26 | -2.45 | -215 |  |
| (0.163, 0.76] | 90 | 37% (27-47) | -1.20 | -3.79 | -341 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.956] | 48 | 42% (29-56) | -1.47 | -2.25 | -108 |  |
| (-0.956, 0.616] | 47 | 55% (41-69) | +0.20 | -0.40 | -19 |  |
| (0.616, 7.522] | 48 | 54% (40-67) | -0.64 | -1.37 | -66 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.538] | 50 | 50% (37-63) | -0.46 | -1.10 | -55 |  |
| (0.538, 0.837] | 52 | 54% (41-67) | -0.92 | -1.61 | -84 |  |
| (0.837, 3.799] | 48 | 46% (33-60) | -0.86 | -1.68 | -81 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.846] | 50 | 48% (35-61) | -1.30 | -1.89 | -95 |  |
| (0.846, 1.46] | 50 | 52% (39-65) | -0.39 | -1.09 | -54 |  |
| (1.46, 9.058] | 50 | 50% (37-63) | -0.55 | -1.41 | -70 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.38] | 50 | 46% (33-60) | -0.72 | -1.31 | -65 |  |
| (0.38, 0.594] | 50 | 60% (46-72) | -0.44 | -1.17 | -59 | ▲ |
| (0.594, 4.001] | 50 | 44% (31-58) | -1.07 | -1.91 | -95 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 119, trail_stop 111, time_stop 31, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 91 | 32% | 33% | 30% |
| (0.104, 0.163] | 88 | 51% | 44% | 2% |
| (0.163, 0.76] | 90 | 50% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
