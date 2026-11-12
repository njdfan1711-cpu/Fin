# Scalp signal analysis (trail exits)

_263 tagged trades, 31 trading days (2026-10-01 to 2026-11-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 263 | 42% (36-48) | -0.66 | -2.19 | -577 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 47 | -12 | -0.26 | 216 | -564 | -2.61 | +12 |
| skip first 30 min | 3 | -10 | -3.32 | 260 | -567 | -2.18 | +10 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 164 | -308 | -1.88 | +268 |
| skip when SPY is below its VWAP | 112 | -326 | -2.91 | 151 | -250 | -1.66 | +326 |
| skip when SPY fell over the last 15 min | 95 | -205 | -2.16 | 168 | -371 | -2.21 | +205 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 65 | -228 | -3.50 | 198 | -349 | -1.76 | +228 |
| skip stock not beating SPY over 15 min | 42 | -93 | -2.20 | 221 | -484 | -2.19 | +93 |
| skip afternoon entries (2:00-3:45 PM) | 58 | -215 | -3.71 | 205 | -362 | -1.76 | +215 |
| skip volume spikes above 5x average | 49 | -174 | -3.55 | 214 | -403 | -1.88 | +174 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 237 | -536 | -2.26 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 36 | -57 | -1.59 | 227 | -519 | -2.29 | +57 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -416 | -3.35 | 139 | -161 | -1.16 | +416 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 49% (33-64) | -0.33 | -2.03 | -75 |  |
| 60-240 | 105 | 39% (30-49) | -1.02 | -2.34 | -246 |  |
| 240-375 | 74 | 41% (30-52) | -1.51 | -3.28 | -243 |  |
| 375-390 | 47 | 47% (33-61) | +1.25 | -0.26 | -12 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 68 | 35% (25-47) | -1.54 | -2.86 | -195 |  |
| > 0.2 | 96 | 48% (38-58) | +0.31 | -1.18 | -113 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 37% (28-46) | -1.25 | -2.91 | -326 |  |
| above VWAP | 151 | 46% (39-54) | -0.22 | -1.66 | -250 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 88 | 40% (30-50) | -0.31 | -1.53 | -135 |  |
| (0.133, 0.376] | 87 | 53% (42-63) | -0.13 | -1.68 | -146 | ▲ |
| (0.376, 5.591] | 88 | 34% (25-44) | -1.53 | -3.36 | -296 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.117] | 87 | 48% (38-59) | +0.35 | -0.84 | -73 |  |
| (0.117, 0.44] | 86 | 42% (32-52) | -0.86 | -2.67 | -230 |  |
| (0.44, 4.846] | 87 | 37% (27-47) | -1.39 | -3.03 | -263 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 88 | 45% (35-56) | -0.76 | -2.49 | -219 |  |
| (-0.367, 0.398] | 87 | 47% (37-58) | +0.47 | -0.66 | -57 |  |
| (0.398, 5.005] | 88 | 34% (25-44) | -1.67 | -3.41 | -300 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0559] | 88 | 43% (33-54) | -0.89 | -2.25 | -198 |  |
| (0.0559, 0.126] | 87 | 44% (34-54) | +0.06 | -1.40 | -121 |  |
| (0.126, 0.924] | 88 | 40% (30-50) | -1.13 | -2.92 | -257 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.214] | 88 | 44% (34-55) | +0.08 | -0.99 | -87 |  |
| (0.214, 0.334] | 87 | 45% (35-55) | -0.68 | -2.46 | -214 |  |
| (0.334, 2.663] | 88 | 38% (28-48) | -1.37 | -3.13 | -276 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.348] | 88 | 41% (31-51) | -0.62 | -2.10 | -185 |  |
| (2.348, 3.475] | 87 | 49% (39-60) | -0.18 | -1.72 | -150 |  |
| (3.475, 18.762] | 88 | 36% (27-47) | -1.17 | -2.75 | -242 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.103] | 88 | 49% (39-59) | +0.44 | -0.33 | -29 |  |
| (0.103, 0.161] | 87 | 41% (32-52) | -1.20 | -2.37 | -207 |  |
| (0.161, 0.76] | 88 | 36% (27-47) | -1.21 | -3.87 | -341 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.918] | 46 | 43% (30-58) | -1.25 | -2.06 | -95 |  |
| (-0.918, 0.616] | 45 | 53% (39-67) | +0.06 | -0.52 | -24 |  |
| (0.616, 7.522] | 46 | 57% (42-70) | -0.41 | -1.15 | -53 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.538] | 48 | 50% (36-64) | -0.37 | -1.03 | -49 |  |
| (0.538, 0.834] | 48 | 52% (38-66) | -1.05 | -1.75 | -84 |  |
| (0.834, 3.799] | 48 | 50% (36-64) | -0.51 | -1.34 | -64 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.837] | 48 | 48% (34-62) | -1.26 | -1.85 | -89 |  |
| (0.837, 1.475] | 48 | 54% (40-67) | -0.19 | -0.89 | -43 |  |
| (1.475, 9.058] | 48 | 50% (36-64) | -0.49 | -1.38 | -66 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.376] | 48 | 46% (33-60) | -0.78 | -1.36 | -65 |  |
| (0.376, 0.576] | 48 | 58% (44-71) | -0.42 | -1.17 | -56 | ▲ |
| (0.576, 4.001] | 48 | 48% (34-62) | -0.74 | -1.59 | -76 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 115, trail_stop 109, time_stop 31, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.103] | 88 | 31% | 33% | 31% |
| (0.103, 0.161] | 87 | 51% | 45% | 2% |
| (0.161, 0.76] | 88 | 50% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
