# Scalp signal analysis (fixed exits)

_109 tagged trades, 7 trading days (2026-10-01 to 2026-10-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 109 | 39% (31-49) | +0.31 | -1.60 | -175 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 37 | -8 | -0.22 | 72 | -166 | -2.31 | +8 |
| skip first 30 min | 27 | -4 | -0.16 | 82 | -170 | -2.08 | +4 |
| skip when SPY is down on the day | 33 | -25 | -0.76 | 76 | -150 | -1.97 | +25 |
| skip when SPY is below its VWAP | 34 | -75 | -2.22 | 75 | -99 | -1.32 | +75 |
| skip when SPY fell over the last 15 min | 32 | -32 | -0.99 | 77 | -143 | -1.86 | +32 |
| skip over-extended (30-min run in top quarter, > 0.44%) | 21 | -48 | -2.29 | 88 | -126 | -1.44 | +48 |
| skip stock not beating SPY over 15 min | 10 | -35 | -3.52 | 99 | -139 | -1.41 | +35 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 58 | -169 | -2.92 | 51 | -5 | -0.10 | +169 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 27 | 41% (25-59) | +0.91 | -0.16 | -4 |  |
| 15-60 | 11 | 64% (35-85) | +3.20 | +0.25 | +3 |  |
| 60-240 | 39 | 36% (23-52) | -0.04 | -1.65 | -64 |  |
| 240-375 | 22 | 27% (13-48) | -2.06 | -4.76 | -105 |  |
| 375-390 | 10 | 50% (24-76) | +2.11 | -0.38 | -4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 9 | 33% (12-65) | +0.01 | -2.10 | -19 | few trades |
| -0.2 to 0 | 24 | 50% (31-69) | +2.12 | -0.25 | -6 |  |
| 0 to 0.2 | 43 | 33% (20-47) | -0.48 | -1.88 | -81 |  |
| > 0.2 | 33 | 42% (27-59) | +0.11 | -2.09 | -69 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 34 | 38% (24-55) | +0.08 | -2.22 | -75 |  |
| above VWAP | 75 | 40% (30-51) | +0.41 | -1.32 | -99 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 28 | 36% (21-54) | -0.77 | -2.40 | -67 |  |
| (0.136, 0.37] | 27 | 41% (25-59) | -0.21 | -2.53 | -68 |  |
| (0.37, 1.123] | 27 | 41% (25-59) | +1.36 | -1.28 | -35 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.719, 0.185] | 28 | 50% (33-67) | +1.11 | -0.49 | -14 |  |
| (0.185, 0.405] | 27 | 30% (16-48) | -0.56 | -3.13 | -85 |  |
| (0.405, 1.022] | 27 | 37% (22-56) | -0.24 | -2.66 | -72 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-2.266, -0.0634] | 37 | 41% (26-57) | +0.57 | -2.07 | -76 |  |
| (-0.0634, 0.338] | 36 | 36% (22-52) | -0.10 | -1.43 | -52 |  |
| (0.338, 2.633] | 36 | 42% (27-58) | +0.46 | -1.30 | -47 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.0029, 0.0572] | 37 | 49% (33-64) | +1.25 | -0.42 | -16 |  |
| (0.0572, 0.142] | 37 | 35% (22-51) | -0.65 | -2.32 | -86 |  |
| (0.142, 0.786] | 35 | 34% (21-51) | +0.34 | -2.09 | -73 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.153, 0.221] | 37 | 46% (31-62) | +0.73 | -0.49 | -18 |  |
| (0.221, 0.423] | 36 | 36% (22-52) | +0.08 | -2.77 | -100 |  |
| (0.423, 3.871] | 36 | 36% (22-52) | +0.12 | -1.58 | -57 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0060000000000002, 2.546] | 37 | 49% (33-64) | +1.64 | -0.54 | -20 |  |
| (2.546, 5.129] | 36 | 39% (25-55) | -0.10 | -2.10 | -76 |  |
| (5.129, 18.76] | 36 | 31% (18-47) | -0.65 | -2.20 | -79 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0955] | 37 | 51% (36-67) | +1.31 | +0.60 | +22 |  |
| (0.0955, 0.145] | 36 | 36% (22-52) | +0.16 | -1.18 | -43 |  |
| (0.145, 0.392] | 36 | 31% (18-47) | -0.57 | -4.29 | -154 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.20%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 29% of trades
- Reached +0.5% at some point: 10% of trades
- Reached +0.75% at some point: 5% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 53, target 32, time_stop 24

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0955] | 37 | 30% | 24% | 46% |
| (0.0955, 0.145] | 36 | 56% | 33% | 11% |
| (0.145, 0.392] | 36 | 61% | 31% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
