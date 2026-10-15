# Scalp signal analysis (trail exits)

_168 tagged trades, 11 trading days (2026-10-01 to 2026-10-15). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 168 | 35% (28-43) | -0.48 | -2.31 | -388 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | -6 | -0.09 | 108 | -382 | -3.54 | +6 |
| skip first 30 min | 41 | -19 | -0.47 | 127 | -369 | -2.90 | +19 |
| skip when SPY is down on the day | 59 | -138 | -2.35 | 109 | -250 | -2.29 | +138 |
| skip when SPY is below its VWAP | 56 | -144 | -2.57 | 112 | -244 | -2.18 | +144 |
| skip when SPY fell over the last 15 min | 52 | -135 | -2.59 | 116 | -253 | -2.19 | +135 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 32 | -155 | -4.84 | 136 | -233 | -1.72 | +155 |
| skip stock not beating SPY over 15 min | 15 | -47 | -3.13 | 153 | -341 | -2.23 | +47 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 86 | -246 | -2.86 | 82 | -142 | -1.74 | +246 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 41 | 37% (24-52) | +0.51 | -0.47 | -19 |  |
| 15-60 | 17 | 53% (31-74) | +0.73 | -1.74 | -30 |  |
| 60-240 | 52 | 27% (17-40) | -1.55 | -3.21 | -167 |  |
| 240-375 | 39 | 33% (21-49) | -2.38 | -4.77 | -186 |  |
| 375-390 | 19 | 42% (23-64) | +3.14 | +0.73 | +14 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 15 | 33% (15-58) | -1.12 | -2.62 | -39 |  |
| -0.2 to 0 | 44 | 36% (24-51) | +0.07 | -2.25 | -99 |  |
| 0 to 0.2 | 67 | 28% (19-40) | -1.64 | -2.98 | -200 |  |
| > 0.2 | 42 | 45% (31-60) | +1.03 | -1.19 | -50 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 56 | 30% (20-43) | -0.40 | -2.57 | -144 |  |
| above VWAP | 112 | 38% (29-47) | -0.52 | -2.18 | -244 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 43 | 33% (20-47) | +0.37 | -1.54 | -66 |  |
| (0.136, 0.37] | 42 | 43% (29-58) | -1.30 | -3.31 | -139 |  |
| (0.37, 1.555] | 42 | 29% (17-44) | -1.48 | -3.89 | -163 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.153] | 43 | 40% (26-54) | +0.70 | -0.95 | -41 |  |
| (0.153, 0.406] | 42 | 36% (23-51) | -0.78 | -3.27 | -137 |  |
| (0.406, 1.192] | 42 | 29% (17-44) | -2.34 | -4.53 | -190 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.1] | 56 | 38% (26-51) | -0.65 | -2.96 | -166 |  |
| (-0.1, 0.377] | 56 | 45% (32-58) | +0.85 | -0.33 | -18 |  |
| (0.377, 2.726] | 56 | 23% (14-36) | -1.63 | -3.64 | -204 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0593] | 56 | 39% (28-52) | -1.59 | -3.09 | -173 |  |
| (0.0593, 0.136] | 56 | 39% (28-52) | +0.48 | -1.29 | -72 |  |
| (0.136, 0.786] | 56 | 27% (17-40) | -0.32 | -2.55 | -143 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.22] | 56 | 45% (32-58) | +0.46 | -0.67 | -38 |  |
| (0.22, 0.416] | 56 | 29% (18-41) | -1.85 | -4.42 | -248 |  |
| (0.416, 3.871] | 56 | 32% (21-45) | -0.04 | -1.84 | -103 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.624] | 56 | 39% (28-52) | -0.68 | -2.64 | -148 |  |
| (2.624, 5.006] | 56 | 39% (28-52) | +0.44 | -1.64 | -92 |  |
| (5.006, 18.76] | 56 | 27% (17-40) | -1.20 | -2.66 | -149 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0958] | 56 | 45% (32-58) | +0.38 | -0.28 | -16 |  |
| (0.0958, 0.145] | 57 | 35% (24-48) | -1.39 | -2.71 | -155 |  |
| (0.145, 0.392] | 55 | 25% (16-38) | -0.41 | -3.96 | -218 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 12% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 2% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 83, trail_stop 62, time_stop 23

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0958] | 56 | 36% | 32% | 32% |
| (0.0958, 0.145] | 57 | 54% | 40% | 5% |
| (0.145, 0.392] | 55 | 58% | 38% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
