# Scalp signal analysis (fixed exits)

_297 tagged trades, 34 trading days (2026-10-01 to 2026-11-17). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 297 | 39% (34-45) | -0.03 | -1.47 | -438 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 56 | +10 | +0.17 | 241 | -448 | -1.86 | -10 |
| skip first 30 min | 4 | -21 | -5.34 | 293 | -417 | -1.42 | +21 |
| skip when SPY is down on the day | 127 | -163 | -1.28 | 170 | -275 | -1.62 | +163 |
| skip when SPY is below its VWAP | 132 | -191 | -1.45 | 165 | -247 | -1.50 | +191 |
| skip when SPY fell over the last 15 min | 102 | -131 | -1.29 | 195 | -307 | -1.57 | +131 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 73 | -196 | -2.68 | 224 | -242 | -1.08 | +196 |
| skip stock not beating SPY over 15 min | 47 | -57 | -1.20 | 250 | -381 | -1.53 | +57 |
| skip afternoon entries (2:00-3:45 PM) | 66 | -238 | -3.60 | 231 | -200 | -0.87 | +238 |
| skip volume spikes above 5x average | 60 | -156 | -2.59 | 237 | -282 | -1.19 | +156 |
| skip when the stop is inside normal noise (range > stop) | 37 | -62 | -1.66 | 260 | -376 | -1.45 | +62 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 45 | -73 | -1.61 | 252 | -365 | -1.45 | +73 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 135 | -359 | -2.66 | 162 | -78 | -0.48 | +359 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 50% (35-65) | +1.69 | +0.01 | +0 |  |
| 60-240 | 120 | 37% (29-46) | -0.41 | -1.63 | -196 |  |
| 240-375 | 83 | 31% (22-42) | -1.36 | -3.04 | -252 |  |
| 375-390 | 56 | 50% (37-63) | +1.57 | +0.17 | +10 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 76 | 41% (30-52) | +0.21 | -0.86 | -65 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 132 | 41% (33-49) | +0.06 | -1.45 | -191 |  |
| above VWAP | 165 | 38% (31-46) | -0.11 | -1.50 | -247 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 99 | 39% (30-49) | -0.01 | -1.15 | -114 |  |
| (0.129, 0.375] | 99 | 42% (33-52) | +0.14 | -1.33 | -132 |  |
| (0.375, 5.591] | 99 | 36% (28-46) | -0.23 | -1.94 | -192 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.128] | 98 | 47% (37-57) | +0.74 | -0.40 | -39 |  |
| (0.128, 0.446] | 97 | 41% (32-51) | +0.52 | -1.25 | -121 |  |
| (0.446, 4.846] | 98 | 32% (23-41) | -1.16 | -2.62 | -256 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.506] | 99 | 42% (33-52) | +0.17 | -1.38 | -136 |  |
| (-0.506, 0.364] | 99 | 40% (31-50) | +0.43 | -0.74 | -73 |  |
| (0.364, 9.926] | 99 | 35% (27-45) | -0.70 | -2.31 | -229 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0558] | 99 | 39% (30-49) | -0.36 | -1.66 | -164 |  |
| (0.0558, 0.129] | 99 | 44% (35-54) | +0.57 | -0.77 | -76 |  |
| (0.129, 0.924] | 99 | 34% (26-44) | -0.31 | -2.00 | -198 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 99 | 44% (35-54) | +0.50 | -0.52 | -51 |  |
| (0.217, 0.346] | 99 | 41% (32-51) | +0.26 | -1.40 | -139 |  |
| (0.346, 2.663] | 99 | 32% (24-42) | -0.86 | -2.50 | -248 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.377] | 100 | 36% (27-46) | -0.27 | -1.67 | -167 |  |
| (2.377, 3.61] | 98 | 47% (37-57) | +0.82 | -0.65 | -64 |  |
| (3.61, 19.488] | 99 | 35% (27-45) | -0.64 | -2.09 | -207 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 99 | 46% (37-56) | +0.47 | -0.28 | -28 |  |
| (0.104, 0.166] | 99 | 35% (27-45) | -0.48 | -1.67 | -165 |  |
| (0.166, 0.76] | 99 | 36% (28-46) | -0.09 | -2.48 | -245 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.821] | 57 | 33% (22-46) | -0.90 | -1.73 | -98 |  |
| (-0.821, 0.615] | 57 | 47% (35-60) | +0.97 | +0.41 | +23 |  |
| (0.615, 7.522] | 57 | 42% (30-55) | +0.14 | -0.61 | -35 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.555] | 60 | 43% (32-56) | +0.02 | -0.62 | -37 |  |
| (0.555, 0.843] | 59 | 44% (32-57) | +0.27 | -0.45 | -26 |  |
| (0.843, 3.799] | 59 | 34% (23-47) | -0.38 | -1.20 | -71 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.891] | 60 | 42% (30-54) | -0.14 | -0.74 | -45 |  |
| (0.891, 1.624] | 59 | 47% (35-60) | +1.04 | +0.33 | +20 |  |
| (1.624, 9.058] | 59 | 32% (22-45) | -0.99 | -1.85 | -109 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 60 | 40% (29-53) | -0.02 | -0.61 | -37 |  |
| (0.408, 0.618] | 59 | 51% (38-63) | +1.08 | +0.35 | +21 |  |
| (0.618, 4.001] | 59 | 31% (20-43) | -1.16 | -2.01 | -118 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 149, target 73, time_stop 59, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 99 | 35% | 17% | 41% |
| (0.104, 0.166] | 99 | 57% | 24% | 11% |
| (0.166, 0.76] | 99 | 59% | 32% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
