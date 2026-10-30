# Scalp signal analysis (trail exits)

_194 tagged trades, 22 trading days (2026-10-01 to 2026-10-30). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 194 | 38% (32-45) | -0.82 | -2.64 | -512 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 28 | +11 | +0.38 | 166 | -523 | -3.15 | -11 |
| skip first 30 min | 1 | -6 | -6.31 | 193 | -506 | -2.62 | +6 |
| skip when SPY is down on the day | 75 | -249 | -3.33 | 119 | -263 | -2.21 | +249 |
| skip when SPY is below its VWAP | 79 | -290 | -3.67 | 115 | -223 | -1.94 | +290 |
| skip when SPY fell over the last 15 min | 72 | -178 | -2.48 | 122 | -334 | -2.74 | +178 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 48 | -191 | -3.98 | 146 | -321 | -2.20 | +191 |
| skip stock not beating SPY over 15 min | 32 | -70 | -2.19 | 162 | -442 | -2.73 | +70 |
| skip afternoon entries (2:00-3:45 PM) | 42 | -218 | -5.19 | 152 | -294 | -1.93 | +218 |
| skip volume spikes above 5x average | 35 | -159 | -4.55 | 159 | -353 | -2.22 | +159 |
| skip when the stop is inside normal noise (range > stop) | 8 | -15 | -1.91 | 186 | -497 | -2.67 | +15 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.62%) | 19 | -71 | -3.71 | 175 | -442 | -2.52 | +71 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 104 | -362 | -3.48 | 90 | -151 | -1.67 | +362 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 27 | 56% (37-72) | +0.58 | -1.48 | -40 |  |
| 60-240 | 84 | 35% (25-45) | -1.26 | -2.76 | -232 |  |
| 240-375 | 55 | 33% (22-46) | -2.45 | -4.57 | -251 |  |
| 375-390 | 28 | 43% (27-61) | +2.40 | +0.38 | +11 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 26 | 38% (22-57) | -1.03 | -2.68 | -70 |  |
| -0.2 to 0 | 49 | 37% (25-51) | -1.45 | -3.67 | -180 |  |
| 0 to 0.2 | 61 | 36% (25-49) | -1.36 | -2.73 | -167 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 79 | 30% (21-41) | -1.62 | -3.67 | -290 |  |
| above VWAP | 115 | 43% (35-53) | -0.27 | -1.94 | -223 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.134] | 65 | 35% (25-48) | -0.07 | -1.49 | -97 |  |
| (0.134, 0.374] | 65 | 48% (36-60) | -0.62 | -2.45 | -159 |  |
| (0.374, 1.555] | 64 | 31% (21-43) | -1.78 | -4.01 | -257 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.133] | 65 | 42% (30-54) | +0.12 | -1.29 | -84 |  |
| (0.133, 0.405] | 64 | 41% (29-53) | -0.80 | -2.85 | -183 |  |
| (0.405, 1.281] | 64 | 33% (23-45) | -1.71 | -3.74 | -239 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.326] | 65 | 38% (28-51) | -1.13 | -3.24 | -210 |  |
| (-0.326, 0.356] | 64 | 45% (34-57) | +0.70 | -0.56 | -36 |  |
| (0.356, 2.726] | 65 | 31% (21-43) | -2.00 | -4.09 | -266 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 65 | 40% (29-52) | -1.13 | -2.72 | -177 |  |
| (0.0521, 0.122] | 64 | 39% (28-51) | +0.23 | -1.39 | -89 |  |
| (0.122, 0.678] | 65 | 35% (25-48) | -1.53 | -3.79 | -246 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.207] | 65 | 42% (30-54) | +0.02 | -1.22 | -79 |  |
| (0.207, 0.314] | 64 | 39% (28-51) | -0.84 | -2.85 | -182 |  |
| (0.314, 0.875] | 65 | 34% (24-46) | -1.63 | -3.85 | -251 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 65 | 38% (28-51) | -0.69 | -2.43 | -158 |  |
| (2.389, 3.589] | 64 | 45% (34-57) | +0.69 | -1.14 | -73 |  |
| (3.589, 18.762] | 65 | 31% (21-43) | -2.43 | -4.33 | -281 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0972] | 65 | 46% (35-58) | +0.42 | -0.34 | -22 |  |
| (0.0972, 0.145] | 64 | 42% (31-54) | -0.95 | -2.18 | -139 |  |
| (0.145, 0.392] | 65 | 26% (17-38) | -1.92 | -5.40 | -351 | ▼ |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.514] | 23 | 30% (16-51) | -2.58 | -3.44 | -79 |  |
| (-0.514, 0.464] | 22 | 50% (31-69) | -0.52 | -1.02 | -23 |  |
| (0.464, 5.305] | 23 | 65% (45-81) | +0.51 | -0.21 | -5 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.487] | 25 | 44% (27-63) | -0.71 | -1.39 | -35 |  |
| (0.487, 0.694] | 26 | 50% (32-68) | -1.04 | -1.73 | -45 |  |
| (0.694, 1.74] | 24 | 50% (31-69) | -1.41 | -2.23 | -54 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.769] | 25 | 52% (33-70) | -0.71 | -1.16 | -29 |  |
| (0.769, 1.203] | 25 | 40% (23-59) | -1.53 | -2.36 | -59 |  |
| (1.203, 3.566] | 25 | 52% (33-70) | -0.90 | -1.81 | -45 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.35] | 25 | 36% (20-55) | -1.40 | -1.99 | -50 |  |
| (0.35, 0.56] | 25 | 68% (48-83) | +0.55 | -0.18 | -5 | ▲ |
| (0.56, 1.21] | 25 | 40% (23-59) | -2.30 | -3.16 | -79 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.15%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 8% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 87, trail_stop 76, time_stop 29, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0972] | 65 | 32% | 29% | 37% |
| (0.0972, 0.145] | 64 | 47% | 47% | 5% |
| (0.145, 0.392] | 65 | 55% | 42% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
