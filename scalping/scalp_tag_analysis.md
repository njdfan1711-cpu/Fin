# Scalp signal analysis (fixed exits)

_304 tagged trades, 35 trading days (2026-10-01 to 2026-11-18). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 304 | 39% (34-45) | -0.06 | -1.48 | -451 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 59 | +20 | +0.34 | 245 | -471 | -1.92 | -20 |
| skip first 30 min | 4 | -21 | -5.34 | 300 | -429 | -1.43 | +21 |
| skip when SPY is down on the day | 134 | -176 | -1.31 | 170 | -275 | -1.62 | +176 |
| skip when SPY is below its VWAP | 133 | -182 | -1.37 | 171 | -268 | -1.57 | +182 |
| skip when SPY fell over the last 15 min | 102 | -131 | -1.29 | 202 | -320 | -1.58 | +131 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 75 | -193 | -2.58 | 229 | -257 | -1.12 | +193 |
| skip stock not beating SPY over 15 min | 47 | -57 | -1.20 | 257 | -394 | -1.53 | +57 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -244 | -3.64 | 237 | -207 | -0.87 | +244 |
| skip volume spikes above 5x average | 63 | -172 | -2.74 | 241 | -278 | -1.16 | +172 |
| skip when the stop is inside normal noise (range > stop) | 39 | -59 | -1.52 | 265 | -391 | -1.48 | +59 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 46 | -64 | -1.40 | 258 | -386 | -1.50 | +64 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 137 | -357 | -2.61 | 167 | -94 | -0.56 | +357 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 50% (35-65) | +1.69 | +0.01 | +0 |  |
| 60-240 | 123 | 36% (28-45) | -0.52 | -1.73 | -213 |  |
| 240-375 | 84 | 31% (22-41) | -1.42 | -3.08 | -258 |  |
| 375-390 | 59 | 51% (38-63) | +1.72 | +0.34 | +20 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 83 | 40% (30-51) | +0.09 | -0.94 | -78 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 133 | 41% (33-50) | +0.14 | -1.37 | -182 |  |
| above VWAP | 171 | 37% (31-45) | -0.22 | -1.57 | -268 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 102 | 39% (30-49) | -0.01 | -1.13 | -116 |  |
| (0.132, 0.374] | 101 | 42% (32-51) | +0.01 | -1.44 | -145 |  |
| (0.374, 5.591] | 101 | 37% (28-46) | -0.18 | -1.88 | -190 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.135] | 100 | 47% (38-57) | +0.77 | -0.36 | -36 |  |
| (0.135, 0.453] | 100 | 39% (30-49) | +0.18 | -1.55 | -155 |  |
| (0.453, 4.846] | 100 | 33% (25-43) | -0.94 | -2.39 | -239 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.537] | 102 | 42% (33-52) | +0.14 | -1.35 | -137 |  |
| (-0.537, 0.34] | 101 | 41% (32-50) | +0.48 | -0.72 | -72 |  |
| (0.34, 9.926] | 101 | 35% (26-44) | -0.80 | -2.39 | -241 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0558] | 102 | 39% (30-49) | -0.36 | -1.63 | -166 |  |
| (0.0558, 0.128] | 101 | 44% (34-53) | +0.44 | -0.89 | -90 |  |
| (0.128, 0.924] | 101 | 35% (26-44) | -0.26 | -1.93 | -195 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 102 | 44% (35-54) | +0.48 | -0.53 | -54 |  |
| (0.217, 0.346] | 101 | 40% (31-49) | -0.02 | -1.66 | -168 |  |
| (0.346, 2.663] | 101 | 34% (25-43) | -0.65 | -2.27 | -229 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.381] | 102 | 35% (27-45) | -0.38 | -1.77 | -180 |  |
| (2.381, 3.611] | 101 | 49% (39-58) | +1.01 | -0.44 | -44 |  |
| (3.611, 19.488] | 101 | 34% (25-43) | -0.81 | -2.24 | -226 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 102 | 46% (37-56) | +0.43 | -0.31 | -32 |  |
| (0.104, 0.166] | 102 | 36% (28-46) | -0.33 | -1.48 | -151 |  |
| (0.166, 0.76] | 100 | 35% (26-45) | -0.29 | -2.68 | -268 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 60 | 32% (21-44) | -1.16 | -1.96 | -118 |  |
| (-0.793, 0.617] | 59 | 47% (35-60) | +1.07 | +0.52 | +30 |  |
| (0.617, 7.522] | 59 | 42% (31-55) | +0.17 | -0.60 | -35 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.553] | 62 | 44% (32-56) | +0.08 | -0.55 | -34 |  |
| (0.553, 0.851] | 61 | 43% (31-55) | +0.08 | -0.63 | -39 |  |
| (0.851, 3.799] | 62 | 34% (23-46) | -0.38 | -1.20 | -74 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.9] | 62 | 42% (30-54) | -0.08 | -0.68 | -42 |  |
| (0.9, 1.638] | 61 | 46% (34-58) | +0.83 | +0.13 | +8 |  |
| (1.638, 9.058] | 62 | 32% (22-45) | -0.95 | -1.82 | -113 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 62 | 39% (28-51) | -0.20 | -0.78 | -48 |  |
| (0.408, 0.617] | 61 | 49% (37-61) | +0.86 | +0.13 | +8 |  |
| (0.617, 4.001] | 62 | 32% (22-45) | -0.87 | -1.72 | -107 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 154, target 75, time_stop 59, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 102 | 36% | 18% | 40% |
| (0.104, 0.166] | 102 | 56% | 25% | 11% |
| (0.166, 0.76] | 100 | 60% | 31% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
