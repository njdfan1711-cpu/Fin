# Scalp signal analysis (trail exits)

_146 tagged trades, 14 trading days (2026-10-01 to 2026-10-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 146 | 34% (26-42) | -0.93 | -3.13 | -456 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 22 | +4 | +0.20 | 124 | -461 | -3.72 | -4 |
| skip first 30 min | 1 | -6 | -6.31 | 145 | -450 | -3.10 | +6 |
| skip when SPY is down on the day | 57 | -255 | -4.48 | 89 | -201 | -2.26 | +255 |
| skip when SPY is below its VWAP | 58 | -273 | -4.71 | 88 | -183 | -2.08 | +273 |
| skip when SPY fell over the last 15 min | 58 | -181 | -3.13 | 88 | -275 | -3.13 | +181 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 36 | -181 | -5.02 | 110 | -276 | -2.51 | +181 |
| skip stock not beating SPY over 15 min | 20 | -60 | -2.98 | 126 | -397 | -3.15 | +60 |
| skip afternoon entries (2:00-3:45 PM) | 31 | -187 | -6.04 | 115 | -269 | -2.34 | +187 |
| skip volume spikes above 5x average | 26 | -138 | -5.30 | 120 | -319 | -2.66 | +138 |
| skip when the stop is inside normal noise (range > stop) | 3 | -2 | -0.68 | 143 | -454 | -3.18 | +2 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.58%) | 6 | -25 | -4.19 | 140 | -431 | -3.08 | +25 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 90 | -362 | -4.03 | 56 | -94 | -1.68 | +362 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 20 | 50% (30-70) | +0.07 | -2.52 | -50 |  |
| 60-240 | 62 | 29% (19-41) | -1.36 | -3.13 | -194 |  |
| 240-375 | 42 | 31% (19-46) | -2.61 | -5.15 | -216 |  |
| 375-390 | 22 | 36% (20-57) | +2.58 | +0.20 | +4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 32% (16-53) | -1.38 | -3.24 | -71 |  |
| -0.2 to 0 | 35 | 26% (14-42) | -2.49 | -5.26 | -184 |  |
| 0 to 0.2 | 40 | 32% (20-48) | -1.19 | -2.89 | -115 |  |
| > 0.2 | 49 | 41% (28-55) | +0.59 | -1.75 | -86 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 58 | 22% (14-35) | -2.14 | -4.71 | -273 |  |
| above VWAP | 88 | 41% (31-51) | -0.13 | -2.08 | -183 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.134] | 49 | 31% (20-45) | +0.13 | -1.60 | -79 |  |
| (0.134, 0.372] | 48 | 44% (31-58) | -1.14 | -3.29 | -158 |  |
| (0.372, 1.555] | 49 | 27% (16-40) | -1.79 | -4.49 | -220 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.148] | 49 | 33% (21-47) | -0.04 | -1.99 | -97 |  |
| (0.148, 0.405] | 48 | 40% (27-54) | -0.60 | -2.91 | -140 |  |
| (0.405, 1.192] | 48 | 29% (18-43) | -2.06 | -4.44 | -213 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.276] | 49 | 33% (21-47) | -1.38 | -3.95 | -193 |  |
| (-0.276, 0.356] | 48 | 48% (34-62) | +1.11 | -0.32 | -16 | ▲ |
| (0.356, 2.726] | 49 | 20% (11-34) | -2.49 | -5.05 | -247 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0519] | 49 | 33% (21-47) | -1.67 | -3.53 | -173 |  |
| (0.0519, 0.124] | 48 | 38% (25-52) | +0.53 | -1.62 | -78 |  |
| (0.124, 0.678] | 49 | 31% (20-45) | -1.63 | -4.19 | -205 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 49 | 43% (30-57) | +0.40 | -0.97 | -48 |  |
| (0.198, 0.311] | 48 | 29% (18-43) | -1.54 | -3.99 | -192 |  |
| (0.311, 0.875] | 49 | 29% (18-42) | -1.68 | -4.43 | -217 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.41] | 49 | 37% (25-51) | -0.79 | -2.99 | -147 |  |
| (2.41, 3.475] | 48 | 40% (27-54) | -0.56 | -2.61 | -125 |  |
| (3.475, 18.76] | 49 | 24% (15-38) | -1.44 | -3.77 | -185 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.095] | 49 | 45% (32-59) | +0.57 | -0.20 | -10 |  |
| (0.095, 0.149] | 48 | 31% (20-45) | -1.79 | -3.29 | -158 |  |
| (0.149, 0.392] | 49 | 24% (15-38) | -1.60 | -5.90 | -289 |  |

### Gap at the open vs yesterday's close (%)
_Not enough tagged trades with this value yet (17)._

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.438] | 8 | 38% (14-69) | -2.10 | -2.78 | -22 | few trades |
| (0.438, 0.649] | 8 | 25% (7-59) | -3.25 | -4.21 | -34 | few trades |
| (0.649, 1.2] | 8 | 62% (31-86) | -0.50 | -1.23 | -10 | few trades |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.261, 0.75] | 8 | 50% (22-78) | -1.49 | -2.01 | -16 | few trades |
| (0.75, 1.096] | 8 | 38% (14-69) | -1.59 | -2.52 | -20 | few trades |
| (1.096, 3.566] | 8 | 38% (14-69) | -2.77 | -3.69 | -30 | few trades |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.296] | 8 | 12% (2-47) | -3.45 | -4.09 | -33 | few trades |
| (0.296, 0.554] | 8 | 62% (31-86) | -0.37 | -1.10 | -9 | few trades |
| (0.554, 0.815] | 8 | 50% (22-78) | -2.03 | -3.02 | -24 | few trades |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.17%
- Reached +0.175% at some point: 42% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 69, trail_stop 54, time_stop 22, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.095] | 49 | 33% | 31% | 35% |
| (0.095, 0.149] | 48 | 56% | 38% | 6% |
| (0.149, 0.392] | 49 | 53% | 43% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
