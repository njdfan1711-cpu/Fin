# Scalp signal analysis (fixed exits)

_194 tagged trades, 13 trading days (2026-10-01 to 2026-10-19). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 194 | 37% (31-44) | -0.10 | -1.91 | -371 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 76 | -91 | -1.20 | 118 | -280 | -2.37 | +91 |
| skip first 30 min | 56 | -68 | -1.21 | 138 | -304 | -2.20 | +68 |
| skip when SPY is down on the day | 70 | -112 | -1.60 | 124 | -259 | -2.09 | +112 |
| skip when SPY is below its VWAP | 64 | -128 | -2.01 | 130 | -243 | -1.87 | +128 |
| skip when SPY fell over the last 15 min | 55 | -134 | -2.44 | 139 | -237 | -1.70 | +134 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 35 | -146 | -4.17 | 159 | -225 | -1.42 | +146 |
| skip stock not beating SPY over 15 min | 16 | -35 | -2.18 | 178 | -336 | -1.89 | +35 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 96 | -248 | -2.59 | 98 | -123 | -1.25 | +248 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 55 | 35% (23-48) | -0.01 | -1.11 | -61 |  |
| 15-60 | 20 | 60% (39-78) | +2.90 | +0.34 | +7 | ▲ |
| 60-240 | 58 | 36% (25-49) | -0.31 | -1.94 | -113 |  |
| 240-375 | 40 | 28% (16-43) | -2.00 | -4.35 | -174 |  |
| 375-390 | 21 | 43% (24-63) | +1.01 | -1.43 | -30 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 41% (23-61) | +0.35 | -1.45 | -32 |  |
| -0.2 to 0 | 48 | 42% (29-56) | +0.54 | -1.67 | -80 |  |
| 0 to 0.2 | 80 | 31% (22-42) | -0.53 | -1.89 | -152 |  |
| > 0.2 | 44 | 41% (28-56) | -0.25 | -2.44 | -107 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 64 | 41% (29-53) | +0.17 | -2.01 | -128 |  |
| above VWAP | 130 | 35% (28-44) | -0.23 | -1.87 | -243 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.145] | 47 | 38% (26-53) | -0.41 | -2.19 | -103 |  |
| (0.145, 0.374] | 47 | 43% (30-57) | +0.10 | -1.90 | -89 |  |
| (0.374, 1.555] | 45 | 33% (21-48) | -0.11 | -2.61 | -118 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.166] | 46 | 48% (34-62) | +0.80 | -0.81 | -37 |  |
| (0.166, 0.415] | 46 | 35% (23-49) | -0.10 | -2.54 | -117 |  |
| (0.415, 1.192] | 46 | 33% (21-47) | -0.99 | -3.25 | -149 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.113] | 65 | 42% (30-54) | +0.44 | -1.74 | -113 |  |
| (-0.113, 0.364] | 64 | 38% (27-50) | +0.16 | -1.18 | -76 |  |
| (0.364, 2.726] | 65 | 32% (22-44) | -0.90 | -2.81 | -182 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0583] | 65 | 37% (26-49) | -0.50 | -2.11 | -137 |  |
| (0.0583, 0.136] | 64 | 44% (32-56) | +0.64 | -1.03 | -66 |  |
| (0.136, 0.786] | 65 | 31% (21-43) | -0.43 | -2.58 | -168 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.232] | 65 | 42% (30-54) | -0.03 | -1.12 | -73 |  |
| (0.232, 0.438] | 64 | 36% (25-48) | -0.08 | -2.85 | -183 |  |
| (0.438, 4.92] | 65 | 34% (24-46) | -0.20 | -1.78 | -116 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.625] | 65 | 42% (30-54) | +0.50 | -1.33 | -87 |  |
| (2.625, 5.046] | 64 | 44% (32-56) | +0.60 | -1.66 | -106 |  |
| (5.046, 18.76] | 65 | 26% (17-38) | -1.39 | -2.74 | -178 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0986] | 65 | 42% (30-54) | -0.17 | -0.85 | -55 |  |
| (0.0986, 0.161] | 64 | 33% (23-45) | -0.35 | -1.63 | -104 |  |
| (0.161, 0.395] | 65 | 37% (26-49) | +0.21 | -3.25 | -211 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 28% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 55%
- Exit mix: stop 104, target 55, time_stop 35

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0986] | 65 | 42% | 18% | 40% |
| (0.0986, 0.161] | 64 | 59% | 30% | 11% |
| (0.161, 0.395] | 65 | 60% | 37% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
