# Scalp signal analysis (fixed exits)

_157 tagged trades, 17 trading days (2026-10-01 to 2026-10-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 157 | 37% (30-45) | -0.25 | -2.34 | -367 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 23 | -21 | -0.92 | 134 | -346 | -2.58 | +21 |
| skip first 30 min | 1 | -6 | -6.31 | 156 | -361 | -2.31 | +6 |
| skip when SPY is down on the day | 62 | -145 | -2.34 | 95 | -222 | -2.34 | +145 |
| skip when SPY is below its VWAP | 64 | -184 | -2.87 | 93 | -183 | -1.97 | +184 |
| skip when SPY fell over the last 15 min | 61 | -148 | -2.42 | 96 | -219 | -2.28 | +148 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 39 | -167 | -4.28 | 118 | -200 | -1.70 | +167 |
| skip stock not beating SPY over 15 min | 25 | -22 | -0.90 | 132 | -345 | -2.61 | +22 |
| skip afternoon entries (2:00-3:45 PM) | 34 | -184 | -5.41 | 123 | -183 | -1.49 | +184 |
| skip volume spikes above 5x average | 28 | -134 | -4.79 | 129 | -233 | -1.81 | +134 |
| skip when the stop is inside normal noise (range > stop) | 6 | -11 | -1.76 | 151 | -357 | -2.36 | +11 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 10 | -21 | -2.12 | 147 | -346 | -2.35 | +21 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -305 | -3.32 | 65 | -62 | -0.95 | +305 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 22 | 59% (39-77) | +2.81 | +0.42 | +9 | ▲ |
| 60-240 | 67 | 34% (24-46) | -0.59 | -2.27 | -152 |  |
| 240-375 | 45 | 27% (16-41) | -2.09 | -4.51 | -203 |  |
| 375-390 | 23 | 43% (26-63) | +1.37 | -0.92 | -21 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 38 | 37% (23-53) | -0.44 | -3.03 | -115 |  |
| 0 to 0.2 | 44 | 36% (24-51) | +0.17 | -1.45 | -64 |  |
| > 0.2 | 51 | 35% (24-49) | -0.84 | -3.10 | -158 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 64 | 36% (25-48) | -0.48 | -2.87 | -184 |  |
| above VWAP | 93 | 38% (28-48) | -0.10 | -1.97 | -183 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 53 | 36% (24-49) | -0.24 | -1.84 | -98 |  |
| (0.122, 0.368] | 52 | 40% (28-54) | -0.30 | -2.27 | -118 |  |
| (0.368, 1.555] | 52 | 35% (23-48) | -0.22 | -2.91 | -151 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.145] | 52 | 38% (26-52) | -0.24 | -2.02 | -105 |  |
| (0.145, 0.404] | 52 | 42% (30-56) | +0.95 | -1.27 | -66 |  |
| (0.404, 1.281] | 52 | 31% (20-44) | -1.37 | -3.65 | -190 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.25] | 53 | 38% (26-51) | -0.10 | -2.52 | -134 |  |
| (-0.25, 0.394] | 52 | 44% (32-58) | +0.72 | -0.64 | -33 |  |
| (0.394, 2.726] | 52 | 29% (18-42) | -1.39 | -3.85 | -200 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 53 | 38% (26-51) | -0.60 | -2.37 | -126 |  |
| (0.0521, 0.122] | 52 | 44% (32-58) | +0.69 | -1.17 | -61 |  |
| (0.122, 0.678] | 52 | 29% (18-42) | -0.84 | -3.47 | -181 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.197] | 53 | 45% (33-59) | +0.18 | -1.11 | -59 |  |
| (0.197, 0.301] | 52 | 33% (22-46) | -0.32 | -2.61 | -136 |  |
| (0.301, 0.875] | 52 | 33% (22-46) | -0.63 | -3.31 | -172 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 53 | 36% (24-49) | +0.05 | -1.89 | -100 |  |
| (2.39, 3.502] | 52 | 48% (35-61) | +0.82 | -1.30 | -68 |  |
| (3.502, 18.76] | 52 | 27% (17-40) | -1.64 | -3.83 | -199 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0963] | 53 | 43% (31-57) | -0.04 | -0.83 | -44 |  |
| (0.0963, 0.147] | 52 | 33% (22-46) | -0.52 | -1.92 | -100 |  |
| (0.147, 0.392] | 52 | 35% (23-48) | -0.20 | -4.30 | -224 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -1.439] | 11 | 27% (10-57) | -2.04 | -3.07 | -34 |  |
| (-1.439, 0.0115] | 10 | 20% (6-51) | -1.85 | -2.34 | -23 |  |
| (0.0115, 5.305] | 10 | 60% (31-83) | +2.32 | +1.84 | +18 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.477] | 13 | 23% (8-50) | -2.64 | -3.37 | -44 |  |
| (0.477, 0.691] | 12 | 33% (14-61) | -1.01 | -1.69 | -20 |  |
| (0.691, 1.74] | 13 | 46% (23-71) | +0.86 | +0.05 | +1 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.763] | 13 | 38% (18-64) | +0.11 | -0.34 | -4 |  |
| (0.763, 1.164] | 12 | 42% (19-68) | +0.41 | -0.44 | -5 |  |
| (1.164, 3.566] | 13 | 23% (8-50) | -3.20 | -4.13 | -54 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.313] | 13 | 15% (4-42) | -2.66 | -3.31 | -43 |  |
| (0.313, 0.495] | 12 | 58% (32-81) | +1.01 | +0.45 | +5 |  |
| (0.495, 1.14] | 13 | 31% (13-58) | -0.98 | -1.98 | -26 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 53%
- Exit mix: stop 82, target 39, time_stop 35, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0963] | 53 | 38% | 15% | 45% |
| (0.0963, 0.147] | 52 | 60% | 29% | 12% |
| (0.147, 0.392] | 52 | 60% | 31% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
