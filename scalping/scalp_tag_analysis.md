# Scalp signal analysis (fixed exits)

_220 tagged trades, 24 trading days (2026-10-01 to 2026-11-03). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 220 | 39% (32-45) | -0.16 | -1.85 | -408 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 37 | -13 | -0.35 | 183 | -395 | -2.16 | +13 |
| skip first 30 min | 2 | -8 | -4.06 | 218 | -399 | -1.83 | +8 |
| skip when SPY is down on the day | 89 | -137 | -1.54 | 131 | -270 | -2.06 | +137 |
| skip when SPY is below its VWAP | 96 | -210 | -2.18 | 124 | -198 | -1.60 | +210 |
| skip when SPY fell over the last 15 min | 80 | -130 | -1.63 | 140 | -277 | -1.98 | +130 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 55 | -200 | -3.64 | 165 | -207 | -1.26 | +200 |
| skip stock not beating SPY over 15 min | 37 | -39 | -1.06 | 183 | -368 | -2.01 | +39 |
| skip afternoon entries (2:00-3:45 PM) | 46 | -209 | -4.54 | 174 | -199 | -1.14 | +209 |
| skip volume spikes above 5x average | 40 | -177 | -4.42 | 180 | -231 | -1.28 | +177 |
| skip when the stop is inside normal noise (range > stop) | 14 | -43 | -3.08 | 206 | -364 | -1.77 | +43 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 25 | -50 | -2.01 | 195 | -357 | -1.83 | +50 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 111 | -321 | -2.89 | 109 | -87 | -0.79 | +321 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 33 | 52% (35-67) | +1.89 | +0.09 | +3 |  |
| 60-240 | 89 | 36% (27-46) | -0.53 | -1.98 | -176 |  |
| 240-375 | 61 | 30% (20-42) | -1.65 | -3.63 | -221 |  |
| 375-390 | 37 | 49% (33-64) | +1.36 | -0.35 | -13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 42% (28-58) | +0.35 | -1.04 | -40 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 65 | 34% (24-46) | -0.29 | -1.62 | -105 |  |
| > 0.2 | 66 | 39% (29-51) | -0.63 | -2.50 | -165 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 96 | 39% (29-49) | -0.37 | -2.18 | -210 |  |
| above VWAP | 124 | 39% (31-47) | +0.01 | -1.60 | -198 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 74 | 38% (28-49) | -0.18 | -1.50 | -111 |  |
| (0.132, 0.374] | 73 | 45% (34-57) | +0.24 | -1.48 | -108 |  |
| (0.374, 1.555] | 73 | 33% (23-44) | -0.53 | -2.58 | -188 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.117] | 73 | 44% (33-55) | +0.26 | -1.06 | -78 |  |
| (0.117, 0.41] | 72 | 42% (31-53) | +0.55 | -1.36 | -98 |  |
| (0.41, 2.453] | 73 | 32% (22-43) | -1.18 | -3.07 | -224 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.349] | 74 | 39% (29-51) | -0.08 | -2.01 | -149 |  |
| (-0.349, 0.364] | 73 | 44% (33-55) | +0.78 | -0.41 | -30 |  |
| (0.364, 2.726] | 73 | 33% (23-44) | -1.18 | -3.13 | -229 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0549] | 74 | 38% (28-49) | -0.56 | -2.07 | -153 |  |
| (0.0549, 0.123] | 73 | 45% (34-57) | +0.63 | -0.96 | -70 |  |
| (0.123, 0.678] | 73 | 33% (23-44) | -0.54 | -2.53 | -185 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 74 | 41% (30-52) | -0.15 | -1.31 | -97 |  |
| (0.212, 0.315] | 73 | 41% (31-53) | +0.27 | -1.59 | -116 |  |
| (0.315, 0.979] | 73 | 34% (24-46) | -0.60 | -2.66 | -194 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.356] | 74 | 38% (28-49) | -0.03 | -1.63 | -121 |  |
| (2.356, 3.611] | 73 | 49% (38-61) | +1.09 | -0.61 | -44 |  |
| (3.611, 18.762] | 73 | 29% (20-40) | -1.53 | -3.32 | -242 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 74 | 46% (35-57) | +0.31 | -0.45 | -33 |  |
| (0.0985, 0.15] | 73 | 38% (28-50) | +0.02 | -1.16 | -84 |  |
| (0.15, 0.392] | 73 | 32% (22-43) | -0.82 | -3.97 | -290 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.911] | 32 | 25% (13-42) | -2.62 | -3.45 | -111 |  |
| (-0.911, 0.444] | 31 | 45% (29-62) | +0.69 | +0.16 | +5 |  |
| (0.444, 5.305] | 31 | 52% (35-68) | +1.61 | +0.85 | +26 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.515] | 34 | 44% (29-61) | +0.11 | -0.51 | -17 |  |
| (0.515, 0.743] | 33 | 42% (27-59) | +0.12 | -0.63 | -21 |  |
| (0.743, 1.74] | 34 | 32% (19-49) | -1.11 | -1.93 | -66 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 34 | 44% (29-61) | +0.24 | -0.28 | -9 |  |
| (0.779, 1.197] | 33 | 39% (25-56) | -0.03 | -0.76 | -25 |  |
| (1.197, 5.866] | 34 | 35% (21-52) | -1.09 | -2.04 | -69 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.349] | 34 | 38% (24-55) | -0.42 | -1.00 | -34 |  |
| (0.349, 0.557] | 33 | 45% (30-62) | +0.27 | -0.48 | -16 |  |
| (0.557, 1.659] | 34 | 35% (21-52) | -0.72 | -1.58 | -54 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 111, target 52, time_stop 48, eod 9

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 74 | 35% | 16% | 43% |
| (0.0985, 0.15] | 73 | 55% | 29% | 11% |
| (0.15, 0.392] | 73 | 62% | 26% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
