# Scalp signal analysis (fixed exits)

_160 tagged trades, 10 trading days (2026-10-01 to 2026-10-14). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 160 | 36% (29-44) | -0.29 | -2.09 | -335 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 58 | -78 | -1.35 | 102 | -257 | -2.52 | +78 |
| skip first 30 min | 40 | -55 | -1.38 | 120 | -279 | -2.33 | +55 |
| skip when SPY is down on the day | 57 | -92 | -1.61 | 103 | -243 | -2.36 | +92 |
| skip when SPY is below its VWAP | 54 | -113 | -2.10 | 106 | -221 | -2.09 | +113 |
| skip when SPY fell over the last 15 min | 51 | -101 | -1.99 | 109 | -233 | -2.14 | +101 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 30 | -115 | -3.84 | 130 | -219 | -1.69 | +115 |
| skip stock not beating SPY over 15 min | 13 | -31 | -2.37 | 147 | -304 | -2.07 | +31 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 81 | -238 | -2.93 | 79 | -97 | -1.23 | +238 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 40 | 32% (20-48) | -0.43 | -1.38 | -55 |  |
| 15-60 | 15 | 60% (36-80) | +2.60 | +0.14 | +2 |  |
| 60-240 | 48 | 35% (23-50) | -0.32 | -1.89 | -91 |  |
| 240-375 | 39 | 28% (17-44) | -1.91 | -4.30 | -168 |  |
| 375-390 | 18 | 44% (25-66) | +1.25 | -1.27 | -23 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 14 | 43% (21-67) | +0.50 | -1.07 | -15 |  |
| -0.2 to 0 | 43 | 42% (28-57) | +0.54 | -1.78 | -77 |  |
| 0 to 0.2 | 65 | 28% (18-40) | -1.16 | -2.46 | -160 |  |
| > 0.2 | 38 | 42% (28-58) | -0.02 | -2.18 | -83 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 54 | 41% (29-54) | +0.10 | -2.10 | -113 |  |
| above VWAP | 106 | 34% (26-43) | -0.48 | -2.09 | -221 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.158] | 40 | 38% (24-53) | -0.49 | -2.19 | -88 |  |
| (0.158, 0.374] | 40 | 42% (29-58) | -0.03 | -2.15 | -86 |  |
| (0.374, 1.555] | 40 | 32% (20-48) | -0.20 | -2.65 | -106 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.166] | 40 | 48% (33-63) | +0.75 | -0.91 | -37 |  |
| (0.166, 0.422] | 40 | 35% (22-50) | -0.02 | -2.49 | -100 |  |
| (0.422, 1.192] | 40 | 30% (18-45) | -1.44 | -3.58 | -143 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0828] | 54 | 39% (27-52) | +0.13 | -2.19 | -118 |  |
| (-0.0828, 0.383] | 53 | 40% (28-53) | +0.07 | -1.09 | -58 |  |
| (0.383, 2.726] | 53 | 30% (20-44) | -1.06 | -3.00 | -159 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0604] | 54 | 43% (30-56) | +0.12 | -1.26 | -68 |  |
| (0.0604, 0.137] | 53 | 40% (28-53) | +0.05 | -1.74 | -92 |  |
| (0.137, 0.786] | 53 | 26% (16-40) | -1.03 | -3.29 | -175 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.228] | 54 | 43% (30-56) | +0.10 | -1.01 | -55 |  |
| (0.228, 0.421] | 53 | 34% (23-47) | -0.39 | -3.04 | -161 |  |
| (0.421, 3.871] | 53 | 32% (21-45) | -0.58 | -2.25 | -119 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.593] | 54 | 43% (30-56) | +0.61 | -1.37 | -74 |  |
| (2.593, 5.086] | 53 | 42% (29-55) | +0.19 | -1.75 | -93 |  |
| (5.086, 18.76] | 53 | 25% (15-38) | -1.67 | -3.17 | -168 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0955] | 54 | 46% (34-59) | +0.42 | -0.25 | -14 |  |
| (0.0955, 0.145] | 53 | 32% (21-45) | -0.45 | -1.74 | -92 |  |
| (0.145, 0.392] | 53 | 30% (20-44) | -0.84 | -4.32 | -229 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.21%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 54%
- Exit mix: stop 86, target 42, time_stop 32

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0955] | 54 | 37% | 20% | 43% |
| (0.0955, 0.145] | 53 | 60% | 30% | 9% |
| (0.145, 0.392] | 53 | 64% | 28% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
