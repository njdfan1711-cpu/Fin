# Scalp signal analysis (fixed exits)

_302 tagged trades, 35 trading days (2026-10-01 to 2026-11-18). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 302 | 39% (34-45) | -0.07 | -1.50 | -452 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 57 | +18 | +0.32 | 245 | -471 | -1.92 | -18 |
| skip first 30 min | 4 | -21 | -5.34 | 298 | -431 | -1.45 | +21 |
| skip when SPY is down on the day | 132 | -177 | -1.34 | 170 | -275 | -1.62 | +177 |
| skip when SPY is below its VWAP | 133 | -182 | -1.37 | 169 | -270 | -1.60 | +182 |
| skip when SPY fell over the last 15 min | 102 | -131 | -1.29 | 200 | -321 | -1.60 | +131 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 75 | -184 | -2.45 | 227 | -268 | -1.18 | +184 |
| skip stock not beating SPY over 15 min | 47 | -57 | -1.20 | 255 | -396 | -1.55 | +57 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -244 | -3.64 | 235 | -208 | -0.88 | +244 |
| skip volume spikes above 5x average | 63 | -172 | -2.74 | 239 | -280 | -1.17 | +172 |
| skip when the stop is inside normal noise (range > stop) | 38 | -53 | -1.39 | 264 | -399 | -1.51 | +53 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 46 | -64 | -1.39 | 256 | -388 | -1.52 | +64 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 136 | -351 | -2.58 | 166 | -101 | -0.61 | +351 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 50% (35-65) | +1.69 | +0.01 | +0 |  |
| 60-240 | 123 | 36% (28-45) | -0.52 | -1.73 | -213 |  |
| 240-375 | 84 | 31% (22-41) | -1.42 | -3.08 | -258 |  |
| 375-390 | 57 | 51% (38-63) | +1.72 | +0.32 | +18 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 81 | 40% (30-50) | +0.06 | -0.98 | -79 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 133 | 41% (33-50) | +0.14 | -1.37 | -182 |  |
| above VWAP | 169 | 37% (30-45) | -0.24 | -1.60 | -270 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 101 | 39% (30-48) | -0.11 | -1.24 | -125 |  |
| (0.126, 0.374] | 100 | 42% (33-52) | +0.08 | -1.36 | -136 |  |
| (0.374, 5.591] | 101 | 37% (28-46) | -0.18 | -1.89 | -191 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.133] | 100 | 47% (38-57) | +0.77 | -0.36 | -36 |  |
| (0.133, 0.446] | 99 | 39% (30-49) | +0.24 | -1.50 | -149 |  |
| (0.446, 4.846] | 99 | 32% (24-42) | -1.04 | -2.49 | -246 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.516] | 101 | 43% (33-52) | +0.21 | -1.32 | -133 |  |
| (-0.516, 0.356] | 100 | 40% (31-50) | +0.38 | -0.77 | -77 |  |
| (0.356, 9.926] | 101 | 35% (26-44) | -0.80 | -2.39 | -241 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0557] | 101 | 39% (30-48) | -0.46 | -1.74 | -176 |  |
| (0.0557, 0.13] | 100 | 44% (35-54) | +0.51 | -0.82 | -82 |  |
| (0.13, 0.924] | 101 | 35% (26-44) | -0.26 | -1.93 | -195 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.216] | 101 | 44% (34-53) | +0.38 | -0.63 | -63 |  |
| (0.216, 0.346] | 100 | 41% (32-51) | +0.20 | -1.45 | -145 |  |
| (0.346, 2.663] | 101 | 33% (24-42) | -0.79 | -2.42 | -244 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.384] | 101 | 36% (27-45) | -0.32 | -1.72 | -174 |  |
| (2.384, 3.625] | 100 | 48% (38-58) | +0.93 | -0.52 | -52 |  |
| (3.625, 19.488] | 101 | 34% (25-43) | -0.81 | -2.24 | -226 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 101 | 46% (36-55) | +0.35 | -0.39 | -40 |  |
| (0.104, 0.166] | 100 | 35% (26-45) | -0.52 | -1.70 | -170 |  |
| (0.166, 0.76] | 101 | 37% (28-46) | -0.04 | -2.40 | -242 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 60 | 32% (21-44) | -1.16 | -1.96 | -118 |  |
| (-0.793, 0.616] | 57 | 47% (35-60) | +1.00 | +0.45 | +26 |  |
| (0.616, 7.522] | 59 | 42% (31-55) | +0.22 | -0.54 | -32 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.554] | 61 | 43% (31-55) | -0.06 | -0.69 | -42 |  |
| (0.554, 0.847] | 61 | 43% (31-55) | +0.08 | -0.63 | -39 |  |
| (0.847, 3.799] | 61 | 34% (24-47) | -0.29 | -1.11 | -68 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.909] | 61 | 41% (30-54) | -0.23 | -0.82 | -50 |  |
| (0.909, 1.631] | 61 | 46% (34-58) | +0.83 | +0.13 | +8 |  |
| (1.631, 9.058] | 61 | 33% (22-45) | -0.88 | -1.74 | -106 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.404] | 61 | 39% (28-52) | -0.10 | -0.68 | -42 |  |
| (0.404, 0.616] | 61 | 48% (36-60) | +0.62 | -0.11 | -7 |  |
| (0.616, 4.001] | 61 | 33% (22-45) | -0.79 | -1.64 | -100 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 153, target 74, time_stop 59, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 101 | 37% | 17% | 41% |
| (0.104, 0.166] | 100 | 57% | 24% | 11% |
| (0.166, 0.76] | 101 | 58% | 33% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
