# Scalp signal analysis (fixed exits)

_197 tagged trades, 13 trading days (2026-10-01 to 2026-10-19). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 197 | 37% (31-44) | -0.11 | -1.95 | -384 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 76 | -91 | -1.20 | 121 | -293 | -2.42 | +91 |
| skip first 30 min | 56 | -68 | -1.21 | 141 | -317 | -2.25 | +68 |
| skip when SPY is down on the day | 70 | -112 | -1.60 | 127 | -272 | -2.14 | +112 |
| skip when SPY is below its VWAP | 66 | -131 | -1.98 | 131 | -253 | -1.93 | +131 |
| skip when SPY fell over the last 15 min | 57 | -137 | -2.40 | 140 | -248 | -1.77 | +137 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 35 | -146 | -4.17 | 162 | -238 | -1.47 | +146 |
| skip stock not beating SPY over 15 min | 18 | -37 | -2.07 | 179 | -347 | -1.94 | +37 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 99 | -262 | -2.64 | 98 | -123 | -1.25 | +262 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 55 | 35% (23-48) | -0.01 | -1.11 | -61 |  |
| 15-60 | 20 | 60% (39-78) | +2.90 | +0.34 | +7 | ▲ |
| 60-240 | 61 | 36% (25-49) | -0.32 | -2.06 | -126 |  |
| 240-375 | 40 | 28% (16-43) | -2.00 | -4.35 | -174 |  |
| 375-390 | 21 | 43% (24-63) | +1.01 | -1.43 | -30 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 41% (23-61) | +0.35 | -1.45 | -32 |  |
| -0.2 to 0 | 48 | 42% (29-56) | +0.54 | -1.67 | -80 |  |
| 0 to 0.2 | 82 | 32% (23-42) | -0.46 | -1.88 | -154 |  |
| > 0.2 | 45 | 40% (27-55) | -0.38 | -2.63 | -118 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 66 | 41% (30-53) | +0.23 | -1.98 | -131 |  |
| above VWAP | 131 | 35% (27-44) | -0.28 | -1.93 | -253 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 48 | 38% (25-52) | -0.36 | -2.23 | -107 |  |
| (0.136, 0.374] | 48 | 44% (31-58) | +0.16 | -1.82 | -87 |  |
| (0.374, 1.555] | 46 | 33% (21-47) | -0.24 | -2.79 | -129 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.153] | 47 | 45% (31-59) | +0.32 | -1.45 | -68 |  |
| (0.153, 0.408] | 47 | 38% (26-53) | +0.46 | -1.87 | -88 |  |
| (0.408, 1.192] | 47 | 32% (20-46) | -1.09 | -3.42 | -161 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.113] | 66 | 41% (30-53) | +0.34 | -1.83 | -121 |  |
| (-0.113, 0.371] | 65 | 38% (28-51) | +0.23 | -1.10 | -71 |  |
| (0.371, 2.726] | 66 | 32% (22-44) | -0.89 | -2.91 | -192 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0583] | 66 | 38% (27-50) | -0.33 | -1.99 | -131 |  |
| (0.0583, 0.135] | 65 | 42% (30-54) | +0.28 | -1.44 | -93 |  |
| (0.135, 0.786] | 66 | 32% (22-44) | -0.27 | -2.42 | -160 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.23] | 66 | 41% (30-53) | -0.11 | -1.35 | -89 |  |
| (0.23, 0.436] | 65 | 35% (25-48) | -0.17 | -2.79 | -181 |  |
| (0.436, 4.92] | 66 | 35% (24-47) | -0.04 | -1.73 | -114 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.623] | 66 | 42% (31-54) | +0.65 | -1.22 | -81 |  |
| (2.623, 4.926] | 65 | 43% (32-55) | +0.50 | -1.76 | -114 |  |
| (4.926, 18.76] | 66 | 26% (17-37) | -1.46 | -2.87 | -189 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0986] | 66 | 41% (30-53) | -0.26 | -0.96 | -64 |  |
| (0.0986, 0.161] | 65 | 34% (24-46) | -0.18 | -1.52 | -99 |  |
| (0.161, 0.395] | 66 | 36% (26-48) | +0.11 | -3.37 | -222 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 28% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 55%
- Exit mix: stop 106, target 56, time_stop 35

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0986] | 66 | 42% | 18% | 39% |
| (0.0986, 0.161] | 65 | 58% | 31% | 11% |
| (0.161, 0.395] | 66 | 61% | 36% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
