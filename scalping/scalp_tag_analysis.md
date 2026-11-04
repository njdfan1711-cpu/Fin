# Scalp signal analysis (fixed exits)

_223 tagged trades, 25 trading days (2026-10-01 to 2026-11-04). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 223 | 39% (33-46) | -0.12 | -1.80 | -402 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 38 | -8 | -0.21 | 185 | -394 | -2.13 | +8 |
| skip first 30 min | 2 | -8 | -4.06 | 221 | -394 | -1.78 | +8 |
| skip when SPY is down on the day | 89 | -137 | -1.54 | 134 | -265 | -1.97 | +137 |
| skip when SPY is below its VWAP | 98 | -212 | -2.16 | 125 | -190 | -1.52 | +212 |
| skip when SPY fell over the last 15 min | 81 | -137 | -1.70 | 142 | -264 | -1.86 | +137 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 55 | -200 | -3.64 | 168 | -202 | -1.20 | +200 |
| skip stock not beating SPY over 15 min | 37 | -39 | -1.06 | 186 | -363 | -1.95 | +39 |
| skip afternoon entries (2:00-3:45 PM) | 47 | -216 | -4.59 | 176 | -186 | -1.06 | +216 |
| skip volume spikes above 5x average | 40 | -177 | -4.42 | 183 | -225 | -1.23 | +177 |
| skip when the stop is inside normal noise (range > stop) | 14 | -43 | -3.08 | 209 | -359 | -1.72 | +43 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.63%) | 26 | -57 | -2.20 | 197 | -345 | -1.75 | +57 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 112 | -328 | -2.93 | 111 | -74 | -0.66 | +328 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 53% (37-69) | +2.10 | +0.32 | +11 |  |
| 60-240 | 89 | 36% (27-46) | -0.53 | -1.98 | -176 |  |
| 240-375 | 62 | 29% (19-41) | -1.72 | -3.68 | -228 |  |
| 375-390 | 38 | 50% (35-65) | +1.47 | -0.21 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 42% (28-58) | +0.35 | -1.04 | -40 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 66 | 33% (23-45) | -0.38 | -1.70 | -112 |  |
| > 0.2 | 68 | 41% (30-53) | -0.40 | -2.24 | -152 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 98 | 39% (30-49) | -0.37 | -2.16 | -212 |  |
| above VWAP | 125 | 39% (31-48) | +0.08 | -1.52 | -190 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 75 | 39% (28-50) | -0.13 | -1.45 | -109 |  |
| (0.133, 0.377] | 74 | 46% (35-57) | +0.34 | -1.36 | -100 |  |
| (0.377, 1.555] | 74 | 32% (23-44) | -0.56 | -2.60 | -193 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.117] | 74 | 45% (34-56) | +0.33 | -0.98 | -73 |  |
| (0.117, 0.41] | 73 | 41% (31-53) | +0.46 | -1.44 | -105 |  |
| (0.41, 2.453] | 74 | 32% (23-44) | -1.04 | -2.91 | -216 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.352] | 75 | 41% (31-53) | +0.19 | -1.73 | -130 |  |
| (-0.352, 0.364] | 74 | 43% (33-55) | +0.69 | -0.49 | -36 |  |
| (0.364, 2.726] | 74 | 32% (23-44) | -1.24 | -3.19 | -236 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0549] | 75 | 39% (28-50) | -0.48 | -1.98 | -148 |  |
| (0.0549, 0.123] | 74 | 46% (35-57) | +0.75 | -0.83 | -62 |  |
| (0.123, 0.678] | 74 | 32% (23-44) | -0.61 | -2.59 | -192 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 75 | 43% (32-54) | +0.05 | -1.11 | -83 |  |
| (0.211, 0.315] | 74 | 41% (30-52) | +0.26 | -1.58 | -117 |  |
| (0.315, 0.979] | 74 | 34% (24-45) | -0.67 | -2.73 | -202 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.337] | 75 | 39% (28-50) | +0.02 | -1.55 | -116 |  |
| (2.337, 3.61] | 74 | 49% (38-60) | +1.10 | -0.61 | -45 |  |
| (3.61, 18.762] | 74 | 30% (21-41) | -1.47 | -3.24 | -240 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 75 | 47% (36-58) | +0.38 | -0.38 | -29 |  |
| (0.0985, 0.15] | 74 | 38% (28-49) | -0.06 | -1.24 | -92 |  |
| (0.15, 0.392] | 74 | 32% (23-44) | -0.68 | -3.81 | -282 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.876] | 33 | 27% (15-44) | -2.23 | -3.08 | -101 |  |
| (-0.876, 0.474] | 32 | 47% (31-64) | +0.75 | +0.23 | +7 |  |
| (0.474, 5.305] | 32 | 50% (34-66) | +1.42 | +0.65 | +21 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.515] | 35 | 46% (30-62) | +0.26 | -0.36 | -13 |  |
| (0.515, 0.743] | 34 | 41% (26-58) | -0.06 | -0.82 | -28 |  |
| (0.743, 1.74] | 35 | 34% (21-51) | -0.83 | -1.64 | -58 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 35 | 43% (28-59) | +0.06 | -0.48 | -17 |  |
| (0.779, 1.197] | 34 | 41% (26-58) | +0.13 | -0.60 | -20 |  |
| (1.197, 5.866] | 35 | 37% (23-54) | -0.81 | -1.74 | -61 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.349] | 35 | 40% (26-56) | -0.25 | -0.84 | -29 |  |
| (0.349, 0.557] | 34 | 44% (29-61) | +0.08 | -0.68 | -23 |  |
| (0.557, 1.659] | 35 | 37% (23-54) | -0.45 | -1.30 | -46 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 112, target 53, time_stop 48, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 75 | 35% | 16% | 43% |
| (0.0985, 0.15] | 74 | 55% | 28% | 11% |
| (0.15, 0.392] | 74 | 61% | 27% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
