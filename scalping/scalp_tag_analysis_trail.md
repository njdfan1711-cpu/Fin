# Scalp signal analysis (trail exits)

_153 tagged trades, 9 trading days (2026-10-01 to 2026-10-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 153 | 35% (28-42) | -0.48 | -2.31 | -353 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 53 | +15 | +0.28 | 100 | -368 | -3.68 | -15 |
| skip first 30 min | 38 | -21 | -0.55 | 115 | -332 | -2.89 | +21 |
| skip when SPY is down on the day | 54 | -135 | -2.51 | 99 | -218 | -2.20 | +135 |
| skip when SPY is below its VWAP | 51 | -141 | -2.76 | 102 | -212 | -2.08 | +141 |
| skip when SPY fell over the last 15 min | 48 | -122 | -2.53 | 105 | -231 | -2.20 | +122 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 29 | -143 | -4.94 | 124 | -210 | -1.69 | +143 |
| skip stock not beating SPY over 15 min | 13 | -43 | -3.28 | 140 | -310 | -2.22 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 78 | -238 | -3.05 | 75 | -115 | -1.54 | +238 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 38 | 37% (23-53) | +0.43 | -0.55 | -21 |  |
| 15-60 | 15 | 47% (25-70) | +0.34 | -2.12 | -32 |  |
| 60-240 | 48 | 25% (15-39) | -1.53 | -3.10 | -149 |  |
| 240-375 | 37 | 32% (20-49) | -2.62 | -5.06 | -187 |  |
| 375-390 | 15 | 53% (30-75) | +5.07 | +2.38 | +36 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 33% (14-61) | -0.61 | -2.37 | -28 |  |
| -0.2 to 0 | 42 | 36% (23-51) | -0.18 | -2.55 | -107 |  |
| 0 to 0.2 | 61 | 28% (18-40) | -1.78 | -3.05 | -186 |  |
| > 0.2 | 38 | 45% (30-60) | +1.33 | -0.83 | -32 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 51 | 29% (19-43) | -0.46 | -2.76 | -141 |  |
| above VWAP | 102 | 37% (28-47) | -0.49 | -2.08 | -212 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.17] | 39 | 31% (19-46) | +0.43 | -1.26 | -49 |  |
| (0.17, 0.374] | 38 | 45% (30-60) | -1.15 | -3.29 | -125 |  |
| (0.374, 1.555] | 38 | 26% (15-42) | -1.64 | -4.15 | -158 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.181] | 39 | 41% (27-57) | +0.87 | -0.70 | -27 |  |
| (0.181, 0.421] | 38 | 34% (21-50) | -0.86 | -3.41 | -130 |  |
| (0.421, 1.192] | 38 | 26% (15-42) | -2.37 | -4.60 | -175 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0885] | 51 | 33% (22-47) | -1.00 | -3.43 | -175 |  |
| (-0.0885, 0.374] | 51 | 45% (32-59) | +1.08 | -0.06 | -3 |  |
| (0.374, 2.726] | 51 | 25% (16-39) | -1.51 | -3.43 | -175 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0567] | 51 | 41% (29-55) | -1.33 | -2.70 | -138 |  |
| (0.0567, 0.137] | 51 | 37% (25-51) | +0.45 | -1.38 | -70 |  |
| (0.137, 0.786] | 51 | 25% (16-39) | -0.55 | -2.84 | -145 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.23] | 51 | 45% (32-59) | +0.62 | -0.50 | -26 |  |
| (0.23, 0.422] | 51 | 27% (17-41) | -1.84 | -4.50 | -229 |  |
| (0.422, 3.871] | 51 | 31% (20-45) | -0.20 | -1.92 | -98 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.613] | 51 | 39% (27-53) | -0.79 | -2.79 | -142 |  |
| (2.613, 5.006] | 51 | 37% (25-51) | +0.27 | -1.69 | -86 |  |
| (5.006, 18.76] | 51 | 27% (17-41) | -0.90 | -2.45 | -125 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0945] | 51 | 43% (31-57) | +0.36 | -0.32 | -16 |  |
| (0.0945, 0.145] | 52 | 38% (26-52) | -1.14 | -2.41 | -125 |  |
| (0.145, 0.392] | 50 | 22% (13-35) | -0.63 | -4.23 | -212 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 13% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 76, trail_stop 56, time_stop 21

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0945] | 51 | 35% | 33% | 31% |
| (0.0945, 0.145] | 52 | 54% | 40% | 6% |
| (0.145, 0.392] | 50 | 60% | 36% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
