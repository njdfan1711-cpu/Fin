# Scalp signal analysis (trail exits)

_148 tagged trades, 15 trading days (2026-10-01 to 2026-10-21). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 148 | 34% (27-42) | -0.91 | -3.08 | -457 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 22 | +4 | +0.20 | 126 | -461 | -3.66 | -4 |
| skip first 30 min | 1 | -6 | -6.31 | 147 | -450 | -3.06 | +6 |
| skip when SPY is down on the day | 58 | -254 | -4.39 | 90 | -202 | -2.25 | +254 |
| skip when SPY is below its VWAP | 59 | -274 | -4.65 | 89 | -182 | -2.05 | +274 |
| skip when SPY fell over the last 15 min | 58 | -181 | -3.13 | 90 | -275 | -3.06 | +181 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 37 | -181 | -4.90 | 111 | -275 | -2.48 | +181 |
| skip stock not beating SPY over 15 min | 22 | -60 | -2.71 | 126 | -397 | -3.15 | +60 |
| skip afternoon entries (2:00-3:45 PM) | 32 | -188 | -5.88 | 116 | -268 | -2.31 | +188 |
| skip volume spikes above 5x average | 27 | -137 | -5.06 | 121 | -320 | -2.64 | +137 |
| skip when the stop is inside normal noise (range > stop) | 4 | -2 | -0.40 | 144 | -455 | -3.16 | +2 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 7 | -25 | -3.56 | 141 | -432 | -3.06 | +25 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 90 | -362 | -4.03 | 58 | -94 | -1.62 | +362 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 20 | 50% (30-70) | +0.07 | -2.52 | -50 |  |
| 60-240 | 63 | 30% (20-42) | -1.32 | -3.07 | -193 |  |
| 240-375 | 43 | 30% (19-45) | -2.56 | -5.06 | -217 |  |
| 375-390 | 22 | 36% (20-57) | +2.58 | +0.20 | +4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 32% (16-53) | -1.38 | -3.24 | -71 |  |
| -0.2 to 0 | 36 | 28% (16-44) | -2.38 | -5.09 | -183 |  |
| 0 to 0.2 | 41 | 32% (20-47) | -1.18 | -2.84 | -116 |  |
| > 0.2 | 49 | 41% (28-55) | +0.59 | -1.75 | -86 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 59 | 22% (13-34) | -2.12 | -4.65 | -274 |  |
| above VWAP | 89 | 42% (32-52) | -0.12 | -2.05 | -182 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 50 | 32% (21-46) | +0.13 | -1.56 | -78 |  |
| (0.132, 0.37] | 49 | 43% (30-57) | -1.10 | -3.23 | -158 |  |
| (0.37, 1.555] | 49 | 27% (16-40) | -1.79 | -4.49 | -220 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 49 | 33% (21-47) | -0.10 | -1.99 | -97 |  |
| (0.147, 0.404] | 49 | 39% (26-53) | -0.60 | -2.91 | -143 |  |
| (0.404, 1.192] | 49 | 31% (20-45) | -1.94 | -4.29 | -210 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.257] | 50 | 32% (21-46) | -1.38 | -3.91 | -195 |  |
| (-0.257, 0.364] | 49 | 47% (34-61) | +0.99 | -0.42 | -21 |  |
| (0.364, 2.726] | 49 | 22% (13-36) | -2.34 | -4.91 | -240 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0518] | 50 | 34% (22-48) | -1.60 | -3.44 | -172 |  |
| (0.0518, 0.123] | 49 | 37% (25-51) | +0.50 | -1.61 | -79 |  |
| (0.123, 0.678] | 49 | 31% (20-45) | -1.63 | -4.19 | -205 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.197] | 50 | 44% (31-58) | +0.39 | -0.94 | -47 |  |
| (0.197, 0.307] | 49 | 29% (18-42) | -1.47 | -3.93 | -192 |  |
| (0.307, 0.875] | 49 | 29% (18-42) | -1.68 | -4.43 | -217 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.408] | 50 | 36% (24-50) | -0.79 | -2.96 | -148 |  |
| (2.408, 3.502] | 49 | 41% (28-55) | +0.83 | -1.20 | -59 |  |
| (3.502, 18.76] | 49 | 24% (15-38) | -2.79 | -5.10 | -250 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0946] | 50 | 44% (31-58) | +0.55 | -0.21 | -11 |  |
| (0.0946, 0.15] | 49 | 31% (20-45) | -1.86 | -3.36 | -164 |  |
| (0.15, 0.392] | 49 | 27% (16-40) | -1.45 | -5.74 | -281 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-5.5520000000000005, -0.913] | 8 | 38% (14-69) | -2.44 | -3.42 | -27 | few trades |
| (-0.913, 0.577] | 7 | 14% (3-51) | -3.45 | -4.02 | -28 | few trades |
| (0.577, 5.305] | 7 | 71% (36-92) | +1.10 | +0.64 | +4 | few trades |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.457] | 10 | 30% (11-60) | -2.33 | -3.08 | -31 |  |
| (0.457, 0.698] | 9 | 22% (6-55) | -3.51 | -4.28 | -39 | few trades |
| (0.698, 1.74] | 10 | 70% (40-89) | -0.06 | -0.84 | -8 | ▲ |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.261, 0.743] | 10 | 40% (17-69) | -1.81 | -2.31 | -23 |  |
| (0.743, 1.116] | 9 | 44% (19-73) | -1.25 | -2.13 | -19 | few trades |
| (1.116, 3.566] | 10 | 40% (17-69) | -2.62 | -3.54 | -35 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.296] | 10 | 10% (2-40) | -3.39 | -3.98 | -40 |  |
| (0.296, 0.495] | 9 | 56% (27-81) | -1.26 | -1.91 | -17 | few trades |
| (0.495, 0.815] | 10 | 60% (31-83) | -1.04 | -2.07 | -21 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.17%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 47%
- Exit mix: stop 69, trail_stop 55, time_stop 23, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0946] | 50 | 32% | 30% | 36% |
| (0.0946, 0.15] | 49 | 57% | 37% | 6% |
| (0.15, 0.392] | 49 | 51% | 45% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
