# Scalp signal analysis (trail exits)

_163 tagged trades, 11 trading days (2026-10-01 to 2026-10-15). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 163 | 34% (28-42) | -0.48 | -2.28 | -372 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | -6 | -0.09 | 103 | -366 | -3.55 | +6 |
| skip first 30 min | 41 | -19 | -0.47 | 122 | -352 | -2.89 | +19 |
| skip when SPY is down on the day | 59 | -138 | -2.35 | 104 | -233 | -2.24 | +138 |
| skip when SPY is below its VWAP | 56 | -144 | -2.57 | 107 | -228 | -2.13 | +144 |
| skip when SPY fell over the last 15 min | 51 | -129 | -2.52 | 112 | -243 | -2.17 | +129 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 31 | -148 | -4.78 | 132 | -224 | -1.69 | +148 |
| skip stock not beating SPY over 15 min | 13 | -43 | -3.28 | 150 | -329 | -2.19 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 83 | -233 | -2.81 | 80 | -138 | -1.73 | +233 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 41 | 37% (24-52) | +0.51 | -0.47 | -19 |  |
| 15-60 | 16 | 50% (28-72) | +0.52 | -1.95 | -31 |  |
| 60-240 | 48 | 25% (15-39) | -1.53 | -3.10 | -149 |  |
| 240-375 | 39 | 33% (21-49) | -2.38 | -4.77 | -186 |  |
| 375-390 | 19 | 42% (23-64) | +3.14 | +0.73 | +14 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 15 | 33% (15-58) | -1.12 | -2.62 | -39 |  |
| -0.2 to 0 | 44 | 36% (24-51) | +0.07 | -2.25 | -99 |  |
| 0 to 0.2 | 66 | 27% (18-39) | -1.73 | -3.05 | -201 |  |
| > 0.2 | 38 | 45% (30-60) | +1.33 | -0.83 | -32 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 56 | 30% (20-43) | -0.40 | -2.57 | -144 |  |
| above VWAP | 107 | 36% (28-46) | -0.52 | -2.13 | -228 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.147] | 41 | 32% (20-47) | +0.43 | -1.29 | -53 |  |
| (0.147, 0.374] | 41 | 41% (28-57) | -1.22 | -3.30 | -135 |  |
| (0.374, 1.555] | 40 | 28% (16-43) | -1.65 | -4.10 | -164 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.165] | 41 | 39% (26-54) | +0.79 | -0.89 | -37 |  |
| (0.165, 0.418] | 40 | 32% (20-48) | -0.96 | -3.41 | -136 |  |
| (0.418, 1.192] | 41 | 29% (18-44) | -2.25 | -4.37 | -179 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.1] | 55 | 35% (23-48) | -0.81 | -3.13 | -172 |  |
| (-0.1, 0.374] | 54 | 44% (32-58) | +0.87 | -0.31 | -16 |  |
| (0.374, 2.726] | 54 | 24% (15-37) | -1.48 | -3.39 | -183 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0606] | 55 | 40% (28-53) | -0.19 | -1.58 | -87 |  |
| (0.0606, 0.137] | 54 | 37% (25-50) | -0.94 | -2.71 | -146 |  |
| (0.137, 0.786] | 54 | 26% (16-39) | -0.30 | -2.56 | -138 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.221] | 55 | 44% (31-57) | +0.41 | -0.73 | -40 |  |
| (0.221, 0.421] | 54 | 28% (18-41) | -1.75 | -4.35 | -235 |  |
| (0.421, 3.871] | 54 | 31% (21-45) | -0.11 | -1.79 | -97 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.593] | 55 | 40% (28-53) | -0.58 | -2.57 | -141 |  |
| (2.593, 4.966] | 54 | 37% (25-50) | +0.33 | -1.61 | -87 |  |
| (4.966, 18.76] | 54 | 26% (16-39) | -1.17 | -2.66 | -143 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0955] | 55 | 44% (31-57) | +0.34 | -0.32 | -18 |  |
| (0.0955, 0.145] | 55 | 35% (23-48) | -1.42 | -2.73 | -150 |  |
| (0.145, 0.392] | 53 | 25% (15-38) | -0.35 | -3.84 | -204 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 13% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 2% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 81, trail_stop 60, time_stop 22

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0955] | 55 | 36% | 33% | 31% |
| (0.0955, 0.145] | 55 | 55% | 40% | 5% |
| (0.145, 0.392] | 53 | 58% | 38% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
