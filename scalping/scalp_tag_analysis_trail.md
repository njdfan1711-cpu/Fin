# Scalp signal analysis (trail exits)

_165 tagged trades, 11 trading days (2026-10-01 to 2026-10-15). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 165 | 35% (28-43) | -0.43 | -2.24 | -369 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | -6 | -0.09 | 105 | -364 | -3.46 | +6 |
| skip first 30 min | 41 | -19 | -0.47 | 124 | -350 | -2.82 | +19 |
| skip when SPY is down on the day | 59 | -138 | -2.35 | 106 | -231 | -2.18 | +138 |
| skip when SPY is below its VWAP | 56 | -144 | -2.57 | 109 | -225 | -2.07 | +144 |
| skip when SPY fell over the last 15 min | 51 | -129 | -2.52 | 114 | -241 | -2.11 | +129 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 31 | -148 | -4.78 | 134 | -221 | -1.65 | +148 |
| skip stock not beating SPY over 15 min | 14 | -41 | -2.93 | 151 | -328 | -2.17 | +41 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 85 | -231 | -2.72 | 80 | -138 | -1.73 | +231 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 41 | 37% (24-52) | +0.51 | -0.47 | -19 |  |
| 15-60 | 17 | 53% (31-74) | +0.73 | -1.74 | -30 |  |
| 60-240 | 49 | 27% (16-40) | -1.46 | -3.02 | -148 |  |
| 240-375 | 39 | 33% (21-49) | -2.38 | -4.77 | -186 |  |
| 375-390 | 19 | 42% (23-64) | +3.14 | +0.73 | +14 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 15 | 33% (15-58) | -1.12 | -2.62 | -39 |  |
| -0.2 to 0 | 44 | 36% (24-51) | +0.07 | -2.25 | -99 |  |
| 0 to 0.2 | 67 | 28% (19-40) | -1.64 | -2.98 | -200 |  |
| > 0.2 | 39 | 46% (32-61) | +1.34 | -0.80 | -31 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 56 | 30% (20-43) | -0.40 | -2.57 | -144 |  |
| above VWAP | 109 | 38% (29-47) | -0.45 | -2.07 | -225 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 42 | 33% (21-48) | +0.52 | -1.22 | -51 |  |
| (0.136, 0.374] | 42 | 43% (29-58) | -1.15 | -3.21 | -135 |  |
| (0.374, 1.555] | 40 | 28% (16-43) | -1.65 | -4.10 | -164 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.154] | 42 | 40% (27-56) | +0.88 | -0.84 | -35 |  |
| (0.154, 0.412] | 41 | 34% (22-49) | -0.90 | -3.30 | -135 |  |
| (0.412, 1.192] | 41 | 29% (18-44) | -2.25 | -4.37 | -179 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.1] | 55 | 36% (25-50) | -0.71 | -3.05 | -168 |  |
| (-0.1, 0.374] | 55 | 45% (33-58) | +0.97 | -0.19 | -10 |  |
| (0.374, 2.726] | 55 | 24% (14-36) | -1.56 | -3.47 | -191 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0605] | 55 | 42% (30-55) | -0.18 | -1.56 | -86 |  |
| (0.0605, 0.138] | 55 | 36% (25-50) | -0.90 | -2.67 | -147 |  |
| (0.138, 0.786] | 55 | 27% (17-40) | -0.22 | -2.48 | -137 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.226] | 55 | 44% (31-57) | +0.41 | -0.73 | -40 |  |
| (0.226, 0.419] | 55 | 31% (20-44) | -1.50 | -3.97 | -218 |  |
| (0.419, 3.871] | 55 | 31% (20-44) | -0.21 | -2.02 | -111 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.613] | 55 | 40% (28-53) | -0.58 | -2.57 | -141 |  |
| (2.613, 5.006] | 55 | 38% (27-51) | +0.40 | -1.55 | -85 |  |
| (5.006, 18.76] | 55 | 27% (17-40) | -1.12 | -2.60 | -143 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0958] | 55 | 44% (31-57) | +0.34 | -0.32 | -18 |  |
| (0.0958, 0.145] | 56 | 36% (24-49) | -1.32 | -2.65 | -149 |  |
| (0.145, 0.392] | 54 | 26% (16-39) | -0.31 | -3.76 | -203 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 13% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 2% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 81, trail_stop 62, time_stop 22

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0958] | 55 | 36% | 33% | 31% |
| (0.0958, 0.145] | 56 | 54% | 41% | 5% |
| (0.145, 0.392] | 54 | 57% | 39% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
