# Scalp signal analysis (trail exits)

_279 tagged trades, 33 trading days (2026-10-01 to 2026-11-16). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 279 | 42% (36-47) | -0.74 | -2.23 | -622 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 49 | -19 | -0.39 | 230 | -603 | -2.62 | +19 |
| skip first 30 min | 3 | -10 | -3.32 | 276 | -612 | -2.22 | +10 |
| skip when SPY is down on the day | 110 | -299 | -2.72 | 169 | -323 | -1.91 | +299 |
| skip when SPY is below its VWAP | 121 | -368 | -3.04 | 158 | -254 | -1.61 | +368 |
| skip when SPY fell over the last 15 min | 101 | -227 | -2.25 | 178 | -395 | -2.22 | +227 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 69 | -240 | -3.47 | 210 | -383 | -1.82 | +240 |
| skip stock not beating SPY over 15 min | 45 | -103 | -2.30 | 234 | -519 | -2.22 | +103 |
| skip afternoon entries (2:00-3:45 PM) | 62 | -230 | -3.71 | 217 | -392 | -1.81 | +230 |
| skip volume spikes above 5x average | 57 | -200 | -3.50 | 222 | -423 | -1.90 | +200 |
| skip when the stop is inside normal noise (range > stop) | 30 | -58 | -1.93 | 249 | -564 | -2.27 | +58 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 40 | -79 | -1.97 | 239 | -543 | -2.27 | +79 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 130 | -425 | -3.27 | 149 | -197 | -1.32 | +425 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 49% (33-64) | -0.33 | -2.03 | -75 |  |
| 60-240 | 114 | 39% (31-49) | -1.10 | -2.36 | -269 |  |
| 240-375 | 79 | 39% (29-50) | -1.55 | -3.27 | -258 |  |
| 375-390 | 49 | 45% (32-59) | +1.10 | -0.39 | -19 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 59 | 42% (31-55) | -0.76 | -1.95 | -115 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 68 | 35% (25-47) | -1.54 | -2.86 | -195 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 121 | 36% (28-44) | -1.46 | -3.04 | -368 |  |
| above VWAP | 158 | 46% (39-54) | -0.19 | -1.61 | -254 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 93 | 39% (29-49) | -0.41 | -1.60 | -149 |  |
| (0.129, 0.374] | 93 | 52% (42-62) | -0.22 | -1.72 | -160 | ▲ |
| (0.374, 5.591] | 93 | 34% (26-45) | -1.59 | -3.37 | -313 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.119] | 92 | 47% (37-57) | +0.20 | -0.97 | -90 |  |
| (0.119, 0.441] | 92 | 42% (33-53) | -0.88 | -2.70 | -248 |  |
| (0.441, 4.846] | 92 | 36% (27-46) | -1.47 | -2.98 | -274 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.397] | 93 | 45% (35-55) | -0.72 | -2.43 | -226 |  |
| (-0.397, 0.396] | 93 | 46% (36-56) | +0.27 | -0.81 | -75 |  |
| (0.396, 9.926] | 93 | 33% (25-43) | -1.77 | -3.45 | -320 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0555] | 93 | 42% (32-52) | -1.07 | -2.40 | -223 |  |
| (0.0555, 0.127] | 94 | 46% (36-56) | +0.17 | -1.21 | -114 |  |
| (0.127, 0.924] | 92 | 37% (28-47) | -1.33 | -3.10 | -285 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 93 | 44% (34-54) | +0.02 | -1.03 | -96 |  |
| (0.217, 0.342] | 93 | 46% (36-56) | -0.60 | -2.32 | -215 |  |
| (0.342, 2.663] | 93 | 34% (26-45) | -1.64 | -3.34 | -311 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.354] | 93 | 40% (30-50) | -0.69 | -2.13 | -198 |  |
| (2.354, 3.618] | 93 | 49% (40-59) | +0.49 | -1.02 | -95 |  |
| (3.618, 19.488] | 93 | 35% (27-46) | -2.02 | -3.53 | -329 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 94 | 48% (38-58) | +0.25 | -0.52 | -49 |  |
| (0.104, 0.165] | 93 | 41% (31-51) | -1.24 | -2.47 | -229 |  |
| (0.165, 0.76] | 92 | 36% (27-46) | -1.24 | -3.74 | -344 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.136] | 51 | 41% (29-55) | -1.41 | -2.24 | -114 |  |
| (-1.136, 0.615] | 51 | 51% (38-64) | -0.13 | -0.72 | -37 |  |
| (0.615, 7.522] | 51 | 55% (41-68) | -0.56 | -1.29 | -66 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.541] | 54 | 50% (37-63) | -0.38 | -1.03 | -55 |  |
| (0.541, 0.837] | 54 | 52% (39-65) | -1.05 | -1.78 | -96 |  |
| (0.837, 3.799] | 52 | 44% (32-58) | -0.95 | -1.77 | -92 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.869] | 54 | 46% (34-59) | -1.45 | -2.04 | -110 |  |
| (0.869, 1.545] | 53 | 53% (40-66) | -0.33 | -1.05 | -56 |  |
| (1.545, 9.058] | 53 | 47% (34-60) | -0.58 | -1.46 | -77 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.385] | 54 | 44% (32-58) | -0.76 | -1.35 | -73 |  |
| (0.385, 0.6] | 53 | 62% (49-74) | -0.20 | -0.95 | -50 | ▲ |
| (0.6, 4.001] | 53 | 40% (28-53) | -1.41 | -2.26 | -120 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 123, trail_stop 115, time_stop 33, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 94 | 32% | 32% | 31% |
| (0.104, 0.165] | 93 | 51% | 45% | 2% |
| (0.165, 0.76] | 92 | 50% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
