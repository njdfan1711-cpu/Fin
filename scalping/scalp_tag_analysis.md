# Scalp signal analysis (fixed exits)

_225 tagged trades, 25 trading days (2026-10-01 to 2026-11-04). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 225 | 40% (33-46) | -0.03 | -1.70 | -382 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 38 | -8 | -0.21 | 187 | -374 | -2.00 | +8 |
| skip first 30 min | 2 | -8 | -4.06 | 223 | -374 | -1.68 | +8 |
| skip when SPY is down on the day | 89 | -137 | -1.54 | 136 | -245 | -1.80 | +137 |
| skip when SPY is below its VWAP | 98 | -212 | -2.16 | 127 | -170 | -1.34 | +212 |
| skip when SPY fell over the last 15 min | 81 | -137 | -1.70 | 144 | -245 | -1.70 | +137 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 56 | -190 | -3.40 | 169 | -192 | -1.14 | +190 |
| skip stock not beating SPY over 15 min | 37 | -39 | -1.06 | 188 | -343 | -1.83 | +39 |
| skip afternoon entries (2:00-3:45 PM) | 47 | -216 | -4.59 | 178 | -166 | -0.94 | +216 |
| skip volume spikes above 5x average | 42 | -158 | -3.75 | 183 | -225 | -1.23 | +158 |
| skip when the stop is inside normal noise (range > stop) | 15 | -33 | -2.22 | 210 | -349 | -1.66 | +33 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 27 | -47 | -1.75 | 198 | -335 | -1.69 | +47 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 112 | -328 | -2.93 | 113 | -54 | -0.48 | +328 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 53% (37-69) | +2.10 | +0.32 | +11 |  |
| 60-240 | 91 | 37% (28-48) | -0.29 | -1.72 | -157 |  |
| 240-375 | 62 | 29% (19-41) | -1.72 | -3.68 | -228 |  |
| 375-390 | 38 | 50% (35-65) | +1.47 | -0.21 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 42% (28-58) | +0.35 | -1.04 | -40 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 66 | 33% (23-45) | -0.38 | -1.70 | -112 |  |
| > 0.2 | 70 | 43% (32-55) | -0.10 | -1.90 | -133 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 98 | 39% (30-49) | -0.37 | -2.16 | -212 |  |
| above VWAP | 127 | 40% (32-49) | +0.24 | -1.34 | -170 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 75 | 39% (28-50) | -0.04 | -1.35 | -101 |  |
| (0.133, 0.379] | 75 | 47% (36-58) | +0.38 | -1.31 | -98 |  |
| (0.379, 2.096] | 75 | 33% (24-45) | -0.42 | -2.44 | -183 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.116] | 75 | 45% (35-57) | +0.46 | -0.84 | -63 |  |
| (0.116, 0.412] | 74 | 41% (30-52) | +0.37 | -1.58 | -117 |  |
| (0.412, 2.453] | 74 | 34% (24-45) | -0.82 | -2.63 | -195 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.357] | 75 | 41% (31-53) | +0.19 | -1.72 | -129 |  |
| (-0.357, 0.371] | 75 | 44% (33-55) | +0.82 | -0.37 | -28 |  |
| (0.371, 2.726] | 75 | 33% (24-45) | -1.09 | -3.01 | -226 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.054] | 75 | 40% (30-51) | -0.27 | -1.76 | -132 |  |
| (0.054, 0.123] | 75 | 45% (35-57) | +0.66 | -0.91 | -68 |  |
| (0.123, 0.924] | 75 | 33% (24-45) | -0.47 | -2.43 | -182 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 75 | 43% (32-54) | +0.05 | -1.11 | -83 |  |
| (0.211, 0.316] | 75 | 41% (31-53) | +0.39 | -1.43 | -107 |  |
| (0.316, 2.663] | 75 | 35% (25-46) | -0.52 | -2.56 | -192 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.344] | 75 | 39% (28-50) | +0.02 | -1.55 | -116 |  |
| (2.344, 3.618] | 75 | 49% (38-60) | +1.12 | -0.57 | -43 |  |
| (3.618, 18.762] | 75 | 31% (21-42) | -1.22 | -2.97 | -223 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0986] | 75 | 47% (36-58) | +0.38 | -0.38 | -29 |  |
| (0.0986, 0.15] | 75 | 37% (27-49) | -0.13 | -1.30 | -98 |  |
| (0.15, 0.392] | 75 | 35% (25-46) | -0.33 | -3.41 | -256 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 33 | 30% (17-47) | -1.75 | -2.57 | -85 |  |
| (-0.912, 0.454] | 33 | 45% (30-62) | +0.64 | +0.10 | +3 |  |
| (0.454, 5.305] | 33 | 52% (35-67) | +1.60 | +0.83 | +27 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.518] | 37 | 46% (31-62) | +0.37 | -0.25 | -9 |  |
| (0.518, 0.748] | 34 | 38% (24-55) | -0.52 | -1.29 | -44 |  |
| (0.748, 1.75] | 35 | 40% (26-56) | +0.07 | -0.72 | -25 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 36 | 42% (27-58) | -0.11 | -0.64 | -23 |  |
| (0.789, 1.21] | 35 | 40% (26-56) | -0.03 | -0.78 | -27 |  |
| (1.21, 5.866] | 35 | 43% (28-59) | +0.09 | -0.81 | -28 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.353] | 36 | 42% (27-58) | +0.04 | -0.54 | -19 |  |
| (0.353, 0.559] | 35 | 46% (30-62) | +0.36 | -0.41 | -14 |  |
| (0.559, 2.726] | 35 | 37% (23-54) | -0.45 | -1.29 | -45 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 112, target 55, time_stop 48, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0986] | 75 | 35% | 16% | 43% |
| (0.0986, 0.15] | 75 | 56% | 28% | 11% |
| (0.15, 0.392] | 75 | 59% | 29% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
