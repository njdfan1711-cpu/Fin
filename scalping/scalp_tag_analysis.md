# Scalp signal analysis (fixed exits)

_270 tagged trades, 32 trading days (2026-10-01 to 2026-11-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 270 | 40% (35-46) | +0.11 | -1.40 | -379 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 48 | -28 | -0.58 | 222 | -351 | -1.58 | +28 |
| skip first 30 min | 3 | -15 | -4.90 | 267 | -364 | -1.36 | +15 |
| skip when SPY is down on the day | 101 | -110 | -1.09 | 169 | -268 | -1.59 | +110 |
| skip when SPY is below its VWAP | 117 | -187 | -1.60 | 153 | -192 | -1.25 | +187 |
| skip when SPY fell over the last 15 min | 99 | -141 | -1.42 | 171 | -238 | -1.39 | +141 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 67 | -177 | -2.65 | 203 | -201 | -0.99 | +177 |
| skip stock not beating SPY over 15 min | 44 | -50 | -1.14 | 226 | -328 | -1.45 | +50 |
| skip afternoon entries (2:00-3:45 PM) | 60 | -212 | -3.53 | 210 | -167 | -0.79 | +212 |
| skip volume spikes above 5x average | 54 | -117 | -2.17 | 216 | -261 | -1.21 | +117 |
| skip when the stop is inside normal noise (range > stop) | 27 | -13 | -0.48 | 243 | -366 | -1.51 | +13 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 38 | -29 | -0.76 | 232 | -350 | -1.51 | +29 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -326 | -2.63 | 146 | -52 | -0.36 | +326 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 51% (36-67) | +1.89 | +0.19 | +7 |  |
| 60-240 | 109 | 39% (31-49) | +0.02 | -1.27 | -138 |  |
| 240-375 | 76 | 33% (23-44) | -1.16 | -2.89 | -220 |  |
| 375-390 | 48 | 46% (33-60) | +0.92 | -0.58 | -28 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 50 | 46% (33-60) | +0.98 | -0.25 | -13 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 68 | 32% (22-44) | -0.51 | -1.83 | -125 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 117 | 41% (33-50) | +0.02 | -1.60 | -187 |  |
| above VWAP | 153 | 40% (32-48) | +0.17 | -1.25 | -192 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 90 | 39% (29-49) | -0.04 | -1.24 | -111 |  |
| (0.129, 0.379] | 90 | 46% (36-56) | +0.50 | -1.02 | -92 |  |
| (0.379, 5.591] | 90 | 37% (27-47) | -0.14 | -1.95 | -175 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.119] | 89 | 46% (36-56) | +0.70 | -0.48 | -42 |  |
| (0.119, 0.441] | 89 | 42% (32-52) | +0.54 | -1.32 | -118 |  |
| (0.441, 4.846] | 89 | 35% (26-45) | -0.77 | -2.29 | -204 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 90 | 44% (35-55) | +0.57 | -1.13 | -101 |  |
| (-0.367, 0.421] | 90 | 44% (35-55) | +0.83 | -0.28 | -26 |  |
| (0.421, 9.926] | 90 | 32% (23-42) | -1.08 | -2.79 | -251 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 90 | 40% (30-50) | -0.21 | -1.55 | -140 |  |
| (0.0559, 0.126] | 90 | 46% (36-56) | +0.64 | -0.79 | -71 |  |
| (0.126, 0.924] | 90 | 36% (26-46) | -0.11 | -1.87 | -168 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.215] | 90 | 42% (33-53) | +0.15 | -0.90 | -81 |  |
| (0.215, 0.339] | 90 | 43% (34-54) | +0.56 | -1.19 | -107 |  |
| (0.339, 2.663] | 90 | 36% (26-46) | -0.39 | -2.12 | -191 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.354] | 90 | 38% (28-48) | -0.01 | -1.47 | -132 |  |
| (2.354, 3.618] | 90 | 47% (37-57) | +0.68 | -0.84 | -75 |  |
| (3.618, 19.488] | 90 | 37% (27-47) | -0.35 | -1.90 | -171 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.103] | 90 | 48% (38-58) | +0.59 | -0.17 | -16 |  |
| (0.103, 0.162] | 90 | 34% (25-45) | -0.55 | -1.72 | -155 |  |
| (0.162, 0.76] | 90 | 39% (29-49) | +0.28 | -2.31 | -208 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.938] | 48 | 35% (23-50) | -0.52 | -1.30 | -62 |  |
| (-0.938, 0.615] | 48 | 50% (36-64) | +1.16 | +0.57 | +27 |  |
| (0.615, 7.522] | 48 | 44% (31-58) | +0.42 | -0.32 | -15 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 51 | 45% (32-59) | +0.17 | -0.47 | -24 |  |
| (0.533, 0.837] | 52 | 42% (30-56) | +0.18 | -0.51 | -26 |  |
| (0.837, 3.799] | 48 | 40% (27-54) | +0.32 | -0.50 | -24 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.849] | 51 | 43% (31-57) | +0.17 | -0.41 | -21 |  |
| (0.849, 1.457] | 50 | 44% (31-58) | +0.69 | -0.01 | -0 |  |
| (1.457, 9.058] | 50 | 40% (28-54) | -0.21 | -1.07 | -53 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.377] | 51 | 41% (29-55) | -0.03 | -0.61 | -31 |  |
| (0.377, 0.594] | 50 | 46% (33-60) | +0.53 | -0.20 | -10 |  |
| (0.594, 4.001] | 50 | 40% (28-54) | +0.16 | -0.67 | -34 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 132, target 69, time_stop 56, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.103] | 90 | 33% | 17% | 43% |
| (0.103, 0.162] | 90 | 58% | 26% | 11% |
| (0.162, 0.76] | 90 | 56% | 34% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
