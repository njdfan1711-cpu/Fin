# Scalp signal analysis (trail exits)

_235 tagged trades, 26 trading days (2026-10-01 to 2026-11-05). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 235 | 41% (35-47) | -0.65 | -2.29 | -537 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 40 | +2 | +0.06 | 195 | -540 | -2.77 | -2 |
| skip first 30 min | 2 | -3 | -1.70 | 233 | -534 | -2.29 | +3 |
| skip when SPY is down on the day | 92 | -268 | -2.91 | 143 | -270 | -1.89 | +268 |
| skip when SPY is below its VWAP | 102 | -316 | -3.10 | 133 | -221 | -1.66 | +316 |
| skip when SPY fell over the last 15 min | 86 | -181 | -2.11 | 149 | -356 | -2.39 | +181 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 58 | -219 | -3.77 | 177 | -319 | -1.80 | +219 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 198 | -456 | -2.30 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 49 | -221 | -4.52 | 186 | -316 | -1.70 | +221 |
| skip volume spikes above 5x average | 45 | -166 | -3.68 | 190 | -372 | -1.96 | +166 |
| skip when the stop is inside normal noise (range > stop) | 20 | -21 | -1.05 | 215 | -516 | -2.40 | +21 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 29 | -40 | -1.38 | 206 | -497 | -2.41 | +40 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 116 | -405 | -3.49 | 119 | -132 | -1.11 | +405 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 96 | 39% (29-49) | -0.97 | -2.36 | -226 |  |
| 240-375 | 65 | 35% (25-48) | -1.93 | -3.84 | -249 |  |
| 375-390 | 40 | 48% (33-63) | +1.72 | +0.06 | +2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 41 | 41% (28-57) | -0.71 | -2.04 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 77 | 48% (37-59) | +0.68 | -1.03 | -79 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 102 | 34% (26-44) | -1.35 | -3.10 | -316 |  |
| above VWAP | 133 | 46% (38-54) | -0.12 | -1.66 | -221 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 79 | 38% (28-49) | -0.18 | -1.56 | -123 |  |
| (0.136, 0.382] | 78 | 53% (42-63) | -0.15 | -1.69 | -132 | ▲ |
| (0.382, 5.591] | 78 | 32% (23-43) | -1.64 | -3.62 | -282 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.108] | 78 | 47% (37-58) | +0.54 | -0.71 | -55 |  |
| (0.108, 0.422] | 77 | 42% (31-53) | -0.93 | -2.85 | -220 |  |
| (0.422, 4.846] | 78 | 33% (24-44) | -1.56 | -3.32 | -259 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.0920000000000005, -0.352] | 79 | 43% (33-54) | -0.86 | -2.70 | -213 |  |
| (-0.352, 0.4] | 78 | 47% (37-58) | +0.69 | -0.46 | -36 |  |
| (0.4, 4.204] | 78 | 32% (23-43) | -1.80 | -3.69 | -288 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 79 | 42% (32-53) | -0.95 | -2.39 | -189 |  |
| (0.056, 0.126] | 78 | 44% (33-55) | +0.30 | -1.25 | -97 |  |
| (0.126, 0.924] | 78 | 37% (27-48) | -1.31 | -3.22 | -251 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 79 | 44% (34-55) | +0.27 | -0.85 | -67 |  |
| (0.212, 0.329] | 78 | 42% (32-53) | -0.98 | -2.75 | -215 |  |
| (0.329, 2.663] | 78 | 36% (26-47) | -1.26 | -3.27 | -255 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.337] | 79 | 42% (32-53) | -0.50 | -2.03 | -160 |  |
| (2.337, 3.637] | 78 | 47% (37-58) | +0.57 | -1.10 | -86 |  |
| (3.637, 18.762] | 78 | 33% (24-44) | -2.04 | -3.73 | -291 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0988] | 79 | 48% (37-59) | +0.43 | -0.32 | -25 |  |
| (0.0988, 0.152] | 78 | 40% (30-51) | -1.33 | -2.50 | -195 |  |
| (0.152, 0.76] | 78 | 35% (25-46) | -1.08 | -4.06 | -317 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.974] | 37 | 41% (26-57) | -1.58 | -2.39 | -88 |  |
| (-0.974, 0.444] | 36 | 53% (37-68) | -0.17 | -0.75 | -27 |  |
| (0.444, 5.599] | 36 | 58% (42-73) | +0.27 | -0.46 | -16 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.519] | 39 | 51% (36-66) | -0.20 | -0.82 | -32 |  |
| (0.519, 0.762] | 38 | 45% (30-60) | -1.57 | -2.33 | -89 |  |
| (0.762, 3.799] | 39 | 54% (39-68) | -0.17 | -0.98 | -38 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.822] | 39 | 46% (32-61) | -1.39 | -1.93 | -75 |  |
| (0.822, 1.378] | 38 | 50% (35-65) | -0.51 | -1.25 | -47 |  |
| (1.378, 7.752] | 39 | 54% (39-68) | -0.02 | -0.92 | -36 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.355] | 39 | 46% (32-61) | -0.45 | -1.01 | -39 |  |
| (0.355, 0.585] | 38 | 58% (42-72) | -0.69 | -1.45 | -55 | ▲ |
| (0.585, 4.001] | 39 | 46% (32-61) | -0.78 | -1.65 | -64 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.15%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 103, trail_stop 96, time_stop 29, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0988] | 79 | 32% | 32% | 30% |
| (0.0988, 0.152] | 78 | 51% | 44% | 4% |
| (0.152, 0.76] | 78 | 49% | 47% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
