# Scalp signal analysis (fixed exits)

_158 tagged trades, 10 trading days (2026-10-01 to 2026-10-14). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 158 | 36% (29-44) | -0.27 | -2.09 | -330 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 57 | -72 | -1.26 | 101 | -258 | -2.56 | +72 |
| skip first 30 min | 40 | -55 | -1.38 | 118 | -275 | -2.33 | +55 |
| skip when SPY is down on the day | 55 | -87 | -1.58 | 103 | -243 | -2.36 | +87 |
| skip when SPY is below its VWAP | 52 | -109 | -2.10 | 106 | -221 | -2.09 | +109 |
| skip when SPY fell over the last 15 min | 50 | -103 | -2.06 | 108 | -227 | -2.10 | +103 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 30 | -124 | -4.13 | 128 | -206 | -1.61 | +124 |
| skip stock not beating SPY over 15 min | 13 | -31 | -2.37 | 145 | -299 | -2.06 | +31 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 81 | -238 | -2.93 | 77 | -93 | -1.20 | +238 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 40 | 32% (20-48) | -0.43 | -1.38 | -55 |  |
| 15-60 | 15 | 60% (36-80) | +2.60 | +0.14 | +2 |  |
| 60-240 | 48 | 35% (23-50) | -0.32 | -1.89 | -91 |  |
| 240-375 | 38 | 26% (15-42) | -2.02 | -4.47 | -170 |  |
| 375-390 | 17 | 47% (26-69) | +1.67 | -0.97 | -16 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 42% (19-68) | +0.89 | -0.88 | -11 |  |
| -0.2 to 0 | 43 | 42% (28-57) | +0.54 | -1.78 | -77 |  |
| 0 to 0.2 | 65 | 28% (18-40) | -1.16 | -2.46 | -160 |  |
| > 0.2 | 38 | 42% (28-58) | -0.02 | -2.18 | -83 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 52 | 40% (28-54) | +0.17 | -2.10 | -109 |  |
| above VWAP | 106 | 34% (26-43) | -0.48 | -2.09 | -221 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 40 | 38% (24-53) | -0.49 | -2.19 | -88 |  |
| (0.136, 0.374] | 39 | 44% (29-59) | +0.12 | -2.04 | -80 |  |
| (0.374, 1.555] | 39 | 31% (19-46) | -0.26 | -2.76 | -108 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.165] | 40 | 48% (33-63) | +0.75 | -0.91 | -37 |  |
| (0.165, 0.412] | 39 | 33% (21-49) | -0.29 | -2.79 | -109 |  |
| (0.412, 1.192] | 39 | 31% (19-46) | -1.12 | -3.32 | -130 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0575] | 53 | 40% (28-53) | +0.26 | -2.11 | -112 |  |
| (-0.0575, 0.386] | 52 | 38% (26-52) | +0.01 | -1.14 | -60 |  |
| (0.386, 2.726] | 53 | 30% (20-44) | -1.06 | -3.00 | -159 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0583] | 53 | 42% (29-55) | -0.04 | -1.43 | -76 |  |
| (0.0583, 0.139] | 52 | 40% (28-54) | +0.29 | -1.54 | -80 |  |
| (0.139, 0.786] | 53 | 26% (16-40) | -1.03 | -3.29 | -175 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.229] | 53 | 42% (29-55) | +0.06 | -1.10 | -58 |  |
| (0.229, 0.422] | 52 | 35% (23-48) | -0.29 | -2.93 | -153 |  |
| (0.422, 3.871] | 53 | 32% (21-45) | -0.58 | -2.25 | -119 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.603] | 53 | 42% (29-55) | +0.57 | -1.43 | -76 |  |
| (2.603, 5.046] | 52 | 42% (30-56) | +0.30 | -1.67 | -87 |  |
| (5.046, 18.76] | 53 | 25% (15-38) | -1.66 | -3.16 | -168 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0956] | 53 | 45% (33-59) | +0.38 | -0.29 | -16 |  |
| (0.0956, 0.145] | 52 | 33% (22-46) | -0.35 | -1.65 | -86 |  |
| (0.145, 0.392] | 53 | 30% (20-44) | -0.84 | -4.32 | -229 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.21%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 27% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 54%
- Exit mix: stop 85, target 42, time_stop 31

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0956] | 53 | 38% | 21% | 42% |
| (0.0956, 0.145] | 52 | 60% | 31% | 10% |
| (0.145, 0.392] | 53 | 64% | 28% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
