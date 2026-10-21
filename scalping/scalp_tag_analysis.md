# Scalp signal analysis (fixed exits)

_148 tagged trades, 15 trading days (2026-10-01 to 2026-10-21). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 148 | 37% (30-45) | -0.19 | -2.36 | -350 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 22 | -31 | -1.41 | 126 | -319 | -2.53 | +31 |
| skip first 30 min | 1 | -6 | -6.31 | 147 | -344 | -2.34 | +6 |
| skip when SPY is down on the day | 58 | -151 | -2.61 | 90 | -198 | -2.20 | +151 |
| skip when SPY is below its VWAP | 59 | -193 | -3.27 | 89 | -157 | -1.77 | +193 |
| skip when SPY fell over the last 15 min | 58 | -154 | -2.65 | 90 | -196 | -2.18 | +154 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 37 | -147 | -3.96 | 111 | -203 | -1.83 | +147 |
| skip stock not beating SPY over 15 min | 22 | -36 | -1.63 | 126 | -314 | -2.49 | +36 |
| skip afternoon entries (2:00-3:45 PM) | 32 | -180 | -5.62 | 116 | -170 | -1.46 | +180 |
| skip volume spikes above 5x average | 27 | -128 | -4.73 | 121 | -222 | -1.84 | +128 |
| skip when the stop is inside normal noise (range > stop) | 4 | +4 | +0.89 | 144 | -353 | -2.45 | -4 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 7 | -16 | -2.30 | 141 | -334 | -2.37 | +16 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 90 | -301 | -3.34 | 58 | -49 | -0.85 | +301 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 20 | 60% (39-78) | +2.90 | +0.31 | +6 | ▲ |
| 60-240 | 63 | 37% (26-49) | -0.25 | -2.00 | -126 |  |
| 240-375 | 43 | 26% (15-40) | -2.14 | -4.63 | -199 |  |
| 375-390 | 22 | 41% (23-61) | +0.97 | -1.41 | -31 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 41% (23-61) | +0.35 | -1.51 | -33 |  |
| -0.2 to 0 | 36 | 36% (22-52) | -0.57 | -3.28 | -118 |  |
| 0 to 0.2 | 41 | 37% (24-52) | +0.37 | -1.29 | -53 |  |
| > 0.2 | 49 | 37% (25-51) | -0.63 | -2.97 | -146 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 59 | 34% (23-47) | -0.73 | -3.27 | -193 |  |
| above VWAP | 89 | 39% (30-50) | +0.16 | -1.77 | -157 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 50 | 36% (24-50) | -0.21 | -1.91 | -96 |  |
| (0.132, 0.37] | 49 | 41% (28-55) | -0.29 | -2.42 | -119 |  |
| (0.37, 1.555] | 49 | 35% (23-49) | -0.07 | -2.76 | -135 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 49 | 37% (25-51) | -0.53 | -2.42 | -119 |  |
| (0.147, 0.404] | 49 | 45% (32-59) | +1.36 | -0.94 | -46 |  |
| (0.404, 1.192] | 49 | 31% (20-45) | -1.29 | -3.64 | -178 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.257] | 50 | 38% (26-52) | +0.01 | -2.52 | -126 |  |
| (-0.257, 0.364] | 49 | 43% (30-57) | +0.66 | -0.75 | -37 |  |
| (0.364, 2.726] | 49 | 31% (20-45) | -1.25 | -3.82 | -187 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0518] | 50 | 38% (26-52) | -0.60 | -2.44 | -122 |  |
| (0.0518, 0.123] | 49 | 43% (30-57) | +0.56 | -1.55 | -76 |  |
| (0.123, 0.678] | 49 | 31% (20-45) | -0.53 | -3.09 | -152 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.197] | 50 | 44% (31-58) | +0.03 | -1.30 | -65 |  |
| (0.197, 0.307] | 49 | 33% (21-47) | -0.31 | -2.76 | -135 |  |
| (0.307, 0.875] | 49 | 35% (23-49) | -0.31 | -3.06 | -150 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.408] | 50 | 38% (26-52) | +0.25 | -1.92 | -96 |  |
| (2.408, 3.502] | 49 | 47% (34-61) | +0.86 | -1.17 | -57 |  |
| (3.502, 18.76] | 49 | 27% (16-40) | -1.70 | -4.01 | -196 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0946] | 50 | 46% (33-60) | +0.31 | -0.45 | -23 |  |
| (0.0946, 0.15] | 49 | 29% (18-42) | -1.04 | -2.53 | -124 |  |
| (0.15, 0.392] | 49 | 37% (25-51) | +0.15 | -4.14 | -203 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-5.5520000000000005, -0.913] | 8 | 25% (7-59) | -1.79 | -2.77 | -22 | few trades |
| (-0.913, 0.577] | 7 | 14% (3-51) | -3.45 | -4.02 | -28 | few trades |
| (0.577, 5.305] | 7 | 71% (36-92) | +4.59 | +4.13 | +29 | few trades |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.457] | 10 | 30% (11-60) | -2.26 | -3.01 | -30 |  |
| (0.457, 0.698] | 9 | 11% (2-44) | -3.37 | -4.14 | -37 | few trades |
| (0.698, 1.74] | 10 | 60% (31-83) | +2.90 | +2.12 | +21 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.261, 0.743] | 10 | 40% (17-69) | +0.03 | -0.47 | -5 |  |
| (0.743, 1.116] | 9 | 44% (19-73) | +1.03 | +0.15 | +1 | few trades |
| (1.116, 3.566] | 10 | 20% (6-51) | -3.35 | -4.28 | -43 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.296] | 10 | 10% (2-40) | -3.31 | -3.91 | -39 |  |
| (0.296, 0.495] | 9 | 56% (27-81) | +0.46 | -0.19 | -2 | few trades |
| (0.495, 0.815] | 10 | 40% (17-69) | +0.50 | -0.53 | -5 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 76, target 37, time_stop 34, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0946] | 50 | 34% | 16% | 48% |
| (0.0946, 0.15] | 49 | 63% | 27% | 10% |
| (0.15, 0.392] | 49 | 57% | 33% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
