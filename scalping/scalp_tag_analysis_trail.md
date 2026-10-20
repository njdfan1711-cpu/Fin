# Scalp signal analysis (trail exits)

_197 tagged trades, 13 trading days (2026-10-01 to 2026-10-19). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 197 | 34% (28-41) | -0.59 | -2.48 | -488 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 76 | -51 | -0.68 | 121 | -436 | -3.61 | +51 |
| skip first 30 min | 56 | -63 | -1.12 | 141 | -425 | -3.01 | +63 |
| skip when SPY is down on the day | 70 | -182 | -2.60 | 127 | -306 | -2.41 | +182 |
| skip when SPY is below its VWAP | 66 | -187 | -2.83 | 131 | -301 | -2.30 | +187 |
| skip when SPY fell over the last 15 min | 57 | -167 | -2.92 | 140 | -321 | -2.29 | +167 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 35 | -174 | -4.98 | 162 | -313 | -1.93 | +174 |
| skip stock not beating SPY over 15 min | 18 | -56 | -3.12 | 179 | -432 | -2.41 | +56 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 108 | -339 | -3.14 | 89 | -148 | -1.67 | +339 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 55 | 33% (22-46) | +0.11 | -1.02 | -56 |  |
| 15-60 | 20 | 50% (30-70) | +0.07 | -2.52 | -50 |  |
| 60-240 | 61 | 30% (20-42) | -1.34 | -3.13 | -191 |  |
| 240-375 | 40 | 32% (20-48) | -2.46 | -4.87 | -195 |  |
| 375-390 | 21 | 38% (21-59) | +2.69 | +0.23 | +5 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 32% (16-53) | -1.38 | -3.24 | -71 |  |
| -0.2 to 0 | 48 | 35% (23-50) | -0.06 | -2.31 | -111 |  |
| 0 to 0.2 | 82 | 28% (19-39) | -1.53 | -2.99 | -245 |  |
| > 0.2 | 45 | 44% (31-59) | +0.95 | -1.35 | -61 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 66 | 30% (21-42) | -0.57 | -2.83 | -187 |  |
| above VWAP | 131 | 36% (28-44) | -0.60 | -2.30 | -301 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 48 | 31% (20-45) | +0.06 | -1.85 | -89 |  |
| (0.136, 0.374] | 48 | 46% (33-60) | -0.82 | -2.85 | -137 |  |
| (0.374, 1.555] | 46 | 26% (16-40) | -1.86 | -4.47 | -206 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.153] | 47 | 38% (26-53) | +0.48 | -1.33 | -63 |  |
| (0.153, 0.408] | 47 | 38% (26-53) | -0.80 | -3.16 | -149 |  |
| (0.408, 1.192] | 47 | 28% (17-42) | -2.15 | -4.55 | -214 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.113] | 66 | 36% (26-48) | -0.97 | -3.20 | -211 |  |
| (-0.113, 0.371] | 65 | 42% (30-54) | +0.96 | -0.40 | -26 |  |
| (0.371, 2.726] | 66 | 24% (16-36) | -1.73 | -3.80 | -251 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0583] | 66 | 35% (24-47) | -1.64 | -3.34 | -220 |  |
| (0.0583, 0.135] | 65 | 38% (28-51) | +0.45 | -1.32 | -86 |  |
| (0.135, 0.786] | 66 | 29% (19-41) | -0.56 | -2.75 | -182 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.23] | 66 | 41% (30-53) | -0.00 | -1.28 | -84 |  |
| (0.23, 0.436] | 65 | 32% (22-44) | -1.44 | -4.11 | -267 |  |
| (0.436, 4.92] | 66 | 29% (19-41) | -0.34 | -2.07 | -136 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.623] | 66 | 39% (29-51) | -0.60 | -2.52 | -166 |  |
| (2.623, 4.926] | 65 | 35% (25-48) | -0.04 | -2.34 | -152 |  |
| (4.926, 18.76] | 66 | 27% (18-39) | -1.12 | -2.56 | -169 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0986] | 66 | 38% (27-50) | -0.26 | -1.00 | -66 |  |
| (0.0986, 0.161] | 65 | 37% (26-49) | -1.15 | -2.53 | -164 |  |
| (0.161, 0.395] | 66 | 27% (18-39) | -0.36 | -3.89 | -257 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 13% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 99, trail_stop 73, time_stop 25

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0986] | 66 | 39% | 30% | 30% |
| (0.0986, 0.161] | 65 | 52% | 43% | 5% |
| (0.161, 0.395] | 66 | 59% | 38% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
