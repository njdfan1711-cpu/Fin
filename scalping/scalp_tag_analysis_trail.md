# Scalp signal analysis (trail exits)

_166 tagged trades, 18 trading days (2026-10-01 to 2026-10-26). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 166 | 36% (29-43) | -0.91 | -2.91 | -482 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | +12 | +0.47 | 141 | -494 | -3.50 | -12 |
| skip first 30 min | 1 | -6 | -6.31 | 165 | -476 | -2.89 | +6 |
| skip when SPY is down on the day | 62 | -254 | -4.09 | 104 | -228 | -2.20 | +254 |
| skip when SPY is below its VWAP | 70 | -287 | -4.10 | 96 | -196 | -2.04 | +287 |
| skip when SPY fell over the last 15 min | 65 | -176 | -2.71 | 101 | -306 | -3.03 | +176 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 41 | -194 | -4.72 | 125 | -289 | -2.31 | +194 |
| skip stock not beating SPY over 15 min | 27 | -48 | -1.79 | 139 | -434 | -3.12 | +48 |
| skip afternoon entries (2:00-3:45 PM) | 37 | -202 | -5.45 | 129 | -281 | -2.18 | +202 |
| skip volume spikes above 5x average | 30 | -146 | -4.87 | 136 | -336 | -2.47 | +146 |
| skip when the stop is inside normal noise (range > stop) | 6 | -9 | -1.42 | 160 | -474 | -2.96 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 12 | -44 | -3.67 | 154 | -438 | -2.85 | +44 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 93 | -364 | -3.91 | 73 | -119 | -1.62 | +364 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 23 | 57% (37-74) | +0.47 | -1.83 | -42 | ▲ |
| 60-240 | 69 | 30% (21-42) | -1.47 | -3.11 | -214 |  |
| 240-375 | 49 | 31% (20-45) | -2.56 | -4.85 | -237 |  |
| 375-390 | 25 | 40% (23-59) | +2.61 | +0.47 | +12 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 38 | 32% (19-47) | -2.18 | -4.78 | -182 |  |
| 0 to 0.2 | 46 | 33% (21-47) | -1.30 | -2.88 | -132 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 70 | 27% (18-39) | -1.87 | -4.10 | -287 |  |
| above VWAP | 96 | 42% (32-52) | -0.21 | -2.04 | -196 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 56 | 36% (24-49) | +0.28 | -1.26 | -71 |  |
| (0.122, 0.37] | 55 | 44% (31-57) | -1.20 | -3.18 | -175 |  |
| (0.37, 1.555] | 55 | 27% (17-40) | -1.82 | -4.30 | -237 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.145] | 55 | 38% (27-51) | +0.21 | -1.50 | -82 |  |
| (0.145, 0.404] | 55 | 38% (27-51) | -0.86 | -2.99 | -164 |  |
| (0.404, 1.281] | 55 | 31% (20-44) | -1.98 | -4.17 | -229 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.25] | 56 | 32% (21-45) | -1.38 | -3.71 | -208 |  |
| (-0.25, 0.401] | 55 | 49% (36-62) | +0.89 | -0.42 | -23 | ▲ |
| (0.401, 2.726] | 55 | 25% (16-38) | -2.22 | -4.57 | -251 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 56 | 36% (24-49) | -1.43 | -3.14 | -176 |  |
| (0.0521, 0.121] | 55 | 40% (28-53) | +0.51 | -1.25 | -69 |  |
| (0.121, 0.678] | 55 | 31% (20-44) | -1.80 | -4.32 | -237 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 56 | 45% (32-58) | +0.29 | -1.01 | -56 |  |
| (0.198, 0.301] | 55 | 36% (25-50) | -1.13 | -3.27 | -180 |  |
| (0.301, 0.875] | 55 | 25% (16-38) | -1.91 | -4.47 | -246 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.367] | 56 | 36% (24-49) | -0.89 | -2.76 | -155 |  |
| (2.367, 3.421] | 55 | 44% (31-57) | -0.34 | -2.35 | -129 |  |
| (3.421, 18.762] | 55 | 27% (17-40) | -1.49 | -3.60 | -198 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0966] | 56 | 45% (32-58) | +0.37 | -0.40 | -23 |  |
| (0.0966, 0.145] | 55 | 36% (25-50) | -1.31 | -2.64 | -145 |  |
| (0.145, 0.392] | 55 | 25% (16-38) | -1.81 | -5.72 | -314 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.913] | 14 | 36% (16-61) | -2.09 | -3.05 | -43 |  |
| (-0.913, 0.134] | 13 | 23% (8-50) | -3.24 | -3.72 | -48 |  |
| (0.134, 5.305] | 13 | 77% (50-92) | +1.51 | +1.09 | +14 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.484] | 16 | 38% (18-61) | -1.52 | -2.20 | -35 |  |
| (0.484, 0.597] | 15 | 40% (20-64) | -1.72 | -2.30 | -34 |  |
| (0.597, 1.74] | 16 | 56% (33-77) | -1.33 | -2.11 | -34 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.763] | 16 | 50% (28-72) | -0.85 | -1.23 | -20 |  |
| (0.763, 1.164] | 15 | 40% (20-64) | -2.04 | -2.82 | -42 |  |
| (1.164, 3.566] | 16 | 44% (23-67) | -1.70 | -2.59 | -41 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 17 | 29% (13-53) | -2.33 | -2.96 | -50 |  |
| (0.315, 0.495] | 14 | 57% (33-79) | -0.14 | -0.65 | -9 |  |
| (0.495, 1.14] | 16 | 50% (28-72) | -1.86 | -2.76 | -44 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.17%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 47%
- Exit mix: stop 77, trail_stop 62, time_stop 25, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0966] | 56 | 34% | 29% | 36% |
| (0.0966, 0.145] | 55 | 51% | 42% | 5% |
| (0.145, 0.392] | 55 | 55% | 42% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
