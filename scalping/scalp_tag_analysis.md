# Scalp signal analysis (fixed exits)

_334 tagged trades, 41 trading days (2026-10-01 to 2026-11-27). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 334 | 39% (34-45) | -0.04 | -1.39 | -463 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +0 | +0.01 | 272 | -463 | -1.70 | -0 |
| skip first 30 min | 5 | -27 | -5.42 | 329 | -436 | -1.32 | +27 |
| skip when SPY is down on the day | 156 | -181 | -1.16 | 178 | -282 | -1.58 | +181 |
| skip when SPY is below its VWAP | 143 | -204 | -1.42 | 191 | -259 | -1.36 | +204 |
| skip when SPY fell over the last 15 min | 110 | -134 | -1.22 | 224 | -329 | -1.47 | +134 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 82 | -180 | -2.20 | 252 | -283 | -1.12 | +180 |
| skip stock not beating SPY over 15 min | 52 | -88 | -1.69 | 282 | -375 | -1.33 | +88 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -227 | -3.25 | 264 | -236 | -0.89 | +227 |
| skip volume spikes above 5x average | 72 | -173 | -2.40 | 262 | -290 | -1.11 | +173 |
| skip when the stop is inside normal noise (range > stop) | 51 | -49 | -0.97 | 283 | -414 | -1.46 | +49 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 54 | -56 | -1.04 | 280 | -407 | -1.45 | +56 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 141 | -366 | -2.60 | 193 | -97 | -0.50 | +366 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 42 | 48% (33-62) | +1.39 | -0.18 | -8 |  |
| 60-240 | 141 | 38% (30-46) | -0.30 | -1.43 | -202 |  |
| 240-375 | 89 | 31% (23-42) | -1.25 | -2.85 | -254 |  |
| 375-390 | 62 | 48% (36-61) | +1.36 | +0.01 | +0 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 98 | 39% (30-49) | -0.01 | -0.98 | -96 |  |
| -0.2 to 0 | 58 | 43% (31-56) | +0.50 | -1.46 | -85 |  |
| 0 to 0.2 | 71 | 32% (23-44) | -0.52 | -1.83 | -130 |  |
| > 0.2 | 107 | 42% (33-52) | -0.02 | -1.42 | -152 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 143 | 41% (33-49) | +0.03 | -1.42 | -204 |  |
| above VWAP | 191 | 38% (32-45) | -0.08 | -1.36 | -259 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.117] | 112 | 38% (29-47) | -0.34 | -1.33 | -149 |  |
| (0.117, 0.37] | 111 | 41% (33-51) | +0.15 | -1.27 | -141 |  |
| (0.37, 5.591] | 111 | 39% (30-48) | +0.09 | -1.55 | -172 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.137] | 110 | 47% (38-57) | +0.85 | -0.24 | -26 |  |
| (0.137, 0.446] | 109 | 38% (29-47) | -0.03 | -1.65 | -180 |  |
| (0.446, 4.846] | 110 | 35% (26-44) | -0.70 | -2.08 | -229 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.576] | 112 | 43% (34-52) | +0.29 | -1.11 | -124 |  |
| (-0.576, 0.291] | 111 | 38% (29-47) | +0.13 | -1.00 | -111 |  |
| (0.291, 9.926] | 111 | 37% (29-46) | -0.53 | -2.05 | -228 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0561] | 113 | 37% (29-46) | -0.61 | -1.81 | -205 |  |
| (0.0561, 0.126] | 110 | 45% (36-54) | +0.55 | -0.71 | -78 |  |
| (0.126, 0.924] | 111 | 36% (28-45) | -0.03 | -1.62 | -180 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.221] | 112 | 43% (34-52) | +0.29 | -0.69 | -78 |  |
| (0.221, 0.351] | 111 | 39% (30-48) | -0.11 | -1.72 | -191 |  |
| (0.351, 2.663] | 111 | 36% (28-45) | -0.30 | -1.76 | -195 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 112 | 36% (27-45) | -0.25 | -1.58 | -177 |  |
| (2.39, 3.611] | 111 | 48% (39-57) | +0.90 | -0.48 | -53 |  |
| (3.611, 19.488] | 111 | 34% (26-43) | -0.75 | -2.10 | -233 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.105] | 112 | 45% (36-54) | +0.29 | -0.45 | -51 |  |
| (0.105, 0.168] | 111 | 36% (28-45) | -0.43 | -1.57 | -174 |  |
| (0.168, 0.76] | 111 | 37% (29-46) | +0.03 | -2.14 | -238 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.913] | 70 | 31% (22-43) | -1.06 | -1.85 | -129 |  |
| (-0.913, 0.638] | 69 | 45% (34-57) | +0.59 | +0.02 | +1 |  |
| (0.638, 14.989] | 69 | 45% (34-57) | +0.63 | -0.10 | -7 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.549] | 72 | 43% (32-55) | +0.07 | -0.55 | -39 |  |
| (0.549, 0.889] | 71 | 42% (31-54) | +0.07 | -0.64 | -46 |  |
| (0.889, 3.799] | 72 | 35% (25-46) | -0.23 | -1.03 | -74 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.934] | 72 | 42% (31-53) | -0.15 | -0.75 | -54 |  |
| (0.934, 1.68] | 71 | 42% (31-54) | +0.35 | -0.33 | -23 |  |
| (1.68, 9.058] | 72 | 36% (26-48) | -0.30 | -1.14 | -82 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 72 | 36% (26-48) | -0.51 | -1.10 | -79 |  |
| (0.409, 0.627] | 71 | 48% (37-59) | +0.70 | -0.00 | -0 |  |
| (0.627, 4.001] | 72 | 36% (26-48) | -0.28 | -1.11 | -80 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.20%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 170, target 84, time_stop 64, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.105] | 112 | 38% | 18% | 38% |
| (0.105, 0.168] | 111 | 56% | 24% | 13% |
| (0.168, 0.76] | 111 | 59% | 33% | 6% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
