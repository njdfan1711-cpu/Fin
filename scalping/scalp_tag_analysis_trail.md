# Scalp signal analysis (trail exits)

_214 tagged trades, 24 trading days (2026-10-01 to 2026-11-03). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 214 | 37% (31-44) | -0.96 | -2.68 | -574 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -8 | -0.23 | 179 | -566 | -3.16 | +8 |
| skip first 30 min | 2 | -3 | -1.70 | 212 | -571 | -2.69 | +3 |
| skip when SPY is down on the day | 89 | -281 | -3.16 | 125 | -292 | -2.34 | +281 |
| skip when SPY is below its VWAP | 94 | -328 | -3.49 | 120 | -246 | -2.05 | +328 |
| skip when SPY fell over the last 15 min | 79 | -192 | -2.43 | 135 | -382 | -2.83 | +192 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 53 | -222 | -4.20 | 161 | -352 | -2.18 | +222 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 177 | -493 | -2.78 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 45 | -217 | -4.83 | 169 | -357 | -2.11 | +217 |
| skip volume spikes above 5x average | 40 | -190 | -4.74 | 174 | -384 | -2.21 | +190 |
| skip when the stop is inside normal noise (range > stop) | 14 | -46 | -3.27 | 200 | -528 | -2.64 | +46 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 24 | -81 | -3.36 | 190 | -493 | -2.60 | +81 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 109 | -386 | -3.54 | 105 | -188 | -1.79 | +386 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 33 | 48% (33-65) | -0.32 | -2.12 | -70 |  |
| 60-240 | 87 | 33% (24-44) | -1.42 | -2.89 | -252 |  |
| 240-375 | 59 | 34% (23-47) | -2.12 | -4.13 | -244 |  |
| 375-390 | 35 | 43% (28-59) | +1.54 | -0.23 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 37% (23-53) | -1.17 | -2.57 | -98 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 65 | 35% (25-48) | -1.50 | -2.82 | -183 |  |
| > 0.2 | 60 | 40% (29-53) | +0.17 | -1.82 | -109 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 94 | 31% (22-41) | -1.65 | -3.49 | -328 |  |
| above VWAP | 120 | 42% (34-51) | -0.42 | -2.05 | -246 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 72 | 35% (25-46) | -0.37 | -1.70 | -123 |  |
| (0.122, 0.374] | 71 | 48% (37-59) | -0.55 | -2.29 | -163 |  |
| (0.374, 1.555] | 71 | 30% (20-41) | -1.97 | -4.07 | -289 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.12] | 71 | 42% (31-54) | +0.09 | -1.26 | -90 |  |
| (0.12, 0.41] | 70 | 40% (29-52) | -0.99 | -2.93 | -205 |  |
| (0.41, 2.453] | 71 | 30% (20-41) | -1.97 | -3.89 | -276 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.352] | 72 | 38% (27-49) | -1.36 | -3.33 | -240 |  |
| (-0.352, 0.34] | 71 | 45% (34-57) | +0.57 | -0.64 | -45 |  |
| (0.34, 2.726] | 71 | 30% (20-41) | -2.08 | -4.06 | -288 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0522] | 72 | 39% (28-50) | -1.21 | -2.74 | -197 |  |
| (0.0522, 0.123] | 71 | 39% (29-51) | +0.06 | -1.55 | -110 |  |
| (0.123, 0.678] | 71 | 34% (24-45) | -1.73 | -3.75 | -266 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.208] | 72 | 42% (31-53) | -0.01 | -1.19 | -85 |  |
| (0.208, 0.314] | 71 | 37% (26-48) | -1.23 | -3.12 | -222 |  |
| (0.314, 0.979] | 71 | 34% (24-45) | -1.65 | -3.76 | -267 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.356] | 72 | 39% (28-50) | -0.61 | -2.24 | -161 |  |
| (2.356, 3.61] | 71 | 45% (34-57) | +0.38 | -1.34 | -95 |  |
| (3.61, 18.762] | 71 | 28% (19-40) | -2.66 | -4.48 | -318 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 73 | 44% (33-55) | +0.20 | -0.57 | -41 |  |
| (0.0985, 0.15] | 70 | 41% (31-53) | -1.20 | -2.40 | -168 |  |
| (0.15, 0.392] | 71 | 27% (18-38) | -1.91 | -5.13 | -364 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.911] | 30 | 27% (14-44) | -2.88 | -3.75 | -112 |  |
| (-0.911, 0.444] | 30 | 50% (33-67) | -0.48 | -1.01 | -30 |  |
| (0.444, 5.305] | 28 | 57% (39-73) | -0.19 | -0.92 | -26 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.509] | 32 | 47% (31-64) | -0.52 | -1.15 | -37 |  |
| (0.509, 0.743] | 31 | 45% (29-62) | -1.42 | -2.16 | -67 |  |
| (0.743, 1.74] | 32 | 41% (26-58) | -2.04 | -2.85 | -91 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 32 | 47% (31-64) | -1.18 | -1.68 | -54 |  |
| (0.779, 1.197] | 31 | 42% (26-59) | -1.27 | -2.01 | -62 |  |
| (1.197, 5.866] | 32 | 44% (28-61) | -1.52 | -2.47 | -79 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.346] | 32 | 38% (23-55) | -1.28 | -1.87 | -60 |  |
| (0.346, 0.557] | 31 | 55% (38-71) | -0.58 | -1.32 | -41 | ▲ |
| (0.557, 1.659] | 32 | 41% (26-58) | -2.09 | -2.95 | -95 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.17%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 8% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 47%
- Exit mix: stop 99, trail_stop 82, time_stop 29, eod 4

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 73 | 34% | 29% | 33% |
| (0.0985, 0.15] | 70 | 50% | 44% | 4% |
| (0.15, 0.392] | 71 | 55% | 42% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
