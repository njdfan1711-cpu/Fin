# Scalp signal analysis (trail exits)

_160 tagged trades, 10 trading days (2026-10-01 to 2026-10-14). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 160 | 34% (27-41) | -0.57 | -2.37 | -380 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 58 | -13 | -0.22 | 102 | -367 | -3.59 | +13 |
| skip first 30 min | 40 | -33 | -0.83 | 120 | -346 | -2.89 | +33 |
| skip when SPY is down on the day | 57 | -146 | -2.56 | 103 | -234 | -2.27 | +146 |
| skip when SPY is below its VWAP | 54 | -151 | -2.80 | 106 | -228 | -2.15 | +151 |
| skip when SPY fell over the last 15 min | 51 | -129 | -2.52 | 109 | -251 | -2.30 | +129 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 30 | -141 | -4.71 | 130 | -238 | -1.83 | +141 |
| skip stock not beating SPY over 15 min | 13 | -43 | -3.28 | 147 | -337 | -2.29 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 81 | -248 | -3.06 | 79 | -132 | -1.67 | +248 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 40 | 35% (22-50) | +0.12 | -0.83 | -33 |  |
| 15-60 | 15 | 47% (25-70) | +0.34 | -2.12 | -32 |  |
| 60-240 | 48 | 25% (15-39) | -1.53 | -3.10 | -149 |  |
| 240-375 | 39 | 33% (21-49) | -2.38 | -4.77 | -186 |  |
| 375-390 | 18 | 44% (25-66) | +3.65 | +1.12 | +20 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 14 | 36% (16-61) | -0.78 | -2.35 | -33 |  |
| -0.2 to 0 | 43 | 35% (22-50) | -0.30 | -2.62 | -113 |  |
| 0 to 0.2 | 65 | 26% (17-38) | -1.80 | -3.11 | -202 |  |
| > 0.2 | 38 | 45% (30-60) | +1.33 | -0.83 | -32 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 54 | 30% (19-43) | -0.60 | -2.80 | -151 |  |
| above VWAP | 106 | 36% (27-45) | -0.55 | -2.15 | -228 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.158] | 40 | 30% (18-45) | +0.36 | -1.34 | -54 |  |
| (0.158, 0.374] | 40 | 42% (29-58) | -1.10 | -3.22 | -129 |  |
| (0.374, 1.555] | 40 | 28% (16-43) | -1.65 | -4.10 | -164 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.166] | 40 | 38% (24-53) | +0.73 | -0.93 | -37 |  |
| (0.166, 0.422] | 40 | 35% (22-50) | -0.78 | -3.24 | -130 |  |
| (0.422, 1.192] | 40 | 28% (16-43) | -2.34 | -4.49 | -179 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0828] | 54 | 33% (22-47) | -1.11 | -3.43 | -185 |  |
| (-0.0828, 0.383] | 53 | 45% (33-59) | +0.97 | -0.18 | -9 |  |
| (0.383, 2.726] | 53 | 23% (13-36) | -1.55 | -3.49 | -185 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0604] | 54 | 41% (29-54) | -0.22 | -1.60 | -86 |  |
| (0.0604, 0.137] | 53 | 36% (24-49) | -0.88 | -2.66 | -141 |  |
| (0.137, 0.786] | 53 | 25% (15-38) | -0.61 | -2.87 | -152 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.228] | 54 | 43% (30-56) | +0.42 | -0.70 | -38 |  |
| (0.228, 0.421] | 53 | 28% (18-42) | -1.73 | -4.37 | -232 |  |
| (0.421, 3.871] | 53 | 30% (20-44) | -0.41 | -2.08 | -110 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.593] | 54 | 39% (27-52) | -0.65 | -2.62 | -142 |  |
| (2.593, 5.086] | 53 | 36% (24-49) | +0.04 | -1.89 | -100 |  |
| (5.086, 18.76] | 53 | 26% (16-40) | -1.09 | -2.59 | -138 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0955] | 54 | 44% (32-58) | +0.46 | -0.21 | -11 |  |
| (0.0955, 0.145] | 53 | 36% (24-49) | -1.25 | -2.53 | -134 |  |
| (0.145, 0.392] | 53 | 21% (12-33) | -0.93 | -4.42 | -234 | ▼ |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 12% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 2% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 80, trail_stop 58, time_stop 22

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0955] | 54 | 35% | 33% | 31% |
| (0.0955, 0.145] | 53 | 53% | 42% | 6% |
| (0.145, 0.392] | 53 | 62% | 34% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
