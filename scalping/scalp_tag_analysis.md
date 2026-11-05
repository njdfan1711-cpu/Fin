# Scalp signal analysis (fixed exits)

_232 tagged trades, 25 trading days (2026-10-01 to 2026-11-04). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 232 | 40% (34-46) | +0.04 | -1.61 | -373 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 40 | -2 | -0.05 | 192 | -372 | -1.94 | +2 |
| skip first 30 min | 2 | -8 | -4.06 | 230 | -365 | -1.59 | +8 |
| skip when SPY is down on the day | 89 | -137 | -1.54 | 143 | -236 | -1.65 | +137 |
| skip when SPY is below its VWAP | 99 | -215 | -2.17 | 133 | -159 | -1.19 | +215 |
| skip when SPY fell over the last 15 min | 84 | -126 | -1.50 | 148 | -247 | -1.67 | +126 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 58 | -192 | -3.31 | 174 | -181 | -1.04 | +192 |
| skip stock not beating SPY over 15 min | 37 | -39 | -1.06 | 195 | -334 | -1.71 | +39 |
| skip afternoon entries (2:00-3:45 PM) | 49 | -224 | -4.56 | 183 | -150 | -0.82 | +224 |
| skip volume spikes above 5x average | 43 | -148 | -3.44 | 189 | -225 | -1.19 | +148 |
| skip when the stop is inside normal noise (range > stop) | 17 | -27 | -1.60 | 215 | -346 | -1.61 | +27 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.67%) | 28 | -35 | -1.25 | 204 | -338 | -1.66 | +35 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 115 | -329 | -2.86 | 117 | -44 | -0.38 | +329 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 53% (37-69) | +2.10 | +0.32 | +11 |  |
| 60-240 | 93 | 38% (28-48) | -0.22 | -1.63 | -151 |  |
| 240-375 | 65 | 29% (20-41) | -1.65 | -3.56 | -231 |  |
| 375-390 | 40 | 50% (35-65) | +1.62 | -0.05 | -2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 42% (28-58) | +0.35 | -1.04 | -40 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 66 | 33% (23-45) | -0.38 | -1.70 | -112 |  |
| > 0.2 | 77 | 43% (32-54) | +0.10 | -1.61 | -124 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 99 | 38% (29-48) | -0.38 | -2.17 | -215 |  |
| above VWAP | 133 | 41% (33-49) | +0.35 | -1.19 | -159 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 78 | 40% (30-51) | -0.01 | -1.40 | -109 |  |
| (0.136, 0.377] | 77 | 45% (35-57) | +0.47 | -1.08 | -83 |  |
| (0.377, 2.096] | 77 | 34% (24-45) | -0.35 | -2.35 | -181 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.108] | 77 | 45% (35-57) | +0.68 | -0.58 | -45 |  |
| (0.108, 0.418] | 76 | 41% (30-52) | +0.31 | -1.63 | -124 |  |
| (0.418, 2.453] | 77 | 34% (24-45) | -0.77 | -2.56 | -197 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.348] | 78 | 42% (32-53) | +0.27 | -1.60 | -125 |  |
| (-0.348, 0.401] | 77 | 45% (35-57) | +1.06 | -0.11 | -8 |  |
| (0.401, 4.204] | 77 | 31% (22-42) | -1.22 | -3.12 | -241 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0558] | 78 | 41% (31-52) | -0.08 | -1.53 | -120 |  |
| (0.0558, 0.124] | 77 | 45% (35-57) | +0.71 | -0.84 | -65 |  |
| (0.124, 0.924] | 77 | 32% (23-44) | -0.52 | -2.45 | -189 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 78 | 44% (33-55) | +0.24 | -0.89 | -69 |  |
| (0.211, 0.326] | 77 | 40% (30-51) | +0.23 | -1.57 | -121 |  |
| (0.326, 2.663] | 77 | 35% (25-46) | -0.36 | -2.38 | -184 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.337] | 78 | 37% (27-48) | -0.10 | -1.64 | -128 |  |
| (2.337, 3.632] | 77 | 49% (38-60) | +1.15 | -0.54 | -41 |  |
| (3.632, 18.762] | 77 | 32% (23-44) | -0.94 | -2.65 | -204 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0986] | 78 | 47% (37-58) | +0.56 | -0.19 | -14 |  |
| (0.0986, 0.15] | 77 | 36% (27-48) | -0.25 | -1.41 | -109 |  |
| (0.15, 0.392] | 77 | 35% (25-46) | -0.21 | -3.25 | -250 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.913] | 36 | 28% (16-44) | -1.90 | -2.73 | -98 |  |
| (-0.913, 0.452] | 35 | 49% (33-64) | +1.17 | +0.62 | +22 |  |
| (0.452, 5.599] | 35 | 51% (36-67) | +1.65 | +0.90 | +32 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.518] | 39 | 46% (32-61) | +0.48 | -0.13 | -5 |  |
| (0.518, 0.748] | 36 | 39% (25-55) | -0.32 | -1.09 | -39 |  |
| (0.748, 1.75] | 38 | 39% (26-55) | +0.15 | -0.67 | -25 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.8] | 38 | 42% (28-58) | -0.02 | -0.55 | -21 |  |
| (0.8, 1.235] | 37 | 43% (29-59) | +0.45 | -0.28 | -10 |  |
| (1.235, 5.866] | 38 | 39% (26-55) | -0.07 | -1.01 | -38 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.354] | 38 | 42% (28-58) | +0.17 | -0.40 | -15 |  |
| (0.354, 0.564] | 37 | 49% (33-64) | +0.80 | +0.05 | +2 |  |
| (0.564, 2.726] | 38 | 34% (21-50) | -0.60 | -1.49 | -56 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.19%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 113, target 57, time_stop 51, eod 11

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0986] | 78 | 33% | 17% | 44% |
| (0.0986, 0.15] | 77 | 56% | 27% | 12% |
| (0.15, 0.392] | 77 | 57% | 30% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
