# Scalp signal analysis (fixed exits)

_252 tagged trades, 28 trading days (2026-10-01 to 2026-11-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 252 | 41% (35-47) | +0.24 | -1.34 | -336 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 44 | -2 | -0.05 | 208 | -334 | -1.61 | +2 |
| skip first 30 min | 2 | -8 | -4.06 | 250 | -328 | -1.31 | +8 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 153 | -237 | -1.55 | +99 |
| skip when SPY is below its VWAP | 112 | -178 | -1.59 | 140 | -158 | -1.13 | +178 |
| skip when SPY fell over the last 15 min | 92 | -128 | -1.39 | 160 | -209 | -1.30 | +128 |
| skip over-extended (30-min run in top quarter, > 0.50%) | 63 | -173 | -2.75 | 189 | -163 | -0.86 | +173 |
| skip stock not beating SPY over 15 min | 42 | -40 | -0.94 | 210 | -297 | -1.41 | +40 |
| skip afternoon entries (2:00-3:45 PM) | 55 | -215 | -3.92 | 197 | -121 | -0.61 | +215 |
| skip volume spikes above 5x average | 48 | -117 | -2.44 | 204 | -219 | -1.07 | +117 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 226 | -330 | -1.46 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 33 | -12 | -0.36 | 219 | -325 | -1.48 | +12 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 122 | -312 | -2.56 | 130 | -24 | -0.18 | +312 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 53% (37-68) | +2.11 | +0.38 | +14 |  |
| 60-240 | 101 | 40% (31-49) | +0.11 | -1.24 | -125 |  |
| 240-375 | 71 | 31% (21-42) | -1.33 | -3.14 | -223 |  |
| 375-390 | 44 | 50% (36-64) | +1.54 | -0.05 | -2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 67 | 33% (23-45) | -0.43 | -1.75 | -118 |  |
| > 0.2 | 86 | 43% (33-54) | +0.21 | -1.39 | -120 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 41% (32-50) | +0.08 | -1.59 | -178 |  |
| above VWAP | 140 | 41% (33-49) | +0.37 | -1.13 | -158 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 84 | 40% (31-51) | +0.26 | -1.00 | -84 |  |
| (0.133, 0.379] | 84 | 46% (36-57) | +0.61 | -0.97 | -81 |  |
| (0.379, 5.591] | 84 | 36% (26-46) | -0.15 | -2.04 | -172 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.11] | 84 | 46% (36-57) | +0.81 | -0.39 | -33 |  |
| (0.11, 0.422] | 83 | 41% (31-52) | +0.54 | -1.33 | -111 |  |
| (0.422, 4.846] | 83 | 36% (27-47) | -0.54 | -2.23 | -185 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.371] | 84 | 45% (35-56) | +0.73 | -1.06 | -89 |  |
| (-0.371, 0.396] | 84 | 45% (35-56) | +1.00 | -0.13 | -11 |  |
| (0.396, 5.005] | 84 | 32% (23-43) | -1.02 | -2.82 | -237 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0561] | 84 | 42% (32-52) | +0.01 | -1.39 | -117 |  |
| (0.0561, 0.126] | 84 | 46% (36-57) | +0.79 | -0.69 | -58 |  |
| (0.126, 0.924] | 84 | 35% (25-45) | -0.08 | -1.92 | -162 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 84 | 44% (34-55) | +0.43 | -0.67 | -56 |  |
| (0.212, 0.333] | 84 | 42% (32-52) | +0.34 | -1.47 | -123 |  |
| (0.333, 2.663] | 84 | 37% (27-48) | -0.05 | -1.87 | -157 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.305] | 84 | 36% (26-46) | -0.20 | -1.70 | -143 |  |
| (2.305, 3.618] | 84 | 51% (41-62) | +1.33 | -0.26 | -22 |  |
| (3.618, 18.762] | 84 | 36% (26-46) | -0.41 | -2.04 | -171 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 84 | 48% (37-58) | +0.64 | -0.13 | -11 |  |
| (0.102, 0.158] | 84 | 36% (26-46) | -0.35 | -1.50 | -126 |  |
| (0.158, 0.76] | 84 | 39% (30-50) | +0.43 | -2.37 | -199 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.938] | 42 | 33% (21-48) | -0.78 | -1.59 | -67 |  |
| (-0.938, 0.589] | 42 | 52% (38-67) | +1.48 | +0.88 | +37 |  |
| (0.589, 7.522] | 42 | 48% (33-62) | +1.26 | +0.52 | +22 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 46 | 43% (30-58) | +0.07 | -0.58 | -27 |  |
| (0.533, 0.832] | 43 | 44% (30-59) | +0.53 | -0.18 | -8 |  |
| (0.832, 3.799] | 44 | 43% (30-58) | +0.88 | +0.03 | +1 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.822] | 45 | 42% (29-57) | +0.10 | -0.47 | -21 |  |
| (0.822, 1.457] | 44 | 45% (32-60) | +1.00 | +0.27 | +12 |  |
| (1.457, 9.058] | 44 | 43% (30-58) | +0.37 | -0.54 | -24 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.369] | 45 | 42% (29-57) | +0.24 | -0.35 | -16 |  |
| (0.369, 0.594] | 44 | 45% (32-60) | +0.60 | -0.15 | -6 |  |
| (0.594, 4.001] | 44 | 43% (30-58) | +0.63 | -0.24 | -11 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 27% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 121, target 67, time_stop 51, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 84 | 33% | 18% | 42% |
| (0.102, 0.158] | 84 | 56% | 26% | 12% |
| (0.158, 0.76] | 84 | 55% | 36% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
