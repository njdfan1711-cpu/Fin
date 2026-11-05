# Scalp signal analysis (fixed exits)

_236 tagged trades, 26 trading days (2026-10-01 to 2026-11-05). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 236 | 41% (35-47) | +0.21 | -1.42 | -336 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 40 | -2 | -0.05 | 196 | -334 | -1.71 | +2 |
| skip first 30 min | 2 | -8 | -4.06 | 234 | -328 | -1.40 | +8 |
| skip when SPY is down on the day | 93 | -100 | -1.07 | 143 | -236 | -1.65 | +100 |
| skip when SPY is below its VWAP | 103 | -177 | -1.72 | 133 | -159 | -1.19 | +177 |
| skip when SPY fell over the last 15 min | 85 | -116 | -1.37 | 151 | -220 | -1.46 | +116 |
| skip over-extended (30-min run in top quarter, > 0.50%) | 59 | -163 | -2.76 | 177 | -173 | -0.98 | +163 |
| skip stock not beating SPY over 15 min | 38 | -30 | -0.78 | 198 | -306 | -1.55 | +30 |
| skip afternoon entries (2:00-3:45 PM) | 50 | -214 | -4.28 | 186 | -122 | -0.66 | +214 |
| skip volume spikes above 5x average | 45 | -130 | -2.88 | 191 | -206 | -1.08 | +130 |
| skip when the stop is inside normal noise (range > stop) | 21 | +10 | +0.48 | 215 | -346 | -1.61 | -10 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 29 | -10 | -0.34 | 207 | -326 | -1.58 | +10 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 116 | -320 | -2.76 | 120 | -16 | -0.13 | +320 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 53% (37-69) | +2.10 | +0.32 | +11 |  |
| 60-240 | 96 | 40% (30-50) | +0.10 | -1.29 | -123 |  |
| 240-375 | 66 | 30% (21-42) | -1.46 | -3.36 | -222 |  |
| 375-390 | 40 | 50% (35-65) | +1.62 | -0.05 | -2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 42 | 48% (33-62) | +1.27 | -0.06 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 66 | 33% (23-45) | -0.38 | -1.70 | -112 |  |
| > 0.2 | 77 | 43% (32-54) | +0.10 | -1.61 | -124 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 103 | 41% (32-50) | +0.02 | -1.72 | -177 |  |
| above VWAP | 133 | 41% (33-49) | +0.35 | -1.19 | -159 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.134] | 79 | 42% (32-53) | +0.33 | -0.95 | -75 |  |
| (0.134, 0.38] | 78 | 45% (34-56) | +0.38 | -1.26 | -98 |  |
| (0.38, 5.591] | 79 | 35% (26-46) | -0.10 | -2.06 | -163 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.109] | 78 | 46% (36-57) | +0.80 | -0.45 | -35 |  |
| (0.109, 0.428] | 78 | 41% (31-52) | +0.43 | -1.50 | -117 |  |
| (0.428, 4.846] | 78 | 36% (26-47) | -0.52 | -2.26 | -176 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.0920000000000005, -0.362] | 79 | 44% (34-55) | +0.69 | -1.16 | -91 |  |
| (-0.362, 0.398] | 78 | 46% (36-57) | +1.08 | -0.09 | -7 |  |
| (0.398, 4.204] | 79 | 32% (22-43) | -1.13 | -3.01 | -238 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 79 | 42% (32-53) | -0.04 | -1.48 | -117 |  |
| (0.056, 0.127] | 78 | 46% (36-57) | +0.79 | -0.75 | -59 |  |
| (0.127, 0.924] | 79 | 34% (25-45) | -0.12 | -2.03 | -160 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 79 | 44% (34-55) | +0.37 | -0.76 | -60 |  |
| (0.211, 0.328] | 78 | 41% (31-52) | +0.34 | -1.43 | -111 |  |
| (0.328, 2.663] | 79 | 37% (27-48) | -0.09 | -2.09 | -165 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.324] | 79 | 38% (28-49) | +0.14 | -1.40 | -111 |  |
| (2.324, 3.635] | 78 | 50% (39-61) | +1.16 | -0.51 | -39 |  |
| (3.635, 18.762] | 79 | 34% (25-45) | -0.67 | -2.35 | -186 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0991] | 79 | 47% (36-58) | +0.48 | -0.28 | -22 |  |
| (0.0991, 0.153] | 78 | 36% (26-47) | -0.23 | -1.41 | -110 |  |
| (0.153, 0.76] | 79 | 39% (29-50) | +0.37 | -2.59 | -204 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.043] | 37 | 35% (22-51) | -0.55 | -1.37 | -51 |  |
| (-1.043, 0.444] | 37 | 46% (31-62) | +0.63 | +0.05 | +2 |  |
| (0.444, 5.599] | 36 | 53% (37-68) | +1.88 | +1.15 | +41 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.519] | 39 | 46% (32-61) | +0.48 | -0.13 | -5 |  |
| (0.519, 0.772] | 39 | 38% (25-54) | -0.32 | -1.07 | -42 |  |
| (0.772, 3.799] | 39 | 46% (32-61) | +1.20 | +0.37 | +14 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.822] | 39 | 41% (27-57) | -0.17 | -0.71 | -28 |  |
| (0.822, 1.412] | 39 | 44% (29-59) | +0.60 | -0.16 | -6 |  |
| (1.412, 7.752] | 39 | 46% (32-61) | +0.93 | +0.03 | +1 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.355] | 39 | 44% (29-59) | +0.42 | -0.14 | -6 |  |
| (0.355, 0.576] | 39 | 46% (32-61) | +0.47 | -0.30 | -12 |  |
| (0.576, 4.001] | 39 | 41% (27-57) | +0.47 | -0.39 | -15 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.19%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 113, target 61, time_stop 51, eod 11

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0991] | 79 | 34% | 16% | 43% |
| (0.0991, 0.153] | 78 | 55% | 27% | 13% |
| (0.153, 0.76] | 79 | 54% | 34% | 9% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
