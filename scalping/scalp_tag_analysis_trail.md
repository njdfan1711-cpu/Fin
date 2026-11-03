# Scalp signal analysis (trail exits)

_217 tagged trades, 24 trading days (2026-10-01 to 2026-11-03). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 217 | 37% (31-44) | -0.95 | -2.66 | -578 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -8 | -0.23 | 182 | -570 | -3.13 | +8 |
| skip first 30 min | 2 | -3 | -1.70 | 215 | -575 | -2.67 | +3 |
| skip when SPY is down on the day | 89 | -281 | -3.16 | 128 | -297 | -2.32 | +281 |
| skip when SPY is below its VWAP | 94 | -328 | -3.49 | 123 | -250 | -2.03 | +328 |
| skip when SPY fell over the last 15 min | 81 | -189 | -2.33 | 136 | -389 | -2.86 | +189 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 54 | -235 | -4.35 | 163 | -344 | -2.11 | +235 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 180 | -497 | -2.76 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 46 | -208 | -4.53 | 171 | -370 | -2.16 | +208 |
| skip volume spikes above 5x average | 40 | -190 | -4.74 | 177 | -389 | -2.20 | +190 |
| skip when the stop is inside normal noise (range > stop) | 14 | -46 | -3.27 | 203 | -532 | -2.62 | +46 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.67%) | 25 | -71 | -2.83 | 192 | -507 | -2.64 | +71 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 111 | -399 | -3.59 | 106 | -179 | -1.69 | +399 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 33 | 48% (33-65) | -0.32 | -2.12 | -70 |  |
| 60-240 | 88 | 33% (24-43) | -1.47 | -2.94 | -259 |  |
| 240-375 | 61 | 34% (24-47) | -1.97 | -3.95 | -241 |  |
| 375-390 | 35 | 43% (28-59) | +1.54 | -0.23 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 37% (23-53) | -1.17 | -2.57 | -98 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 65 | 35% (25-48) | -1.50 | -2.82 | -183 |  |
| > 0.2 | 63 | 40% (29-52) | +0.15 | -1.80 | -113 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 94 | 31% (22-41) | -1.65 | -3.49 | -328 |  |
| above VWAP | 123 | 42% (34-51) | -0.42 | -2.03 | -250 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 73 | 36% (26-47) | -0.33 | -1.67 | -122 |  |
| (0.132, 0.377] | 72 | 47% (36-59) | -0.61 | -2.34 | -169 |  |
| (0.377, 1.555] | 72 | 29% (20-41) | -1.92 | -3.99 | -288 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.127] | 72 | 42% (31-53) | +0.01 | -1.33 | -96 |  |
| (0.127, 0.418] | 71 | 41% (30-52) | -0.84 | -2.83 | -201 |  |
| (0.418, 2.453] | 72 | 29% (20-41) | -2.02 | -3.86 | -278 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.349] | 73 | 37% (27-48) | -1.43 | -3.38 | -247 |  |
| (-0.349, 0.364] | 72 | 44% (34-56) | +0.50 | -0.71 | -51 |  |
| (0.364, 2.726] | 72 | 31% (21-42) | -1.92 | -3.90 | -281 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0522] | 73 | 38% (28-50) | -1.28 | -2.80 | -204 |  |
| (0.0522, 0.123] | 72 | 39% (28-50) | -0.01 | -1.61 | -116 |  |
| (0.123, 0.678] | 72 | 35% (25-46) | -1.57 | -3.58 | -258 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 73 | 41% (31-53) | -0.09 | -1.26 | -92 |  |
| (0.211, 0.315] | 72 | 38% (27-49) | -1.10 | -2.99 | -215 |  |
| (0.315, 0.979] | 72 | 33% (24-45) | -1.68 | -3.77 | -271 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.356] | 73 | 38% (28-50) | -0.68 | -2.30 | -168 |  |
| (2.356, 3.61] | 72 | 46% (35-57) | +0.52 | -1.20 | -86 |  |
| (3.61, 18.762] | 72 | 28% (19-39) | -2.69 | -4.50 | -324 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 73 | 44% (33-55) | +0.20 | -0.57 | -41 |  |
| (0.0985, 0.15] | 72 | 40% (30-52) | -1.33 | -2.52 | -181 |  |
| (0.15, 0.392] | 72 | 28% (19-39) | -1.74 | -4.93 | -355 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.876] | 31 | 29% (16-47) | -2.62 | -3.50 | -108 |  |
| (-0.876, 0.474] | 30 | 50% (33-67) | -0.41 | -0.93 | -28 |  |
| (0.474, 5.305] | 30 | 53% (36-70) | -0.46 | -1.22 | -36 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.515] | 33 | 45% (30-62) | -0.67 | -1.30 | -43 |  |
| (0.515, 0.748] | 32 | 44% (28-61) | -1.56 | -2.34 | -75 |  |
| (0.748, 1.74] | 33 | 42% (27-59) | -1.66 | -2.48 | -82 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 33 | 45% (30-62) | -1.33 | -1.85 | -61 |  |
| (0.779, 1.206] | 32 | 41% (26-58) | -1.40 | -2.16 | -69 |  |
| (1.206, 5.866] | 33 | 45% (30-62) | -1.17 | -2.10 | -69 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.349] | 33 | 36% (22-53) | -1.41 | -1.99 | -66 |  |
| (0.349, 0.561] | 32 | 56% (39-72) | -0.51 | -1.29 | -41 | ▲ |
| (0.561, 1.659] | 33 | 39% (25-56) | -1.95 | -2.80 | -92 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.17%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 47%
- Exit mix: stop 101, trail_stop 83, time_stop 29, eod 4

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 73 | 34% | 29% | 33% |
| (0.0985, 0.15] | 72 | 51% | 43% | 4% |
| (0.15, 0.392] | 72 | 54% | 43% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
