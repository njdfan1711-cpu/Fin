# Scalp signal analysis (fixed exits)

_211 tagged trades, 23 trading days (2026-10-01 to 2026-11-02). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 211 | 38% (32-45) | -0.13 | -1.87 | -395 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -17 | -0.47 | 176 | -379 | -2.15 | +17 |
| skip first 30 min | 1 | -6 | -6.31 | 210 | -389 | -1.85 | +6 |
| skip when SPY is down on the day | 89 | -137 | -1.54 | 122 | -258 | -2.12 | +137 |
| skip when SPY is below its VWAP | 94 | -214 | -2.27 | 117 | -182 | -1.55 | +214 |
| skip when SPY fell over the last 15 min | 78 | -134 | -1.71 | 133 | -262 | -1.97 | +134 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 53 | -187 | -3.52 | 158 | -209 | -1.32 | +187 |
| skip stock not beating SPY over 15 min | 36 | -33 | -0.91 | 175 | -363 | -2.07 | +33 |
| skip afternoon entries (2:00-3:45 PM) | 45 | -218 | -4.85 | 166 | -177 | -1.07 | +218 |
| skip volume spikes above 5x average | 40 | -177 | -4.42 | 171 | -218 | -1.28 | +177 |
| skip when the stop is inside normal noise (range > stop) | 13 | -41 | -3.18 | 198 | -354 | -1.79 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.63%) | 23 | -59 | -2.56 | 188 | -337 | -1.79 | +59 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 109 | -308 | -2.82 | 102 | -87 | -0.86 | +308 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 30 | 57% (39-73) | +2.52 | +0.59 | +18 | ▲ |
| 60-240 | 87 | 36% (26-46) | -0.50 | -1.97 | -172 |  |
| 240-375 | 59 | 29% (19-41) | -1.79 | -3.81 | -225 |  |
| 375-390 | 35 | 46% (30-62) | +1.30 | -0.47 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 42% (28-58) | +0.35 | -1.04 | -40 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 64 | 34% (24-47) | -0.27 | -1.61 | -103 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 94 | 37% (28-47) | -0.43 | -2.27 | -214 |  |
| above VWAP | 117 | 39% (31-48) | +0.10 | -1.55 | -182 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 71 | 37% (26-48) | -0.28 | -1.63 | -116 |  |
| (0.122, 0.374] | 70 | 44% (33-56) | +0.27 | -1.49 | -105 |  |
| (0.374, 1.555] | 70 | 34% (24-46) | -0.38 | -2.50 | -175 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.118] | 70 | 41% (31-53) | +0.17 | -1.20 | -84 |  |
| (0.118, 0.408] | 70 | 41% (31-53) | +0.49 | -1.44 | -101 |  |
| (0.408, 2.453] | 70 | 33% (23-44) | -0.98 | -2.92 | -204 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.352] | 71 | 39% (29-51) | -0.01 | -2.00 | -142 |  |
| (-0.352, 0.34] | 70 | 44% (33-56) | +0.90 | -0.32 | -22 |  |
| (0.34, 2.726] | 70 | 31% (22-43) | -1.30 | -3.30 | -231 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0522] | 71 | 39% (29-51) | -0.33 | -1.87 | -133 |  |
| (0.0522, 0.124] | 70 | 46% (35-57) | +0.83 | -0.81 | -57 |  |
| (0.124, 0.678] | 70 | 30% (21-42) | -0.90 | -2.94 | -206 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.208] | 71 | 42% (31-54) | +0.01 | -1.17 | -83 |  |
| (0.208, 0.314] | 70 | 39% (28-50) | +0.11 | -1.80 | -126 |  |
| (0.314, 0.979] | 70 | 34% (24-46) | -0.53 | -2.66 | -186 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.367] | 71 | 38% (28-50) | +0.04 | -1.61 | -114 |  |
| (2.367, 3.632] | 70 | 49% (37-60) | +1.02 | -0.72 | -50 |  |
| (3.632, 18.762] | 70 | 29% (19-40) | -1.47 | -3.30 | -231 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0984] | 71 | 46% (35-58) | +0.46 | -0.28 | -20 |  |
| (0.0984, 0.15] | 70 | 37% (27-49) | +0.03 | -1.20 | -84 |  |
| (0.15, 0.392] | 70 | 31% (22-43) | -0.91 | -4.16 | -292 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.911] | 29 | 21% (10-38) | -2.89 | -3.75 | -109 |  |
| (-0.911, 0.444] | 28 | 46% (30-64) | +0.96 | +0.42 | +12 |  |
| (0.444, 5.305] | 28 | 54% (36-70) | +1.80 | +1.08 | +30 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.498] | 31 | 42% (26-59) | +0.03 | -0.61 | -19 |  |
| (0.498, 0.743] | 30 | 43% (27-61) | +0.56 | -0.18 | -5 |  |
| (0.743, 1.74] | 31 | 32% (19-50) | -1.35 | -2.17 | -67 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 31 | 45% (29-62) | +0.41 | -0.09 | -3 |  |
| (0.789, 1.206] | 30 | 37% (22-54) | +0.01 | -0.76 | -23 |  |
| (1.206, 5.866] | 31 | 35% (21-53) | -1.19 | -2.12 | -66 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.349] | 31 | 39% (24-56) | -0.18 | -0.76 | -24 |  |
| (0.349, 0.557] | 30 | 43% (27-61) | +0.33 | -0.42 | -13 |  |
| (0.557, 1.659] | 31 | 35% (21-53) | -0.92 | -1.79 | -55 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 107, target 51, time_stop 46, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0984] | 71 | 34% | 17% | 45% |
| (0.0984, 0.15] | 70 | 56% | 30% | 10% |
| (0.15, 0.392] | 70 | 63% | 26% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
