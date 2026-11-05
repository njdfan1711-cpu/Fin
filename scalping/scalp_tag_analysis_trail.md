# Scalp signal analysis (trail exits)

_233 tagged trades, 26 trading days (2026-10-01 to 2026-11-05). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 233 | 40% (34-47) | -0.72 | -2.36 | -550 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 40 | +2 | +0.06 | 193 | -552 | -2.86 | -2 |
| skip first 30 min | 2 | -3 | -1.70 | 231 | -547 | -2.37 | +3 |
| skip when SPY is down on the day | 90 | -280 | -3.11 | 143 | -270 | -1.89 | +280 |
| skip when SPY is below its VWAP | 100 | -329 | -3.29 | 133 | -221 | -1.66 | +329 |
| skip when SPY fell over the last 15 min | 85 | -189 | -2.22 | 148 | -361 | -2.44 | +189 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 58 | -227 | -3.92 | 175 | -323 | -1.84 | +227 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 196 | -469 | -2.39 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 49 | -221 | -4.52 | 184 | -329 | -1.79 | +221 |
| skip volume spikes above 5x average | 44 | -171 | -3.88 | 189 | -379 | -2.01 | +171 |
| skip when the stop is inside normal noise (range > stop) | 18 | -34 | -1.87 | 215 | -516 | -2.40 | +34 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.67%) | 29 | -59 | -2.04 | 204 | -491 | -2.41 | +59 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 115 | -410 | -3.57 | 118 | -140 | -1.18 | +410 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 94 | 37% (28-47) | -1.14 | -2.54 | -239 |  |
| 240-375 | 65 | 35% (25-48) | -1.93 | -3.84 | -249 |  |
| 375-390 | 40 | 48% (33-63) | +1.72 | +0.06 | +2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 39 | 38% (25-54) | -1.11 | -2.47 | -96 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 77 | 48% (37-59) | +0.68 | -1.03 | -79 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 100 | 33% (25-43) | -1.52 | -3.29 | -329 |  |
| above VWAP | 133 | 46% (38-54) | -0.12 | -1.66 | -221 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 78 | 37% (27-48) | -0.29 | -1.68 | -131 |  |
| (0.136, 0.38] | 77 | 52% (41-63) | -0.24 | -1.79 | -138 | ▲ |
| (0.38, 2.096] | 78 | 32% (23-43) | -1.63 | -3.60 | -281 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.109] | 77 | 47% (36-58) | +0.44 | -0.82 | -63 |  |
| (0.109, 0.422] | 77 | 42% (31-53) | -0.93 | -2.85 | -220 |  |
| (0.422, 2.453] | 77 | 32% (23-44) | -1.66 | -3.43 | -264 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.349] | 78 | 41% (31-52) | -1.12 | -2.98 | -233 |  |
| (-0.349, 0.401] | 77 | 48% (37-59) | +0.78 | -0.39 | -30 |  |
| (0.401, 4.204] | 78 | 32% (23-43) | -1.80 | -3.69 | -288 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0559] | 78 | 41% (31-52) | -1.00 | -2.45 | -191 |  |
| (0.0559, 0.124] | 77 | 43% (32-54) | +0.21 | -1.34 | -103 |  |
| (0.124, 0.924] | 78 | 37% (27-48) | -1.36 | -3.27 | -255 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 78 | 45% (34-56) | +0.27 | -0.85 | -67 |  |
| (0.211, 0.323] | 77 | 40% (30-51) | -1.03 | -2.81 | -216 |  |
| (0.323, 2.663] | 78 | 36% (26-47) | -1.41 | -3.42 | -267 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.34] | 78 | 41% (31-52) | -0.61 | -2.15 | -168 |  |
| (2.34, 3.635] | 77 | 47% (36-58) | +0.54 | -1.14 | -88 |  |
| (3.635, 18.762] | 78 | 33% (24-44) | -2.08 | -3.77 | -294 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0987] | 78 | 47% (37-58) | +0.38 | -0.36 | -28 |  |
| (0.0987, 0.15] | 77 | 42% (31-53) | -1.24 | -2.41 | -185 |  |
| (0.15, 0.392] | 78 | 32% (23-43) | -1.31 | -4.31 | -336 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.918] | 36 | 39% (25-55) | -1.86 | -2.69 | -97 |  |
| (-0.918, 0.45] | 35 | 51% (36-67) | -0.33 | -0.89 | -31 |  |
| (0.45, 5.599] | 36 | 58% (42-73) | +0.27 | -0.46 | -16 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.518] | 39 | 51% (36-66) | -0.20 | -0.82 | -32 |  |
| (0.518, 0.748] | 37 | 46% (31-62) | -1.47 | -2.23 | -83 |  |
| (0.748, 1.75] | 38 | 50% (35-65) | -0.68 | -1.49 | -57 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.811] | 38 | 47% (32-63) | -1.28 | -1.81 | -69 |  |
| (0.811, 1.266] | 38 | 50% (35-65) | -0.51 | -1.24 | -47 |  |
| (1.266, 5.866] | 38 | 50% (35-65) | -0.54 | -1.46 | -55 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.354] | 38 | 45% (30-60) | -0.70 | -1.27 | -48 |  |
| (0.354, 0.566] | 38 | 58% (42-72) | -0.48 | -1.22 | -46 | ▲ |
| (0.566, 2.726] | 38 | 45% (30-60) | -1.14 | -2.02 | -77 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.15%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 103, trail_stop 94, time_stop 29, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0987] | 78 | 32% | 31% | 31% |
| (0.0987, 0.15] | 77 | 51% | 44% | 4% |
| (0.15, 0.392] | 78 | 50% | 46% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
