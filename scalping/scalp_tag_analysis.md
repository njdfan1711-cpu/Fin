# Scalp signal analysis (fixed exits)

_254 tagged trades, 28 trading days (2026-10-01 to 2026-11-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 254 | 41% (35-47) | +0.24 | -1.33 | -338 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 44 | -2 | -0.05 | 210 | -336 | -1.60 | +2 |
| skip first 30 min | 2 | -8 | -4.06 | 252 | -330 | -1.31 | +8 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 155 | -239 | -1.54 | +99 |
| skip when SPY is below its VWAP | 112 | -178 | -1.59 | 142 | -160 | -1.13 | +178 |
| skip when SPY fell over the last 15 min | 92 | -128 | -1.39 | 162 | -211 | -1.30 | +128 |
| skip over-extended (30-min run in top quarter, > 0.52%) | 63 | -168 | -2.66 | 191 | -171 | -0.89 | +168 |
| skip stock not beating SPY over 15 min | 42 | -40 | -0.94 | 212 | -299 | -1.41 | +40 |
| skip afternoon entries (2:00-3:45 PM) | 57 | -217 | -3.81 | 197 | -121 | -0.61 | +217 |
| skip volume spikes above 5x average | 48 | -117 | -2.44 | 206 | -221 | -1.07 | +117 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 228 | -332 | -1.45 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 34 | -19 | -0.55 | 220 | -320 | -1.45 | +19 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 123 | -319 | -2.60 | 131 | -19 | -0.14 | +319 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 53% (37-68) | +2.11 | +0.38 | +14 |  |
| 60-240 | 101 | 40% (31-49) | +0.11 | -1.24 | -125 |  |
| 240-375 | 73 | 32% (22-43) | -1.29 | -3.08 | -225 |  |
| 375-390 | 44 | 50% (36-64) | +1.54 | -0.05 | -2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 67 | 33% (23-45) | -0.43 | -1.75 | -118 |  |
| > 0.2 | 88 | 43% (33-54) | +0.21 | -1.38 | -121 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 41% (32-50) | +0.08 | -1.59 | -178 |  |
| above VWAP | 142 | 41% (33-49) | +0.36 | -1.13 | -160 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.134] | 85 | 41% (31-52) | +0.30 | -0.96 | -82 |  |
| (0.134, 0.38] | 84 | 45% (35-56) | +0.50 | -1.07 | -90 |  |
| (0.38, 5.591] | 85 | 36% (27-47) | -0.08 | -1.96 | -167 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.114] | 84 | 46% (36-57) | +0.81 | -0.39 | -33 |  |
| (0.114, 0.439] | 84 | 40% (31-51) | +0.46 | -1.40 | -117 |  |
| (0.439, 4.846] | 84 | 37% (27-48) | -0.46 | -2.15 | -180 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 85 | 45% (35-55) | +0.71 | -1.07 | -91 |  |
| (-0.367, 0.398] | 84 | 46% (36-57) | +1.09 | -0.05 | -4 |  |
| (0.398, 5.005] | 85 | 32% (23-42) | -1.07 | -2.86 | -243 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 85 | 42% (32-53) | +0.07 | -1.31 | -112 |  |
| (0.056, 0.127] | 84 | 46% (36-57) | +0.79 | -0.69 | -58 |  |
| (0.127, 0.924] | 85 | 34% (25-45) | -0.15 | -1.98 | -168 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 85 | 44% (33-54) | +0.35 | -0.73 | -62 |  |
| (0.212, 0.334] | 84 | 43% (33-54) | +0.49 | -1.33 | -112 |  |
| (0.334, 2.663] | 85 | 36% (27-47) | -0.12 | -1.93 | -164 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.324] | 85 | 36% (27-47) | -0.07 | -1.57 | -133 |  |
| (2.324, 3.611] | 84 | 50% (40-60) | +1.17 | -0.43 | -36 |  |
| (3.611, 18.762] | 85 | 36% (27-47) | -0.38 | -1.99 | -169 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 85 | 48% (38-59) | +0.70 | -0.07 | -6 |  |
| (0.102, 0.159] | 84 | 36% (26-46) | -0.35 | -1.50 | -126 |  |
| (0.159, 0.76] | 85 | 39% (29-49) | +0.36 | -2.43 | -206 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.956] | 43 | 35% (22-50) | -0.62 | -1.44 | -62 |  |
| (-0.956, 0.601] | 42 | 52% (38-67) | +1.48 | +0.88 | +37 |  |
| (0.601, 7.522] | 43 | 47% (33-61) | +1.09 | +0.35 | +15 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.532] | 45 | 44% (31-59) | +0.25 | -0.38 | -17 |  |
| (0.532, 0.834] | 45 | 44% (31-59) | +0.46 | -0.27 | -12 |  |
| (0.834, 3.799] | 45 | 42% (29-57) | +0.73 | -0.12 | -5 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.822] | 45 | 44% (31-59) | +0.36 | -0.21 | -9 |  |
| (0.822, 1.46] | 45 | 44% (31-59) | +0.85 | +0.12 | +5 |  |
| (1.46, 9.058] | 45 | 42% (29-57) | +0.23 | -0.68 | -30 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.372] | 45 | 42% (29-57) | +0.24 | -0.35 | -16 |  |
| (0.372, 0.594] | 45 | 47% (33-61) | +0.72 | -0.03 | -1 |  |
| (0.594, 4.001] | 45 | 42% (29-57) | +0.48 | -0.39 | -18 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 122, target 67, time_stop 52, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 85 | 33% | 18% | 42% |
| (0.102, 0.159] | 84 | 56% | 26% | 12% |
| (0.159, 0.76] | 85 | 55% | 35% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
