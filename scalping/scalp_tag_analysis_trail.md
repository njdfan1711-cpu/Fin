# Scalp signal analysis (trail exits)

_243 tagged trades, 27 trading days (2026-10-01 to 2026-11-06). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 243 | 42% (36-48) | -0.60 | -2.21 | -536 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 43 | +2 | +0.05 | 200 | -538 | -2.69 | -2 |
| skip first 30 min | 2 | -3 | -1.70 | 241 | -533 | -2.21 | +3 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 144 | -268 | -1.86 | +268 |
| skip when SPY is below its VWAP | 110 | -315 | -2.87 | 133 | -221 | -1.66 | +315 |
| skip when SPY fell over the last 15 min | 89 | -185 | -2.08 | 154 | -351 | -2.28 | +185 |
| skip over-extended (30-min run in top quarter, > 0.52%) | 60 | -218 | -3.63 | 183 | -318 | -1.74 | +218 |
| skip stock not beating SPY over 15 min | 38 | -76 | -1.99 | 205 | -461 | -2.25 | +76 |
| skip afternoon entries (2:00-3:45 PM) | 53 | -222 | -4.19 | 190 | -314 | -1.66 | +222 |
| skip volume spikes above 5x average | 46 | -164 | -3.56 | 197 | -372 | -1.89 | +164 |
| skip when the stop is inside normal noise (range > stop) | 24 | -28 | -1.17 | 219 | -508 | -2.32 | +28 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.69%) | 31 | -42 | -1.36 | 212 | -494 | -2.33 | +42 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 118 | -403 | -3.42 | 125 | -133 | -1.06 | +403 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 97 | 39% (30-49) | -0.94 | -2.31 | -224 |  |
| 240-375 | 69 | 38% (27-49) | -1.77 | -3.62 | -250 |  |
| 375-390 | 43 | 49% (35-63) | +1.65 | +0.05 | +2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 78 | 49% (38-60) | +0.70 | -0.99 | -77 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 110 | 37% (29-47) | -1.18 | -2.87 | -315 |  |
| above VWAP | 133 | 46% (38-54) | -0.12 | -1.66 | -221 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.135] | 81 | 41% (31-52) | +0.02 | -1.24 | -101 |  |
| (0.135, 0.383] | 81 | 52% (41-62) | -0.25 | -1.87 | -151 |  |
| (0.383, 5.591] | 81 | 33% (24-44) | -1.57 | -3.51 | -284 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.11] | 81 | 49% (39-60) | +0.58 | -0.64 | -52 |  |
| (0.11, 0.44] | 80 | 41% (31-52) | -0.88 | -2.79 | -224 |  |
| (0.44, 4.846] | 80 | 35% (25-46) | -1.51 | -3.22 | -258 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.389] | 81 | 47% (36-58) | -0.65 | -2.48 | -201 |  |
| (-0.389, 0.387] | 81 | 44% (34-55) | +0.42 | -0.72 | -59 |  |
| (0.387, 4.204] | 81 | 35% (25-45) | -1.58 | -3.41 | -277 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0559] | 81 | 42% (32-53) | -0.99 | -2.41 | -195 |  |
| (0.0559, 0.127] | 82 | 46% (36-57) | +0.42 | -1.07 | -88 |  |
| (0.127, 0.924] | 80 | 38% (28-48) | -1.26 | -3.17 | -253 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 81 | 44% (34-55) | +0.27 | -0.84 | -68 |  |
| (0.212, 0.334] | 81 | 44% (34-55) | -0.74 | -2.59 | -210 |  |
| (0.334, 2.663] | 81 | 37% (27-48) | -1.33 | -3.19 | -258 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.331] | 81 | 42% (32-53) | -0.49 | -2.00 | -162 |  |
| (2.331, 3.634] | 81 | 48% (38-59) | +0.55 | -1.09 | -88 |  |
| (3.634, 18.762] | 81 | 36% (26-47) | -1.87 | -3.53 | -286 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.101] | 81 | 48% (38-59) | +0.38 | -0.40 | -32 |  |
| (0.101, 0.155] | 81 | 42% (32-53) | -1.09 | -2.25 | -182 |  |
| (0.155, 0.76] | 81 | 36% (26-47) | -1.09 | -3.98 | -322 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.172] | 39 | 44% (29-59) | -1.42 | -2.26 | -88 |  |
| (-1.172, 0.459] | 39 | 51% (36-66) | -0.09 | -0.65 | -26 |  |
| (0.459, 5.599] | 39 | 62% (46-75) | +0.30 | -0.44 | -17 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 43 | 49% (35-63) | -0.52 | -1.17 | -50 |  |
| (0.533, 0.781] | 40 | 52% (37-67) | -0.97 | -1.69 | -68 |  |
| (0.781, 3.799] | 41 | 54% (39-68) | -0.13 | -0.97 | -40 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.841] | 42 | 48% (33-62) | -1.33 | -1.90 | -80 |  |
| (0.841, 1.467] | 41 | 56% (41-70) | +0.06 | -0.66 | -27 |  |
| (1.467, 9.058] | 41 | 51% (36-66) | -0.33 | -1.24 | -51 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.374] | 42 | 50% (36-64) | -0.30 | -0.86 | -36 |  |
| (0.374, 0.6] | 41 | 61% (46-74) | -0.31 | -1.07 | -44 | ▲ |
| (0.6, 4.001] | 41 | 44% (30-59) | -1.01 | -1.90 | -78 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 105, trail_stop 102, time_stop 29, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.101] | 81 | 31% | 32% | 31% |
| (0.101, 0.155] | 81 | 49% | 47% | 2% |
| (0.155, 0.76] | 81 | 49% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
