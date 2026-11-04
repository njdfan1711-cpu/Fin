# Scalp signal analysis (trail exits)

_223 tagged trades, 25 trading days (2026-10-01 to 2026-11-04). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 223 | 39% (32-45) | -0.88 | -2.56 | -571 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 38 | -0 | -0.01 | 185 | -570 | -3.08 | +0 |
| skip first 30 min | 2 | -3 | -1.70 | 221 | -568 | -2.57 | +3 |
| skip when SPY is down on the day | 89 | -281 | -3.16 | 134 | -289 | -2.16 | +281 |
| skip when SPY is below its VWAP | 98 | -327 | -3.34 | 125 | -243 | -1.95 | +327 |
| skip when SPY fell over the last 15 min | 82 | -196 | -2.39 | 141 | -375 | -2.66 | +196 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 55 | -236 | -4.28 | 168 | -335 | -2.00 | +236 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 186 | -490 | -2.63 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 47 | -216 | -4.59 | 176 | -355 | -2.02 | +216 |
| skip volume spikes above 5x average | 40 | -190 | -4.74 | 183 | -381 | -2.08 | +190 |
| skip when the stop is inside normal noise (range > stop) | 14 | -46 | -3.27 | 209 | -525 | -2.51 | +46 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.63%) | 26 | -78 | -2.98 | 197 | -493 | -2.50 | +78 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 112 | -406 | -3.62 | 111 | -165 | -1.49 | +406 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 89 | 34% (25-44) | -1.45 | -2.90 | -258 |  |
| 240-375 | 62 | 34% (23-46) | -2.04 | -4.00 | -248 |  |
| 375-390 | 38 | 47% (32-63) | +1.67 | -0.01 | -0 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 37% (23-53) | -1.17 | -2.57 | -98 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 68 | 44% (33-56) | +0.39 | -1.45 | -99 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 98 | 33% (24-42) | -1.55 | -3.34 | -327 |  |
| above VWAP | 125 | 43% (35-52) | -0.35 | -1.95 | -243 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 75 | 36% (26-47) | -0.30 | -1.62 | -121 |  |
| (0.133, 0.377] | 74 | 50% (39-61) | -0.47 | -2.17 | -161 | ▲ |
| (0.377, 1.555] | 74 | 30% (21-41) | -1.86 | -3.90 | -289 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.117] | 74 | 45% (34-56) | +0.20 | -1.12 | -83 |  |
| (0.117, 0.41] | 73 | 41% (31-53) | -0.86 | -2.76 | -201 |  |
| (0.41, 2.453] | 74 | 30% (21-41) | -1.95 | -3.83 | -283 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.352] | 75 | 40% (30-51) | -1.12 | -3.04 | -228 |  |
| (-0.352, 0.364] | 74 | 45% (34-56) | +0.47 | -0.72 | -53 |  |
| (0.364, 2.726] | 74 | 31% (22-42) | -1.98 | -3.92 | -290 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0549] | 75 | 39% (28-50) | -1.25 | -2.75 | -206 |  |
| (0.0549, 0.123] | 74 | 42% (31-53) | +0.22 | -1.36 | -101 |  |
| (0.123, 0.678] | 74 | 35% (25-46) | -1.59 | -3.57 | -264 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 75 | 43% (32-54) | +0.08 | -1.08 | -81 |  |
| (0.211, 0.315] | 74 | 39% (29-51) | -1.02 | -2.86 | -212 |  |
| (0.315, 0.979] | 74 | 34% (24-45) | -1.70 | -3.75 | -278 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.337] | 75 | 40% (30-51) | -0.59 | -2.16 | -162 |  |
| (2.337, 3.61] | 74 | 46% (35-57) | +0.54 | -1.18 | -87 |  |
| (3.61, 18.762] | 74 | 30% (21-41) | -2.58 | -4.35 | -322 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 75 | 45% (35-57) | +0.29 | -0.47 | -35 |  |
| (0.0985, 0.15] | 74 | 42% (31-53) | -1.26 | -2.44 | -180 |  |
| (0.15, 0.392] | 74 | 28% (19-40) | -1.68 | -4.80 | -355 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.876] | 33 | 33% (20-50) | -2.37 | -3.22 | -106 |  |
| (-0.876, 0.474] | 32 | 53% (36-69) | -0.15 | -0.67 | -22 |  |
| (0.474, 5.305] | 32 | 53% (36-69) | -0.41 | -1.18 | -38 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.515] | 35 | 49% (33-64) | -0.42 | -1.04 | -37 |  |
| (0.515, 0.743] | 34 | 47% (31-63) | -1.39 | -2.15 | -73 |  |
| (0.743, 1.74] | 35 | 43% (28-59) | -1.53 | -2.35 | -82 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 35 | 46% (30-62) | -1.39 | -1.92 | -67 |  |
| (0.779, 1.197] | 34 | 47% (31-63) | -0.88 | -1.61 | -55 |  |
| (1.197, 5.866] | 35 | 46% (30-62) | -1.06 | -2.00 | -70 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.349] | 35 | 40% (26-56) | -1.12 | -1.70 | -59 |  |
| (0.349, 0.557] | 34 | 56% (39-71) | -0.62 | -1.38 | -47 | ▲ |
| (0.557, 1.659] | 35 | 43% (28-59) | -1.59 | -2.45 | -86 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.17%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 102, trail_stop 86, time_stop 29, eod 6

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 75 | 33% | 28% | 32% |
| (0.0985, 0.15] | 74 | 50% | 45% | 4% |
| (0.15, 0.392] | 74 | 54% | 43% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
