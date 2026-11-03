# Scalp signal analysis (fixed exits)

_216 tagged trades, 24 trading days (2026-10-01 to 2026-11-03). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 216 | 38% (31-44) | -0.24 | -1.96 | -423 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -17 | -0.47 | 181 | -407 | -2.25 | +17 |
| skip first 30 min | 2 | -8 | -4.06 | 214 | -415 | -1.94 | +8 |
| skip when SPY is down on the day | 89 | -137 | -1.54 | 127 | -286 | -2.25 | +137 |
| skip when SPY is below its VWAP | 94 | -214 | -2.27 | 122 | -210 | -1.72 | +214 |
| skip when SPY fell over the last 15 min | 79 | -140 | -1.77 | 137 | -284 | -2.07 | +140 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 54 | -199 | -3.69 | 162 | -224 | -1.38 | +199 |
| skip stock not beating SPY over 15 min | 37 | -39 | -1.06 | 179 | -384 | -2.15 | +39 |
| skip afternoon entries (2:00-3:45 PM) | 45 | -218 | -4.85 | 171 | -205 | -1.20 | +218 |
| skip volume spikes above 5x average | 40 | -177 | -4.42 | 176 | -246 | -1.40 | +177 |
| skip when the stop is inside normal noise (range > stop) | 14 | -43 | -3.08 | 202 | -380 | -1.88 | +43 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 24 | -60 | -2.49 | 192 | -363 | -1.89 | +60 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 111 | -321 | -2.89 | 105 | -102 | -0.97 | +321 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 33 | 52% (35-67) | +1.89 | +0.09 | +3 |  |
| 60-240 | 88 | 35% (26-46) | -0.56 | -2.03 | -179 |  |
| 240-375 | 60 | 28% (19-41) | -1.85 | -3.84 | -231 |  |
| 375-390 | 35 | 46% (30-62) | +1.30 | -0.47 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 42% (28-58) | +0.35 | -1.04 | -40 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 65 | 34% (24-46) | -0.29 | -1.62 | -105 |  |
| > 0.2 | 62 | 35% (25-48) | -0.96 | -2.92 | -181 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 94 | 37% (28-47) | -0.43 | -2.27 | -214 |  |
| above VWAP | 122 | 38% (30-47) | -0.10 | -1.72 | -210 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 72 | 36% (26-48) | -0.36 | -1.70 | -122 |  |
| (0.129, 0.375] | 72 | 44% (34-56) | +0.32 | -1.43 | -103 |  |
| (0.375, 1.555] | 72 | 32% (22-43) | -0.68 | -2.75 | -198 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.124] | 72 | 42% (31-53) | +0.12 | -1.23 | -88 |  |
| (0.124, 0.421] | 71 | 41% (30-52) | +0.51 | -1.48 | -105 |  |
| (0.421, 2.453] | 71 | 31% (21-42) | -1.27 | -3.12 | -222 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.35] | 72 | 39% (28-50) | -0.03 | -2.00 | -144 |  |
| (-0.35, 0.348] | 72 | 43% (32-55) | +0.72 | -0.48 | -35 |  |
| (0.348, 2.726] | 72 | 31% (21-42) | -1.43 | -3.40 | -244 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0522] | 72 | 39% (28-50) | -0.41 | -1.93 | -139 |  |
| (0.0522, 0.122] | 72 | 43% (32-55) | +0.49 | -1.02 | -73 |  |
| (0.122, 0.678] | 72 | 31% (21-42) | -0.82 | -2.93 | -211 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.21] | 72 | 42% (31-53) | -0.06 | -1.24 | -90 |  |
| (0.21, 0.315] | 72 | 39% (28-50) | +0.16 | -1.73 | -124 |  |
| (0.315, 0.979] | 72 | 32% (22-43) | -0.82 | -2.91 | -209 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.353] | 72 | 38% (27-49) | +0.01 | -1.62 | -116 |  |
| (2.353, 3.617] | 72 | 47% (36-59) | +0.84 | -0.87 | -63 |  |
| (3.617, 18.762] | 72 | 28% (19-39) | -1.58 | -3.39 | -244 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 73 | 45% (34-57) | +0.29 | -0.48 | -35 |  |
| (0.0985, 0.15] | 71 | 37% (26-48) | -0.05 | -1.26 | -89 |  |
| (0.15, 0.392] | 72 | 31% (21-42) | -0.97 | -4.16 | -299 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.887] | 30 | 20% (10-37) | -2.98 | -3.85 | -115 | ▼ |
| (-0.887, 0.454] | 30 | 43% (27-61) | +0.65 | +0.12 | +4 |  |
| (0.454, 5.305] | 30 | 50% (33-67) | +1.31 | +0.56 | +17 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.513] | 33 | 42% (27-59) | +0.05 | -0.57 | -19 |  |
| (0.513, 0.747] | 32 | 38% (23-55) | -0.23 | -1.00 | -32 |  |
| (0.747, 1.74] | 32 | 31% (18-49) | -1.33 | -2.14 | -69 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.775] | 33 | 42% (27-59) | +0.16 | -0.36 | -12 |  |
| (0.775, 1.2] | 32 | 34% (20-52) | -0.36 | -1.12 | -36 |  |
| (1.2, 5.866] | 32 | 34% (20-52) | -1.32 | -2.25 | -72 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.347] | 33 | 36% (22-53) | -0.52 | -1.11 | -36 |  |
| (0.347, 0.559] | 32 | 44% (28-61) | +0.44 | -0.33 | -11 |  |
| (0.559, 1.659] | 32 | 31% (18-49) | -1.41 | -2.26 | -72 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 111, target 51, time_stop 47, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 73 | 36% | 16% | 44% |
| (0.0985, 0.15] | 71 | 56% | 30% | 10% |
| (0.15, 0.392] | 72 | 62% | 25% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
