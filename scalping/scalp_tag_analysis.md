# Scalp signal analysis (fixed exits)

_323 tagged trades, 39 trading days (2026-10-01 to 2026-11-24). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 323 | 40% (35-45) | +0.05 | -1.32 | -425 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +13 | +0.22 | 263 | -438 | -1.67 | -13 |
| skip first 30 min | 4 | -21 | -5.34 | 319 | -404 | -1.27 | +21 |
| skip when SPY is down on the day | 148 | -164 | -1.11 | 175 | -262 | -1.49 | +164 |
| skip when SPY is below its VWAP | 140 | -185 | -1.32 | 183 | -241 | -1.31 | +185 |
| skip when SPY fell over the last 15 min | 107 | -115 | -1.08 | 216 | -310 | -1.44 | +115 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 80 | -182 | -2.28 | 243 | -243 | -1.00 | +182 |
| skip stock not beating SPY over 15 min | 51 | -82 | -1.60 | 272 | -344 | -1.26 | +82 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -227 | -3.25 | 253 | -198 | -0.78 | +227 |
| skip volume spikes above 5x average | 70 | -160 | -2.28 | 253 | -265 | -1.05 | +160 |
| skip when the stop is inside normal noise (range > stop) | 47 | -39 | -0.82 | 276 | -387 | -1.40 | +39 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.73%) | 51 | -62 | -1.21 | 272 | -364 | -1.34 | +62 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -363 | -2.63 | 185 | -62 | -0.34 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 40 | 50% (35-65) | +1.68 | +0.08 | +3 |  |
| 60-240 | 134 | 38% (30-47) | -0.26 | -1.40 | -188 |  |
| 240-375 | 89 | 31% (23-42) | -1.25 | -2.85 | -254 |  |
| 375-390 | 60 | 50% (38-62) | +1.59 | +0.22 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 91 | 41% (31-51) | +0.22 | -0.76 | -69 |  |
| -0.2 to 0 | 57 | 42% (30-55) | +0.33 | -1.65 | -94 |  |
| 0 to 0.2 | 70 | 33% (23-44) | -0.44 | -1.75 | -122 |  |
| > 0.2 | 105 | 43% (34-52) | +0.08 | -1.33 | -139 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 140 | 41% (34-50) | +0.14 | -1.32 | -185 |  |
| above VWAP | 183 | 39% (32-46) | -0.02 | -1.31 | -241 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.121] | 108 | 38% (29-47) | -0.31 | -1.31 | -142 |  |
| (0.121, 0.373] | 107 | 43% (34-52) | +0.37 | -1.07 | -115 |  |
| (0.373, 5.591] | 108 | 39% (30-48) | +0.10 | -1.56 | -169 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.135] | 107 | 48% (38-57) | +0.86 | -0.23 | -25 |  |
| (0.135, 0.451] | 106 | 39% (30-48) | +0.13 | -1.52 | -161 |  |
| (0.451, 4.846] | 106 | 35% (27-44) | -0.66 | -2.05 | -218 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.585] | 108 | 44% (35-54) | +0.52 | -0.83 | -90 |  |
| (-0.585, 0.332] | 107 | 38% (30-48) | +0.19 | -1.03 | -110 |  |
| (0.332, 9.926] | 108 | 37% (29-46) | -0.55 | -2.09 | -226 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0564] | 108 | 39% (30-48) | -0.39 | -1.62 | -175 |  |
| (0.0564, 0.127] | 107 | 46% (37-55) | +0.69 | -0.58 | -62 |  |
| (0.127, 0.924] | 108 | 35% (27-45) | -0.14 | -1.75 | -189 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.225] | 108 | 44% (35-53) | +0.34 | -0.64 | -69 |  |
| (0.225, 0.351] | 107 | 39% (31-49) | -0.03 | -1.69 | -180 |  |
| (0.351, 2.663] | 108 | 37% (29-46) | -0.15 | -1.62 | -175 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.384] | 108 | 35% (27-45) | -0.34 | -1.69 | -182 |  |
| (2.384, 3.635] | 107 | 50% (40-59) | +1.12 | -0.28 | -30 | ▲ |
| (3.635, 19.488] | 108 | 35% (27-45) | -0.62 | -1.97 | -213 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 108 | 45% (36-55) | +0.37 | -0.36 | -39 |  |
| (0.104, 0.167] | 107 | 36% (28-46) | -0.34 | -1.51 | -162 |  |
| (0.167, 0.76] | 108 | 38% (29-47) | +0.12 | -2.08 | -225 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 67 | 31% (22-43) | -1.11 | -1.89 | -126 |  |
| (-0.793, 0.658] | 65 | 48% (36-60) | +0.91 | +0.36 | +23 |  |
| (0.658, 14.989] | 65 | 46% (35-58) | +0.82 | +0.09 | +6 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.55] | 68 | 44% (33-56) | +0.17 | -0.44 | -30 |  |
| (0.55, 0.888] | 68 | 44% (33-56) | +0.29 | -0.41 | -28 |  |
| (0.888, 3.799] | 68 | 35% (25-47) | -0.15 | -0.93 | -64 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.952] | 69 | 43% (32-55) | +0.00 | -0.57 | -39 |  |
| (0.952, 1.692] | 67 | 43% (32-55) | +0.52 | -0.18 | -12 |  |
| (1.692, 9.058] | 68 | 37% (26-49) | -0.21 | -1.04 | -71 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 68 | 37% (26-49) | -0.47 | -1.04 | -71 |  |
| (0.409, 0.633] | 68 | 50% (38-62) | +0.99 | +0.28 | +19 |  |
| (0.633, 4.001] | 68 | 37% (26-49) | -0.21 | -1.03 | -70 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.20%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 162, target 82, time_stop 63, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 108 | 37% | 18% | 40% |
| (0.104, 0.167] | 107 | 56% | 25% | 11% |
| (0.167, 0.76] | 108 | 57% | 33% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
