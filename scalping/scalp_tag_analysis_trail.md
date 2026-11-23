# Scalp signal analysis (trail exits)

_315 tagged trades, 38 trading days (2026-10-01 to 2026-11-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 315 | 43% (38-49) | -0.66 | -2.05 | -645 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +29 | +0.48 | 255 | -673 | -2.64 | -29 |
| skip first 30 min | 4 | -17 | -4.16 | 311 | -628 | -2.02 | +17 |
| skip when SPY is down on the day | 145 | -315 | -2.17 | 170 | -330 | -1.94 | +315 |
| skip when SPY is below its VWAP | 138 | -336 | -2.44 | 177 | -309 | -1.74 | +336 |
| skip when SPY fell over the last 15 min | 104 | -212 | -2.04 | 211 | -433 | -2.05 | +212 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 78 | -225 | -2.89 | 237 | -419 | -1.77 | +225 |
| skip stock not beating SPY over 15 min | 49 | -114 | -2.32 | 266 | -531 | -2.00 | +114 |
| skip afternoon entries (2:00-3:45 PM) | 69 | -249 | -3.61 | 246 | -396 | -1.61 | +249 |
| skip volume spikes above 5x average | 67 | -237 | -3.53 | 248 | -408 | -1.65 | +237 |
| skip when the stop is inside normal noise (range > stop) | 42 | -65 | -1.55 | 273 | -580 | -2.12 | +65 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 49 | -81 | -1.64 | 266 | -564 | -2.12 | +81 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 177 | -226 | -1.28 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 49% (34-64) | -0.41 | -2.04 | -80 |  |
| 60-240 | 128 | 38% (30-47) | -1.31 | -2.48 | -318 |  |
| 240-375 | 88 | 41% (31-51) | -1.52 | -3.13 | -276 |  |
| 375-390 | 60 | 53% (41-65) | +1.85 | +0.48 | +29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 89 | 46% (36-56) | -0.47 | -1.46 | -130 |  |
| -0.2 to 0 | 56 | 41% (29-54) | -1.29 | -3.30 | -185 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 138 | 41% (33-49) | -0.96 | -2.44 | -336 |  |
| above VWAP | 177 | 45% (38-53) | -0.42 | -1.74 | -309 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 105 | 41% (32-51) | -0.35 | -1.45 | -152 |  |
| (0.123, 0.374] | 105 | 50% (41-60) | -0.38 | -1.78 | -187 |  |
| (0.374, 5.591] | 105 | 38% (29-48) | -1.24 | -2.91 | -306 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.134] | 104 | 51% (41-60) | +0.33 | -0.77 | -80 |  |
| (0.134, 0.455] | 103 | 40% (31-49) | -1.03 | -2.72 | -280 |  |
| (0.455, 4.846] | 104 | 39% (31-49) | -1.17 | -2.58 | -268 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.578] | 105 | 48% (38-57) | -0.44 | -1.81 | -190 |  |
| (-0.578, 0.325] | 105 | 44% (35-53) | -0.12 | -1.34 | -141 |  |
| (0.325, 9.926] | 105 | 38% (29-48) | -1.42 | -2.99 | -314 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0561] | 105 | 43% (34-52) | -1.02 | -2.27 | -238 |  |
| (0.0561, 0.127] | 106 | 48% (39-58) | +0.20 | -1.08 | -115 |  |
| (0.127, 0.924] | 104 | 38% (30-48) | -1.16 | -2.81 | -292 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.22] | 105 | 46% (37-55) | +0.12 | -0.87 | -92 |  |
| (0.22, 0.349] | 105 | 46% (37-55) | -0.69 | -2.28 | -240 |  |
| (0.349, 2.663] | 105 | 38% (29-48) | -1.41 | -2.98 | -313 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.38] | 105 | 44% (35-53) | -0.47 | -1.84 | -193 |  |
| (2.38, 3.634] | 105 | 50% (41-60) | +0.60 | -0.83 | -87 |  |
| (3.634, 19.488] | 105 | 35% (27-45) | -2.10 | -3.47 | -365 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 105 | 47% (37-56) | +0.05 | -0.68 | -71 |  |
| (0.104, 0.167] | 105 | 44% (35-53) | -1.01 | -2.20 | -231 |  |
| (0.167, 0.76] | 105 | 39% (30-49) | -1.01 | -3.26 | -342 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.734] | 63 | 41% (30-54) | -1.41 | -2.20 | -139 |  |
| (-0.734, 0.658] | 63 | 52% (40-64) | +0.00 | -0.55 | -35 |  |
| (0.658, 14.989] | 63 | 57% (45-69) | -0.31 | -1.04 | -66 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.552] | 66 | 47% (35-59) | -0.72 | -1.33 | -88 |  |
| (0.552, 0.864] | 65 | 55% (43-67) | -0.41 | -1.12 | -73 | ▲ |
| (0.864, 3.799] | 65 | 48% (36-60) | -0.82 | -1.62 | -105 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.918] | 66 | 50% (38-62) | -1.09 | -1.67 | -110 |  |
| (0.918, 1.644] | 65 | 49% (37-61) | -0.60 | -1.29 | -84 |  |
| (1.644, 9.058] | 65 | 51% (39-63) | -0.26 | -1.11 | -72 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 66 | 44% (33-56) | -0.92 | -1.49 | -98 |  |
| (0.408, 0.624] | 65 | 63% (51-74) | +0.09 | -0.62 | -41 | ▲ |
| (0.624, 4.001] | 65 | 43% (32-55) | -1.12 | -1.95 | -127 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.15%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 137, trail_stop 133, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 105 | 34% | 32% | 29% |
| (0.104, 0.167] | 105 | 48% | 46% | 3% |
| (0.167, 0.76] | 105 | 49% | 49% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
