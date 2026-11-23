# Scalp signal analysis (trail exits)

_313 tagged trades, 38 trading days (2026-10-01 to 2026-11-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 313 | 43% (37-48) | -0.67 | -2.07 | -648 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +29 | +0.48 | 253 | -676 | -2.67 | -29 |
| skip first 30 min | 4 | -17 | -4.16 | 309 | -631 | -2.04 | +17 |
| skip when SPY is down on the day | 143 | -318 | -2.22 | 170 | -330 | -1.94 | +318 |
| skip when SPY is below its VWAP | 138 | -336 | -2.44 | 175 | -311 | -1.78 | +336 |
| skip when SPY fell over the last 15 min | 104 | -212 | -2.04 | 209 | -435 | -2.08 | +212 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 77 | -226 | -2.93 | 236 | -422 | -1.79 | +226 |
| skip stock not beating SPY over 15 min | 49 | -114 | -2.32 | 264 | -534 | -2.02 | +114 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -252 | -3.75 | 246 | -396 | -1.61 | +252 |
| skip volume spikes above 5x average | 67 | -237 | -3.53 | 246 | -411 | -1.67 | +237 |
| skip when the stop is inside normal noise (range > stop) | 42 | -65 | -1.55 | 271 | -582 | -2.15 | +65 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 49 | -80 | -1.64 | 264 | -567 | -2.15 | +80 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 175 | -229 | -1.31 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 49% (34-64) | -0.41 | -2.04 | -80 |  |
| 60-240 | 128 | 38% (30-47) | -1.31 | -2.48 | -318 |  |
| 240-375 | 86 | 40% (30-50) | -1.60 | -3.24 | -278 |  |
| 375-390 | 60 | 53% (41-65) | +1.85 | +0.48 | +29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 89 | 46% (36-56) | -0.47 | -1.46 | -130 |  |
| -0.2 to 0 | 54 | 39% (27-52) | -1.42 | -3.47 | -188 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 138 | 41% (33-49) | -0.96 | -2.44 | -336 |  |
| above VWAP | 175 | 45% (37-52) | -0.45 | -1.78 | -311 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 105 | 41% (32-51) | -0.35 | -1.45 | -152 |  |
| (0.122, 0.374] | 104 | 50% (41-59) | -0.39 | -1.80 | -187 |  |
| (0.374, 5.591] | 104 | 38% (29-47) | -1.28 | -2.97 | -309 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.135] | 103 | 50% (41-60) | +0.31 | -0.80 | -82 |  |
| (0.135, 0.453] | 103 | 40% (31-49) | -1.03 | -2.72 | -280 |  |
| (0.453, 4.846] | 103 | 39% (30-48) | -1.19 | -2.61 | -269 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.572] | 105 | 46% (37-55) | -0.59 | -2.04 | -214 |  |
| (-0.572, 0.338] | 104 | 45% (36-55) | +0.01 | -1.15 | -119 |  |
| (0.338, 9.926] | 104 | 38% (29-47) | -1.44 | -3.02 | -315 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.056] | 105 | 43% (34-52) | -1.02 | -2.27 | -238 |  |
| (0.056, 0.127] | 105 | 48% (38-57) | +0.19 | -1.10 | -115 |  |
| (0.127, 0.924] | 103 | 38% (29-48) | -1.20 | -2.86 | -294 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.218] | 105 | 46% (37-55) | +0.12 | -0.87 | -92 |  |
| (0.218, 0.346] | 104 | 46% (37-56) | -0.65 | -2.25 | -234 |  |
| (0.346, 2.663] | 104 | 37% (28-46) | -1.51 | -3.10 | -322 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.381] | 105 | 43% (34-52) | -0.55 | -1.93 | -202 |  |
| (2.381, 3.637] | 104 | 51% (41-60) | +0.67 | -0.76 | -79 |  |
| (3.637, 19.488] | 104 | 35% (26-44) | -2.14 | -3.53 | -367 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 105 | 47% (37-56) | +0.05 | -0.68 | -71 |  |
| (0.104, 0.166] | 104 | 44% (35-54) | -0.97 | -2.11 | -220 |  |
| (0.166, 0.76] | 104 | 38% (29-47) | -1.12 | -3.43 | -357 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.762] | 63 | 41% (30-54) | -1.41 | -2.20 | -139 |  |
| (-0.762, 0.658] | 63 | 52% (40-64) | +0.00 | -0.55 | -35 |  |
| (0.658, 8.282] | 61 | 56% (43-67) | -0.38 | -1.12 | -69 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.547] | 65 | 48% (36-60) | -0.64 | -1.25 | -81 |  |
| (0.547, 0.856] | 64 | 53% (41-65) | -0.77 | -1.47 | -94 |  |
| (0.856, 3.799] | 65 | 48% (36-60) | -0.63 | -1.43 | -93 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.9] | 65 | 49% (37-61) | -1.15 | -1.73 | -113 |  |
| (0.9, 1.621] | 64 | 52% (40-63) | -0.39 | -1.07 | -68 |  |
| (1.621, 9.058] | 65 | 48% (36-60) | -0.49 | -1.35 | -87 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.401] | 65 | 45% (33-57) | -0.85 | -1.41 | -92 |  |
| (0.401, 0.617] | 64 | 61% (49-72) | -0.09 | -0.80 | -51 | ▲ |
| (0.617, 4.001] | 65 | 43% (32-55) | -1.09 | -1.94 | -126 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.15%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 137, trail_stop 131, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 105 | 34% | 32% | 29% |
| (0.104, 0.166] | 104 | 47% | 46% | 3% |
| (0.166, 0.76] | 104 | 50% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
