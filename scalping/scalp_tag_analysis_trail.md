# Scalp signal analysis (trail exits)

_323 tagged trades, 39 trading days (2026-10-01 to 2026-11-24). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 323 | 44% (39-49) | -0.60 | -1.97 | -636 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +29 | +0.48 | 263 | -665 | -2.53 | -29 |
| skip first 30 min | 4 | -17 | -4.16 | 319 | -619 | -1.94 | +17 |
| skip when SPY is down on the day | 148 | -304 | -2.05 | 175 | -333 | -1.90 | +304 |
| skip when SPY is below its VWAP | 140 | -327 | -2.33 | 183 | -309 | -1.69 | +327 |
| skip when SPY fell over the last 15 min | 108 | -208 | -1.93 | 215 | -428 | -1.99 | +208 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 80 | -218 | -2.73 | 243 | -418 | -1.72 | +218 |
| skip stock not beating SPY over 15 min | 51 | -118 | -2.31 | 272 | -518 | -1.90 | +118 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -251 | -3.58 | 253 | -385 | -1.52 | +251 |
| skip volume spikes above 5x average | 70 | -236 | -3.38 | 253 | -400 | -1.58 | +236 |
| skip when the stop is inside normal noise (range > stop) | 47 | -59 | -1.26 | 276 | -577 | -2.09 | +59 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.73%) | 51 | -83 | -1.63 | 272 | -553 | -2.03 | +83 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 185 | -217 | -1.17 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 40 | 48% (33-63) | -0.54 | -2.15 | -86 |  |
| 60-240 | 134 | 41% (33-50) | -1.10 | -2.25 | -301 |  |
| 240-375 | 89 | 40% (31-51) | -1.52 | -3.12 | -278 |  |
| 375-390 | 60 | 53% (41-65) | +1.85 | +0.48 | +29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 91 | 47% (37-57) | -0.34 | -1.33 | -121 |  |
| -0.2 to 0 | 57 | 42% (30-55) | -1.23 | -3.21 | -183 |  |
| 0 to 0.2 | 70 | 36% (26-47) | -1.54 | -2.84 | -199 |  |
| > 0.2 | 105 | 48% (38-57) | +0.14 | -1.27 | -134 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 140 | 41% (34-50) | -0.87 | -2.33 | -327 |  |
| above VWAP | 183 | 46% (39-53) | -0.40 | -1.69 | -309 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.121] | 108 | 43% (34-52) | -0.41 | -1.41 | -152 |  |
| (0.121, 0.373] | 107 | 50% (41-60) | -0.28 | -1.72 | -184 |  |
| (0.373, 5.591] | 108 | 39% (30-48) | -1.12 | -2.78 | -300 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.135] | 107 | 51% (42-61) | +0.38 | -0.71 | -76 |  |
| (0.135, 0.451] | 106 | 41% (32-50) | -1.02 | -2.67 | -283 |  |
| (0.451, 4.846] | 106 | 41% (32-50) | -1.07 | -2.46 | -261 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.585] | 108 | 49% (40-58) | -0.31 | -1.66 | -179 |  |
| (-0.585, 0.332] | 107 | 44% (35-53) | -0.14 | -1.35 | -145 |  |
| (0.332, 9.926] | 108 | 39% (30-48) | -1.35 | -2.89 | -313 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0564] | 108 | 43% (34-52) | -1.02 | -2.25 | -243 |  |
| (0.0564, 0.127] | 107 | 49% (39-58) | +0.22 | -1.05 | -112 |  |
| (0.127, 0.924] | 108 | 41% (32-50) | -1.00 | -2.61 | -282 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.225] | 108 | 45% (36-55) | +0.02 | -0.96 | -104 |  |
| (0.225, 0.351] | 107 | 47% (38-56) | -0.57 | -2.22 | -238 |  |
| (0.351, 2.663] | 108 | 40% (31-49) | -1.26 | -2.73 | -295 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.384] | 108 | 44% (35-53) | -0.50 | -1.85 | -200 |  |
| (2.384, 3.635] | 107 | 52% (43-62) | +0.73 | -0.67 | -72 |  |
| (3.635, 19.488] | 108 | 36% (28-46) | -2.02 | -3.37 | -364 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 108 | 47% (38-57) | +0.09 | -0.63 | -69 |  |
| (0.104, 0.167] | 107 | 44% (35-53) | -1.03 | -2.20 | -235 |  |
| (0.167, 0.76] | 108 | 41% (32-50) | -0.87 | -3.08 | -332 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 67 | 43% (32-55) | -1.27 | -2.05 | -137 |  |
| (-0.793, 0.658] | 65 | 52% (40-64) | -0.02 | -0.57 | -37 |  |
| (0.658, 14.989] | 65 | 58% (46-70) | -0.14 | -0.87 | -56 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.55] | 68 | 49% (37-60) | -0.54 | -1.16 | -79 |  |
| (0.55, 0.888] | 68 | 56% (44-67) | -0.44 | -1.14 | -77 | ▲ |
| (0.888, 3.799] | 68 | 49% (37-60) | -0.71 | -1.49 | -101 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.952] | 69 | 51% (39-62) | -1.00 | -1.56 | -108 |  |
| (0.952, 1.692] | 67 | 49% (38-61) | -0.62 | -1.32 | -88 |  |
| (1.692, 9.058] | 68 | 53% (41-64) | -0.06 | -0.90 | -61 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 68 | 44% (33-56) | -0.90 | -1.46 | -99 |  |
| (0.409, 0.633] | 68 | 62% (50-72) | -0.04 | -0.75 | -51 | ▲ |
| (0.633, 4.001] | 68 | 47% (36-59) | -0.75 | -1.57 | -107 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.15%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 43%
- Exit mix: trail_stop 139, stop 138, time_stop 36, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 108 | 33% | 33% | 29% |
| (0.104, 0.167] | 107 | 48% | 46% | 3% |
| (0.167, 0.76] | 108 | 47% | 50% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
