# Scalp signal analysis (fixed exits)

_278 tagged trades, 32 trading days (2026-10-01 to 2026-11-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 278 | 40% (34-45) | -0.02 | -1.52 | -421 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 49 | -35 | -0.71 | 229 | -386 | -1.69 | +35 |
| skip first 30 min | 3 | -15 | -4.90 | 275 | -407 | -1.48 | +15 |
| skip when SPY is down on the day | 109 | -153 | -1.40 | 169 | -268 | -1.59 | +153 |
| skip when SPY is below its VWAP | 120 | -206 | -1.72 | 158 | -215 | -1.36 | +206 |
| skip when SPY fell over the last 15 min | 100 | -147 | -1.47 | 178 | -275 | -1.54 | +147 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 69 | -191 | -2.77 | 209 | -230 | -1.10 | +191 |
| skip stock not beating SPY over 15 min | 45 | -57 | -1.27 | 233 | -364 | -1.56 | +57 |
| skip afternoon entries (2:00-3:45 PM) | 62 | -215 | -3.46 | 216 | -207 | -0.96 | +215 |
| skip volume spikes above 5x average | 57 | -136 | -2.39 | 221 | -285 | -1.29 | +136 |
| skip when the stop is inside normal noise (range > stop) | 30 | -32 | -1.07 | 248 | -389 | -1.57 | +32 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.69%) | 40 | -42 | -1.04 | 238 | -380 | -1.60 | +42 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 130 | -357 | -2.75 | 148 | -64 | -0.43 | +357 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 51% (36-67) | +1.89 | +0.19 | +7 |  |
| 60-240 | 113 | 38% (30-47) | -0.19 | -1.46 | -165 |  |
| 240-375 | 79 | 33% (24-44) | -1.18 | -2.90 | -229 |  |
| 375-390 | 49 | 45% (32-59) | +0.78 | -0.71 | -35 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 58 | 41% (30-54) | +0.25 | -0.96 | -55 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 68 | 32% (22-44) | -0.51 | -1.83 | -125 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 120 | 40% (32-49) | -0.13 | -1.72 | -206 |  |
| above VWAP | 158 | 39% (32-47) | +0.06 | -1.36 | -215 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 93 | 39% (29-49) | -0.06 | -1.25 | -117 |  |
| (0.133, 0.374] | 92 | 43% (34-54) | +0.20 | -1.31 | -121 |  |
| (0.374, 5.591] | 93 | 37% (27-47) | -0.20 | -1.98 | -184 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.118] | 92 | 45% (35-55) | +0.49 | -0.68 | -62 |  |
| (0.118, 0.442] | 91 | 42% (32-52) | +0.52 | -1.31 | -120 |  |
| (0.442, 4.846] | 92 | 34% (25-44) | -0.93 | -2.44 | -225 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.395] | 93 | 44% (34-54) | +0.42 | -1.30 | -121 |  |
| (-0.395, 0.398] | 92 | 42% (33-53) | +0.57 | -0.52 | -48 |  |
| (0.398, 9.926] | 93 | 32% (24-42) | -1.04 | -2.72 | -253 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 93 | 40% (30-50) | -0.27 | -1.60 | -149 |  |
| (0.0559, 0.127] | 93 | 44% (34-54) | +0.46 | -0.93 | -87 |  |
| (0.127, 0.924] | 92 | 35% (26-45) | -0.26 | -2.02 | -186 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 93 | 44% (34-54) | +0.35 | -0.70 | -65 |  |
| (0.217, 0.342] | 92 | 40% (31-50) | +0.18 | -1.54 | -142 |  |
| (0.342, 2.663] | 93 | 34% (26-45) | -0.60 | -2.30 | -214 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.36] | 93 | 37% (27-47) | -0.20 | -1.64 | -153 |  |
| (2.36, 3.625] | 92 | 47% (37-57) | +0.67 | -0.85 | -78 |  |
| (3.625, 19.488] | 93 | 35% (27-46) | -0.53 | -2.05 | -190 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 93 | 47% (37-57) | +0.50 | -0.27 | -25 |  |
| (0.104, 0.165] | 93 | 34% (26-45) | -0.55 | -1.78 | -165 |  |
| (0.165, 0.76] | 92 | 37% (28-47) | -0.02 | -2.52 | -231 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.193] | 51 | 33% (22-47) | -0.93 | -1.76 | -90 |  |
| (-1.193, 0.616] | 50 | 48% (35-61) | +0.99 | +0.40 | +20 |  |
| (0.616, 7.522] | 51 | 43% (31-57) | +0.27 | -0.46 | -23 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.544] | 53 | 47% (34-60) | +0.45 | -0.20 | -11 |  |
| (0.544, 0.837] | 54 | 39% (27-52) | -0.33 | -1.06 | -57 |  |
| (0.837, 3.799] | 52 | 37% (25-50) | -0.14 | -0.96 | -50 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.876] | 53 | 42% (29-55) | +0.00 | -0.58 | -31 |  |
| (0.876, 1.556] | 53 | 47% (34-60) | +0.93 | +0.21 | +11 |  |
| (1.556, 9.058] | 53 | 34% (23-47) | -0.96 | -1.84 | -98 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.384] | 53 | 42% (29-55) | -0.04 | -0.63 | -33 |  |
| (0.384, 0.605] | 53 | 47% (34-60) | +0.66 | -0.09 | -5 |  |
| (0.605, 4.001] | 53 | 34% (23-47) | -0.65 | -1.50 | -79 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 139, target 69, time_stop 57, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 93 | 34% | 16% | 43% |
| (0.104, 0.165] | 93 | 58% | 26% | 11% |
| (0.165, 0.76] | 92 | 58% | 33% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
