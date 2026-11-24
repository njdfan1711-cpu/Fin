# Scalp signal analysis (fixed exits)

_321 tagged trades, 39 trading days (2026-10-01 to 2026-11-24). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 321 | 40% (35-46) | +0.09 | -1.29 | -413 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +13 | +0.22 | 261 | -426 | -1.63 | -13 |
| skip first 30 min | 4 | -21 | -5.34 | 317 | -392 | -1.24 | +21 |
| skip when SPY is down on the day | 147 | -158 | -1.07 | 174 | -255 | -1.47 | +158 |
| skip when SPY is below its VWAP | 140 | -185 | -1.32 | 181 | -228 | -1.26 | +185 |
| skip when SPY fell over the last 15 min | 106 | -109 | -1.03 | 215 | -304 | -1.41 | +109 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 79 | -176 | -2.23 | 242 | -237 | -0.98 | +176 |
| skip stock not beating SPY over 15 min | 49 | -70 | -1.42 | 272 | -344 | -1.26 | +70 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -227 | -3.25 | 251 | -186 | -0.74 | +227 |
| skip volume spikes above 5x average | 69 | -154 | -2.23 | 252 | -259 | -1.03 | +154 |
| skip when the stop is inside normal noise (range > stop) | 45 | -26 | -0.59 | 276 | -387 | -1.40 | +26 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 51 | -54 | -1.05 | 270 | -359 | -1.33 | +54 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -363 | -2.63 | 183 | -50 | -0.27 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 51% (36-66) | +1.88 | +0.24 | +9 |  |
| 60-240 | 133 | 38% (31-47) | -0.22 | -1.37 | -182 |  |
| 240-375 | 89 | 31% (23-42) | -1.25 | -2.85 | -254 |  |
| 375-390 | 60 | 50% (38-62) | +1.59 | +0.22 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 91 | 41% (31-51) | +0.22 | -0.76 | -69 |  |
| -0.2 to 0 | 56 | 43% (31-56) | +0.43 | -1.57 | -88 |  |
| 0 to 0.2 | 70 | 33% (23-44) | -0.44 | -1.75 | -122 |  |
| > 0.2 | 104 | 43% (34-53) | +0.14 | -1.28 | -133 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 140 | 41% (34-50) | +0.14 | -1.32 | -185 |  |
| above VWAP | 181 | 39% (32-46) | +0.04 | -1.26 | -228 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 107 | 39% (31-49) | -0.11 | -1.19 | -128 |  |
| (0.123, 0.374] | 108 | 44% (35-53) | +0.39 | -0.98 | -106 |  |
| (0.374, 5.591] | 106 | 38% (29-47) | -0.03 | -1.69 | -179 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.134] | 106 | 47% (38-57) | +0.82 | -0.27 | -29 |  |
| (0.134, 0.449] | 105 | 40% (31-50) | +0.29 | -1.38 | -145 |  |
| (0.449, 4.846] | 106 | 35% (27-44) | -0.67 | -2.06 | -218 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.578] | 107 | 45% (36-54) | +0.57 | -0.78 | -84 |  |
| (-0.578, 0.339] | 107 | 39% (31-49) | +0.25 | -0.96 | -103 |  |
| (0.339, 9.926] | 107 | 36% (28-46) | -0.57 | -2.12 | -227 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0561] | 107 | 39% (31-49) | -0.34 | -1.58 | -169 |  |
| (0.0561, 0.127] | 108 | 45% (36-55) | +0.66 | -0.61 | -66 |  |
| (0.127, 0.924] | 106 | 36% (27-45) | -0.06 | -1.69 | -179 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.224] | 107 | 43% (34-52) | +0.25 | -0.73 | -79 |  |
| (0.224, 0.351] | 107 | 40% (31-50) | +0.10 | -1.54 | -165 |  |
| (0.351, 2.663] | 107 | 37% (29-47) | -0.10 | -1.58 | -169 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.38] | 107 | 36% (27-45) | -0.29 | -1.64 | -176 |  |
| (2.38, 3.634] | 107 | 50% (40-59) | +1.12 | -0.28 | -30 | ▲ |
| (3.634, 19.488] | 107 | 36% (27-45) | -0.57 | -1.93 | -207 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 107 | 46% (37-55) | +0.42 | -0.31 | -33 |  |
| (0.104, 0.167] | 107 | 36% (28-46) | -0.33 | -1.50 | -161 |  |
| (0.167, 0.76] | 107 | 38% (30-48) | +0.17 | -2.05 | -219 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.773] | 65 | 32% (22-44) | -0.97 | -1.76 | -114 |  |
| (-0.773, 0.658] | 65 | 48% (36-60) | +0.91 | +0.36 | +23 |  |
| (0.658, 14.989] | 65 | 46% (35-58) | +0.82 | +0.09 | +6 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.545] | 68 | 44% (33-56) | +0.17 | -0.44 | -30 |  |
| (0.545, 0.884] | 67 | 43% (32-55) | +0.15 | -0.56 | -37 |  |
| (0.884, 3.799] | 67 | 37% (27-49) | +0.16 | -0.62 | -42 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.952] | 69 | 43% (32-55) | +0.00 | -0.57 | -39 |  |
| (0.952, 1.669] | 66 | 44% (33-56) | +0.62 | -0.08 | -5 |  |
| (1.669, 9.058] | 67 | 37% (27-49) | -0.13 | -0.97 | -65 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 68 | 37% (26-49) | -0.47 | -1.04 | -71 |  |
| (0.408, 0.628] | 67 | 51% (39-62) | +1.09 | +0.38 | +25 |  |
| (0.628, 4.001] | 67 | 37% (27-49) | -0.13 | -0.95 | -64 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.20%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 160, target 82, time_stop 63, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 107 | 36% | 18% | 40% |
| (0.104, 0.167] | 107 | 56% | 25% | 11% |
| (0.167, 0.76] | 107 | 57% | 34% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
