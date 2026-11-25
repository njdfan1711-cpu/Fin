# Scalp signal analysis (fixed exits)

_327 tagged trades, 40 trading days (2026-10-01 to 2026-11-25). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 327 | 39% (34-45) | -0.02 | -1.38 | -451 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +0 | +0.01 | 265 | -451 | -1.70 | -0 |
| skip first 30 min | 4 | -21 | -5.34 | 323 | -429 | -1.33 | +21 |
| skip when SPY is down on the day | 150 | -176 | -1.18 | 177 | -274 | -1.55 | +176 |
| skip when SPY is below its VWAP | 141 | -191 | -1.35 | 186 | -260 | -1.40 | +191 |
| skip when SPY fell over the last 15 min | 107 | -115 | -1.08 | 220 | -336 | -1.53 | +115 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 81 | -172 | -2.13 | 246 | -278 | -1.13 | +172 |
| skip stock not beating SPY over 15 min | 51 | -82 | -1.60 | 276 | -369 | -1.34 | +82 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -227 | -3.25 | 257 | -223 | -0.87 | +227 |
| skip volume spikes above 5x average | 70 | -160 | -2.28 | 257 | -291 | -1.13 | +160 |
| skip when the stop is inside normal noise (range > stop) | 47 | -39 | -0.82 | 280 | -412 | -1.47 | +39 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 52 | -60 | -1.15 | 275 | -391 | -1.42 | +60 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -363 | -2.63 | 189 | -88 | -0.46 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 40 | 50% (35-65) | +1.68 | +0.08 | +3 |  |
| 60-240 | 136 | 38% (30-46) | -0.34 | -1.48 | -201 |  |
| 240-375 | 89 | 31% (23-42) | -1.25 | -2.85 | -254 |  |
| 375-390 | 62 | 48% (36-61) | +1.36 | +0.01 | +0 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 93 | 40% (30-50) | +0.09 | -0.88 | -82 |  |
| -0.2 to 0 | 57 | 42% (30-55) | +0.33 | -1.65 | -94 |  |
| 0 to 0.2 | 70 | 33% (23-44) | -0.44 | -1.75 | -122 |  |
| > 0.2 | 107 | 42% (33-52) | -0.02 | -1.42 | -152 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 141 | 41% (33-49) | +0.10 | -1.35 | -191 |  |
| above VWAP | 186 | 38% (31-45) | -0.11 | -1.40 | -260 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.119] | 109 | 38% (29-47) | -0.36 | -1.35 | -147 |  |
| (0.119, 0.37] | 109 | 42% (33-52) | +0.26 | -1.18 | -128 |  |
| (0.37, 5.591] | 109 | 39% (30-48) | +0.05 | -1.60 | -175 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.137] | 108 | 47% (38-57) | +0.80 | -0.29 | -31 |  |
| (0.137, 0.446] | 107 | 38% (30-48) | +0.07 | -1.56 | -167 |  |
| (0.446, 4.846] | 108 | 34% (26-44) | -0.76 | -2.14 | -231 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.583] | 109 | 44% (35-53) | +0.46 | -0.88 | -96 |  |
| (-0.583, 0.3] | 109 | 38% (29-47) | +0.08 | -1.12 | -122 |  |
| (0.3, 9.926] | 109 | 37% (28-46) | -0.60 | -2.13 | -232 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 109 | 38% (29-47) | -0.52 | -1.74 | -190 |  |
| (0.0559, 0.126] | 109 | 45% (36-54) | +0.54 | -0.72 | -78 |  |
| (0.126, 0.924] | 109 | 36% (27-45) | -0.07 | -1.67 | -182 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.224] | 109 | 42% (33-52) | +0.14 | -0.84 | -92 |  |
| (0.224, 0.351] | 109 | 39% (31-49) | +0.00 | -1.63 | -177 |  |
| (0.351, 2.663] | 109 | 37% (28-46) | -0.20 | -1.67 | -182 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.386] | 109 | 35% (27-44) | -0.39 | -1.73 | -189 |  |
| (2.386, 3.618] | 109 | 49% (39-58) | +1.00 | -0.39 | -42 |  |
| (3.618, 19.488] | 109 | 35% (27-44) | -0.67 | -2.02 | -220 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 109 | 45% (36-54) | +0.31 | -0.42 | -46 |  |
| (0.104, 0.167] | 109 | 36% (27-45) | -0.43 | -1.59 | -174 |  |
| (0.167, 0.76] | 109 | 38% (29-47) | +0.06 | -2.12 | -231 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.887] | 67 | 30% (20-42) | -1.33 | -2.11 | -141 |  |
| (-0.887, 0.644] | 67 | 46% (35-58) | +0.75 | +0.19 | +13 |  |
| (0.644, 14.989] | 67 | 46% (35-58) | +0.82 | +0.09 | +6 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.547] | 70 | 43% (32-55) | -0.00 | -0.61 | -43 |  |
| (0.547, 0.884] | 69 | 42% (31-54) | -0.02 | -0.72 | -50 |  |
| (0.884, 3.799] | 69 | 36% (26-48) | -0.01 | -0.78 | -54 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.952] | 70 | 43% (32-55) | -0.08 | -0.65 | -45 |  |
| (0.952, 1.669] | 69 | 42% (31-54) | +0.34 | -0.35 | -24 |  |
| (1.669, 9.058] | 69 | 36% (26-48) | -0.29 | -1.12 | -77 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 70 | 37% (27-49) | -0.48 | -1.07 | -75 |  |
| (0.409, 0.624] | 69 | 48% (36-59) | +0.75 | +0.06 | +4 |  |
| (0.624, 4.001] | 69 | 36% (26-48) | -0.29 | -1.11 | -76 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.20%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 166, target 82, time_stop 63, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 109 | 38% | 17% | 39% |
| (0.104, 0.167] | 109 | 57% | 25% | 11% |
| (0.167, 0.76] | 109 | 58% | 33% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
