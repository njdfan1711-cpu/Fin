# Scalp signal analysis (fixed exits)

_243 tagged trades, 27 trading days (2026-10-01 to 2026-11-06). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 243 | 41% (35-47) | +0.26 | -1.34 | -326 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 43 | +3 | +0.07 | 200 | -329 | -1.64 | -3 |
| skip first 30 min | 2 | -8 | -4.06 | 241 | -318 | -1.32 | +8 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 144 | -227 | -1.57 | +99 |
| skip when SPY is below its VWAP | 110 | -167 | -1.52 | 133 | -159 | -1.19 | +167 |
| skip when SPY fell over the last 15 min | 88 | -119 | -1.35 | 155 | -207 | -1.33 | +119 |
| skip over-extended (30-min run in top quarter, > 0.52%) | 60 | -159 | -2.66 | 183 | -167 | -0.91 | +159 |
| skip stock not beating SPY over 15 min | 38 | -30 | -0.78 | 205 | -296 | -1.44 | +30 |
| skip afternoon entries (2:00-3:45 PM) | 53 | -218 | -4.12 | 190 | -107 | -0.57 | +218 |
| skip volume spikes above 5x average | 46 | -120 | -2.61 | 197 | -206 | -1.04 | +120 |
| skip when the stop is inside normal noise (range > stop) | 24 | +6 | +0.26 | 219 | -332 | -1.52 | -6 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.69%) | 31 | +2 | +0.05 | 212 | -327 | -1.54 | -2 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 118 | -302 | -2.56 | 125 | -23 | -0.19 | +302 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 53% (37-69) | +2.10 | +0.32 | +11 |  |
| 60-240 | 97 | 40% (31-50) | +0.20 | -1.17 | -114 |  |
| 240-375 | 69 | 30% (21-42) | -1.42 | -3.27 | -226 |  |
| 375-390 | 43 | 51% (37-65) | +1.67 | +0.07 | +3 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 66 | 33% (23-45) | -0.38 | -1.70 | -112 |  |
| > 0.2 | 78 | 44% (33-55) | +0.23 | -1.47 | -114 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 110 | 42% (33-51) | +0.16 | -1.52 | -167 |  |
| above VWAP | 133 | 41% (33-49) | +0.35 | -1.19 | -159 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.135] | 81 | 42% (32-53) | +0.38 | -0.88 | -72 |  |
| (0.135, 0.383] | 81 | 46% (35-56) | +0.54 | -1.07 | -87 |  |
| (0.383, 5.591] | 81 | 36% (26-47) | -0.12 | -2.06 | -167 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.11] | 81 | 47% (36-58) | +0.85 | -0.37 | -30 |  |
| (0.11, 0.44] | 80 | 41% (31-52) | +0.57 | -1.34 | -107 |  |
| (0.44, 4.846] | 80 | 36% (27-47) | -0.54 | -2.25 | -180 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.389] | 81 | 47% (36-58) | +0.93 | -0.91 | -73 |  |
| (-0.389, 0.387] | 81 | 43% (33-54) | +0.72 | -0.42 | -34 |  |
| (0.387, 4.204] | 81 | 33% (24-44) | -0.86 | -2.69 | -218 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0559] | 81 | 41% (31-52) | -0.09 | -1.51 | -122 |  |
| (0.0559, 0.127] | 82 | 46% (36-57) | +0.71 | -0.79 | -64 |  |
| (0.127, 0.924] | 80 | 36% (27-47) | +0.17 | -1.74 | -139 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 81 | 43% (33-54) | +0.28 | -0.83 | -67 |  |
| (0.212, 0.334] | 81 | 43% (33-54) | +0.55 | -1.30 | -105 |  |
| (0.334, 2.663] | 81 | 37% (27-48) | -0.04 | -1.89 | -153 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.331] | 81 | 37% (27-48) | -0.01 | -1.52 | -123 |  |
| (2.331, 3.634] | 81 | 51% (40-61) | +1.20 | -0.44 | -35 |  |
| (3.634, 18.762] | 81 | 36% (26-47) | -0.40 | -2.06 | -167 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.101] | 81 | 47% (36-58) | +0.53 | -0.24 | -20 |  |
| (0.101, 0.155] | 81 | 37% (27-48) | -0.16 | -1.32 | -107 |  |
| (0.155, 0.76] | 81 | 40% (30-50) | +0.42 | -2.46 | -199 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.172] | 39 | 36% (23-52) | -0.54 | -1.38 | -54 |  |
| (-1.172, 0.459] | 39 | 46% (32-61) | +0.84 | +0.27 | +10 |  |
| (0.459, 5.599] | 39 | 54% (39-68) | +1.92 | +1.17 | +46 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 43 | 44% (30-59) | +0.12 | -0.52 | -22 |  |
| (0.533, 0.781] | 40 | 42% (29-58) | +0.19 | -0.53 | -21 |  |
| (0.781, 3.799] | 41 | 46% (32-61) | +1.36 | +0.52 | +21 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.841] | 42 | 43% (29-58) | +0.09 | -0.47 | -20 |  |
| (0.841, 1.467] | 41 | 46% (32-61) | +1.00 | +0.28 | +11 |  |
| (1.467, 9.058] | 41 | 44% (30-59) | +0.58 | -0.33 | -14 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.374] | 42 | 45% (31-60) | +0.46 | -0.09 | -4 |  |
| (0.374, 0.6] | 41 | 46% (32-61) | +0.74 | -0.02 | -1 |  |
| (0.6, 4.001] | 41 | 41% (28-57) | +0.46 | -0.42 | -17 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.18%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 116, target 64, time_stop 51, eod 12

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.101] | 81 | 33% | 17% | 43% |
| (0.101, 0.155] | 81 | 56% | 27% | 11% |
| (0.155, 0.76] | 81 | 54% | 35% | 9% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
