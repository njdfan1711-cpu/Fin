# Scalp signal analysis (fixed exits)

_217 tagged trades, 24 trading days (2026-10-01 to 2026-11-03). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 217 | 38% (32-44) | -0.19 | -1.91 | -414 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -17 | -0.47 | 182 | -397 | -2.18 | +17 |
| skip first 30 min | 2 | -8 | -4.06 | 215 | -406 | -1.89 | +8 |
| skip when SPY is down on the day | 89 | -137 | -1.54 | 128 | -277 | -2.16 | +137 |
| skip when SPY is below its VWAP | 94 | -214 | -2.27 | 123 | -200 | -1.63 | +214 |
| skip when SPY fell over the last 15 min | 80 | -130 | -1.63 | 137 | -284 | -2.07 | +130 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 54 | -199 | -3.69 | 163 | -214 | -1.32 | +199 |
| skip stock not beating SPY over 15 min | 37 | -39 | -1.06 | 180 | -375 | -2.08 | +39 |
| skip afternoon entries (2:00-3:45 PM) | 46 | -209 | -4.54 | 171 | -205 | -1.20 | +209 |
| skip volume spikes above 5x average | 40 | -177 | -4.42 | 177 | -237 | -1.34 | +177 |
| skip when the stop is inside normal noise (range > stop) | 14 | -43 | -3.08 | 203 | -371 | -1.83 | +43 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.67%) | 25 | -50 | -2.01 | 192 | -363 | -1.89 | +50 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 111 | -321 | -2.89 | 106 | -93 | -0.88 | +321 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 33 | 52% (35-67) | +1.89 | +0.09 | +3 |  |
| 60-240 | 88 | 35% (26-46) | -0.56 | -2.03 | -179 |  |
| 240-375 | 61 | 30% (20-42) | -1.65 | -3.63 | -221 |  |
| 375-390 | 35 | 46% (30-62) | +1.30 | -0.47 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 42% (28-58) | +0.35 | -1.04 | -40 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 65 | 34% (24-46) | -0.29 | -1.62 | -105 |  |
| > 0.2 | 63 | 37% (26-49) | -0.78 | -2.72 | -172 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 94 | 37% (28-47) | -0.43 | -2.27 | -214 |  |
| above VWAP | 123 | 38% (30-47) | -0.01 | -1.63 | -200 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 73 | 37% (27-48) | -0.22 | -1.55 | -113 |  |
| (0.132, 0.377] | 72 | 44% (34-56) | +0.25 | -1.49 | -107 |  |
| (0.377, 1.555] | 72 | 32% (22-43) | -0.62 | -2.69 | -194 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.127] | 72 | 42% (31-53) | +0.12 | -1.23 | -88 |  |
| (0.127, 0.418] | 71 | 41% (30-52) | +0.52 | -1.48 | -105 |  |
| (0.418, 2.453] | 72 | 32% (22-43) | -1.11 | -2.95 | -212 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.349] | 73 | 38% (28-50) | -0.11 | -2.06 | -150 |  |
| (-0.349, 0.364] | 72 | 43% (32-55) | +0.73 | -0.48 | -34 |  |
| (0.364, 2.726] | 72 | 32% (22-43) | -1.20 | -3.18 | -229 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0522] | 73 | 38% (28-50) | -0.49 | -2.01 | -147 |  |
| (0.0522, 0.123] | 72 | 43% (32-55) | +0.49 | -1.11 | -80 |  |
| (0.123, 0.678] | 72 | 32% (22-43) | -0.59 | -2.60 | -187 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 73 | 41% (31-53) | -0.15 | -1.32 | -96 |  |
| (0.211, 0.315] | 72 | 39% (28-50) | +0.21 | -1.68 | -121 |  |
| (0.315, 0.979] | 72 | 33% (24-45) | -0.64 | -2.74 | -197 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.356] | 73 | 37% (27-48) | -0.07 | -1.69 | -123 |  |
| (2.356, 3.61] | 72 | 49% (37-60) | +1.07 | -0.65 | -47 |  |
| (3.61, 18.762] | 72 | 28% (19-39) | -1.58 | -3.39 | -244 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 73 | 45% (34-57) | +0.29 | -0.48 | -35 |  |
| (0.0985, 0.15] | 72 | 36% (26-48) | -0.13 | -1.32 | -95 |  |
| (0.15, 0.392] | 72 | 32% (22-43) | -0.75 | -3.94 | -284 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.876] | 31 | 23% (11-40) | -2.55 | -3.43 | -106 |  |
| (-0.876, 0.474] | 30 | 43% (27-61) | +0.55 | +0.03 | +1 |  |
| (0.474, 5.305] | 30 | 50% (33-67) | +1.42 | +0.66 | +20 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.515] | 33 | 42% (27-59) | +0.05 | -0.57 | -19 |  |
| (0.515, 0.748] | 32 | 38% (23-55) | -0.23 | -1.00 | -32 |  |
| (0.748, 1.74] | 33 | 33% (20-50) | -0.97 | -1.79 | -59 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 33 | 42% (27-59) | +0.16 | -0.36 | -12 |  |
| (0.779, 1.206] | 32 | 34% (20-52) | -0.36 | -1.12 | -36 |  |
| (1.206, 5.866] | 33 | 36% (22-53) | -0.96 | -1.89 | -62 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.349] | 33 | 36% (22-53) | -0.52 | -1.11 | -36 |  |
| (0.349, 0.561] | 32 | 44% (28-61) | +0.44 | -0.33 | -11 |  |
| (0.561, 1.659] | 33 | 33% (20-50) | -1.05 | -1.91 | -63 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 111, target 52, time_stop 47, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 73 | 36% | 16% | 44% |
| (0.0985, 0.15] | 72 | 57% | 29% | 10% |
| (0.15, 0.392] | 72 | 61% | 26% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
