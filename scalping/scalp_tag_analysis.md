# Scalp signal analysis (fixed exits)

_203 tagged trades, 14 trading days (2026-10-01 to 2026-10-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 203 | 36% (30-43) | -0.18 | -2.09 | -425 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 79 | -101 | -1.28 | 124 | -324 | -2.61 | +101 |
| skip first 30 min | 59 | -77 | -1.30 | 144 | -348 | -2.42 | +77 |
| skip when SPY is down on the day | 73 | -123 | -1.68 | 130 | -302 | -2.32 | +123 |
| skip when SPY is below its VWAP | 68 | -152 | -2.23 | 135 | -273 | -2.02 | +152 |
| skip when SPY fell over the last 15 min | 58 | -154 | -2.65 | 145 | -271 | -1.87 | +154 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 36 | -155 | -4.32 | 167 | -270 | -1.61 | +155 |
| skip stock not beating SPY over 15 min | 19 | -41 | -2.14 | 184 | -384 | -2.09 | +41 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 113 | -338 | -2.99 | 90 | -87 | -0.97 | +338 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 58 | 34% (24-47) | -0.04 | -1.21 | -70 |  |
| 15-60 | 20 | 60% (39-78) | +2.90 | +0.31 | +6 | ▲ |
| 60-240 | 62 | 35% (25-48) | -0.36 | -2.13 | -132 |  |
| 240-375 | 42 | 26% (15-41) | -2.18 | -4.72 | -198 |  |
| 375-390 | 21 | 43% (24-63) | +1.01 | -1.46 | -31 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 41% (23-61) | +0.35 | -1.51 | -33 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.48 | -1.76 | -90 |  |
| 0 to 0.2 | 82 | 32% (23-42) | -0.46 | -1.92 | -157 |  |
| > 0.2 | 48 | 38% (25-52) | -0.65 | -3.02 | -145 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 68 | 40% (29-52) | +0.10 | -2.23 | -152 |  |
| above VWAP | 135 | 35% (27-43) | -0.32 | -2.02 | -273 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 49 | 37% (25-51) | -0.40 | -2.31 | -113 |  |
| (0.136, 0.374] | 49 | 43% (30-57) | +0.04 | -1.95 | -96 |  |
| (0.374, 1.555] | 47 | 32% (20-46) | -0.36 | -3.10 | -146 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.15] | 48 | 40% (27-54) | -0.32 | -2.29 | -110 |  |
| (0.15, 0.405] | 48 | 42% (29-56) | +0.92 | -1.40 | -67 |  |
| (0.405, 1.192] | 48 | 31% (20-45) | -1.19 | -3.57 | -171 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.108] | 68 | 40% (29-52) | +0.20 | -1.98 | -134 |  |
| (-0.108, 0.38] | 67 | 40% (29-52) | +0.53 | -0.85 | -57 |  |
| (0.38, 2.726] | 68 | 29% (20-41) | -1.27 | -3.44 | -234 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0583] | 68 | 37% (26-49) | -0.44 | -2.12 | -144 |  |
| (0.0583, 0.135] | 67 | 40% (29-52) | +0.10 | -1.79 | -120 |  |
| (0.135, 0.786] | 68 | 32% (22-44) | -0.19 | -2.37 | -161 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.229] | 68 | 38% (28-50) | -0.47 | -1.74 | -118 |  |
| (0.229, 0.434] | 67 | 37% (27-49) | +0.14 | -2.64 | -177 |  |
| (0.434, 4.92] | 68 | 34% (24-46) | -0.21 | -1.91 | -130 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.603] | 68 | 41% (30-53) | +0.51 | -1.50 | -102 |  |
| (2.603, 4.825] | 67 | 40% (29-52) | +0.06 | -2.20 | -148 |  |
| (4.825, 18.76] | 68 | 28% (19-40) | -1.11 | -2.58 | -175 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0986] | 68 | 40% (29-52) | -0.37 | -1.12 | -76 |  |
| (0.0986, 0.163] | 67 | 33% (23-45) | -0.35 | -1.74 | -117 |  |
| (0.163, 0.395] | 68 | 37% (26-49) | +0.18 | -3.42 | -232 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.21%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 28% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 56%
- Exit mix: stop 110, target 57, time_stop 36

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0986] | 68 | 43% | 18% | 40% |
| (0.0986, 0.163] | 67 | 60% | 30% | 10% |
| (0.163, 0.395] | 68 | 60% | 37% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
