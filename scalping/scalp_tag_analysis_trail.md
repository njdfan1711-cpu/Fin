# Scalp signal analysis (trail exits)

_176 tagged trades, 12 trading days (2026-10-01 to 2026-10-16). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 176 | 35% (29-43) | -0.52 | -2.35 | -414 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 63 | -7 | -0.11 | 113 | -407 | -3.60 | +7 |
| skip first 30 min | 43 | -14 | -0.34 | 133 | -399 | -3.00 | +14 |
| skip when SPY is down on the day | 67 | -164 | -2.45 | 109 | -250 | -2.29 | +164 |
| skip when SPY is below its VWAP | 61 | -166 | -2.73 | 115 | -248 | -2.15 | +166 |
| skip when SPY fell over the last 15 min | 54 | -155 | -2.87 | 122 | -259 | -2.12 | +155 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 33 | -169 | -5.12 | 143 | -245 | -1.71 | +169 |
| skip stock not beating SPY over 15 min | 16 | -53 | -3.32 | 160 | -361 | -2.25 | +53 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 89 | -267 | -3.00 | 87 | -147 | -1.69 | +267 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 43 | 37% (24-52) | +0.63 | -0.34 | -14 |  |
| 15-60 | 18 | 50% (29-71) | +0.36 | -2.45 | -44 |  |
| 60-240 | 56 | 29% (18-41) | -1.53 | -3.15 | -177 |  |
| 240-375 | 39 | 33% (21-49) | -2.38 | -4.77 | -186 |  |
| 375-390 | 20 | 40% (22-61) | +2.69 | +0.37 | +7 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 20 | 35% (18-57) | -1.39 | -3.08 | -62 |  |
| -0.2 to 0 | 47 | 36% (24-50) | +0.07 | -2.18 | -103 |  |
| 0 to 0.2 | 67 | 28% (19-40) | -1.64 | -2.98 | -200 |  |
| > 0.2 | 42 | 45% (31-60) | +1.03 | -1.19 | -50 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 61 | 31% (21-44) | -0.54 | -2.73 | -166 |  |
| above VWAP | 115 | 37% (29-47) | -0.50 | -2.15 | -248 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 45 | 31% (20-46) | +0.10 | -1.73 | -78 |  |
| (0.136, 0.37] | 44 | 45% (32-60) | -1.11 | -3.12 | -137 |  |
| (0.37, 1.555] | 44 | 27% (16-42) | -1.69 | -4.19 | -184 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.154] | 45 | 40% (27-55) | +0.63 | -1.01 | -45 |  |
| (0.154, 0.412] | 44 | 34% (22-49) | -1.05 | -3.57 | -157 |  |
| (0.412, 1.192] | 44 | 30% (18-44) | -2.28 | -4.47 | -197 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.106] | 59 | 37% (26-50) | -0.80 | -3.16 | -186 |  |
| (-0.106, 0.374] | 58 | 47% (34-59) | +1.13 | -0.02 | -1 |  |
| (0.374, 2.726] | 59 | 22% (13-34) | -1.85 | -3.84 | -226 | ▼ |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0605] | 59 | 39% (28-52) | -0.56 | -2.15 | -127 |  |
| (0.0605, 0.135] | 58 | 38% (27-51) | -0.78 | -2.48 | -144 |  |
| (0.135, 0.786] | 59 | 29% (19-41) | -0.22 | -2.42 | -143 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.224] | 59 | 42% (31-55) | +0.14 | -0.96 | -57 |  |
| (0.224, 0.417] | 58 | 29% (19-42) | -1.83 | -4.50 | -261 |  |
| (0.417, 3.871] | 59 | 34% (23-47) | +0.11 | -1.63 | -96 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.623] | 59 | 39% (28-52) | -0.66 | -2.55 | -151 |  |
| (2.623, 4.926] | 58 | 38% (27-51) | +0.21 | -1.89 | -110 |  |
| (4.926, 18.76] | 59 | 29% (19-41) | -1.10 | -2.60 | -154 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0968] | 59 | 42% (31-55) | +0.18 | -0.48 | -28 |  |
| (0.0968, 0.145] | 59 | 36% (25-48) | -1.36 | -2.67 | -158 |  |
| (0.145, 0.392] | 58 | 28% (18-40) | -0.38 | -3.93 | -228 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 12% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 2% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 87, trail_stop 66, time_stop 23

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0968] | 59 | 37% | 32% | 31% |
| (0.0968, 0.145] | 59 | 54% | 41% | 5% |
| (0.145, 0.392] | 58 | 57% | 40% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
