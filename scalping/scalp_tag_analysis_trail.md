# Scalp signal analysis (trail exits)

_230 tagged trades, 25 trading days (2026-10-01 to 2026-11-04). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 230 | 40% (34-46) | -0.76 | -2.41 | -554 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 38 | -0 | -0.01 | 192 | -553 | -2.88 | +0 |
| skip first 30 min | 2 | -3 | -1.70 | 228 | -550 | -2.41 | +3 |
| skip when SPY is down on the day | 89 | -281 | -3.16 | 141 | -272 | -1.93 | +281 |
| skip when SPY is below its VWAP | 98 | -327 | -3.34 | 132 | -226 | -1.72 | +327 |
| skip when SPY fell over the last 15 min | 83 | -192 | -2.31 | 147 | -362 | -2.46 | +192 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 57 | -233 | -4.09 | 173 | -321 | -1.85 | +233 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 193 | -473 | -2.45 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 49 | -221 | -4.52 | 181 | -332 | -1.84 | +221 |
| skip volume spikes above 5x average | 43 | -172 | -3.99 | 187 | -382 | -2.04 | +172 |
| skip when the stop is inside normal noise (range > stop) | 15 | -37 | -2.50 | 215 | -516 | -2.40 | +37 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 28 | -76 | -2.73 | 202 | -477 | -2.36 | +76 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 113 | -413 | -3.65 | 117 | -141 | -1.20 | +413 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 93 | 37% (27-47) | -1.17 | -2.58 | -240 |  |
| 240-375 | 65 | 35% (25-48) | -1.93 | -3.84 | -249 |  |
| 375-390 | 38 | 47% (32-63) | +1.67 | -0.01 | -0 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 37% (23-53) | -1.17 | -2.57 | -98 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 75 | 48% (37-59) | +0.63 | -1.09 | -82 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 98 | 33% (24-42) | -1.55 | -3.34 | -327 |  |
| above VWAP | 132 | 45% (37-54) | -0.17 | -1.72 | -226 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.134] | 77 | 38% (28-49) | -0.21 | -1.51 | -116 |  |
| (0.134, 0.376] | 76 | 51% (40-62) | -0.35 | -2.01 | -153 | ▲ |
| (0.376, 2.096] | 77 | 31% (22-42) | -1.71 | -3.70 | -285 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.109] | 76 | 47% (37-58) | +0.46 | -0.80 | -60 |  |
| (0.109, 0.415] | 76 | 41% (30-52) | -0.96 | -2.89 | -220 |  |
| (0.415, 2.453] | 76 | 32% (22-43) | -1.77 | -3.56 | -270 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.349] | 77 | 40% (30-51) | -1.15 | -3.03 | -234 |  |
| (-0.349, 0.401] | 76 | 47% (37-58) | +0.70 | -0.46 | -35 |  |
| (0.401, 4.204] | 77 | 32% (23-44) | -1.81 | -3.70 | -285 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0552] | 77 | 40% (30-51) | -1.09 | -2.55 | -196 |  |
| (0.0552, 0.122] | 76 | 43% (33-55) | +0.30 | -1.15 | -87 |  |
| (0.122, 0.924] | 77 | 36% (27-48) | -1.48 | -3.51 | -270 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.209] | 77 | 45% (35-57) | +0.36 | -0.78 | -60 |  |
| (0.209, 0.316] | 76 | 39% (29-51) | -1.06 | -2.86 | -218 |  |
| (0.316, 2.663] | 77 | 35% (25-46) | -1.58 | -3.59 | -276 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.299] | 77 | 40% (30-51) | -0.64 | -2.20 | -170 |  |
| (2.299, 3.625] | 76 | 47% (37-58) | +0.57 | -1.11 | -84 |  |
| (3.625, 18.762] | 77 | 32% (23-44) | -2.18 | -3.90 | -300 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 77 | 47% (36-58) | +0.37 | -0.38 | -29 |  |
| (0.0985, 0.149] | 76 | 43% (33-55) | -1.09 | -2.26 | -171 |  |
| (0.149, 0.392] | 77 | 30% (21-41) | -1.56 | -4.58 | -353 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 35 | 37% (23-54) | -2.07 | -2.90 | -101 |  |
| (-0.912, 0.466] | 34 | 53% (37-69) | -0.11 | -0.64 | -22 |  |
| (0.466, 5.599] | 35 | 57% (41-72) | +0.03 | -0.72 | -25 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.516] | 37 | 51% (36-67) | -0.22 | -0.83 | -31 |  |
| (0.516, 0.741] | 37 | 49% (33-64) | -1.17 | -1.92 | -71 |  |
| (0.741, 1.75] | 37 | 46% (31-62) | -1.19 | -1.98 | -73 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 37 | 46% (31-62) | -1.34 | -1.87 | -69 |  |
| (0.789, 1.214] | 37 | 49% (33-64) | -0.66 | -1.39 | -51 |  |
| (1.214, 5.866] | 37 | 51% (36-67) | -0.56 | -1.47 | -54 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.351] | 37 | 43% (29-59) | -0.88 | -1.45 | -54 |  |
| (0.351, 0.56] | 37 | 59% (43-74) | -0.25 | -0.99 | -37 | ▲ |
| (0.56, 2.726] | 37 | 43% (29-59) | -1.44 | -2.29 | -85 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.15%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 103, trail_stop 92, time_stop 29, eod 6

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 77 | 32% | 30% | 31% |
| (0.0985, 0.149] | 76 | 49% | 46% | 4% |
| (0.149, 0.392] | 77 | 53% | 44% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
