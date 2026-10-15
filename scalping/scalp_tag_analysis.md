# Scalp signal analysis (fixed exits)

_165 tagged trades, 11 trading days (2026-10-01 to 2026-10-15). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 165 | 37% (30-45) | -0.16 | -1.96 | -324 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | -76 | -1.27 | 105 | -247 | -2.36 | +76 |
| skip first 30 min | 41 | -47 | -1.15 | 124 | -277 | -2.23 | +47 |
| skip when SPY is down on the day | 59 | -90 | -1.52 | 106 | -234 | -2.21 | +90 |
| skip when SPY is below its VWAP | 56 | -112 | -1.99 | 109 | -212 | -1.94 | +112 |
| skip when SPY fell over the last 15 min | 51 | -101 | -1.99 | 114 | -222 | -1.95 | +101 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 31 | -122 | -3.94 | 134 | -202 | -1.50 | +122 |
| skip stock not beating SPY over 15 min | 14 | -23 | -1.63 | 151 | -301 | -1.99 | +23 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 85 | -220 | -2.59 | 80 | -104 | -1.29 | +220 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 41 | 34% (22-49) | -0.16 | -1.15 | -47 |  |
| 15-60 | 17 | 65% (41-83) | +3.53 | +1.06 | +18 | ▲ |
| 60-240 | 49 | 35% (23-49) | -0.43 | -1.99 | -97 |  |
| 240-375 | 39 | 28% (17-44) | -1.91 | -4.30 | -168 |  |
| 375-390 | 19 | 42% (23-64) | +0.87 | -1.54 | -29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 15 | 40% (20-64) | +0.07 | -1.43 | -21 |  |
| -0.2 to 0 | 44 | 43% (30-58) | +0.77 | -1.55 | -68 |  |
| 0 to 0.2 | 67 | 30% (20-42) | -0.81 | -2.15 | -144 |  |
| > 0.2 | 39 | 41% (27-57) | -0.16 | -2.30 | -90 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 56 | 41% (29-54) | +0.18 | -1.99 | -112 |  |
| above VWAP | 109 | 35% (27-44) | -0.33 | -1.94 | -212 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 42 | 40% (27-56) | +0.03 | -1.71 | -72 |  |
| (0.136, 0.374] | 42 | 40% (27-56) | -0.30 | -2.36 | -99 |  |
| (0.374, 1.555] | 40 | 32% (20-48) | -0.20 | -2.65 | -106 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.154] | 42 | 48% (33-62) | +0.85 | -0.87 | -37 |  |
| (0.154, 0.412] | 41 | 34% (22-49) | -0.18 | -2.58 | -106 |  |
| (0.412, 1.192] | 41 | 32% (20-47) | -1.16 | -3.27 | -134 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.1] | 55 | 40% (28-53) | +0.27 | -2.07 | -114 |  |
| (-0.1, 0.374] | 55 | 40% (28-53) | +0.35 | -0.82 | -45 |  |
| (0.374, 2.726] | 55 | 31% (20-44) | -1.09 | -3.00 | -165 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0605] | 55 | 42% (30-55) | +0.02 | -1.36 | -75 |  |
| (0.0605, 0.138] | 55 | 40% (28-53) | +0.13 | -1.65 | -91 |  |
| (0.138, 0.786] | 55 | 29% (19-42) | -0.62 | -2.88 | -158 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.226] | 55 | 44% (31-57) | +0.23 | -0.91 | -50 |  |
| (0.226, 0.419] | 55 | 35% (23-48) | -0.23 | -2.70 | -148 |  |
| (0.419, 3.871] | 55 | 33% (22-46) | -0.47 | -2.28 | -126 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.613] | 55 | 44% (31-57) | +0.79 | -1.20 | -66 |  |
| (2.613, 5.006] | 55 | 44% (31-57) | +0.55 | -1.40 | -77 |  |
| (5.006, 18.76] | 55 | 24% (14-36) | -1.81 | -3.28 | -181 | ▼ |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0958] | 55 | 45% (33-58) | +0.30 | -0.36 | -20 |  |
| (0.0958, 0.145] | 56 | 34% (23-47) | -0.16 | -1.49 | -84 |  |
| (0.145, 0.392] | 54 | 31% (21-45) | -0.62 | -4.07 | -220 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 27% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 54%
- Exit mix: stop 88, target 45, time_stop 32

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0958] | 55 | 38% | 20% | 42% |
| (0.0958, 0.145] | 56 | 59% | 32% | 9% |
| (0.145, 0.392] | 54 | 63% | 30% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
