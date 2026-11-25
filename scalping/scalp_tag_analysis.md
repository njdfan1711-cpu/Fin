# Scalp signal analysis (fixed exits)

_325 tagged trades, 39 trading days (2026-10-01 to 2026-11-24). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 325 | 40% (35-45) | +0.02 | -1.35 | -438 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +0 | +0.01 | 263 | -438 | -1.67 | -0 |
| skip first 30 min | 4 | -21 | -5.34 | 321 | -417 | -1.30 | +21 |
| skip when SPY is down on the day | 148 | -164 | -1.11 | 177 | -274 | -1.55 | +164 |
| skip when SPY is below its VWAP | 140 | -185 | -1.32 | 185 | -253 | -1.37 | +185 |
| skip when SPY fell over the last 15 min | 107 | -115 | -1.08 | 218 | -323 | -1.48 | +115 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 80 | -182 | -2.28 | 245 | -256 | -1.04 | +182 |
| skip stock not beating SPY over 15 min | 51 | -82 | -1.60 | 274 | -356 | -1.30 | +82 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -227 | -3.25 | 255 | -211 | -0.83 | +227 |
| skip volume spikes above 5x average | 70 | -160 | -2.28 | 255 | -278 | -1.09 | +160 |
| skip when the stop is inside normal noise (range > stop) | 47 | -39 | -0.82 | 278 | -399 | -1.44 | +39 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 52 | -60 | -1.15 | 273 | -378 | -1.39 | +60 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -363 | -2.63 | 187 | -75 | -0.40 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 40 | 50% (35-65) | +1.68 | +0.08 | +3 |  |
| 60-240 | 134 | 38% (30-47) | -0.26 | -1.40 | -188 |  |
| 240-375 | 89 | 31% (23-42) | -1.25 | -2.85 | -254 |  |
| 375-390 | 62 | 48% (36-61) | +1.36 | +0.01 | +0 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 91 | 41% (31-51) | +0.22 | -0.76 | -69 |  |
| -0.2 to 0 | 57 | 42% (30-55) | +0.33 | -1.65 | -94 |  |
| 0 to 0.2 | 70 | 33% (23-44) | -0.44 | -1.75 | -122 |  |
| > 0.2 | 107 | 42% (33-52) | -0.02 | -1.42 | -152 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 140 | 41% (34-50) | +0.14 | -1.32 | -185 |  |
| above VWAP | 185 | 38% (32-46) | -0.08 | -1.37 | -253 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.12] | 109 | 38% (29-47) | -0.36 | -1.36 | -149 |  |
| (0.12, 0.37] | 108 | 43% (34-52) | +0.32 | -1.12 | -121 |  |
| (0.37, 5.591] | 108 | 39% (30-48) | +0.10 | -1.56 | -169 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.139] | 107 | 48% (38-57) | +0.86 | -0.23 | -25 |  |
| (0.139, 0.448] | 107 | 38% (30-48) | +0.07 | -1.57 | -168 |  |
| (0.448, 4.846] | 107 | 35% (26-44) | -0.71 | -2.10 | -224 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.581] | 109 | 44% (35-53) | +0.46 | -0.88 | -96 |  |
| (-0.581, 0.319] | 108 | 38% (29-47) | +0.13 | -1.08 | -116 |  |
| (0.319, 9.926] | 108 | 37% (29-46) | -0.55 | -2.09 | -226 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.056] | 109 | 39% (30-48) | -0.44 | -1.66 | -181 |  |
| (0.056, 0.126] | 108 | 45% (36-55) | +0.63 | -0.63 | -68 |  |
| (0.126, 0.924] | 108 | 35% (27-45) | -0.14 | -1.75 | -189 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.225] | 109 | 43% (34-52) | +0.28 | -0.70 | -76 |  |
| (0.225, 0.35] | 108 | 39% (30-48) | -0.08 | -1.73 | -186 |  |
| (0.35, 2.663] | 108 | 37% (29-46) | -0.15 | -1.62 | -175 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 109 | 36% (27-45) | -0.24 | -1.59 | -173 |  |
| (2.389, 3.632] | 108 | 48% (39-57) | +0.91 | -0.48 | -52 |  |
| (3.632, 19.488] | 108 | 35% (27-45) | -0.62 | -1.97 | -213 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 109 | 45% (36-54) | +0.31 | -0.42 | -46 |  |
| (0.104, 0.167] | 108 | 36% (28-46) | -0.39 | -1.55 | -167 |  |
| (0.167, 0.76] | 108 | 38% (29-47) | +0.12 | -2.08 | -225 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.864] | 67 | 31% (22-43) | -1.10 | -1.88 | -126 |  |
| (-0.864, 0.658] | 67 | 46% (35-58) | +0.71 | +0.16 | +10 |  |
| (0.658, 14.989] | 65 | 46% (35-58) | +0.82 | +0.09 | +6 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.546] | 69 | 43% (32-55) | +0.08 | -0.54 | -37 |  |
| (0.546, 0.887] | 68 | 43% (32-54) | +0.06 | -0.64 | -43 |  |
| (0.887, 3.799] | 69 | 36% (26-48) | -0.01 | -0.78 | -54 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.954] | 69 | 43% (32-55) | +0.00 | -0.57 | -39 |  |
| (0.954, 1.68] | 68 | 43% (32-54) | +0.43 | -0.26 | -18 |  |
| (1.68, 9.058] | 69 | 36% (26-48) | -0.29 | -1.12 | -77 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 69 | 36% (26-48) | -0.55 | -1.12 | -77 |  |
| (0.409, 0.627] | 68 | 50% (38-62) | +0.99 | +0.29 | +19 |  |
| (0.627, 4.001] | 69 | 36% (26-48) | -0.29 | -1.11 | -76 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.20%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 164, target 82, time_stop 63, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 109 | 38% | 17% | 39% |
| (0.104, 0.167] | 108 | 56% | 25% | 11% |
| (0.167, 0.76] | 108 | 57% | 33% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
