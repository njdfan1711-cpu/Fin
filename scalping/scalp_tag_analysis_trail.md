# Scalp signal analysis (trail exits)

_220 tagged trades, 24 trading days (2026-10-01 to 2026-11-03). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 220 | 38% (32-45) | -0.92 | -2.61 | -575 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 37 | -5 | -0.14 | 183 | -569 | -3.11 | +5 |
| skip first 30 min | 2 | -3 | -1.70 | 218 | -571 | -2.62 | +3 |
| skip when SPY is down on the day | 89 | -281 | -3.16 | 131 | -293 | -2.24 | +281 |
| skip when SPY is below its VWAP | 96 | -325 | -3.39 | 124 | -249 | -2.01 | +325 |
| skip when SPY fell over the last 15 min | 81 | -189 | -2.33 | 139 | -386 | -2.77 | +189 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 55 | -236 | -4.28 | 165 | -339 | -2.05 | +236 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 183 | -493 | -2.70 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 46 | -208 | -4.53 | 174 | -366 | -2.10 | +208 |
| skip volume spikes above 5x average | 40 | -190 | -4.74 | 180 | -385 | -2.14 | +190 |
| skip when the stop is inside normal noise (range > stop) | 14 | -46 | -3.27 | 206 | -529 | -2.57 | +46 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 25 | -71 | -2.83 | 195 | -504 | -2.58 | +71 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 111 | -399 | -3.59 | 109 | -176 | -1.61 | +399 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 33 | 48% (33-65) | -0.32 | -2.12 | -70 |  |
| 60-240 | 89 | 34% (25-44) | -1.45 | -2.90 | -258 |  |
| 240-375 | 61 | 34% (24-47) | -1.97 | -3.95 | -241 |  |
| 375-390 | 37 | 46% (31-62) | +1.56 | -0.14 | -5 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 37% (23-53) | -1.17 | -2.57 | -98 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 65 | 35% (25-48) | -1.50 | -2.82 | -183 |  |
| > 0.2 | 66 | 42% (31-54) | +0.22 | -1.66 | -110 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 96 | 32% (24-42) | -1.57 | -3.39 | -325 |  |
| above VWAP | 124 | 43% (34-52) | -0.41 | -2.01 | -249 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 74 | 36% (26-48) | -0.32 | -1.64 | -121 |  |
| (0.132, 0.374] | 73 | 48% (37-59) | -0.59 | -2.31 | -169 |  |
| (0.374, 1.555] | 73 | 30% (21-41) | -1.85 | -3.90 | -285 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.117] | 73 | 44% (33-55) | +0.12 | -1.20 | -88 |  |
| (0.117, 0.41] | 72 | 42% (31-53) | -0.79 | -2.70 | -194 |  |
| (0.41, 2.453] | 73 | 29% (20-40) | -2.07 | -3.96 | -289 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.349] | 74 | 38% (28-49) | -1.38 | -3.31 | -245 |  |
| (-0.349, 0.364] | 73 | 45% (34-57) | +0.56 | -0.64 | -46 |  |
| (0.364, 2.726] | 73 | 32% (22-43) | -1.92 | -3.88 | -283 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0549] | 74 | 38% (28-49) | -1.34 | -2.85 | -211 |  |
| (0.0549, 0.123] | 73 | 41% (31-53) | +0.13 | -1.47 | -107 |  |
| (0.123, 0.678] | 73 | 36% (26-47) | -1.53 | -3.52 | -257 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 74 | 41% (30-52) | -0.09 | -1.26 | -93 |  |
| (0.212, 0.315] | 73 | 40% (29-51) | -1.03 | -2.89 | -211 |  |
| (0.315, 0.979] | 73 | 34% (24-46) | -1.64 | -3.71 | -271 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.356] | 74 | 39% (29-51) | -0.65 | -2.25 | -167 |  |
| (2.356, 3.611] | 73 | 47% (36-58) | +0.52 | -1.17 | -85 |  |
| (3.611, 18.762] | 73 | 29% (20-40) | -2.63 | -4.42 | -322 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 74 | 45% (34-56) | +0.22 | -0.54 | -40 |  |
| (0.0985, 0.15] | 73 | 42% (32-54) | -1.19 | -2.37 | -173 |  |
| (0.15, 0.392] | 73 | 27% (18-39) | -1.80 | -4.95 | -361 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.911] | 32 | 31% (18-49) | -2.61 | -3.44 | -110 |  |
| (-0.911, 0.444] | 31 | 52% (35-68) | -0.40 | -0.93 | -29 |  |
| (0.444, 5.305] | 31 | 55% (38-71) | -0.21 | -0.97 | -30 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.515] | 34 | 47% (31-63) | -0.59 | -1.22 | -41 |  |
| (0.515, 0.743] | 33 | 48% (33-65) | -1.25 | -2.00 | -66 |  |
| (0.743, 1.74] | 34 | 41% (26-58) | -1.78 | -2.60 | -88 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 34 | 47% (31-63) | -1.25 | -1.77 | -60 |  |
| (0.779, 1.197] | 33 | 45% (30-62) | -1.07 | -1.80 | -59 |  |
| (1.197, 5.866] | 34 | 44% (29-61) | -1.29 | -2.24 | -76 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.349] | 34 | 38% (24-55) | -1.31 | -1.89 | -64 |  |
| (0.349, 0.557] | 33 | 58% (41-73) | -0.46 | -1.21 | -40 | ▲ |
| (0.557, 1.659] | 34 | 41% (26-58) | -1.83 | -2.69 | -92 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.17%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 101, trail_stop 85, time_stop 29, eod 5

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 74 | 34% | 28% | 32% |
| (0.0985, 0.15] | 73 | 49% | 45% | 4% |
| (0.15, 0.392] | 73 | 55% | 42% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
