# Scalp signal analysis (trail exits)

_234 tagged trades, 26 trading days (2026-10-01 to 2026-11-05). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 234 | 41% (35-47) | -0.68 | -2.32 | -542 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 40 | +2 | +0.06 | 194 | -545 | -2.81 | -2 |
| skip first 30 min | 2 | -3 | -1.70 | 232 | -539 | -2.32 | +3 |
| skip when SPY is down on the day | 91 | -273 | -3.00 | 143 | -270 | -1.89 | +273 |
| skip when SPY is below its VWAP | 101 | -321 | -3.18 | 133 | -221 | -1.66 | +321 |
| skip when SPY fell over the last 15 min | 86 | -181 | -2.11 | 148 | -361 | -2.44 | +181 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 58 | -227 | -3.92 | 176 | -315 | -1.79 | +227 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 197 | -461 | -2.34 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 49 | -221 | -4.52 | 185 | -321 | -1.73 | +221 |
| skip volume spikes above 5x average | 44 | -171 | -3.88 | 190 | -372 | -1.96 | +171 |
| skip when the stop is inside normal noise (range > stop) | 19 | -26 | -1.36 | 215 | -516 | -2.40 | +26 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 29 | -45 | -1.56 | 205 | -497 | -2.42 | +45 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 115 | -410 | -3.57 | 119 | -132 | -1.11 | +410 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 95 | 38% (29-48) | -1.05 | -2.43 | -231 |  |
| 240-375 | 65 | 35% (25-48) | -1.93 | -3.84 | -249 |  |
| 375-390 | 40 | 48% (33-63) | +1.72 | +0.06 | +2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 40 | 40% (26-55) | -0.88 | -2.22 | -89 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 77 | 48% (37-59) | +0.68 | -1.03 | -79 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 101 | 34% (25-43) | -1.42 | -3.18 | -321 |  |
| above VWAP | 133 | 46% (38-54) | -0.12 | -1.66 | -221 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.135] | 78 | 38% (28-50) | -0.11 | -1.39 | -108 |  |
| (0.135, 0.379] | 78 | 51% (40-62) | -0.32 | -1.96 | -153 |  |
| (0.379, 2.096] | 78 | 32% (23-43) | -1.63 | -3.60 | -281 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.107] | 78 | 47% (37-58) | +0.54 | -0.71 | -55 |  |
| (0.107, 0.421] | 77 | 42% (31-53) | -0.93 | -2.85 | -220 |  |
| (0.421, 2.453] | 77 | 32% (23-44) | -1.66 | -3.43 | -264 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.35] | 78 | 42% (32-53) | -0.94 | -2.80 | -218 |  |
| (-0.35, 0.4] | 78 | 47% (37-58) | +0.69 | -0.46 | -36 |  |
| (0.4, 4.204] | 78 | 32% (23-43) | -1.80 | -3.69 | -288 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0559] | 78 | 41% (31-52) | -1.00 | -2.45 | -191 |  |
| (0.0559, 0.125] | 78 | 44% (33-55) | +0.24 | -1.30 | -102 |  |
| (0.125, 0.924] | 78 | 37% (27-48) | -1.29 | -3.20 | -250 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 78 | 45% (34-56) | +0.27 | -0.85 | -67 |  |
| (0.211, 0.327] | 78 | 41% (31-52) | -1.00 | -2.77 | -216 |  |
| (0.327, 2.663] | 78 | 36% (26-47) | -1.32 | -3.33 | -260 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.331] | 78 | 41% (31-52) | -0.53 | -2.08 | -162 |  |
| (2.331, 3.634] | 78 | 47% (37-58) | +0.56 | -1.10 | -86 |  |
| (3.634, 18.762] | 78 | 33% (24-44) | -2.08 | -3.77 | -294 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0987] | 78 | 47% (37-58) | +0.38 | -0.36 | -28 |  |
| (0.0987, 0.151] | 78 | 41% (31-52) | -1.29 | -2.45 | -191 |  |
| (0.151, 0.392] | 78 | 33% (24-44) | -1.14 | -4.14 | -323 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.938] | 36 | 39% (25-55) | -1.78 | -2.59 | -93 |  |
| (-0.938, 0.447] | 36 | 53% (37-68) | -0.17 | -0.75 | -27 |  |
| (0.447, 5.599] | 36 | 58% (42-73) | +0.27 | -0.46 | -16 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.518] | 39 | 51% (36-66) | -0.20 | -0.82 | -32 |  |
| (0.518, 0.749] | 38 | 45% (30-60) | -1.57 | -2.33 | -89 |  |
| (0.749, 1.75] | 38 | 53% (37-68) | -0.33 | -1.13 | -43 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.822] | 39 | 46% (32-61) | -1.39 | -1.93 | -75 |  |
| (0.822, 1.313] | 38 | 50% (35-65) | -0.51 | -1.25 | -47 |  |
| (1.313, 5.866] | 38 | 53% (37-68) | -0.17 | -1.07 | -41 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.354] | 39 | 46% (32-61) | -0.45 | -1.01 | -39 |  |
| (0.354, 0.566] | 38 | 58% (42-72) | -0.69 | -1.45 | -55 | ▲ |
| (0.566, 2.726] | 38 | 45% (30-60) | -0.96 | -1.82 | -69 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.15%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 103, trail_stop 95, time_stop 29, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0987] | 78 | 32% | 31% | 31% |
| (0.0987, 0.151] | 78 | 51% | 44% | 4% |
| (0.151, 0.392] | 78 | 49% | 47% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
