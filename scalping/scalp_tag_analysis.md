# Scalp signal analysis (fixed exits)

_147 tagged trades, 14 trading days (2026-10-01 to 2026-10-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 147 | 37% (29-45) | -0.24 | -2.42 | -356 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 22 | -31 | -1.41 | 125 | -325 | -2.60 | +31 |
| skip first 30 min | 1 | -6 | -6.31 | 146 | -350 | -2.40 | +6 |
| skip when SPY is down on the day | 57 | -158 | -2.77 | 90 | -198 | -2.20 | +158 |
| skip when SPY is below its VWAP | 59 | -193 | -3.27 | 88 | -163 | -1.86 | +193 |
| skip when SPY fell over the last 15 min | 58 | -154 | -2.65 | 89 | -202 | -2.27 | +154 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 37 | -147 | -3.96 | 110 | -209 | -1.90 | +147 |
| skip stock not beating SPY over 15 min | 21 | -42 | -2.00 | 126 | -314 | -2.49 | +42 |
| skip afternoon entries (2:00-3:45 PM) | 32 | -180 | -5.62 | 115 | -176 | -1.53 | +180 |
| skip volume spikes above 5x average | 26 | -134 | -5.15 | 121 | -222 | -1.84 | +134 |
| skip when the stop is inside normal noise (range > stop) | 4 | +4 | +0.89 | 143 | -360 | -2.51 | -4 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 7 | -16 | -2.30 | 140 | -340 | -2.43 | +16 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 90 | -301 | -3.34 | 57 | -55 | -0.97 | +301 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 20 | 60% (39-78) | +2.90 | +0.31 | +6 | ▲ |
| 60-240 | 62 | 35% (25-48) | -0.36 | -2.13 | -132 |  |
| 240-375 | 43 | 26% (15-40) | -2.14 | -4.63 | -199 |  |
| 375-390 | 22 | 41% (23-61) | +0.97 | -1.41 | -31 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 41% (23-61) | +0.35 | -1.51 | -33 |  |
| -0.2 to 0 | 35 | 34% (21-51) | -0.78 | -3.55 | -124 |  |
| 0 to 0.2 | 41 | 37% (24-52) | +0.37 | -1.29 | -53 |  |
| > 0.2 | 49 | 37% (25-51) | -0.63 | -2.97 | -146 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 59 | 34% (23-47) | -0.73 | -3.27 | -193 |  |
| above VWAP | 88 | 39% (29-49) | +0.09 | -1.86 | -163 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 49 | 35% (23-49) | -0.36 | -2.08 | -102 |  |
| (0.133, 0.371] | 49 | 41% (28-55) | -0.29 | -2.42 | -119 |  |
| (0.371, 1.555] | 49 | 35% (23-49) | -0.07 | -2.76 | -135 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 49 | 37% (25-51) | -0.53 | -2.42 | -119 |  |
| (0.147, 0.404] | 48 | 44% (31-58) | +1.25 | -1.09 | -52 |  |
| (0.404, 1.192] | 49 | 31% (20-45) | -1.29 | -3.64 | -178 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.266] | 49 | 39% (26-53) | +0.04 | -2.53 | -124 |  |
| (-0.266, 0.348] | 49 | 43% (30-57) | +0.75 | -0.67 | -33 |  |
| (0.348, 2.726] | 49 | 29% (18-42) | -1.50 | -4.07 | -199 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 49 | 37% (25-51) | -0.75 | -2.62 | -128 |  |
| (0.052, 0.123] | 49 | 43% (30-57) | +0.56 | -1.55 | -76 |  |
| (0.123, 0.678] | 49 | 31% (20-45) | -0.53 | -3.09 | -152 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 49 | 43% (30-57) | -0.11 | -1.45 | -71 |  |
| (0.198, 0.309] | 49 | 33% (21-47) | -0.31 | -2.76 | -135 |  |
| (0.309, 0.875] | 49 | 35% (23-49) | -0.31 | -3.06 | -150 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.407] | 49 | 37% (25-51) | +0.20 | -2.00 | -98 |  |
| (2.407, 3.448] | 49 | 47% (34-61) | +0.73 | -1.29 | -63 |  |
| (3.448, 18.76] | 49 | 27% (16-40) | -1.65 | -3.98 | -195 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0946] | 50 | 46% (33-60) | +0.31 | -0.45 | -23 |  |
| (0.0946, 0.148] | 48 | 29% (18-43) | -0.95 | -2.45 | -118 |  |
| (0.148, 0.392] | 49 | 35% (23-49) | -0.10 | -4.40 | -216 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-5.5520000000000005, -1.088] | 7 | 29% (8-64) | -1.25 | -2.31 | -16 | few trades |
| (-1.088, 0.281] | 7 | 0% (0-35) | -4.62 | -5.15 | -36 | few trades |
| (0.281, 5.305] | 7 | 71% (36-92) | +3.99 | +3.51 | +25 | few trades |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.449] | 10 | 30% (11-60) | -2.26 | -3.01 | -30 |  |
| (0.449, 0.6] | 9 | 11% (2-44) | -3.37 | -4.14 | -37 | few trades |
| (0.6, 1.74] | 9 | 56% (27-81) | +2.47 | +1.67 | +15 | few trades |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.261, 0.736] | 10 | 40% (17-69) | +0.03 | -0.47 | -5 |  |
| (0.736, 1.136] | 9 | 33% (12-65) | -0.34 | -1.27 | -11 | few trades |
| (1.136, 3.566] | 9 | 22% (6-55) | -3.10 | -4.02 | -36 | few trades |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.296] | 10 | 10% (2-40) | -3.31 | -3.91 | -39 |  |
| (0.296, 0.508] | 9 | 44% (19-73) | -0.89 | -1.64 | -15 | few trades |
| (0.508, 0.815] | 9 | 44% (19-73) | +1.16 | +0.17 | +2 | few trades |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 42% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 76, target 37, time_stop 33, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0946] | 50 | 34% | 16% | 48% |
| (0.0946, 0.148] | 48 | 62% | 27% | 10% |
| (0.148, 0.392] | 49 | 59% | 33% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
