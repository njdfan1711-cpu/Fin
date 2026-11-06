# Scalp signal analysis (fixed exits)

_246 tagged trades, 27 trading days (2026-10-01 to 2026-11-06). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 246 | 41% (35-47) | +0.25 | -1.34 | -329 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 43 | +3 | +0.07 | 203 | -332 | -1.64 | -3 |
| skip first 30 min | 2 | -8 | -4.06 | 244 | -321 | -1.32 | +8 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 147 | -230 | -1.57 | +99 |
| skip when SPY is below its VWAP | 110 | -167 | -1.52 | 136 | -162 | -1.19 | +167 |
| skip when SPY fell over the last 15 min | 89 | -125 | -1.41 | 157 | -204 | -1.30 | +125 |
| skip over-extended (30-min run in top quarter, > 0.53%) | 61 | -166 | -2.72 | 185 | -164 | -0.88 | +166 |
| skip stock not beating SPY over 15 min | 39 | -36 | -0.92 | 207 | -293 | -1.42 | +36 |
| skip afternoon entries (2:00-3:45 PM) | 53 | -218 | -4.12 | 193 | -111 | -0.58 | +218 |
| skip volume spikes above 5x average | 48 | -117 | -2.44 | 198 | -212 | -1.07 | +117 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 220 | -323 | -1.47 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.69%) | 32 | -5 | -0.15 | 214 | -325 | -1.52 | +5 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 119 | -309 | -2.60 | 127 | -21 | -0.16 | +309 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 53% (37-69) | +2.10 | +0.32 | +11 |  |
| 60-240 | 100 | 40% (31-50) | +0.17 | -1.17 | -117 |  |
| 240-375 | 69 | 30% (21-42) | -1.42 | -3.27 | -226 |  |
| 375-390 | 43 | 51% (37-65) | +1.67 | +0.07 | +3 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 66 | 33% (23-45) | -0.38 | -1.70 | -112 |  |
| > 0.2 | 81 | 43% (33-54) | +0.19 | -1.46 | -118 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 110 | 42% (33-51) | +0.16 | -1.52 | -167 |  |
| above VWAP | 136 | 40% (33-49) | +0.32 | -1.19 | -162 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.135] | 82 | 41% (31-52) | +0.30 | -0.95 | -78 |  |
| (0.135, 0.383] | 82 | 46% (36-57) | +0.65 | -0.95 | -78 |  |
| (0.383, 5.591] | 82 | 35% (26-46) | -0.19 | -2.12 | -174 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.11] | 82 | 48% (37-58) | +0.95 | -0.26 | -21 |  |
| (0.11, 0.44] | 81 | 41% (31-52) | +0.50 | -1.40 | -114 |  |
| (0.44, 4.846] | 81 | 36% (26-47) | -0.60 | -2.31 | -187 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.389] | 82 | 46% (36-57) | +0.85 | -0.98 | -80 |  |
| (-0.389, 0.387] | 82 | 44% (34-55) | +0.83 | -0.31 | -25 |  |
| (0.387, 4.204] | 82 | 33% (24-44) | -0.92 | -2.74 | -224 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0561] | 82 | 41% (31-52) | -0.06 | -1.46 | -120 |  |
| (0.0561, 0.127] | 83 | 46% (35-56) | +0.71 | -0.77 | -64 |  |
| (0.127, 0.924] | 81 | 36% (26-47) | +0.10 | -1.80 | -145 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 82 | 44% (34-55) | +0.39 | -0.71 | -58 |  |
| (0.212, 0.334] | 82 | 43% (33-53) | +0.48 | -1.36 | -112 |  |
| (0.334, 2.663] | 82 | 37% (27-47) | -0.11 | -1.95 | -160 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.344] | 82 | 38% (28-49) | +0.02 | -1.48 | -121 |  |
| (2.344, 3.639] | 82 | 50% (39-61) | +1.12 | -0.51 | -42 |  |
| (3.639, 18.762] | 82 | 35% (26-46) | -0.38 | -2.03 | -166 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 82 | 48% (37-58) | +0.61 | -0.17 | -14 |  |
| (0.102, 0.157] | 82 | 37% (27-47) | -0.24 | -1.39 | -114 |  |
| (0.157, 0.76] | 82 | 39% (29-50) | +0.39 | -2.46 | -202 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.008] | 40 | 35% (22-50) | -0.54 | -1.37 | -55 |  |
| (-1.008, 0.589] | 40 | 50% (35-65) | +1.07 | +0.50 | +20 |  |
| (0.589, 7.522] | 40 | 50% (35-65) | +1.57 | +0.84 | +34 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 43 | 44% (30-59) | +0.12 | -0.52 | -22 |  |
| (0.533, 0.832] | 42 | 45% (31-60) | +0.64 | -0.05 | -2 |  |
| (0.832, 3.799] | 42 | 43% (29-58) | +0.82 | -0.03 | -1 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.841] | 43 | 44% (30-59) | +0.30 | -0.25 | -11 |  |
| (0.841, 1.467] | 42 | 45% (31-60) | +0.84 | +0.12 | +5 |  |
| (1.467, 9.058] | 42 | 43% (29-58) | +0.43 | -0.48 | -20 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.377] | 43 | 47% (33-61) | +0.62 | +0.06 | +3 |  |
| (0.377, 0.6] | 42 | 45% (31-60) | +0.63 | -0.11 | -5 |  |
| (0.6, 4.001] | 42 | 40% (27-56) | +0.32 | -0.57 | -24 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 118, target 65, time_stop 51, eod 12

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 82 | 33% | 17% | 43% |
| (0.102, 0.157] | 82 | 56% | 27% | 12% |
| (0.157, 0.76] | 82 | 55% | 35% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
