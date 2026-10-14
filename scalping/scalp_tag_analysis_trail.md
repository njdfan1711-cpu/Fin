# Scalp signal analysis (trail exits)

_159 tagged trades, 10 trading days (2026-10-01 to 2026-10-14). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 159 | 34% (27-42) | -0.53 | -2.35 | -373 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 57 | -7 | -0.12 | 102 | -367 | -3.59 | +7 |
| skip first 30 min | 40 | -33 | -0.83 | 119 | -340 | -2.86 | +33 |
| skip when SPY is down on the day | 56 | -139 | -2.49 | 103 | -234 | -2.27 | +139 |
| skip when SPY is below its VWAP | 53 | -145 | -2.73 | 106 | -228 | -2.15 | +145 |
| skip when SPY fell over the last 15 min | 51 | -129 | -2.52 | 108 | -244 | -2.26 | +129 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 30 | -141 | -4.71 | 129 | -232 | -1.80 | +141 |
| skip stock not beating SPY over 15 min | 13 | -43 | -3.28 | 146 | -330 | -2.26 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 81 | -248 | -3.06 | 78 | -126 | -1.61 | +248 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 40 | 35% (22-50) | +0.12 | -0.83 | -33 |  |
| 15-60 | 15 | 47% (25-70) | +0.34 | -2.12 | -32 |  |
| 60-240 | 48 | 25% (15-39) | -1.53 | -3.10 | -149 |  |
| 240-375 | 39 | 33% (21-49) | -2.38 | -4.77 | -186 |  |
| 375-390 | 17 | 47% (26-69) | +4.21 | +1.57 | +27 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 13 | 38% (18-64) | -0.38 | -2.04 | -27 |  |
| -0.2 to 0 | 43 | 35% (22-50) | -0.30 | -2.62 | -113 |  |
| 0 to 0.2 | 65 | 26% (17-38) | -1.80 | -3.11 | -202 |  |
| > 0.2 | 38 | 45% (30-60) | +1.33 | -0.83 | -32 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 53 | 30% (20-44) | -0.50 | -2.73 | -145 |  |
| above VWAP | 106 | 36% (27-45) | -0.55 | -2.15 | -228 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.147] | 40 | 30% (18-45) | +0.36 | -1.34 | -54 |  |
| (0.147, 0.374] | 39 | 44% (29-59) | -0.98 | -3.14 | -123 |  |
| (0.374, 1.555] | 40 | 28% (16-43) | -1.65 | -4.10 | -164 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.165] | 40 | 38% (24-53) | +0.73 | -0.93 | -37 |  |
| (0.165, 0.418] | 39 | 33% (21-49) | -0.83 | -3.33 | -130 |  |
| (0.418, 1.192] | 40 | 30% (18-45) | -2.16 | -4.32 | -173 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0699] | 53 | 34% (23-47) | -1.02 | -3.37 | -179 |  |
| (-0.0699, 0.384] | 53 | 45% (33-59) | +0.97 | -0.18 | -9 |  |
| (0.384, 2.726] | 53 | 23% (13-36) | -1.55 | -3.49 | -185 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0593] | 53 | 40% (28-53) | -1.50 | -2.89 | -153 |  |
| (0.0593, 0.137] | 53 | 38% (26-51) | +0.51 | -1.29 | -68 |  |
| (0.137, 0.786] | 53 | 25% (15-38) | -0.61 | -2.87 | -152 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.229] | 53 | 43% (31-57) | +0.54 | -0.59 | -31 |  |
| (0.229, 0.422] | 53 | 28% (18-42) | -1.73 | -4.37 | -232 |  |
| (0.422, 3.871] | 53 | 30% (20-44) | -0.41 | -2.08 | -110 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.577] | 53 | 40% (28-53) | -0.62 | -2.59 | -137 |  |
| (2.577, 5.006] | 53 | 36% (24-49) | +0.10 | -1.87 | -99 |  |
| (5.006, 18.76] | 53 | 26% (16-40) | -1.08 | -2.58 | -137 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0952] | 53 | 43% (31-57) | +0.28 | -0.40 | -21 |  |
| (0.0952, 0.145] | 53 | 38% (26-51) | -0.94 | -2.23 | -118 |  |
| (0.145, 0.392] | 53 | 21% (12-33) | -0.93 | -4.42 | -234 | ▼ |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 13% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 79, trail_stop 58, time_stop 22

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0952] | 53 | 36% | 32% | 32% |
| (0.0952, 0.145] | 53 | 51% | 43% | 6% |
| (0.145, 0.392] | 53 | 62% | 34% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
