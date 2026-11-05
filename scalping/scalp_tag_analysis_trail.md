# Scalp signal analysis (trail exits)

_236 tagged trades, 26 trading days (2026-10-01 to 2026-11-05). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 236 | 41% (35-47) | -0.62 | -2.25 | -532 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 40 | +2 | +0.06 | 196 | -534 | -2.73 | -2 |
| skip first 30 min | 2 | -3 | -1.70 | 234 | -529 | -2.26 | +3 |
| skip when SPY is down on the day | 93 | -262 | -2.82 | 143 | -270 | -1.89 | +262 |
| skip when SPY is below its VWAP | 103 | -311 | -3.02 | 133 | -221 | -1.66 | +311 |
| skip when SPY fell over the last 15 min | 86 | -181 | -2.11 | 150 | -351 | -2.34 | +181 |
| skip over-extended (30-min run in top quarter, > 0.50%) | 59 | -213 | -3.62 | 177 | -319 | -1.80 | +213 |
| skip stock not beating SPY over 15 min | 38 | -76 | -1.99 | 198 | -456 | -2.30 | +76 |
| skip afternoon entries (2:00-3:45 PM) | 50 | -216 | -4.32 | 186 | -316 | -1.70 | +216 |
| skip volume spikes above 5x average | 45 | -166 | -3.68 | 191 | -366 | -1.92 | +166 |
| skip when the stop is inside normal noise (range > stop) | 21 | -16 | -0.74 | 215 | -516 | -2.40 | +16 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 29 | -40 | -1.38 | 207 | -492 | -2.38 | +40 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 116 | -405 | -3.49 | 120 | -127 | -1.06 | +405 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 96 | 39% (29-49) | -0.97 | -2.36 | -226 |  |
| 240-375 | 66 | 36% (26-48) | -1.80 | -3.70 | -244 |  |
| 375-390 | 40 | 48% (33-63) | +1.72 | +0.06 | +2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 42 | 43% (29-58) | -0.54 | -1.87 | -78 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 77 | 48% (37-59) | +0.68 | -1.03 | -79 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 103 | 35% (26-45) | -1.27 | -3.02 | -311 |  |
| above VWAP | 133 | 46% (38-54) | -0.12 | -1.66 | -221 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.134] | 79 | 39% (29-50) | -0.02 | -1.30 | -103 |  |
| (0.134, 0.38] | 78 | 51% (40-62) | -0.32 | -1.96 | -153 |  |
| (0.38, 5.591] | 79 | 33% (24-44) | -1.53 | -3.50 | -276 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.109] | 78 | 47% (37-58) | +0.54 | -0.71 | -55 |  |
| (0.109, 0.428] | 78 | 41% (31-52) | -0.90 | -2.83 | -221 |  |
| (0.428, 4.846] | 78 | 35% (25-46) | -1.50 | -3.24 | -253 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.0920000000000005, -0.362] | 79 | 44% (34-55) | -0.78 | -2.63 | -208 |  |
| (-0.362, 0.398] | 78 | 46% (36-57) | +0.59 | -0.57 | -45 |  |
| (0.398, 4.204] | 79 | 33% (24-44) | -1.67 | -3.54 | -280 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 79 | 42% (32-53) | -0.95 | -2.39 | -189 |  |
| (0.056, 0.127] | 78 | 44% (33-55) | +0.30 | -1.25 | -97 |  |
| (0.127, 0.924] | 79 | 38% (28-49) | -1.21 | -3.11 | -246 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 79 | 46% (35-57) | +0.35 | -0.77 | -61 |  |
| (0.211, 0.328] | 78 | 41% (31-52) | -1.00 | -2.77 | -216 |  |
| (0.328, 2.663] | 79 | 37% (27-48) | -1.23 | -3.22 | -255 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.324] | 79 | 42% (32-53) | -0.44 | -1.98 | -156 |  |
| (2.324, 3.635] | 78 | 47% (37-58) | +0.56 | -1.10 | -86 |  |
| (3.635, 18.762] | 79 | 34% (25-45) | -1.98 | -3.66 | -289 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0991] | 79 | 48% (37-59) | +0.43 | -0.32 | -25 |  |
| (0.0991, 0.153] | 78 | 40% (30-51) | -1.33 | -2.50 | -195 |  |
| (0.153, 0.76] | 79 | 35% (26-46) | -0.98 | -3.94 | -311 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.043] | 37 | 43% (29-59) | -1.25 | -2.07 | -77 |  |
| (-1.043, 0.444] | 37 | 51% (36-67) | -0.32 | -0.90 | -33 |  |
| (0.444, 5.599] | 36 | 58% (42-73) | +0.27 | -0.46 | -16 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.519] | 39 | 51% (36-66) | -0.20 | -0.82 | -32 |  |
| (0.519, 0.772] | 39 | 46% (32-61) | -1.51 | -2.25 | -88 |  |
| (0.772, 3.799] | 39 | 54% (39-68) | -0.03 | -0.86 | -33 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.822] | 39 | 46% (32-61) | -1.39 | -1.93 | -75 |  |
| (0.822, 1.412] | 39 | 51% (36-66) | -0.38 | -1.13 | -44 |  |
| (1.412, 7.752] | 39 | 54% (39-68) | +0.03 | -0.86 | -34 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.355] | 39 | 46% (32-61) | -0.45 | -1.01 | -39 |  |
| (0.355, 0.576] | 39 | 59% (43-73) | -0.50 | -1.27 | -50 | ▲ |
| (0.576, 4.001] | 39 | 46% (32-61) | -0.78 | -1.65 | -64 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 103, trail_stop 97, time_stop 29, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0991] | 79 | 32% | 32% | 30% |
| (0.0991, 0.153] | 78 | 51% | 44% | 4% |
| (0.153, 0.76] | 79 | 48% | 48% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
