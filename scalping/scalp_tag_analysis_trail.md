# Scalp signal analysis (trail exits)

_308 tagged trades, 37 trading days (2026-10-01 to 2026-11-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 308 | 42% (37-48) | -0.69 | -2.11 | -648 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +29 | +0.48 | 248 | -677 | -2.73 | -29 |
| skip first 30 min | 4 | -17 | -4.16 | 304 | -632 | -2.08 | +17 |
| skip when SPY is down on the day | 138 | -319 | -2.31 | 170 | -330 | -1.94 | +319 |
| skip when SPY is below its VWAP | 136 | -339 | -2.49 | 172 | -309 | -1.80 | +339 |
| skip when SPY fell over the last 15 min | 103 | -215 | -2.09 | 205 | -434 | -2.12 | +215 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 76 | -225 | -2.96 | 232 | -424 | -1.83 | +225 |
| skip stock not beating SPY over 15 min | 48 | -107 | -2.23 | 260 | -541 | -2.08 | +107 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -252 | -3.75 | 241 | -397 | -1.65 | +252 |
| skip volume spikes above 5x average | 64 | -242 | -3.77 | 244 | -407 | -1.67 | +242 |
| skip when the stop is inside normal noise (range > stop) | 40 | -67 | -1.68 | 268 | -581 | -2.17 | +67 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 47 | -83 | -1.77 | 261 | -565 | -2.16 | +83 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 170 | -229 | -1.35 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 47% (32-63) | -0.47 | -2.15 | -82 |  |
| 60-240 | 124 | 37% (29-46) | -1.36 | -2.56 | -317 |  |
| 240-375 | 86 | 40% (30-50) | -1.60 | -3.24 | -278 |  |
| 375-390 | 60 | 53% (41-65) | +1.85 | +0.48 | +29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 87 | 45% (35-55) | -0.54 | -1.55 | -135 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 136 | 40% (32-48) | -1.00 | -2.49 | -339 |  |
| above VWAP | 172 | 44% (37-52) | -0.45 | -1.80 | -309 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 103 | 40% (31-49) | -0.39 | -1.50 | -155 |  |
| (0.126, 0.374] | 102 | 50% (40-60) | -0.36 | -1.79 | -183 |  |
| (0.374, 5.591] | 103 | 37% (28-47) | -1.32 | -3.02 | -311 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.135] | 102 | 50% (40-60) | +0.33 | -0.79 | -81 |  |
| (0.135, 0.451] | 101 | 40% (31-49) | -1.04 | -2.75 | -278 |  |
| (0.451, 4.846] | 101 | 38% (29-47) | -1.27 | -2.70 | -273 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.56] | 103 | 45% (35-54) | -0.65 | -2.12 | -218 |  |
| (-0.56, 0.34] | 102 | 45% (36-55) | +0.04 | -1.13 | -115 |  |
| (0.34, 9.926] | 103 | 37% (28-47) | -1.47 | -3.06 | -315 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0557] | 103 | 42% (33-51) | -1.12 | -2.39 | -246 |  |
| (0.0557, 0.128] | 102 | 47% (38-57) | +0.25 | -1.06 | -108 |  |
| (0.128, 0.924] | 103 | 38% (29-48) | -1.20 | -2.86 | -294 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 103 | 46% (36-55) | +0.17 | -0.83 | -86 |  |
| (0.217, 0.348] | 102 | 45% (36-55) | -0.70 | -2.34 | -238 |  |
| (0.348, 2.663] | 103 | 36% (27-46) | -1.55 | -3.15 | -325 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.377] | 104 | 43% (34-53) | -0.50 | -1.88 | -196 |  |
| (2.377, 3.611] | 101 | 50% (40-59) | +0.63 | -0.82 | -83 |  |
| (3.611, 19.488] | 103 | 34% (26-44) | -2.18 | -3.59 | -369 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 103 | 48% (38-57) | +0.17 | -0.57 | -59 |  |
| (0.104, 0.166] | 102 | 42% (33-52) | -1.11 | -2.27 | -232 |  |
| (0.166, 0.76] | 103 | 37% (28-47) | -1.14 | -3.47 | -358 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 62 | 42% (30-54) | -1.39 | -2.19 | -136 |  |
| (-0.793, 0.616] | 59 | 53% (40-65) | +0.04 | -0.51 | -30 |  |
| (0.616, 7.522] | 61 | 52% (40-64) | -0.51 | -1.26 | -77 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.55] | 63 | 48% (36-60) | -0.61 | -1.23 | -77 |  |
| (0.55, 0.847] | 63 | 54% (42-66) | -0.69 | -1.39 | -88 |  |
| (0.847, 3.799] | 63 | 44% (33-57) | -0.83 | -1.66 | -104 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.909] | 63 | 48% (36-60) | -1.26 | -1.86 | -117 |  |
| (0.909, 1.652] | 63 | 49% (37-61) | -0.53 | -1.23 | -77 |  |
| (1.652, 9.058] | 63 | 49% (37-61) | -0.33 | -1.19 | -75 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.404] | 63 | 44% (33-57) | -0.82 | -1.39 | -88 |  |
| (0.404, 0.62] | 63 | 60% (48-71) | -0.09 | -0.81 | -51 | ▲ |
| (0.62, 4.001] | 63 | 41% (30-54) | -1.22 | -2.07 | -131 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.16%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 136, trail_stop 127, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 103 | 33% | 33% | 29% |
| (0.104, 0.166] | 102 | 49% | 44% | 3% |
| (0.166, 0.76] | 103 | 50% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
