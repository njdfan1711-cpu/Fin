# Scalp signal analysis (trail exits)

_309 tagged trades, 38 trading days (2026-10-01 to 2026-11-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 309 | 42% (37-48) | -0.69 | -2.09 | -646 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +29 | +0.48 | 249 | -675 | -2.71 | -29 |
| skip first 30 min | 4 | -17 | -4.16 | 305 | -630 | -2.06 | +17 |
| skip when SPY is down on the day | 139 | -317 | -2.28 | 170 | -330 | -1.94 | +317 |
| skip when SPY is below its VWAP | 136 | -339 | -2.49 | 173 | -307 | -1.78 | +339 |
| skip when SPY fell over the last 15 min | 103 | -215 | -2.09 | 206 | -432 | -2.10 | +215 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 76 | -228 | -3.00 | 233 | -418 | -1.79 | +228 |
| skip stock not beating SPY over 15 min | 48 | -107 | -2.23 | 261 | -539 | -2.07 | +107 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -252 | -3.75 | 242 | -395 | -1.63 | +252 |
| skip volume spikes above 5x average | 65 | -240 | -3.69 | 244 | -407 | -1.67 | +240 |
| skip when the stop is inside normal noise (range > stop) | 41 | -65 | -1.60 | 268 | -581 | -2.17 | +65 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 48 | -83 | -1.72 | 261 | -564 | -2.16 | +83 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 171 | -227 | -1.33 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 49% (34-64) | -0.41 | -2.04 | -80 |  |
| 60-240 | 124 | 37% (29-46) | -1.36 | -2.56 | -317 |  |
| 240-375 | 86 | 40% (30-50) | -1.60 | -3.24 | -278 |  |
| 375-390 | 60 | 53% (41-65) | +1.85 | +0.48 | +29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 88 | 45% (35-56) | -0.51 | -1.51 | -133 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 136 | 40% (32-48) | -1.00 | -2.49 | -339 |  |
| above VWAP | 173 | 45% (37-52) | -0.44 | -1.78 | -307 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 103 | 40% (31-49) | -0.39 | -1.50 | -155 |  |
| (0.129, 0.374] | 103 | 50% (41-60) | -0.34 | -1.75 | -181 |  |
| (0.374, 5.591] | 103 | 37% (28-47) | -1.32 | -3.02 | -311 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.137] | 102 | 50% (40-60) | +0.33 | -0.79 | -81 |  |
| (0.137, 0.455] | 101 | 40% (31-49) | -1.04 | -2.75 | -278 |  |
| (0.455, 4.846] | 102 | 38% (29-48) | -1.23 | -2.66 | -271 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.573] | 103 | 46% (36-55) | -0.57 | -2.04 | -210 |  |
| (-0.573, 0.339] | 103 | 45% (35-54) | -0.02 | -1.18 | -121 |  |
| (0.339, 9.926] | 103 | 37% (28-47) | -1.47 | -3.06 | -315 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0558] | 103 | 42% (33-51) | -1.12 | -2.39 | -246 |  |
| (0.0558, 0.127] | 103 | 48% (38-57) | +0.27 | -1.03 | -106 |  |
| (0.127, 0.924] | 103 | 38% (29-48) | -1.20 | -2.86 | -294 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.218] | 103 | 46% (36-55) | +0.17 | -0.83 | -86 |  |
| (0.218, 0.347] | 103 | 46% (36-55) | -0.68 | -2.29 | -236 |  |
| (0.347, 2.663] | 103 | 36% (27-46) | -1.55 | -3.15 | -325 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.377] | 104 | 43% (34-53) | -0.50 | -1.88 | -196 |  |
| (2.377, 3.618] | 102 | 50% (40-60) | +0.63 | -0.81 | -82 |  |
| (3.618, 19.488] | 103 | 34% (26-44) | -2.17 | -3.58 | -368 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 103 | 48% (38-57) | +0.17 | -0.57 | -59 |  |
| (0.104, 0.166] | 104 | 43% (34-53) | -1.05 | -2.19 | -228 |  |
| (0.166, 0.76] | 102 | 36% (28-46) | -1.17 | -3.52 | -359 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 62 | 42% (30-54) | -1.39 | -2.19 | -136 |  |
| (-0.793, 0.62] | 60 | 52% (39-64) | -0.00 | -0.56 | -33 |  |
| (0.62, 7.53] | 61 | 54% (42-66) | -0.43 | -1.18 | -72 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.552] | 64 | 47% (35-59) | -0.69 | -1.31 | -84 |  |
| (0.552, 0.855] | 63 | 54% (42-66) | -0.69 | -1.39 | -88 |  |
| (0.855, 3.799] | 63 | 46% (34-58) | -0.71 | -1.52 | -96 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.891] | 64 | 48% (37-60) | -1.21 | -1.80 | -115 |  |
| (0.891, 1.644] | 63 | 49% (37-61) | -0.53 | -1.23 | -77 |  |
| (1.644, 9.058] | 63 | 49% (37-61) | -0.33 | -1.19 | -75 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 64 | 44% (32-56) | -0.90 | -1.48 | -95 |  |
| (0.408, 0.618] | 63 | 62% (50-73) | +0.04 | -0.68 | -43 | ▲ |
| (0.618, 4.001] | 63 | 41% (30-54) | -1.22 | -2.07 | -131 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.15%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 136, trail_stop 128, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 103 | 33% | 33% | 29% |
| (0.104, 0.166] | 104 | 48% | 45% | 3% |
| (0.166, 0.76] | 102 | 51% | 46% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
