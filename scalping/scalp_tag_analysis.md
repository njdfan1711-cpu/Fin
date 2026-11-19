# Scalp signal analysis (fixed exits)

_303 tagged trades, 35 trading days (2026-10-01 to 2026-11-18). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 303 | 39% (34-45) | -0.04 | -1.47 | -444 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 58 | +26 | +0.45 | 245 | -471 | -1.92 | -26 |
| skip first 30 min | 4 | -21 | -5.34 | 299 | -423 | -1.41 | +21 |
| skip when SPY is down on the day | 133 | -169 | -1.27 | 170 | -275 | -1.62 | +169 |
| skip when SPY is below its VWAP | 133 | -182 | -1.37 | 170 | -262 | -1.54 | +182 |
| skip when SPY fell over the last 15 min | 102 | -131 | -1.29 | 201 | -313 | -1.56 | +131 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 75 | -184 | -2.45 | 228 | -260 | -1.14 | +184 |
| skip stock not beating SPY over 15 min | 47 | -57 | -1.20 | 256 | -388 | -1.51 | +57 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -244 | -3.64 | 236 | -200 | -0.85 | +244 |
| skip volume spikes above 5x average | 63 | -172 | -2.74 | 240 | -272 | -1.13 | +172 |
| skip when the stop is inside normal noise (range > stop) | 38 | -53 | -1.39 | 265 | -391 | -1.48 | +53 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 46 | -64 | -1.39 | 257 | -380 | -1.48 | +64 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 136 | -351 | -2.58 | 167 | -94 | -0.56 | +351 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 50% (35-65) | +1.69 | +0.01 | +0 |  |
| 60-240 | 123 | 36% (28-45) | -0.52 | -1.73 | -213 |  |
| 240-375 | 84 | 31% (22-41) | -1.42 | -3.08 | -258 |  |
| 375-390 | 58 | 52% (39-64) | +1.84 | +0.45 | +26 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 82 | 40% (30-51) | +0.16 | -0.87 | -72 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 133 | 41% (33-50) | +0.14 | -1.37 | -182 |  |
| above VWAP | 170 | 38% (31-45) | -0.18 | -1.54 | -262 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 101 | 39% (30-48) | -0.11 | -1.24 | -125 |  |
| (0.129, 0.374] | 101 | 43% (33-52) | +0.17 | -1.27 | -128 |  |
| (0.374, 5.591] | 101 | 37% (28-46) | -0.18 | -1.89 | -191 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.134] | 100 | 47% (38-57) | +0.77 | -0.36 | -36 |  |
| (0.134, 0.449] | 99 | 39% (30-49) | +0.24 | -1.50 | -149 |  |
| (0.449, 4.846] | 100 | 33% (25-43) | -0.94 | -2.39 | -239 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.53] | 101 | 43% (33-52) | +0.19 | -1.29 | -131 |  |
| (-0.53, 0.348] | 101 | 41% (32-50) | +0.48 | -0.72 | -72 |  |
| (0.348, 9.926] | 101 | 35% (26-44) | -0.80 | -2.39 | -241 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0558] | 101 | 39% (30-48) | -0.46 | -1.74 | -176 |  |
| (0.0558, 0.129] | 101 | 45% (35-54) | +0.60 | -0.73 | -74 |  |
| (0.129, 0.924] | 101 | 35% (26-44) | -0.26 | -1.93 | -195 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 101 | 44% (34-53) | +0.38 | -0.63 | -63 |  |
| (0.217, 0.347] | 101 | 41% (32-50) | +0.14 | -1.50 | -152 |  |
| (0.347, 2.663] | 101 | 34% (25-43) | -0.65 | -2.27 | -229 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.386] | 101 | 36% (27-45) | -0.32 | -1.72 | -174 |  |
| (2.386, 3.618] | 101 | 49% (39-58) | +1.01 | -0.44 | -44 |  |
| (3.618, 19.488] | 101 | 34% (25-43) | -0.81 | -2.24 | -226 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 101 | 47% (37-56) | +0.49 | -0.25 | -26 |  |
| (0.104, 0.166] | 101 | 35% (26-44) | -0.58 | -1.74 | -176 |  |
| (0.166, 0.76] | 101 | 37% (28-46) | -0.04 | -2.40 | -242 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 60 | 32% (21-44) | -1.16 | -1.96 | -118 |  |
| (-0.793, 0.616] | 58 | 48% (36-61) | +1.13 | +0.58 | +34 |  |
| (0.616, 7.522] | 59 | 42% (31-55) | +0.22 | -0.54 | -32 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.552] | 62 | 44% (32-56) | +0.08 | -0.55 | -34 |  |
| (0.552, 0.843] | 61 | 43% (31-55) | +0.08 | -0.63 | -39 |  |
| (0.843, 3.799] | 61 | 34% (24-47) | -0.29 | -1.11 | -68 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.891] | 62 | 42% (30-54) | -0.08 | -0.68 | -42 |  |
| (0.891, 1.624] | 61 | 46% (34-58) | +0.83 | +0.13 | +8 |  |
| (1.624, 9.058] | 61 | 33% (22-45) | -0.88 | -1.74 | -106 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 62 | 39% (28-51) | -0.20 | -0.78 | -48 |  |
| (0.408, 0.616] | 61 | 49% (37-61) | +0.86 | +0.13 | +8 |  |
| (0.616, 4.001] | 61 | 33% (22-45) | -0.79 | -1.64 | -100 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 153, target 75, time_stop 59, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 101 | 36% | 18% | 41% |
| (0.104, 0.166] | 101 | 57% | 24% | 11% |
| (0.166, 0.76] | 101 | 58% | 33% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
