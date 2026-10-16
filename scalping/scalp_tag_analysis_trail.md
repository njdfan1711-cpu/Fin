# Scalp signal analysis (trail exits)

_175 tagged trades, 12 trading days (2026-10-01 to 2026-10-16). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 175 | 35% (29-43) | -0.49 | -2.33 | -407 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | -1 | -0.01 | 113 | -407 | -3.60 | +1 |
| skip first 30 min | 43 | -14 | -0.34 | 132 | -393 | -2.98 | +14 |
| skip when SPY is down on the day | 66 | -158 | -2.39 | 109 | -250 | -2.29 | +158 |
| skip when SPY is below its VWAP | 60 | -160 | -2.67 | 115 | -248 | -2.15 | +160 |
| skip when SPY fell over the last 15 min | 54 | -155 | -2.87 | 121 | -252 | -2.08 | +155 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 33 | -169 | -5.13 | 142 | -238 | -1.68 | +169 |
| skip stock not beating SPY over 15 min | 16 | -53 | -3.32 | 159 | -354 | -2.23 | +53 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 89 | -267 | -3.00 | 86 | -140 | -1.63 | +267 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 43 | 37% (24-52) | +0.63 | -0.34 | -14 |  |
| 15-60 | 18 | 50% (29-71) | +0.36 | -2.45 | -44 |  |
| 60-240 | 56 | 29% (18-41) | -1.53 | -3.15 | -177 |  |
| 240-375 | 39 | 33% (21-49) | -2.38 | -4.77 | -186 |  |
| 375-390 | 19 | 42% (23-64) | +3.14 | +0.73 | +14 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 19 | 37% (19-59) | -1.15 | -2.91 | -55 |  |
| -0.2 to 0 | 47 | 36% (24-50) | +0.07 | -2.18 | -103 |  |
| 0 to 0.2 | 67 | 28% (19-40) | -1.64 | -2.98 | -200 |  |
| > 0.2 | 42 | 45% (31-60) | +1.03 | -1.19 | -50 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 60 | 32% (21-44) | -0.45 | -2.67 | -160 |  |
| above VWAP | 115 | 37% (29-47) | -0.50 | -2.15 | -248 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 44 | 32% (20-47) | +0.23 | -1.64 | -72 |  |
| (0.136, 0.369] | 44 | 45% (32-60) | -1.09 | -2.99 | -132 |  |
| (0.369, 1.555] | 44 | 27% (16-42) | -1.69 | -4.30 | -189 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.153] | 44 | 39% (26-53) | +0.55 | -1.07 | -47 |  |
| (0.153, 0.408] | 44 | 36% (24-51) | -0.82 | -3.28 | -144 |  |
| (0.408, 1.192] | 44 | 30% (18-44) | -2.28 | -4.59 | -202 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.108] | 59 | 37% (26-50) | -0.80 | -3.16 | -186 |  |
| (-0.108, 0.374] | 58 | 47% (34-59) | +1.13 | -0.02 | -1 |  |
| (0.374, 2.726] | 58 | 22% (14-35) | -1.78 | -3.79 | -220 | ▼ |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0604] | 59 | 39% (28-52) | -0.56 | -2.15 | -127 |  |
| (0.0604, 0.136] | 58 | 40% (28-53) | -0.58 | -2.31 | -134 |  |
| (0.136, 0.786] | 58 | 28% (18-40) | -0.32 | -2.52 | -146 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.228] | 59 | 42% (31-55) | +0.19 | -0.91 | -53 |  |
| (0.228, 0.419] | 58 | 31% (21-44) | -1.62 | -4.30 | -249 |  |
| (0.419, 3.871] | 58 | 33% (22-46) | -0.05 | -1.81 | -105 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.623] | 59 | 39% (28-52) | -0.66 | -2.55 | -151 |  |
| (2.623, 4.966] | 58 | 38% (27-51) | +0.21 | -1.98 | -115 |  |
| (4.966, 18.76] | 58 | 29% (19-42) | -1.02 | -2.45 | -142 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0967] | 59 | 42% (31-55) | +0.18 | -0.48 | -28 |  |
| (0.0967, 0.145] | 58 | 36% (25-49) | -1.28 | -2.61 | -151 |  |
| (0.145, 0.392] | 58 | 28% (18-40) | -0.38 | -3.93 | -228 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 12% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 2% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 86, trail_stop 66, time_stop 23

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0967] | 59 | 37% | 32% | 31% |
| (0.0967, 0.145] | 58 | 53% | 41% | 5% |
| (0.145, 0.392] | 58 | 57% | 40% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
