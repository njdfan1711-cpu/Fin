# Scalp signal analysis (fixed exits)

_163 tagged trades, 11 trading days (2026-10-01 to 2026-10-15). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 163 | 37% (30-44) | -0.19 | -1.99 | -325 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | -76 | -1.27 | 103 | -249 | -2.41 | +76 |
| skip first 30 min | 41 | -47 | -1.15 | 122 | -278 | -2.28 | +47 |
| skip when SPY is down on the day | 59 | -90 | -1.52 | 104 | -235 | -2.26 | +90 |
| skip when SPY is below its VWAP | 56 | -112 | -1.99 | 107 | -213 | -1.99 | +112 |
| skip when SPY fell over the last 15 min | 51 | -101 | -1.99 | 112 | -224 | -2.00 | +101 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 31 | -122 | -3.94 | 132 | -203 | -1.54 | +122 |
| skip stock not beating SPY over 15 min | 13 | -31 | -2.37 | 150 | -294 | -1.96 | +31 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 83 | -221 | -2.67 | 80 | -104 | -1.29 | +221 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 41 | 34% (22-49) | -0.16 | -1.15 | -47 |  |
| 15-60 | 16 | 62% (39-82) | +3.09 | +0.62 | +10 | ▲ |
| 60-240 | 48 | 35% (23-50) | -0.32 | -1.89 | -91 |  |
| 240-375 | 39 | 28% (17-44) | -1.91 | -4.30 | -168 |  |
| 375-390 | 19 | 42% (23-64) | +0.87 | -1.54 | -29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 15 | 40% (20-64) | +0.07 | -1.43 | -21 |  |
| -0.2 to 0 | 44 | 43% (30-58) | +0.77 | -1.55 | -68 |  |
| 0 to 0.2 | 66 | 29% (19-41) | -0.98 | -2.31 | -152 |  |
| > 0.2 | 38 | 42% (28-58) | -0.02 | -2.18 | -83 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 56 | 41% (29-54) | +0.18 | -1.99 | -112 |  |
| above VWAP | 107 | 35% (26-44) | -0.38 | -1.99 | -213 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.147] | 41 | 39% (26-54) | -0.22 | -1.94 | -80 |  |
| (0.147, 0.374] | 41 | 41% (28-57) | -0.17 | -2.25 | -92 |  |
| (0.374, 1.555] | 40 | 32% (20-48) | -0.20 | -2.65 | -106 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.165] | 41 | 49% (34-64) | +0.99 | -0.70 | -29 |  |
| (0.165, 0.418] | 40 | 32% (20-48) | -0.43 | -2.88 | -115 |  |
| (0.418, 1.192] | 41 | 32% (20-47) | -1.16 | -3.27 | -134 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.1] | 55 | 40% (28-53) | +0.31 | -2.01 | -111 |  |
| (-0.1, 0.374] | 54 | 39% (27-52) | +0.11 | -1.06 | -57 |  |
| (0.374, 2.726] | 54 | 31% (21-45) | -1.00 | -2.91 | -157 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0606] | 55 | 42% (30-55) | +0.01 | -1.38 | -76 |  |
| (0.0606, 0.137] | 54 | 41% (29-54) | +0.24 | -1.53 | -83 |  |
| (0.137, 0.786] | 54 | 28% (18-41) | -0.82 | -3.08 | -166 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.221] | 55 | 44% (31-57) | +0.23 | -0.91 | -50 |  |
| (0.221, 0.421] | 54 | 33% (22-47) | -0.44 | -3.04 | -164 |  |
| (0.421, 3.871] | 54 | 33% (22-47) | -0.37 | -2.06 | -111 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.593] | 55 | 44% (31-57) | +0.79 | -1.20 | -66 |  |
| (2.593, 4.966] | 54 | 43% (30-56) | +0.37 | -1.57 | -85 |  |
| (4.966, 18.76] | 54 | 24% (15-37) | -1.74 | -3.22 | -174 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0955] | 55 | 45% (33-58) | +0.30 | -0.36 | -20 |  |
| (0.0955, 0.145] | 55 | 33% (22-46) | -0.35 | -1.67 | -92 |  |
| (0.145, 0.392] | 53 | 32% (21-45) | -0.53 | -4.02 | -213 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 27% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 54%
- Exit mix: stop 87, target 44, time_stop 32

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0955] | 55 | 38% | 20% | 42% |
| (0.0955, 0.145] | 55 | 60% | 31% | 9% |
| (0.145, 0.392] | 53 | 62% | 30% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
