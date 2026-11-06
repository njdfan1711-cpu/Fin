# Scalp signal analysis (trail exits)

_246 tagged trades, 27 trading days (2026-10-01 to 2026-11-06). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 246 | 42% (36-48) | -0.63 | -2.22 | -546 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 43 | +2 | +0.05 | 203 | -548 | -2.70 | -2 |
| skip first 30 min | 2 | -3 | -1.70 | 244 | -543 | -2.22 | +3 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 147 | -278 | -1.89 | +268 |
| skip when SPY is below its VWAP | 110 | -315 | -2.87 | 136 | -231 | -1.70 | +315 |
| skip when SPY fell over the last 15 min | 90 | -191 | -2.13 | 156 | -355 | -2.27 | +191 |
| skip over-extended (30-min run in top quarter, > 0.53%) | 61 | -225 | -3.68 | 185 | -322 | -1.74 | +225 |
| skip stock not beating SPY over 15 min | 39 | -82 | -2.10 | 207 | -464 | -2.24 | +82 |
| skip afternoon entries (2:00-3:45 PM) | 53 | -222 | -4.19 | 193 | -324 | -1.68 | +222 |
| skip volume spikes above 5x average | 48 | -167 | -3.48 | 198 | -379 | -1.91 | +167 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 220 | -505 | -2.30 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.69%) | 32 | -49 | -1.52 | 214 | -498 | -2.33 | +49 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 119 | -410 | -3.45 | 127 | -136 | -1.07 | +410 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 100 | 39% (30-49) | -1.00 | -2.34 | -234 |  |
| 240-375 | 69 | 38% (27-49) | -1.77 | -3.62 | -250 |  |
| 375-390 | 43 | 49% (35-63) | +1.65 | +0.05 | +2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 81 | 48% (38-59) | +0.58 | -1.08 | -87 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 110 | 37% (29-47) | -1.18 | -2.87 | -315 |  |
| above VWAP | 136 | 46% (37-54) | -0.18 | -1.70 | -231 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.135] | 82 | 40% (30-51) | -0.05 | -1.31 | -107 |  |
| (0.135, 0.383] | 82 | 52% (42-63) | -0.21 | -1.81 | -148 |  |
| (0.383, 5.591] | 82 | 33% (24-44) | -1.62 | -3.55 | -291 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.11] | 82 | 50% (39-61) | +0.61 | -0.59 | -49 |  |
| (0.11, 0.44] | 81 | 41% (31-52) | -0.94 | -2.84 | -230 |  |
| (0.44, 4.846] | 81 | 35% (25-45) | -1.56 | -3.26 | -264 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.389] | 82 | 46% (36-57) | -0.71 | -2.53 | -208 |  |
| (-0.389, 0.387] | 82 | 45% (35-56) | +0.45 | -0.68 | -56 |  |
| (0.387, 4.204] | 82 | 34% (25-45) | -1.63 | -3.45 | -283 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0561] | 82 | 43% (33-53) | -0.94 | -2.35 | -193 |  |
| (0.0561, 0.127] | 83 | 46% (35-56) | +0.35 | -1.13 | -94 |  |
| (0.127, 0.924] | 81 | 37% (27-48) | -1.31 | -3.21 | -260 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 82 | 45% (35-56) | +0.30 | -0.80 | -65 |  |
| (0.212, 0.334] | 82 | 44% (34-55) | -0.80 | -2.64 | -216 |  |
| (0.334, 2.663] | 82 | 37% (27-47) | -1.38 | -3.23 | -265 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.344] | 82 | 43% (33-53) | -0.45 | -1.95 | -160 |  |
| (2.344, 3.639] | 82 | 48% (37-58) | +0.48 | -1.16 | -95 |  |
| (3.639, 18.762] | 82 | 35% (26-46) | -1.91 | -3.55 | -291 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 82 | 49% (38-59) | +0.39 | -0.38 | -31 |  |
| (0.102, 0.157] | 82 | 41% (31-52) | -1.14 | -2.29 | -188 |  |
| (0.157, 0.76] | 82 | 35% (26-46) | -1.14 | -3.99 | -328 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.008] | 40 | 42% (29-58) | -1.40 | -2.22 | -89 |  |
| (-1.008, 0.589] | 40 | 55% (40-69) | +0.17 | -0.40 | -16 |  |
| (0.589, 7.522] | 40 | 58% (42-71) | -0.16 | -0.89 | -36 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 43 | 49% (35-63) | -0.52 | -1.17 | -50 |  |
| (0.533, 0.832] | 42 | 55% (40-69) | -0.83 | -1.52 | -64 |  |
| (0.832, 3.799] | 42 | 50% (36-64) | -0.42 | -1.27 | -53 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.841] | 43 | 49% (35-63) | -1.23 | -1.78 | -77 |  |
| (0.841, 1.467] | 42 | 55% (40-69) | -0.07 | -0.79 | -33 |  |
| (1.467, 9.058] | 42 | 50% (36-64) | -0.45 | -1.36 | -57 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.377] | 43 | 51% (37-65) | -0.12 | -0.68 | -29 |  |
| (0.377, 0.6] | 42 | 60% (44-73) | -0.54 | -1.28 | -54 | ▲ |
| (0.6, 4.001] | 42 | 43% (29-58) | -1.12 | -2.01 | -84 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 107, trail_stop 103, time_stop 29, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 82 | 30% | 33% | 30% |
| (0.102, 0.157] | 82 | 50% | 46% | 2% |
| (0.157, 0.76] | 82 | 50% | 46% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
