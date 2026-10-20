# Scalp signal analysis (trail exits)

_203 tagged trades, 14 trading days (2026-10-01 to 2026-10-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 203 | 33% (27-40) | -0.73 | -2.64 | -536 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 79 | -75 | -0.95 | 124 | -461 | -3.72 | +75 |
| skip first 30 min | 59 | -86 | -1.46 | 144 | -450 | -3.12 | +86 |
| skip when SPY is down on the day | 73 | -206 | -2.82 | 130 | -330 | -2.54 | +206 |
| skip when SPY is below its VWAP | 68 | -205 | -3.01 | 135 | -332 | -2.46 | +205 |
| skip when SPY fell over the last 15 min | 58 | -181 | -3.13 | 145 | -355 | -2.45 | +181 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 36 | -181 | -5.02 | 167 | -355 | -2.13 | +181 |
| skip stock not beating SPY over 15 min | 19 | -59 | -3.11 | 184 | -477 | -2.59 | +59 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 113 | -385 | -3.40 | 90 | -151 | -1.68 | +385 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 58 | 31% (21-44) | -0.20 | -1.38 | -80 |  |
| 15-60 | 20 | 50% (30-70) | +0.07 | -2.52 | -50 |  |
| 60-240 | 62 | 29% (19-41) | -1.36 | -3.13 | -194 |  |
| 240-375 | 42 | 31% (19-46) | -2.61 | -5.15 | -216 |  |
| 375-390 | 21 | 38% (21-59) | +2.69 | +0.23 | +5 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 32% (16-53) | -1.38 | -3.24 | -71 |  |
| -0.2 to 0 | 51 | 33% (22-47) | -0.41 | -2.64 | -135 |  |
| 0 to 0.2 | 82 | 28% (19-39) | -1.53 | -2.99 | -245 |  |
| > 0.2 | 48 | 42% (29-56) | +0.60 | -1.78 | -85 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 68 | 29% (20-41) | -0.68 | -3.01 | -205 |  |
| above VWAP | 135 | 35% (27-43) | -0.75 | -2.46 | -332 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 49 | 31% (20-45) | +0.01 | -1.90 | -93 |  |
| (0.136, 0.374] | 49 | 45% (32-59) | -0.92 | -2.91 | -143 |  |
| (0.374, 1.555] | 47 | 26% (15-40) | -1.95 | -4.69 | -220 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.15] | 48 | 33% (22-47) | -0.05 | -2.02 | -97 |  |
| (0.15, 0.405] | 48 | 40% (27-54) | -0.60 | -2.91 | -140 |  |
| (0.405, 1.192] | 48 | 29% (18-43) | -2.06 | -4.44 | -213 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.108] | 68 | 35% (25-47) | -1.07 | -3.25 | -221 |  |
| (-0.108, 0.38] | 67 | 43% (32-55) | +1.04 | -0.33 | -22 |  |
| (0.38, 2.726] | 68 | 21% (13-32) | -2.14 | -4.31 | -293 | ▼ |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0583] | 68 | 34% (24-46) | -1.71 | -3.38 | -230 |  |
| (0.0583, 0.135] | 67 | 37% (27-49) | +0.25 | -1.63 | -109 |  |
| (0.135, 0.786] | 68 | 28% (19-40) | -0.72 | -2.90 | -197 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.229] | 68 | 38% (28-50) | -0.33 | -1.60 | -109 |  |
| (0.229, 0.434] | 67 | 33% (23-45) | -1.37 | -4.15 | -278 |  |
| (0.434, 4.92] | 68 | 28% (19-40) | -0.49 | -2.20 | -149 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.603] | 68 | 38% (28-50) | -0.70 | -2.71 | -184 |  |
| (2.603, 4.825] | 67 | 34% (24-46) | -0.22 | -2.48 | -166 |  |
| (4.825, 18.76] | 68 | 26% (17-38) | -1.26 | -2.73 | -186 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0986] | 68 | 37% (26-49) | -0.37 | -1.12 | -76 |  |
| (0.0986, 0.163] | 67 | 36% (25-48) | -1.30 | -2.69 | -180 |  |
| (0.163, 0.395] | 68 | 26% (17-38) | -0.53 | -4.12 | -280 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 13% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 104, trail_stop 73, time_stop 26

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0986] | 68 | 40% | 29% | 31% |
| (0.0986, 0.163] | 67 | 54% | 42% | 4% |
| (0.163, 0.395] | 68 | 60% | 37% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
