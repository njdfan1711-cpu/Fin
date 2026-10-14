# Scalp signal analysis (fixed exits)

_159 tagged trades, 10 trading days (2026-10-01 to 2026-10-14). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 159 | 36% (29-44) | -0.25 | -2.06 | -328 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 57 | -72 | -1.26 | 102 | -257 | -2.52 | +72 |
| skip first 30 min | 40 | -55 | -1.38 | 119 | -273 | -2.29 | +55 |
| skip when SPY is down on the day | 56 | -85 | -1.52 | 103 | -243 | -2.36 | +85 |
| skip when SPY is below its VWAP | 53 | -107 | -2.02 | 106 | -221 | -2.09 | +107 |
| skip when SPY fell over the last 15 min | 51 | -101 | -1.99 | 108 | -227 | -2.10 | +101 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 30 | -115 | -3.84 | 129 | -213 | -1.65 | +115 |
| skip stock not beating SPY over 15 min | 13 | -31 | -2.37 | 146 | -297 | -2.04 | +31 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 81 | -238 | -2.93 | 78 | -91 | -1.16 | +238 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 40 | 32% (20-48) | -0.43 | -1.38 | -55 |  |
| 15-60 | 15 | 60% (36-80) | +2.60 | +0.14 | +2 |  |
| 60-240 | 48 | 35% (23-50) | -0.32 | -1.89 | -91 |  |
| 240-375 | 39 | 28% (17-44) | -1.91 | -4.30 | -168 |  |
| 375-390 | 17 | 47% (26-69) | +1.67 | -0.97 | -16 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 13 | 46% (23-71) | +0.99 | -0.66 | -9 |  |
| -0.2 to 0 | 43 | 42% (28-57) | +0.54 | -1.78 | -77 |  |
| 0 to 0.2 | 65 | 28% (18-40) | -1.16 | -2.46 | -160 |  |
| > 0.2 | 38 | 42% (28-58) | -0.02 | -2.18 | -83 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 53 | 42% (29-55) | +0.21 | -2.02 | -107 |  |
| above VWAP | 106 | 34% (26-43) | -0.48 | -2.09 | -221 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.147] | 40 | 38% (24-53) | -0.49 | -2.19 | -88 |  |
| (0.147, 0.374] | 39 | 44% (29-59) | +0.12 | -2.04 | -80 |  |
| (0.374, 1.555] | 40 | 32% (20-48) | -0.20 | -2.65 | -106 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.165] | 40 | 48% (33-63) | +0.75 | -0.91 | -37 |  |
| (0.165, 0.418] | 39 | 33% (21-49) | -0.29 | -2.79 | -109 |  |
| (0.418, 1.192] | 40 | 32% (20-48) | -1.04 | -3.19 | -128 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0699] | 53 | 40% (28-53) | +0.24 | -2.11 | -112 |  |
| (-0.0699, 0.384] | 53 | 40% (28-53) | +0.07 | -1.09 | -58 |  |
| (0.384, 2.726] | 53 | 30% (20-44) | -1.06 | -3.00 | -159 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0593] | 53 | 42% (29-55) | -0.04 | -1.43 | -76 |  |
| (0.0593, 0.137] | 53 | 42% (29-55) | +0.32 | -1.47 | -78 |  |
| (0.137, 0.786] | 53 | 26% (16-40) | -1.03 | -3.29 | -175 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.229] | 53 | 43% (31-57) | +0.22 | -0.91 | -48 |  |
| (0.229, 0.422] | 53 | 34% (23-47) | -0.39 | -3.04 | -161 |  |
| (0.422, 3.871] | 53 | 32% (21-45) | -0.58 | -2.25 | -119 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.577] | 53 | 43% (31-57) | +0.66 | -1.31 | -69 |  |
| (2.577, 5.006] | 53 | 42% (29-55) | +0.25 | -1.72 | -91 |  |
| (5.006, 18.76] | 53 | 25% (15-38) | -1.66 | -3.16 | -168 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0952] | 53 | 45% (33-59) | +0.24 | -0.43 | -23 |  |
| (0.0952, 0.145] | 53 | 34% (23-47) | -0.16 | -1.44 | -76 |  |
| (0.145, 0.392] | 53 | 30% (20-44) | -0.84 | -4.32 | -229 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 54%
- Exit mix: stop 85, target 42, time_stop 32

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0952] | 53 | 38% | 19% | 43% |
| (0.0952, 0.145] | 53 | 58% | 32% | 9% |
| (0.145, 0.392] | 53 | 64% | 28% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
