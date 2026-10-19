# Scalp signal analysis (fixed exits)

_193 tagged trades, 13 trading days (2026-10-01 to 2026-10-19). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 193 | 37% (31-44) | -0.07 | -1.88 | -362 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 76 | -91 | -1.20 | 117 | -271 | -2.32 | +91 |
| skip first 30 min | 56 | -68 | -1.21 | 137 | -295 | -2.15 | +68 |
| skip when SPY is down on the day | 70 | -112 | -1.60 | 123 | -250 | -2.03 | +112 |
| skip when SPY is below its VWAP | 64 | -128 | -2.01 | 129 | -234 | -1.81 | +128 |
| skip when SPY fell over the last 15 min | 55 | -134 | -2.44 | 138 | -228 | -1.65 | +134 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 34 | -137 | -4.04 | 159 | -225 | -1.42 | +137 |
| skip stock not beating SPY over 15 min | 16 | -35 | -2.18 | 177 | -328 | -1.85 | +35 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 95 | -240 | -2.52 | 98 | -123 | -1.25 | +240 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 55 | 35% (23-48) | -0.01 | -1.11 | -61 |  |
| 15-60 | 20 | 60% (39-78) | +2.90 | +0.34 | +7 | ▲ |
| 60-240 | 57 | 37% (26-50) | -0.22 | -1.82 | -104 |  |
| 240-375 | 40 | 28% (16-43) | -2.00 | -4.35 | -174 |  |
| 375-390 | 21 | 43% (24-63) | +1.01 | -1.43 | -30 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 41% (23-61) | +0.35 | -1.45 | -32 |  |
| -0.2 to 0 | 48 | 42% (29-56) | +0.54 | -1.67 | -80 |  |
| 0 to 0.2 | 80 | 31% (22-42) | -0.53 | -1.89 | -152 |  |
| > 0.2 | 43 | 42% (28-57) | -0.12 | -2.30 | -99 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 64 | 41% (29-53) | +0.17 | -2.01 | -128 |  |
| above VWAP | 129 | 36% (28-44) | -0.19 | -1.81 | -234 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.142] | 46 | 37% (25-51) | -0.47 | -2.28 | -105 |  |
| (0.142, 0.374] | 47 | 45% (31-59) | +0.28 | -1.68 | -79 |  |
| (0.374, 1.555] | 45 | 33% (21-48) | -0.11 | -2.61 | -118 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.165] | 46 | 48% (34-62) | +0.80 | -0.81 | -37 |  |
| (0.165, 0.41] | 45 | 36% (23-50) | +0.03 | -2.34 | -105 |  |
| (0.41, 1.192] | 46 | 33% (21-47) | -0.99 | -3.31 | -152 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.108] | 65 | 42% (30-54) | +0.44 | -1.71 | -111 |  |
| (-0.108, 0.364] | 64 | 39% (28-51) | +0.33 | -1.01 | -64 |  |
| (0.364, 2.726] | 64 | 31% (21-43) | -0.99 | -2.92 | -187 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0604] | 65 | 38% (28-51) | -0.27 | -1.86 | -121 |  |
| (0.0604, 0.137] | 64 | 42% (31-54) | +0.41 | -1.26 | -80 |  |
| (0.137, 0.786] | 64 | 31% (21-43) | -0.35 | -2.52 | -161 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.231] | 65 | 42% (30-54) | -0.03 | -1.12 | -73 |  |
| (0.231, 0.439] | 64 | 36% (25-48) | -0.08 | -2.95 | -189 |  |
| (0.439, 4.92] | 64 | 34% (24-47) | -0.11 | -1.58 | -101 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.626] | 65 | 43% (32-55) | +0.75 | -1.06 | -69 |  |
| (2.626, 5.086] | 64 | 42% (31-54) | +0.35 | -1.90 | -121 |  |
| (5.086, 18.76] | 64 | 27% (17-38) | -1.33 | -2.69 | -172 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 65 | 42% (30-54) | -0.17 | -0.85 | -55 |  |
| (0.0985, 0.162] | 64 | 33% (23-45) | -0.35 | -1.62 | -104 |  |
| (0.162, 0.395] | 64 | 38% (27-50) | +0.30 | -3.17 | -203 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 28% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 55%
- Exit mix: stop 103, target 55, time_stop 35

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 65 | 42% | 18% | 40% |
| (0.0985, 0.162] | 64 | 59% | 30% | 11% |
| (0.162, 0.395] | 64 | 59% | 38% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
