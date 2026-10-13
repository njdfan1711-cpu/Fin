# Scalp signal analysis (fixed exits)

_147 tagged trades, 9 trading days (2026-10-01 to 2026-10-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 147 | 38% (31-46) | -0.01 | -1.90 | -280 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 52 | -53 | -1.01 | 95 | -227 | -2.39 | +53 |
| skip first 30 min | 38 | -45 | -1.17 | 109 | -235 | -2.16 | +45 |
| skip when SPY is down on the day | 53 | -76 | -1.43 | 94 | -204 | -2.17 | +76 |
| skip when SPY is below its VWAP | 51 | -106 | -2.08 | 96 | -174 | -1.81 | +106 |
| skip when SPY fell over the last 15 min | 45 | -85 | -1.90 | 102 | -194 | -1.91 | +85 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 27 | -105 | -3.88 | 120 | -175 | -1.46 | +105 |
| skip stock not beating SPY over 15 min | 13 | -32 | -2.43 | 134 | -248 | -1.85 | +32 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 74 | -207 | -2.79 | 73 | -73 | -1.00 | +207 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 38 | 34% (21-50) | -0.15 | -1.17 | -45 |  |
| 15-60 | 15 | 60% (36-80) | +2.60 | +0.13 | +2 |  |
| 60-240 | 47 | 36% (24-50) | -0.27 | -1.91 | -90 |  |
| 240-375 | 33 | 30% (17-47) | -1.60 | -4.22 | -139 |  |
| 375-390 | 14 | 50% (27-73) | +2.16 | -0.58 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 42% (19-68) | +0.89 | -0.88 | -11 |  |
| -0.2 to 0 | 41 | 44% (30-59) | +0.85 | -1.59 | -65 |  |
| 0 to 0.2 | 56 | 30% (20-43) | -0.83 | -2.13 | -119 |  |
| > 0.2 | 38 | 42% (28-58) | -0.02 | -2.23 | -85 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 51 | 41% (29-55) | +0.29 | -2.08 | -106 |  |
| above VWAP | 96 | 36% (28-46) | -0.17 | -1.81 | -174 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 37 | 41% (26-57) | -0.05 | -1.83 | -68 |  |
| (0.136, 0.374] | 36 | 44% (30-60) | -0.04 | -2.23 | -80 |  |
| (0.374, 1.555] | 36 | 33% (20-50) | +0.20 | -2.42 | -87 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.166] | 37 | 51% (36-67) | +1.16 | -0.44 | -16 |  |
| (0.166, 0.406] | 36 | 33% (20-50) | -0.36 | -2.91 | -105 |  |
| (0.406, 1.192] | 36 | 33% (20-50) | -0.73 | -3.17 | -114 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.104] | 49 | 39% (26-53) | +0.18 | -2.36 | -116 |  |
| (-0.104, 0.367] | 49 | 39% (26-53) | +0.05 | -1.11 | -55 |  |
| (0.367, 2.726] | 49 | 37% (25-51) | -0.28 | -2.23 | -110 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0567] | 49 | 45% (32-59) | +0.43 | -0.98 | -48 |  |
| (0.0567, 0.137] | 49 | 43% (30-57) | +0.60 | -1.34 | -66 |  |
| (0.137, 0.786] | 49 | 27% (16-40) | -1.07 | -3.39 | -166 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.23] | 49 | 47% (34-61) | +0.72 | -0.43 | -21 |  |
| (0.23, 0.422] | 49 | 33% (21-47) | -0.60 | -3.36 | -165 |  |
| (0.422, 3.871] | 49 | 35% (23-49) | -0.16 | -1.92 | -94 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.577] | 49 | 43% (30-57) | +0.60 | -1.43 | -70 |  |
| (2.577, 5.1] | 49 | 45% (32-59) | +0.69 | -1.35 | -66 |  |
| (5.1, 18.76] | 49 | 27% (16-40) | -1.33 | -2.93 | -144 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0952] | 49 | 47% (34-61) | +0.51 | -0.20 | -10 |  |
| (0.0952, 0.146] | 49 | 37% (25-51) | +0.21 | -1.03 | -50 |  |
| (0.146, 0.392] | 49 | 31% (20-45) | -0.76 | -4.48 | -220 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 28% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 53%
- Exit mix: stop 77, target 41, time_stop 29

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0952] | 49 | 37% | 20% | 43% |
| (0.0952, 0.146] | 49 | 57% | 35% | 8% |
| (0.146, 0.392] | 49 | 63% | 29% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
