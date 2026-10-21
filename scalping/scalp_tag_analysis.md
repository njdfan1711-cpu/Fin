# Scalp signal analysis (fixed exits)

_146 tagged trades, 14 trading days (2026-10-01 to 2026-10-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 146 | 37% (30-45) | -0.24 | -2.43 | -355 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 22 | -31 | -1.41 | 124 | -324 | -2.61 | +31 |
| skip first 30 min | 1 | -6 | -6.31 | 145 | -349 | -2.40 | +6 |
| skip when SPY is down on the day | 57 | -158 | -2.77 | 89 | -197 | -2.22 | +158 |
| skip when SPY is below its VWAP | 58 | -192 | -3.30 | 88 | -163 | -1.86 | +192 |
| skip when SPY fell over the last 15 min | 58 | -154 | -2.65 | 88 | -201 | -2.29 | +154 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 36 | -155 | -4.32 | 110 | -200 | -1.81 | +155 |
| skip stock not beating SPY over 15 min | 20 | -41 | -2.05 | 126 | -314 | -2.49 | +41 |
| skip afternoon entries (2:00-3:45 PM) | 31 | -179 | -5.77 | 115 | -176 | -1.53 | +179 |
| skip volume spikes above 5x average | 26 | -134 | -5.15 | 120 | -221 | -1.84 | +134 |
| skip when the stop is inside normal noise (range > stop) | 3 | +10 | +3.46 | 143 | -365 | -2.55 | -10 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.58%) | 6 | -9 | -1.54 | 140 | -346 | -2.47 | +9 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 90 | -301 | -3.34 | 56 | -54 | -0.97 | +301 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 20 | 60% (39-78) | +2.90 | +0.31 | +6 | ▲ |
| 60-240 | 62 | 35% (25-48) | -0.36 | -2.13 | -132 |  |
| 240-375 | 42 | 26% (15-41) | -2.18 | -4.72 | -198 |  |
| 375-390 | 22 | 41% (23-61) | +0.97 | -1.41 | -31 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 41% (23-61) | +0.35 | -1.51 | -33 |  |
| -0.2 to 0 | 35 | 34% (21-51) | -0.78 | -3.55 | -124 |  |
| 0 to 0.2 | 40 | 38% (24-53) | +0.40 | -1.30 | -52 |  |
| > 0.2 | 49 | 37% (25-51) | -0.63 | -2.97 | -146 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 58 | 34% (24-47) | -0.73 | -3.30 | -192 |  |
| above VWAP | 88 | 39% (29-49) | +0.09 | -1.86 | -163 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.134] | 49 | 37% (25-51) | -0.28 | -2.01 | -99 |  |
| (0.134, 0.372] | 48 | 40% (27-54) | -0.36 | -2.52 | -121 |  |
| (0.372, 1.555] | 49 | 35% (23-49) | -0.07 | -2.76 | -135 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.148] | 49 | 39% (26-53) | -0.31 | -2.25 | -110 |  |
| (0.148, 0.405] | 48 | 42% (29-56) | +0.92 | -1.40 | -67 |  |
| (0.405, 1.192] | 48 | 31% (20-45) | -1.19 | -3.57 | -171 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.276] | 49 | 39% (26-53) | +0.04 | -2.53 | -124 |  |
| (-0.276, 0.356] | 48 | 44% (31-58) | +0.78 | -0.66 | -32 |  |
| (0.356, 2.726] | 49 | 29% (18-42) | -1.50 | -4.07 | -199 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0519] | 49 | 37% (25-51) | -0.75 | -2.62 | -128 |  |
| (0.0519, 0.124] | 48 | 44% (31-58) | +0.59 | -1.57 | -75 |  |
| (0.124, 0.678] | 49 | 31% (20-45) | -0.53 | -3.09 | -152 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 49 | 43% (30-57) | -0.21 | -1.59 | -78 |  |
| (0.198, 0.311] | 48 | 33% (22-47) | -0.19 | -2.65 | -127 |  |
| (0.311, 0.875] | 49 | 35% (23-49) | -0.31 | -3.06 | -150 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.41] | 49 | 39% (26-53) | +0.26 | -1.94 | -95 |  |
| (2.41, 3.475] | 48 | 46% (33-60) | +0.70 | -1.35 | -65 |  |
| (3.475, 18.76] | 49 | 27% (16-40) | -1.65 | -3.98 | -195 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.095] | 49 | 47% (34-61) | +0.33 | -0.44 | -22 |  |
| (0.095, 0.149] | 48 | 29% (18-43) | -0.95 | -2.45 | -118 |  |
| (0.149, 0.392] | 49 | 35% (23-49) | -0.10 | -4.40 | -216 |  |

### Gap at the open vs yesterday's close (%)
_Not enough tagged trades with this value yet (17)._

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.438] | 8 | 38% (14-69) | -2.01 | -2.69 | -22 | few trades |
| (0.438, 0.649] | 8 | 12% (2-47) | -3.09 | -4.04 | -32 | few trades |
| (0.649, 1.2] | 8 | 62% (31-86) | +3.46 | +2.73 | +22 | few trades |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.261, 0.75] | 8 | 50% (22-78) | +0.81 | +0.29 | +2 | few trades |
| (0.75, 1.096] | 8 | 38% (14-69) | +0.32 | -0.60 | -5 | few trades |
| (1.096, 3.566] | 8 | 25% (7-59) | -2.78 | -3.70 | -30 | few trades |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.296] | 8 | 12% (2-47) | -3.37 | -4.01 | -32 | few trades |
| (0.296, 0.554] | 8 | 62% (31-86) | +1.60 | +0.87 | +7 | few trades |
| (0.554, 0.815] | 8 | 38% (14-69) | +0.12 | -0.88 | -7 | few trades |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 42% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 53%
- Exit mix: stop 76, target 37, time_stop 32, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.095] | 49 | 35% | 16% | 47% |
| (0.095, 0.149] | 48 | 62% | 27% | 10% |
| (0.149, 0.392] | 49 | 59% | 33% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
