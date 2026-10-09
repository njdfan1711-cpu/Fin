# Scalp signal analysis (fixed exits)

_110 tagged trades, 7 trading days (2026-10-01 to 2026-10-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 110 | 40% (31-49) | +0.40 | -1.50 | -165 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 37 | -8 | -0.22 | 73 | -157 | -2.15 | +8 |
| skip first 30 min | 27 | -4 | -0.16 | 83 | -160 | -1.93 | +4 |
| skip when SPY is down on the day | 33 | -25 | -0.76 | 77 | -140 | -1.82 | +25 |
| skip when SPY is below its VWAP | 34 | -75 | -2.22 | 76 | -90 | -1.18 | +75 |
| skip when SPY fell over the last 15 min | 32 | -32 | -0.99 | 78 | -133 | -1.71 | +32 |
| skip over-extended (30-min run in top quarter, > 0.45%) | 21 | -47 | -2.22 | 89 | -118 | -1.33 | +47 |
| skip stock not beating SPY over 15 min | 10 | -35 | -3.52 | 100 | -130 | -1.30 | +35 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 58 | -169 | -2.92 | 52 | +5 | +0.09 | +169 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 27 | 41% (25-59) | +0.91 | -0.16 | -4 |  |
| 15-60 | 11 | 64% (35-85) | +3.20 | +0.25 | +3 |  |
| 60-240 | 39 | 36% (23-52) | -0.04 | -1.65 | -64 |  |
| 240-375 | 23 | 30% (16-51) | -1.51 | -4.13 | -95 |  |
| 375-390 | 10 | 50% (24-76) | +2.11 | -0.38 | -4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 9 | 33% (12-65) | +0.01 | -2.10 | -19 | few trades |
| -0.2 to 0 | 24 | 50% (31-69) | +2.12 | -0.25 | -6 |  |
| 0 to 0.2 | 43 | 33% (20-47) | -0.48 | -1.88 | -81 |  |
| > 0.2 | 34 | 44% (29-61) | +0.41 | -1.74 | -59 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 34 | 38% (24-55) | +0.08 | -2.22 | -75 |  |
| above VWAP | 76 | 41% (30-52) | +0.55 | -1.18 | -90 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 28 | 36% (21-54) | -0.77 | -2.40 | -67 |  |
| (0.136, 0.372] | 27 | 41% (25-59) | -0.21 | -2.53 | -68 |  |
| (0.372, 1.123] | 28 | 43% (27-61) | +1.68 | -0.89 | -25 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.719, 0.189] | 28 | 50% (33-67) | +1.11 | -0.49 | -14 |  |
| (0.189, 0.406] | 27 | 30% (16-48) | -0.56 | -3.13 | -85 |  |
| (0.406, 1.022] | 28 | 39% (24-58) | +0.14 | -2.21 | -62 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0763] | 37 | 41% (26-57) | +0.77 | -1.85 | -68 |  |
| (-0.0763, 0.335] | 36 | 36% (22-52) | -0.06 | -1.41 | -51 |  |
| (0.335, 2.633] | 37 | 43% (29-59) | +0.48 | -1.24 | -46 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.0029, 0.0583] | 37 | 49% (33-64) | +1.25 | -0.42 | -16 |  |
| (0.0583, 0.142] | 36 | 39% (25-55) | -0.09 | -1.78 | -64 |  |
| (0.142, 0.786] | 37 | 32% (20-49) | +0.04 | -2.30 | -85 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.153, 0.218] | 37 | 49% (33-64) | +1.17 | -0.04 | -2 |  |
| (0.218, 0.422] | 36 | 36% (22-52) | +0.08 | -2.72 | -98 |  |
| (0.422, 3.871] | 37 | 35% (22-51) | -0.05 | -1.76 | -65 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0060000000000002, 2.562] | 37 | 49% (33-64) | +1.64 | -0.54 | -20 |  |
| (2.562, 5.075] | 36 | 42% (27-58) | +0.36 | -1.60 | -58 |  |
| (5.075, 18.76] | 37 | 30% (17-46) | -0.79 | -2.36 | -87 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0956] | 37 | 51% (36-67) | +1.31 | +0.60 | +22 |  |
| (0.0956, 0.145] | 37 | 38% (24-54) | +0.44 | -0.89 | -33 |  |
| (0.145, 0.392] | 36 | 31% (18-47) | -0.57 | -4.29 | -154 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.20%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 30% of trades
- Reached +0.5% at some point: 10% of trades
- Reached +0.75% at some point: 5% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 53, target 33, time_stop 24

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0956] | 37 | 30% | 24% | 46% |
| (0.0956, 0.145] | 37 | 54% | 35% | 11% |
| (0.145, 0.392] | 36 | 61% | 31% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
