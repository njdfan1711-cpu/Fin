# Scalp signal analysis (trail exits)

_311 tagged trades, 38 trading days (2026-10-01 to 2026-11-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 311 | 43% (37-48) | -0.67 | -2.07 | -644 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +29 | +0.48 | 251 | -672 | -2.68 | -29 |
| skip first 30 min | 4 | -17 | -4.16 | 307 | -627 | -2.04 | +17 |
| skip when SPY is down on the day | 141 | -314 | -2.22 | 170 | -330 | -1.94 | +314 |
| skip when SPY is below its VWAP | 138 | -336 | -2.44 | 173 | -307 | -1.78 | +336 |
| skip when SPY fell over the last 15 min | 104 | -212 | -2.04 | 207 | -431 | -2.08 | +212 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 77 | -223 | -2.89 | 234 | -421 | -1.80 | +223 |
| skip stock not beating SPY over 15 min | 48 | -107 | -2.23 | 263 | -536 | -2.04 | +107 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -252 | -3.75 | 244 | -392 | -1.61 | +252 |
| skip volume spikes above 5x average | 67 | -237 | -3.53 | 244 | -407 | -1.67 | +237 |
| skip when the stop is inside normal noise (range > stop) | 42 | -65 | -1.55 | 269 | -578 | -2.15 | +65 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 48 | -83 | -1.72 | 263 | -561 | -2.13 | +83 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 173 | -225 | -1.30 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 49% (34-64) | -0.41 | -2.04 | -80 |  |
| 60-240 | 126 | 38% (30-47) | -1.31 | -2.49 | -314 |  |
| 240-375 | 86 | 40% (30-50) | -1.60 | -3.24 | -278 |  |
| 375-390 | 60 | 53% (41-65) | +1.85 | +0.48 | +29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 88 | 45% (35-56) | -0.51 | -1.51 | -133 |  |
| -0.2 to 0 | 53 | 40% (28-53) | -1.33 | -3.42 | -181 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 138 | 41% (33-49) | -0.96 | -2.44 | -336 |  |
| above VWAP | 173 | 45% (37-52) | -0.44 | -1.78 | -307 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 104 | 41% (32-51) | -0.30 | -1.40 | -145 |  |
| (0.123, 0.374] | 103 | 50% (40-59) | -0.43 | -1.84 | -190 |  |
| (0.374, 5.591] | 104 | 38% (29-47) | -1.28 | -2.96 | -308 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.133] | 103 | 50% (41-60) | +0.31 | -0.80 | -82 |  |
| (0.133, 0.451] | 102 | 40% (31-50) | -0.98 | -2.68 | -274 |  |
| (0.451, 4.846] | 102 | 38% (29-48) | -1.23 | -2.66 | -271 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.566] | 104 | 45% (36-55) | -0.62 | -2.08 | -216 |  |
| (-0.566, 0.34] | 103 | 46% (36-55) | +0.06 | -1.09 | -113 |  |
| (0.34, 9.926] | 104 | 38% (29-47) | -1.44 | -3.02 | -315 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 104 | 42% (33-52) | -1.06 | -2.31 | -240 |  |
| (0.0559, 0.127] | 104 | 48% (39-58) | +0.25 | -1.05 | -109 |  |
| (0.127, 0.924] | 103 | 38% (29-48) | -1.20 | -2.86 | -294 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.219] | 104 | 46% (37-56) | +0.18 | -0.82 | -85 |  |
| (0.219, 0.346] | 103 | 47% (37-56) | -0.66 | -2.27 | -234 |  |
| (0.346, 2.663] | 104 | 36% (27-45) | -1.53 | -3.12 | -325 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.378] | 104 | 43% (34-53) | -0.50 | -1.88 | -196 |  |
| (2.378, 3.635] | 103 | 50% (40-59) | +0.57 | -0.87 | -90 |  |
| (3.635, 19.488] | 104 | 36% (27-45) | -2.06 | -3.45 | -358 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 104 | 47% (38-57) | +0.11 | -0.63 | -65 |  |
| (0.104, 0.166] | 103 | 44% (35-53) | -1.01 | -2.16 | -222 |  |
| (0.166, 0.76] | 104 | 38% (29-47) | -1.12 | -3.43 | -357 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.783] | 62 | 42% (30-54) | -1.39 | -2.19 | -136 |  |
| (-0.783, 0.633] | 61 | 52% (40-64) | +0.03 | -0.52 | -32 |  |
| (0.633, 8.282] | 62 | 55% (43-67) | -0.41 | -1.14 | -71 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.554] | 64 | 47% (35-59) | -0.69 | -1.31 | -84 |  |
| (0.554, 0.859] | 64 | 55% (43-66) | -0.57 | -1.28 | -82 |  |
| (0.859, 3.799] | 64 | 47% (35-59) | -0.75 | -1.55 | -99 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.889] | 64 | 48% (37-60) | -1.20 | -1.78 | -114 |  |
| (0.889, 1.631] | 64 | 52% (40-63) | -0.39 | -1.08 | -69 |  |
| (1.631, 9.058] | 64 | 48% (37-60) | -0.42 | -1.27 | -81 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.404] | 64 | 45% (34-57) | -0.77 | -1.33 | -85 |  |
| (0.404, 0.616] | 64 | 61% (49-72) | -0.09 | -0.80 | -51 | ▲ |
| (0.616, 4.001] | 64 | 42% (31-54) | -1.16 | -2.01 | -128 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.15%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 136, trail_stop 130, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 104 | 34% | 33% | 29% |
| (0.104, 0.166] | 103 | 48% | 46% | 3% |
| (0.166, 0.76] | 104 | 50% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
