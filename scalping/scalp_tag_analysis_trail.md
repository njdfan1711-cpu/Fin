# Scalp signal analysis (trail exits)

_275 tagged trades, 32 trading days (2026-10-01 to 2026-11-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 275 | 42% (36-48) | -0.73 | -2.23 | -613 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 48 | -19 | -0.40 | 227 | -594 | -2.62 | +19 |
| skip first 30 min | 3 | -10 | -3.32 | 272 | -603 | -2.22 | +10 |
| skip when SPY is down on the day | 106 | -289 | -2.73 | 169 | -323 | -1.91 | +289 |
| skip when SPY is below its VWAP | 120 | -362 | -3.01 | 155 | -251 | -1.62 | +362 |
| skip when SPY fell over the last 15 min | 101 | -227 | -2.25 | 174 | -385 | -2.21 | +227 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 68 | -232 | -3.42 | 207 | -380 | -1.84 | +232 |
| skip stock not beating SPY over 15 min | 44 | -103 | -2.34 | 231 | -510 | -2.21 | +103 |
| skip afternoon entries (2:00-3:45 PM) | 60 | -227 | -3.79 | 215 | -385 | -1.79 | +227 |
| skip volume spikes above 5x average | 57 | -200 | -3.50 | 218 | -413 | -1.89 | +200 |
| skip when the stop is inside normal noise (range > stop) | 30 | -58 | -1.93 | 245 | -555 | -2.26 | +58 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 39 | -72 | -1.85 | 236 | -541 | -2.29 | +72 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 127 | -422 | -3.32 | 148 | -191 | -1.29 | +422 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 49% (33-64) | -0.33 | -2.03 | -75 |  |
| 60-240 | 113 | 40% (31-49) | -1.06 | -2.33 | -263 |  |
| 240-375 | 77 | 39% (29-50) | -1.59 | -3.32 | -256 |  |
| 375-390 | 48 | 46% (33-60) | +1.11 | -0.40 | -19 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 55 | 44% (31-57) | -0.72 | -1.92 | -105 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 68 | 35% (25-47) | -1.54 | -2.86 | -195 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 120 | 36% (28-45) | -1.42 | -3.01 | -362 |  |
| above VWAP | 155 | 46% (39-54) | -0.20 | -1.62 | -251 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 92 | 40% (31-50) | -0.34 | -1.53 | -141 |  |
| (0.133, 0.376] | 91 | 51% (40-61) | -0.31 | -1.82 | -166 |  |
| (0.376, 5.591] | 92 | 35% (26-45) | -1.54 | -3.32 | -305 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.12] | 91 | 48% (38-58) | +0.28 | -0.89 | -81 |  |
| (0.12, 0.444] | 90 | 42% (33-53) | -0.88 | -2.72 | -245 |  |
| (0.444, 4.846] | 91 | 35% (26-45) | -1.52 | -3.04 | -277 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.385] | 92 | 46% (36-56) | -0.79 | -2.48 | -229 |  |
| (-0.385, 0.401] | 91 | 47% (37-57) | +0.49 | -0.61 | -55 |  |
| (0.401, 9.926] | 92 | 33% (24-43) | -1.88 | -3.57 | -329 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 92 | 42% (33-53) | -1.01 | -2.34 | -216 |  |
| (0.0559, 0.127] | 91 | 44% (34-54) | +0.07 | -1.34 | -122 |  |
| (0.127, 0.924] | 92 | 39% (30-49) | -1.24 | -2.99 | -275 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 92 | 45% (35-55) | +0.10 | -0.96 | -88 |  |
| (0.217, 0.341] | 91 | 46% (36-56) | -0.69 | -2.42 | -220 |  |
| (0.341, 2.663] | 92 | 35% (26-45) | -1.59 | -3.31 | -304 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.37] | 92 | 41% (32-52) | -0.63 | -2.07 | -191 |  |
| (2.37, 3.635] | 91 | 48% (38-58) | +0.42 | -1.10 | -100 |  |
| (3.635, 19.488] | 92 | 36% (27-46) | -1.97 | -3.50 | -322 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 92 | 48% (38-58) | +0.26 | -0.50 | -46 |  |
| (0.104, 0.166] | 91 | 42% (32-52) | -1.22 | -2.44 | -222 |  |
| (0.166, 0.76] | 92 | 36% (27-46) | -1.24 | -3.74 | -344 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.043] | 50 | 42% (29-56) | -1.35 | -2.16 | -108 |  |
| (-1.043, 0.616] | 49 | 53% (39-66) | -0.00 | -0.60 | -30 |  |
| (0.616, 7.522] | 50 | 54% (40-67) | -0.68 | -1.39 | -70 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.544] | 52 | 50% (37-63) | -0.38 | -1.02 | -53 |  |
| (0.544, 0.839] | 52 | 54% (41-67) | -1.01 | -1.71 | -89 |  |
| (0.839, 3.799] | 52 | 44% (32-58) | -0.95 | -1.77 | -92 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.866] | 52 | 48% (35-61) | -1.34 | -1.93 | -100 |  |
| (0.866, 1.536] | 52 | 50% (37-63) | -0.54 | -1.24 | -64 |  |
| (1.536, 9.058] | 52 | 50% (37-63) | -0.46 | -1.33 | -69 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.384] | 52 | 44% (32-58) | -0.89 | -1.46 | -76 |  |
| (0.384, 0.605] | 52 | 63% (50-75) | -0.11 | -0.85 | -44 | ▲ |
| (0.605, 4.001] | 52 | 40% (28-54) | -1.34 | -2.18 | -113 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 121, trail_stop 114, time_stop 32, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 92 | 32% | 33% | 30% |
| (0.104, 0.166] | 91 | 51% | 45% | 2% |
| (0.166, 0.76] | 92 | 50% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
