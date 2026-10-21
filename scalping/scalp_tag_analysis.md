# Scalp signal analysis (fixed exits)

_149 tagged trades, 15 trading days (2026-10-01 to 2026-10-21). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 149 | 37% (30-45) | -0.23 | -2.39 | -356 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 22 | -31 | -1.41 | 127 | -325 | -2.56 | +31 |
| skip first 30 min | 1 | -6 | -6.31 | 148 | -350 | -2.36 | +6 |
| skip when SPY is down on the day | 58 | -151 | -2.61 | 91 | -205 | -2.25 | +151 |
| skip when SPY is below its VWAP | 59 | -193 | -3.27 | 90 | -164 | -1.82 | +193 |
| skip when SPY fell over the last 15 min | 58 | -154 | -2.65 | 91 | -203 | -2.23 | +154 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 37 | -147 | -3.96 | 112 | -210 | -1.87 | +147 |
| skip stock not beating SPY over 15 min | 22 | -36 | -1.63 | 127 | -320 | -2.52 | +36 |
| skip afternoon entries (2:00-3:45 PM) | 32 | -180 | -5.62 | 117 | -176 | -1.51 | +180 |
| skip volume spikes above 5x average | 27 | -128 | -4.73 | 122 | -228 | -1.87 | +128 |
| skip when the stop is inside normal noise (range > stop) | 4 | +4 | +0.89 | 145 | -360 | -2.48 | -4 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 8 | -7 | -0.88 | 141 | -349 | -2.48 | +7 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 90 | -301 | -3.34 | 59 | -55 | -0.94 | +301 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 20 | 60% (39-78) | +2.90 | +0.31 | +6 | ▲ |
| 60-240 | 64 | 36% (25-48) | -0.34 | -2.06 | -132 |  |
| 240-375 | 43 | 26% (15-40) | -2.14 | -4.63 | -199 |  |
| 375-390 | 22 | 41% (23-61) | +0.97 | -1.41 | -31 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 41% (23-61) | +0.35 | -1.51 | -33 |  |
| -0.2 to 0 | 36 | 36% (22-52) | -0.57 | -3.28 | -118 |  |
| 0 to 0.2 | 42 | 36% (23-51) | +0.22 | -1.41 | -59 |  |
| > 0.2 | 49 | 37% (25-51) | -0.63 | -2.97 | -146 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 59 | 34% (23-47) | -0.73 | -3.27 | -193 |  |
| above VWAP | 90 | 39% (29-49) | +0.10 | -1.82 | -164 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 50 | 34% (22-48) | -0.54 | -2.22 | -111 |  |
| (0.126, 0.369] | 49 | 43% (30-57) | +0.04 | -2.01 | -98 |  |
| (0.369, 1.555] | 50 | 34% (22-48) | -0.19 | -2.93 | -147 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.146] | 50 | 36% (24-50) | -0.64 | -2.50 | -125 |  |
| (0.146, 0.403] | 49 | 45% (32-59) | +1.36 | -0.94 | -46 |  |
| (0.403, 1.192] | 49 | 31% (20-45) | -1.29 | -3.64 | -178 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.254] | 50 | 38% (26-52) | +0.01 | -2.52 | -126 |  |
| (-0.254, 0.364] | 49 | 43% (30-57) | +0.66 | -0.75 | -37 |  |
| (0.364, 2.726] | 50 | 30% (19-44) | -1.34 | -3.87 | -193 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0519] | 50 | 38% (26-52) | -0.60 | -2.44 | -122 |  |
| (0.0519, 0.122] | 49 | 43% (30-57) | +0.56 | -1.38 | -68 |  |
| (0.122, 0.678] | 50 | 30% (19-44) | -0.64 | -3.33 | -166 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.197] | 50 | 44% (31-58) | +0.03 | -1.30 | -65 |  |
| (0.197, 0.305] | 49 | 33% (21-47) | -0.31 | -2.71 | -133 |  |
| (0.305, 0.875] | 50 | 34% (22-48) | -0.42 | -3.17 | -159 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.405] | 50 | 36% (24-50) | +0.08 | -2.09 | -104 |  |
| (2.405, 3.475] | 49 | 47% (34-61) | +0.73 | -1.29 | -63 |  |
| (3.475, 18.76] | 50 | 28% (17-42) | -1.48 | -3.78 | -189 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.095] | 50 | 46% (33-60) | +0.31 | -0.45 | -23 |  |
| (0.095, 0.149] | 49 | 29% (18-42) | -1.05 | -2.53 | -124 |  |
| (0.149, 0.392] | 50 | 36% (24-50) | +0.03 | -4.19 | -210 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.612, -1.264] | 8 | 25% (7-59) | -1.83 | -2.82 | -23 | few trades |
| (-1.264, 0.429] | 7 | 0% (0-35) | -4.62 | -5.15 | -36 | few trades |
| (0.429, 5.305] | 8 | 75% (41-93) | +4.33 | +3.85 | +31 | few trades |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.465] | 10 | 30% (11-60) | -2.26 | -3.01 | -30 |  |
| (0.465, 0.74] | 10 | 10% (2-40) | -3.62 | -4.36 | -44 |  |
| (0.74, 1.74] | 10 | 60% (31-83) | +2.90 | +2.12 | +21 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.261, 0.75] | 10 | 40% (17-69) | +0.03 | -0.47 | -5 |  |
| (0.75, 1.15] | 10 | 40% (17-69) | +0.36 | -0.52 | -5 |  |
| (1.15, 3.566] | 10 | 20% (6-51) | -3.38 | -4.25 | -43 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.296] | 10 | 10% (2-40) | -3.31 | -3.91 | -39 |  |
| (0.296, 0.483] | 10 | 50% (24-76) | -0.18 | -0.81 | -8 |  |
| (0.483, 0.815] | 10 | 40% (17-69) | +0.50 | -0.53 | -5 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 42% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 77, target 37, time_stop 34, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.095] | 50 | 34% | 16% | 48% |
| (0.095, 0.149] | 49 | 63% | 27% | 10% |
| (0.149, 0.392] | 50 | 58% | 32% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
