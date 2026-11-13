# Scalp signal analysis (fixed exits)

_275 tagged trades, 32 trading days (2026-10-01 to 2026-11-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 275 | 40% (34-46) | +0.00 | -1.50 | -412 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 48 | -28 | -0.58 | 227 | -384 | -1.69 | +28 |
| skip first 30 min | 3 | -15 | -4.90 | 272 | -397 | -1.46 | +15 |
| skip when SPY is down on the day | 106 | -143 | -1.35 | 169 | -268 | -1.59 | +143 |
| skip when SPY is below its VWAP | 120 | -206 | -1.72 | 155 | -205 | -1.33 | +206 |
| skip when SPY fell over the last 15 min | 100 | -147 | -1.47 | 175 | -265 | -1.51 | +147 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 68 | -184 | -2.71 | 207 | -227 | -1.10 | +184 |
| skip stock not beating SPY over 15 min | 44 | -50 | -1.14 | 231 | -361 | -1.56 | +50 |
| skip afternoon entries (2:00-3:45 PM) | 60 | -212 | -3.53 | 215 | -200 | -0.93 | +212 |
| skip volume spikes above 5x average | 57 | -136 | -2.39 | 218 | -275 | -1.26 | +136 |
| skip when the stop is inside normal noise (range > stop) | 30 | -32 | -1.07 | 245 | -380 | -1.55 | +32 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 39 | -35 | -0.90 | 236 | -377 | -1.60 | +35 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 127 | -347 | -2.73 | 148 | -64 | -0.43 | +347 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 51% (36-67) | +1.89 | +0.19 | +7 |  |
| 60-240 | 113 | 38% (30-47) | -0.19 | -1.46 | -165 |  |
| 240-375 | 77 | 32% (23-44) | -1.21 | -2.94 | -226 |  |
| 375-390 | 48 | 46% (33-60) | +0.92 | -0.58 | -28 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 55 | 42% (30-55) | +0.37 | -0.83 | -46 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 68 | 32% (22-44) | -0.51 | -1.83 | -125 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 120 | 40% (32-49) | -0.13 | -1.72 | -206 |  |
| above VWAP | 155 | 39% (32-47) | +0.10 | -1.33 | -205 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 92 | 39% (30-49) | +0.01 | -1.19 | -109 |  |
| (0.133, 0.376] | 91 | 43% (33-53) | +0.13 | -1.38 | -126 |  |
| (0.376, 5.591] | 92 | 37% (28-47) | -0.14 | -1.92 | -176 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.12] | 91 | 46% (36-56) | +0.65 | -0.51 | -47 |  |
| (0.12, 0.444] | 90 | 41% (32-51) | +0.48 | -1.36 | -123 |  |
| (0.444, 4.846] | 91 | 33% (24-43) | -0.98 | -2.50 | -228 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.385] | 92 | 43% (34-54) | +0.36 | -1.34 | -123 |  |
| (-0.385, 0.401] | 91 | 44% (34-54) | +0.81 | -0.28 | -26 |  |
| (0.401, 9.926] | 92 | 32% (23-42) | -1.16 | -2.85 | -263 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 92 | 39% (30-49) | -0.33 | -1.66 | -153 |  |
| (0.0559, 0.127] | 91 | 45% (35-55) | +0.57 | -0.84 | -77 |  |
| (0.127, 0.924] | 92 | 35% (26-45) | -0.23 | -1.98 | -182 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 92 | 43% (34-54) | +0.30 | -0.75 | -69 |  |
| (0.217, 0.341] | 91 | 41% (31-51) | +0.24 | -1.49 | -135 |  |
| (0.341, 2.663] | 92 | 35% (26-45) | -0.54 | -2.25 | -207 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.37] | 92 | 37% (28-47) | -0.13 | -1.58 | -145 |  |
| (2.37, 3.635] | 91 | 46% (36-56) | +0.61 | -0.91 | -83 |  |
| (3.635, 19.488] | 92 | 36% (27-46) | -0.47 | -1.99 | -183 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 92 | 47% (37-57) | +0.45 | -0.31 | -29 |  |
| (0.104, 0.166] | 91 | 35% (26-45) | -0.44 | -1.66 | -151 |  |
| (0.166, 0.76] | 92 | 37% (28-47) | -0.02 | -2.52 | -231 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.043] | 50 | 34% (22-48) | -0.73 | -1.54 | -77 |  |
| (-1.043, 0.616] | 49 | 49% (36-63) | +1.02 | +0.43 | +21 |  |
| (0.616, 7.522] | 50 | 42% (29-56) | +0.17 | -0.55 | -27 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.544] | 52 | 46% (33-59) | +0.36 | -0.28 | -15 |  |
| (0.544, 0.839] | 52 | 40% (28-54) | -0.13 | -0.83 | -43 |  |
| (0.839, 3.799] | 52 | 37% (25-50) | -0.14 | -0.96 | -50 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.866] | 52 | 42% (30-56) | +0.05 | -0.54 | -28 |  |
| (0.866, 1.536] | 52 | 44% (32-58) | +0.60 | -0.10 | -5 |  |
| (1.536, 9.058] | 52 | 37% (25-50) | -0.57 | -1.44 | -75 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.384] | 52 | 40% (28-54) | -0.14 | -0.72 | -37 |  |
| (0.384, 0.605] | 52 | 48% (35-61) | +0.78 | +0.04 | +2 |  |
| (0.605, 4.001] | 52 | 35% (23-48) | -0.56 | -1.40 | -73 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 137, target 69, time_stop 56, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 92 | 35% | 16% | 42% |
| (0.104, 0.166] | 91 | 57% | 26% | 11% |
| (0.166, 0.76] | 92 | 58% | 33% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
