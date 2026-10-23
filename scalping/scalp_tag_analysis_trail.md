# Scalp signal analysis (trail exits)

_157 tagged trades, 17 trading days (2026-10-01 to 2026-10-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 157 | 34% (27-42) | -0.98 | -3.06 | -481 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 23 | +10 | +0.43 | 134 | -491 | -3.66 | -10 |
| skip first 30 min | 1 | -6 | -6.31 | 156 | -474 | -3.04 | +6 |
| skip when SPY is down on the day | 62 | -254 | -4.09 | 95 | -227 | -2.39 | +254 |
| skip when SPY is below its VWAP | 64 | -272 | -4.26 | 93 | -208 | -2.24 | +272 |
| skip when SPY fell over the last 15 min | 61 | -178 | -2.92 | 96 | -303 | -3.15 | +178 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 39 | -186 | -4.78 | 118 | -294 | -2.50 | +186 |
| skip stock not beating SPY over 15 min | 25 | -59 | -2.37 | 132 | -421 | -3.19 | +59 |
| skip afternoon entries (2:00-3:45 PM) | 34 | -193 | -5.68 | 123 | -288 | -2.34 | +193 |
| skip volume spikes above 5x average | 28 | -143 | -5.10 | 129 | -338 | -2.62 | +143 |
| skip when the stop is inside normal noise (range > stop) | 6 | -9 | -1.42 | 151 | -472 | -3.13 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 10 | -31 | -3.11 | 147 | -450 | -3.06 | +31 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -368 | -4.00 | 65 | -113 | -1.73 | +368 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 22 | 55% (35-73) | +0.18 | -2.22 | -49 | ▲ |
| 60-240 | 67 | 28% (19-40) | -1.59 | -3.27 | -219 |  |
| 240-375 | 45 | 31% (20-46) | -2.51 | -4.94 | -222 |  |
| 375-390 | 23 | 39% (22-59) | +2.72 | +0.43 | +10 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 38 | 32% (19-47) | -2.18 | -4.78 | -182 |  |
| 0 to 0.2 | 44 | 32% (20-47) | -1.30 | -2.92 | -129 |  |
| > 0.2 | 51 | 39% (27-53) | +0.34 | -1.93 | -98 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 64 | 27% (17-38) | -1.86 | -4.26 | -272 |  |
| above VWAP | 93 | 40% (30-50) | -0.37 | -2.24 | -208 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 53 | 32% (21-45) | +0.00 | -1.60 | -85 |  |
| (0.122, 0.368] | 52 | 44% (32-58) | -1.09 | -3.06 | -159 |  |
| (0.368, 1.555] | 52 | 27% (17-40) | -1.86 | -4.56 | -237 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.145] | 52 | 35% (23-48) | -0.08 | -1.86 | -96 |  |
| (0.145, 0.404] | 52 | 37% (25-50) | -0.90 | -3.12 | -162 |  |
| (0.404, 1.281] | 52 | 33% (22-46) | -1.86 | -4.14 | -215 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.25] | 53 | 32% (21-45) | -1.44 | -3.86 | -205 |  |
| (-0.25, 0.394] | 52 | 48% (35-61) | +0.90 | -0.46 | -24 | ▲ |
| (0.394, 2.726] | 52 | 23% (14-36) | -2.38 | -4.85 | -252 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 53 | 36% (24-49) | -1.49 | -3.26 | -173 |  |
| (0.0521, 0.122] | 52 | 37% (25-50) | +0.31 | -1.55 | -81 |  |
| (0.122, 0.678] | 52 | 31% (20-44) | -1.74 | -4.37 | -227 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.197] | 53 | 45% (33-59) | +0.33 | -0.96 | -51 |  |
| (0.197, 0.301] | 52 | 31% (20-44) | -1.53 | -3.82 | -199 |  |
| (0.301, 0.875] | 52 | 27% (17-40) | -1.76 | -4.45 | -231 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 53 | 36% (24-49) | -0.87 | -2.81 | -149 |  |
| (2.39, 3.502] | 52 | 42% (30-56) | +0.77 | -1.35 | -70 |  |
| (3.502, 18.76] | 52 | 25% (15-38) | -2.83 | -5.02 | -261 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0963] | 53 | 42% (29-55) | +0.18 | -0.60 | -32 |  |
| (0.0963, 0.147] | 52 | 35% (23-48) | -1.57 | -2.96 | -154 |  |
| (0.147, 0.392] | 52 | 27% (17-40) | -1.57 | -5.67 | -295 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -1.439] | 11 | 36% (15-65) | -2.61 | -3.64 | -40 |  |
| (-1.439, 0.0115] | 10 | 30% (11-60) | -2.42 | -2.92 | -29 |  |
| (0.0115, 5.305] | 10 | 60% (31-83) | -0.12 | -0.60 | -6 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.477] | 13 | 23% (8-50) | -2.69 | -3.42 | -44 |  |
| (0.477, 0.691] | 12 | 42% (19-68) | -2.29 | -2.97 | -36 |  |
| (0.691, 1.74] | 13 | 62% (36-82) | -0.86 | -1.67 | -22 | ▲ |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.763] | 13 | 38% (18-64) | -1.97 | -2.41 | -31 |  |
| (0.763, 1.164] | 12 | 50% (25-75) | -1.06 | -1.91 | -23 |  |
| (1.164, 3.566] | 13 | 38% (18-64) | -2.72 | -3.65 | -47 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.313] | 13 | 15% (4-42) | -3.38 | -4.03 | -52 |  |
| (0.313, 0.495] | 12 | 58% (32-81) | -0.74 | -1.29 | -15 |  |
| (0.495, 1.14] | 13 | 54% (29-77) | -1.61 | -2.61 | -34 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.17%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 74, trail_stop 59, time_stop 23, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0963] | 53 | 36% | 28% | 34% |
| (0.0963, 0.147] | 52 | 54% | 40% | 6% |
| (0.147, 0.392] | 52 | 52% | 44% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
