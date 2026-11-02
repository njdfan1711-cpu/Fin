# Scalp signal analysis (fixed exits)

_210 tagged trades, 23 trading days (2026-10-01 to 2026-11-02). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 210 | 39% (32-45) | -0.11 | -1.85 | -389 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -17 | -0.47 | 175 | -372 | -2.13 | +17 |
| skip first 30 min | 1 | -6 | -6.31 | 209 | -382 | -1.83 | +6 |
| skip when SPY is down on the day | 89 | -137 | -1.54 | 121 | -251 | -2.08 | +137 |
| skip when SPY is below its VWAP | 93 | -207 | -2.22 | 117 | -182 | -1.55 | +207 |
| skip when SPY fell over the last 15 min | 77 | -127 | -1.65 | 133 | -262 | -1.97 | +127 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 52 | -181 | -3.47 | 158 | -208 | -1.32 | +181 |
| skip stock not beating SPY over 15 min | 36 | -33 | -0.91 | 174 | -356 | -2.05 | +33 |
| skip afternoon entries (2:00-3:45 PM) | 45 | -218 | -4.85 | 165 | -171 | -1.03 | +218 |
| skip volume spikes above 5x average | 40 | -177 | -4.42 | 170 | -212 | -1.25 | +177 |
| skip when the stop is inside normal noise (range > stop) | 13 | -41 | -3.18 | 197 | -347 | -1.76 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 23 | -59 | -2.56 | 187 | -330 | -1.76 | +59 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 109 | -308 | -2.82 | 101 | -81 | -0.80 | +308 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 30 | 57% (39-73) | +2.52 | +0.59 | +18 | ▲ |
| 60-240 | 86 | 36% (27-47) | -0.44 | -1.92 | -165 |  |
| 240-375 | 59 | 29% (19-41) | -1.79 | -3.81 | -225 |  |
| 375-390 | 35 | 46% (30-62) | +1.30 | -0.47 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 42% (28-58) | +0.35 | -1.04 | -40 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 63 | 35% (24-47) | -0.18 | -1.53 | -97 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 93 | 38% (28-48) | -0.37 | -2.22 | -207 |  |
| above VWAP | 117 | 39% (31-48) | +0.10 | -1.55 | -182 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 70 | 37% (27-49) | -0.20 | -1.56 | -109 |  |
| (0.129, 0.374] | 70 | 44% (33-56) | +0.27 | -1.49 | -105 |  |
| (0.374, 1.555] | 70 | 34% (24-46) | -0.38 | -2.50 | -175 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.12] | 70 | 43% (32-55) | +0.29 | -1.07 | -75 |  |
| (0.12, 0.41] | 69 | 41% (30-52) | +0.46 | -1.49 | -103 |  |
| (0.41, 2.453] | 70 | 33% (23-44) | -0.98 | -2.92 | -204 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.357] | 70 | 39% (28-50) | -0.15 | -2.16 | -151 |  |
| (-0.357, 0.339] | 70 | 44% (33-56) | +0.90 | -0.31 | -22 |  |
| (0.339, 2.726] | 70 | 33% (23-44) | -1.07 | -3.08 | -216 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.054] | 70 | 40% (29-52) | -0.25 | -1.81 | -126 |  |
| (0.054, 0.124] | 70 | 46% (35-57) | +0.83 | -0.81 | -57 |  |
| (0.124, 0.678] | 70 | 30% (21-42) | -0.90 | -2.94 | -206 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.21] | 70 | 43% (32-55) | +0.10 | -1.09 | -76 |  |
| (0.21, 0.314] | 70 | 39% (28-50) | +0.11 | -1.80 | -126 |  |
| (0.314, 0.979] | 70 | 34% (24-46) | -0.53 | -2.66 | -186 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.382] | 70 | 39% (28-50) | +0.13 | -1.54 | -108 |  |
| (2.382, 3.634] | 70 | 49% (37-60) | +1.02 | -0.72 | -50 |  |
| (3.634, 18.762] | 70 | 29% (19-40) | -1.47 | -3.30 | -231 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0982] | 70 | 46% (35-57) | +0.33 | -0.41 | -29 |  |
| (0.0982, 0.15] | 70 | 39% (28-50) | +0.26 | -0.98 | -68 |  |
| (0.15, 0.392] | 70 | 31% (22-43) | -0.91 | -4.16 | -292 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 28 | 21% (10-40) | -2.78 | -3.66 | -102 |  |
| (-0.912, 0.444] | 29 | 45% (28-62) | +0.72 | +0.19 | +5 |  |
| (0.444, 5.305] | 27 | 56% (37-72) | +2.09 | +1.36 | +37 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.493] | 31 | 42% (26-59) | +0.03 | -0.61 | -19 |  |
| (0.493, 0.747] | 30 | 43% (27-61) | +0.57 | -0.18 | -5 |  |
| (0.747, 1.74] | 30 | 33% (19-51) | -1.20 | -2.03 | -61 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 31 | 45% (29-62) | +0.41 | -0.09 | -3 |  |
| (0.789, 1.21] | 30 | 37% (22-54) | +0.01 | -0.75 | -23 |  |
| (1.21, 5.866] | 30 | 37% (22-54) | -1.04 | -1.98 | -59 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.353] | 31 | 42% (26-59) | +0.35 | -0.23 | -7 |  |
| (0.353, 0.559] | 30 | 43% (27-61) | +0.33 | -0.45 | -13 |  |
| (0.559, 1.659] | 30 | 33% (19-51) | -1.29 | -2.15 | -65 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 106, target 51, time_stop 46, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0982] | 70 | 34% | 16% | 46% |
| (0.0982, 0.15] | 70 | 54% | 31% | 10% |
| (0.15, 0.392] | 70 | 63% | 26% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
