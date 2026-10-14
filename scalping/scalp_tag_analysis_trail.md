# Scalp signal analysis (trail exits)

_158 tagged trades, 10 trading days (2026-10-01 to 2026-10-14). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 158 | 34% (27-41) | -0.55 | -2.37 | -375 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 57 | -7 | -0.12 | 101 | -368 | -3.65 | +7 |
| skip first 30 min | 40 | -33 | -0.83 | 118 | -342 | -2.90 | +33 |
| skip when SPY is down on the day | 55 | -141 | -2.57 | 103 | -234 | -2.27 | +141 |
| skip when SPY is below its VWAP | 52 | -147 | -2.82 | 106 | -228 | -2.15 | +147 |
| skip when SPY fell over the last 15 min | 50 | -131 | -2.61 | 108 | -244 | -2.26 | +131 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 30 | -150 | -5.00 | 128 | -225 | -1.76 | +150 |
| skip stock not beating SPY over 15 min | 13 | -43 | -3.28 | 145 | -332 | -2.29 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 81 | -248 | -3.06 | 77 | -127 | -1.66 | +248 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 40 | 35% (22-50) | +0.12 | -0.83 | -33 |  |
| 15-60 | 15 | 47% (25-70) | +0.34 | -2.12 | -32 |  |
| 60-240 | 48 | 25% (15-39) | -1.53 | -3.10 | -149 |  |
| 240-375 | 38 | 32% (19-47) | -2.50 | -4.95 | -188 |  |
| 375-390 | 17 | 47% (26-69) | +4.21 | +1.57 | +27 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 33% (14-61) | -0.61 | -2.37 | -28 |  |
| -0.2 to 0 | 43 | 35% (22-50) | -0.30 | -2.62 | -113 |  |
| 0 to 0.2 | 65 | 26% (17-38) | -1.80 | -3.11 | -202 |  |
| > 0.2 | 38 | 45% (30-60) | +1.33 | -0.83 | -32 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 52 | 29% (18-42) | -0.55 | -2.82 | -147 |  |
| above VWAP | 106 | 36% (27-45) | -0.55 | -2.15 | -228 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 40 | 30% (18-45) | +0.36 | -1.34 | -54 |  |
| (0.136, 0.374] | 39 | 44% (29-59) | -0.98 | -3.14 | -123 |  |
| (0.374, 1.555] | 39 | 26% (15-41) | -1.75 | -4.25 | -166 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.165] | 40 | 38% (24-53) | +0.73 | -0.93 | -37 |  |
| (0.165, 0.412] | 39 | 33% (21-49) | -0.83 | -3.33 | -130 |  |
| (0.412, 1.192] | 39 | 28% (17-44) | -2.28 | -4.48 | -175 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0575] | 53 | 34% (23-47) | -1.03 | -3.39 | -180 |  |
| (-0.0575, 0.386] | 52 | 44% (32-58) | +0.96 | -0.20 | -10 |  |
| (0.386, 2.726] | 53 | 23% (13-36) | -1.55 | -3.49 | -185 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0583] | 53 | 40% (28-53) | -1.50 | -2.89 | -153 |  |
| (0.0583, 0.139] | 52 | 37% (25-50) | +0.47 | -1.35 | -70 |  |
| (0.139, 0.786] | 53 | 25% (15-38) | -0.61 | -2.87 | -152 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.229] | 53 | 42% (29-55) | +0.38 | -0.78 | -41 |  |
| (0.229, 0.422] | 52 | 29% (18-42) | -1.65 | -4.30 | -223 |  |
| (0.422, 3.871] | 53 | 30% (20-44) | -0.41 | -2.08 | -110 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.603] | 53 | 38% (26-51) | -0.71 | -2.71 | -144 |  |
| (2.603, 5.046] | 52 | 37% (25-50) | +0.15 | -1.82 | -94 |  |
| (5.046, 18.76] | 53 | 26% (16-40) | -1.08 | -2.58 | -137 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0956] | 53 | 43% (31-57) | +0.42 | -0.25 | -13 |  |
| (0.0956, 0.145] | 52 | 37% (25-50) | -1.16 | -2.46 | -128 |  |
| (0.145, 0.392] | 53 | 21% (12-33) | -0.93 | -4.42 | -234 | ▼ |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 13% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 79, trail_stop 58, time_stop 21

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0956] | 53 | 36% | 34% | 30% |
| (0.0956, 0.145] | 52 | 52% | 42% | 6% |
| (0.145, 0.392] | 53 | 62% | 34% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
