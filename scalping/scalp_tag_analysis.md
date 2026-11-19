# Scalp signal analysis (fixed exits)

_305 tagged trades, 36 trading days (2026-10-01 to 2026-11-19). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 305 | 39% (34-45) | -0.08 | -1.50 | -457 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 59 | +20 | +0.34 | 246 | -476 | -1.94 | -20 |
| skip first 30 min | 4 | -21 | -5.34 | 301 | -435 | -1.45 | +21 |
| skip when SPY is down on the day | 135 | -182 | -1.35 | 170 | -275 | -1.62 | +182 |
| skip when SPY is below its VWAP | 133 | -182 | -1.37 | 172 | -274 | -1.59 | +182 |
| skip when SPY fell over the last 15 min | 102 | -131 | -1.29 | 203 | -326 | -1.60 | +131 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 75 | -193 | -2.58 | 230 | -263 | -1.15 | +193 |
| skip stock not beating SPY over 15 min | 47 | -57 | -1.20 | 258 | -400 | -1.55 | +57 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -244 | -3.64 | 238 | -213 | -0.89 | +244 |
| skip volume spikes above 5x average | 64 | -178 | -2.78 | 241 | -278 | -1.16 | +178 |
| skip when the stop is inside normal noise (range > stop) | 39 | -59 | -1.52 | 266 | -397 | -1.49 | +59 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 47 | -70 | -1.50 | 258 | -386 | -1.50 | +70 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 137 | -357 | -2.61 | 168 | -99 | -0.59 | +357 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 50% (35-65) | +1.69 | +0.01 | +0 |  |
| 60-240 | 124 | 35% (28-44) | -0.57 | -1.76 | -218 |  |
| 240-375 | 84 | 31% (22-41) | -1.42 | -3.08 | -258 |  |
| 375-390 | 59 | 51% (38-63) | +1.72 | +0.34 | +20 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 84 | 39% (30-50) | +0.02 | -1.00 | -84 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 133 | 41% (33-50) | +0.14 | -1.37 | -182 |  |
| above VWAP | 172 | 37% (30-45) | -0.25 | -1.59 | -274 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 102 | 38% (29-48) | -0.17 | -1.28 | -131 |  |
| (0.126, 0.374] | 101 | 43% (33-52) | +0.17 | -1.27 | -128 |  |
| (0.374, 5.591] | 102 | 36% (28-46) | -0.23 | -1.94 | -198 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.135] | 101 | 48% (38-57) | +0.81 | -0.31 | -31 |  |
| (0.135, 0.451] | 100 | 38% (29-48) | +0.07 | -1.65 | -165 |  |
| (0.451, 4.846] | 100 | 33% (25-43) | -0.94 | -2.39 | -239 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.56] | 102 | 41% (32-51) | -0.00 | -1.48 | -151 |  |
| (-0.56, 0.34] | 101 | 41% (32-50) | +0.46 | -0.72 | -73 |  |
| (0.34, 9.926] | 102 | 35% (27-45) | -0.69 | -2.28 | -233 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0557] | 102 | 38% (29-48) | -0.51 | -1.78 | -182 |  |
| (0.0557, 0.128] | 101 | 45% (35-54) | +0.60 | -0.73 | -73 |  |
| (0.128, 0.924] | 102 | 34% (26-44) | -0.31 | -1.98 | -202 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 102 | 44% (35-54) | +0.48 | -0.53 | -54 |  |
| (0.217, 0.346] | 101 | 40% (31-49) | -0.02 | -1.65 | -167 |  |
| (0.346, 2.663] | 102 | 33% (25-43) | -0.70 | -2.32 | -236 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.384] | 102 | 35% (27-45) | -0.38 | -1.77 | -180 |  |
| (2.384, 3.625] | 101 | 49% (39-58) | +1.01 | -0.44 | -44 |  |
| (3.625, 19.488] | 102 | 33% (25-43) | -0.86 | -2.27 | -232 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 102 | 46% (37-56) | +0.43 | -0.31 | -32 |  |
| (0.104, 0.166] | 101 | 35% (26-44) | -0.58 | -1.74 | -176 |  |
| (0.166, 0.76] | 102 | 36% (28-46) | -0.10 | -2.44 | -249 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.783] | 60 | 32% (21-44) | -1.16 | -1.96 | -118 |  |
| (-0.783, 0.622] | 59 | 47% (35-60) | +1.07 | +0.52 | +30 |  |
| (0.622, 7.522] | 60 | 42% (30-54) | +0.07 | -0.68 | -41 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.55] | 62 | 44% (32-56) | +0.08 | -0.54 | -34 |  |
| (0.55, 0.847] | 62 | 42% (30-54) | -0.02 | -0.73 | -45 |  |
| (0.847, 3.799] | 62 | 34% (23-46) | -0.38 | -1.20 | -74 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.909] | 62 | 42% (30-54) | -0.08 | -0.68 | -42 |  |
| (0.909, 1.631] | 62 | 45% (33-57) | +0.72 | +0.03 | +2 |  |
| (1.631, 9.058] | 62 | 32% (22-45) | -0.95 | -1.82 | -113 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.404] | 62 | 39% (28-51) | -0.20 | -0.77 | -48 |  |
| (0.404, 0.616] | 62 | 48% (36-61) | +0.75 | +0.02 | +1 |  |
| (0.616, 4.001] | 62 | 32% (22-45) | -0.87 | -1.72 | -107 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 155, target 75, time_stop 59, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 102 | 36% | 18% | 40% |
| (0.104, 0.166] | 101 | 57% | 24% | 11% |
| (0.166, 0.76] | 102 | 59% | 32% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
