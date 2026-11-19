# Scalp signal analysis (trail exits)

_304 tagged trades, 35 trading days (2026-10-01 to 2026-11-18). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 304 | 42% (36-47) | -0.70 | -2.12 | -644 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 59 | +28 | +0.48 | 245 | -673 | -2.75 | -28 |
| skip first 30 min | 4 | -17 | -4.16 | 300 | -628 | -2.09 | +17 |
| skip when SPY is down on the day | 134 | -315 | -2.35 | 170 | -330 | -1.94 | +315 |
| skip when SPY is below its VWAP | 133 | -341 | -2.56 | 171 | -303 | -1.77 | +341 |
| skip when SPY fell over the last 15 min | 103 | -215 | -2.09 | 201 | -430 | -2.14 | +215 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 75 | -225 | -3.00 | 229 | -419 | -1.83 | +225 |
| skip stock not beating SPY over 15 min | 47 | -108 | -2.29 | 257 | -537 | -2.09 | +108 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -252 | -3.75 | 237 | -393 | -1.66 | +252 |
| skip volume spikes above 5x average | 63 | -236 | -3.74 | 241 | -409 | -1.70 | +236 |
| skip when the stop is inside normal noise (range > stop) | 39 | -68 | -1.73 | 265 | -577 | -2.18 | +68 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 46 | -84 | -1.83 | 258 | -560 | -2.17 | +84 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 137 | -419 | -3.06 | 167 | -225 | -1.35 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 47% (32-63) | -0.47 | -2.15 | -82 |  |
| 60-240 | 123 | 37% (29-46) | -1.32 | -2.53 | -311 |  |
| 240-375 | 84 | 38% (28-49) | -1.68 | -3.33 | -280 |  |
| 375-390 | 59 | 53% (40-65) | +1.86 | +0.48 | +28 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 83 | 43% (33-54) | -0.54 | -1.57 | -131 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 133 | 38% (31-47) | -1.05 | -2.56 | -341 |  |
| above VWAP | 171 | 44% (37-52) | -0.42 | -1.77 | -303 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 102 | 40% (31-50) | -0.33 | -1.46 | -149 |  |
| (0.132, 0.374] | 101 | 49% (39-58) | -0.46 | -1.91 | -193 |  |
| (0.374, 5.591] | 101 | 37% (28-46) | -1.30 | -3.00 | -303 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.135] | 100 | 49% (39-59) | +0.27 | -0.85 | -85 |  |
| (0.135, 0.453] | 100 | 40% (31-50) | -0.96 | -2.69 | -269 |  |
| (0.453, 4.846] | 100 | 37% (28-47) | -1.29 | -2.73 | -273 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.537] | 102 | 45% (36-55) | -0.55 | -2.04 | -208 |  |
| (-0.537, 0.34] | 101 | 45% (35-54) | +0.05 | -1.15 | -116 |  |
| (0.34, 9.926] | 101 | 36% (27-45) | -1.59 | -3.18 | -321 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0558] | 102 | 42% (33-52) | -1.03 | -2.30 | -235 |  |
| (0.0558, 0.128] | 101 | 46% (36-55) | +0.12 | -1.21 | -122 |  |
| (0.128, 0.924] | 101 | 38% (29-47) | -1.18 | -2.85 | -288 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 102 | 45% (36-55) | +0.16 | -0.84 | -86 |  |
| (0.217, 0.346] | 101 | 46% (36-55) | -0.65 | -2.30 | -232 |  |
| (0.346, 2.663] | 101 | 35% (26-44) | -1.61 | -3.23 | -326 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.381] | 102 | 41% (32-51) | -0.61 | -2.00 | -204 |  |
| (2.381, 3.611] | 101 | 50% (41-60) | +0.69 | -0.75 | -76 |  |
| (3.611, 19.488] | 101 | 34% (25-43) | -2.18 | -3.61 | -364 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 102 | 47% (38-57) | +0.16 | -0.58 | -60 |  |
| (0.104, 0.166] | 102 | 43% (34-53) | -1.03 | -2.19 | -223 |  |
| (0.166, 0.76] | 100 | 35% (26-45) | -1.23 | -3.62 | -362 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 60 | 40% (29-53) | -1.48 | -2.29 | -137 |  |
| (-0.793, 0.617] | 59 | 51% (38-63) | -0.02 | -0.57 | -34 |  |
| (0.617, 7.522] | 59 | 54% (42-66) | -0.38 | -1.15 | -68 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.553] | 62 | 47% (35-59) | -0.64 | -1.26 | -78 |  |
| (0.553, 0.851] | 61 | 54% (42-66) | -0.64 | -1.35 | -83 |  |
| (0.851, 3.799] | 62 | 44% (32-56) | -0.86 | -1.69 | -105 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.9] | 62 | 47% (35-59) | -1.30 | -1.90 | -118 |  |
| (0.9, 1.638] | 61 | 51% (39-63) | -0.36 | -1.06 | -65 |  |
| (1.638, 9.058] | 62 | 47% (35-59) | -0.48 | -1.34 | -83 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 62 | 44% (32-56) | -0.86 | -1.44 | -89 |  |
| (0.408, 0.617] | 61 | 61% (48-72) | -0.04 | -0.76 | -47 | ▲ |
| (0.617, 4.001] | 62 | 40% (29-53) | -1.24 | -2.10 | -130 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.16%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 135, trail_stop 124, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 102 | 33% | 32% | 29% |
| (0.104, 0.166] | 102 | 48% | 45% | 3% |
| (0.166, 0.76] | 100 | 52% | 45% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
