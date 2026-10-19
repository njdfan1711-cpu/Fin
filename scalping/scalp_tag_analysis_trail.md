# Scalp signal analysis (trail exits)

_194 tagged trades, 13 trading days (2026-10-01 to 2026-10-19). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 194 | 34% (28-41) | -0.59 | -2.40 | -465 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 76 | -49 | -0.64 | 118 | -416 | -3.53 | +49 |
| skip first 30 min | 56 | -61 | -1.08 | 138 | -405 | -2.93 | +61 |
| skip when SPY is down on the day | 70 | -179 | -2.55 | 124 | -287 | -2.31 | +179 |
| skip when SPY is below its VWAP | 64 | -181 | -2.83 | 130 | -285 | -2.19 | +181 |
| skip when SPY fell over the last 15 min | 55 | -162 | -2.94 | 139 | -304 | -2.19 | +162 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 35 | -171 | -4.90 | 159 | -294 | -1.85 | +171 |
| skip stock not beating SPY over 15 min | 16 | -53 | -3.32 | 178 | -412 | -2.32 | +53 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 96 | -273 | -2.84 | 98 | -193 | -1.97 | +273 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 55 | 33% (22-46) | +0.11 | -0.99 | -54 |  |
| 15-60 | 20 | 50% (30-70) | +0.07 | -2.49 | -50 |  |
| 60-240 | 58 | 29% (19-42) | -1.38 | -3.01 | -174 |  |
| 240-375 | 40 | 32% (20-48) | -2.46 | -4.81 | -192 |  |
| 375-390 | 21 | 38% (21-59) | +2.69 | +0.26 | +5 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 32% (16-53) | -1.38 | -3.18 | -70 |  |
| -0.2 to 0 | 48 | 35% (23-50) | -0.06 | -2.27 | -109 |  |
| 0 to 0.2 | 80 | 28% (19-38) | -1.62 | -2.99 | -239 |  |
| > 0.2 | 44 | 45% (32-60) | +1.11 | -1.08 | -48 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 64 | 30% (20-42) | -0.65 | -2.83 | -181 |  |
| above VWAP | 130 | 36% (28-45) | -0.56 | -2.19 | -285 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.145] | 47 | 32% (20-46) | +0.03 | -1.75 | -82 |  |
| (0.145, 0.374] | 47 | 45% (31-59) | -0.89 | -2.90 | -136 |  |
| (0.374, 1.555] | 45 | 27% (16-41) | -1.77 | -4.27 | -192 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.166] | 46 | 41% (28-56) | +0.65 | -0.97 | -44 |  |
| (0.166, 0.415] | 46 | 35% (23-49) | -1.06 | -3.50 | -161 |  |
| (0.415, 1.192] | 46 | 28% (17-43) | -2.07 | -4.33 | -199 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.113] | 65 | 37% (26-49) | -0.89 | -3.07 | -199 |  |
| (-0.113, 0.364] | 64 | 41% (29-53) | +0.90 | -0.45 | -29 |  |
| (0.364, 2.726] | 65 | 25% (16-36) | -1.75 | -3.65 | -237 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0583] | 65 | 34% (24-46) | -1.82 | -3.43 | -223 |  |
| (0.0583, 0.136] | 64 | 41% (29-53) | +0.73 | -0.94 | -60 |  |
| (0.136, 0.786] | 65 | 28% (18-40) | -0.65 | -2.80 | -182 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.232] | 65 | 42% (30-54) | +0.02 | -1.07 | -69 |  |
| (0.232, 0.438] | 64 | 31% (21-43) | -1.33 | -4.10 | -263 |  |
| (0.438, 4.92] | 65 | 29% (20-41) | -0.47 | -2.05 | -133 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.625] | 65 | 38% (28-51) | -0.76 | -2.59 | -169 |  |
| (2.625, 5.046] | 64 | 36% (25-48) | +0.05 | -2.21 | -142 |  |
| (5.046, 18.76] | 65 | 28% (18-40) | -1.04 | -2.39 | -155 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0986] | 65 | 38% (28-51) | -0.17 | -0.86 | -56 |  |
| (0.0986, 0.161] | 64 | 36% (25-48) | -1.33 | -2.61 | -167 |  |
| (0.161, 0.395] | 65 | 28% (18-40) | -0.27 | -3.73 | -243 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 13% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 97, trail_stop 72, time_stop 25

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0986] | 65 | 38% | 31% | 31% |
| (0.0986, 0.161] | 64 | 53% | 42% | 5% |
| (0.161, 0.395] | 65 | 58% | 38% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
