# Scalp signal analysis (trail exits)

_180 tagged trades, 20 trading days (2026-10-01 to 2026-10-28). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 180 | 37% (30-44) | -0.81 | -2.72 | -490 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | +12 | +0.47 | 155 | -501 | -3.23 | -12 |
| skip first 30 min | 1 | -6 | -6.31 | 179 | -483 | -2.70 | +6 |
| skip when SPY is down on the day | 69 | -243 | -3.52 | 111 | -247 | -2.22 | +243 |
| skip when SPY is below its VWAP | 74 | -290 | -3.91 | 106 | -200 | -1.89 | +290 |
| skip when SPY fell over the last 15 min | 68 | -177 | -2.60 | 112 | -313 | -2.79 | +177 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 45 | -189 | -4.21 | 135 | -300 | -2.22 | +189 |
| skip stock not beating SPY over 15 min | 30 | -57 | -1.92 | 150 | -432 | -2.88 | +57 |
| skip afternoon entries (2:00-3:45 PM) | 37 | -202 | -5.45 | 143 | -288 | -2.01 | +202 |
| skip volume spikes above 5x average | 33 | -155 | -4.70 | 147 | -335 | -2.28 | +155 |
| skip when the stop is inside normal noise (range > stop) | 7 | -9 | -1.25 | 173 | -481 | -2.78 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.57%) | 15 | -56 | -3.76 | 165 | -433 | -2.63 | +56 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 100 | -362 | -3.62 | 80 | -128 | -1.60 | +362 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 25 | 56% (37-73) | +0.76 | -1.43 | -36 | ▲ |
| 60-240 | 81 | 33% (24-44) | -1.29 | -2.82 | -228 |  |
| 240-375 | 49 | 31% (20-45) | -2.56 | -4.85 | -237 |  |
| 375-390 | 25 | 40% (23-59) | +2.61 | +0.47 | +12 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 45 | 36% (23-50) | -1.44 | -3.79 | -171 |  |
| 0 to 0.2 | 53 | 34% (23-47) | -1.37 | -2.84 | -151 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 74 | 27% (18-38) | -1.77 | -3.91 | -290 |  |
| above VWAP | 106 | 43% (34-53) | -0.14 | -1.89 | -200 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 60 | 37% (26-49) | +0.18 | -1.30 | -78 |  |
| (0.129, 0.367] | 60 | 45% (33-58) | -0.74 | -2.57 | -154 |  |
| (0.367, 1.555] | 60 | 28% (19-41) | -1.86 | -4.29 | -257 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.149] | 60 | 38% (27-51) | +0.20 | -1.47 | -88 |  |
| (0.149, 0.41] | 59 | 42% (31-55) | -0.65 | -2.65 | -156 |  |
| (0.41, 1.281] | 60 | 30% (20-43) | -1.89 | -3.98 | -239 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.286] | 60 | 35% (24-48) | -1.25 | -3.50 | -210 |  |
| (-0.286, 0.371] | 60 | 47% (35-59) | +0.97 | -0.30 | -18 |  |
| (0.371, 2.726] | 60 | 28% (19-41) | -2.15 | -4.36 | -262 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 60 | 38% (27-51) | -1.12 | -2.79 | -168 |  |
| (0.052, 0.119] | 60 | 40% (29-53) | +0.40 | -1.14 | -69 |  |
| (0.119, 0.678] | 60 | 32% (21-44) | -1.71 | -4.22 | -253 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.201] | 60 | 45% (33-58) | +0.38 | -0.88 | -53 |  |
| (0.201, 0.303] | 60 | 38% (27-51) | -1.01 | -3.04 | -182 |  |
| (0.303, 0.875] | 60 | 27% (17-39) | -1.80 | -4.24 | -255 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.382] | 60 | 37% (26-49) | -0.66 | -2.49 | -149 |  |
| (2.382, 3.545] | 60 | 45% (33-58) | +0.84 | -1.07 | -64 |  |
| (3.545, 18.762] | 60 | 28% (19-41) | -2.60 | -4.60 | -276 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0962] | 60 | 47% (35-59) | +0.61 | -0.11 | -7 |  |
| (0.0962, 0.145] | 60 | 38% (27-51) | -1.17 | -2.45 | -147 |  |
| (0.145, 0.392] | 60 | 25% (16-37) | -1.88 | -5.59 | -336 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.564] | 18 | 28% (12-51) | -2.77 | -3.64 | -66 |  |
| (-0.564, 0.454] | 18 | 44% (25-66) | -0.65 | -1.20 | -22 |  |
| (0.454, 5.305] | 18 | 67% (44-84) | +0.84 | +0.17 | +3 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.473] | 21 | 43% (24-63) | -0.67 | -1.32 | -28 |  |
| (0.473, 0.619] | 20 | 40% (22-61) | -1.79 | -2.42 | -48 |  |
| (0.619, 1.74] | 20 | 55% (34-74) | -0.81 | -1.73 | -35 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 21 | 52% (32-72) | -0.47 | -0.88 | -19 |  |
| (0.789, 1.188] | 20 | 40% (22-61) | -1.31 | -2.15 | -43 |  |
| (1.188, 3.566] | 20 | 45% (26-66) | -1.51 | -2.46 | -49 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.316] | 21 | 33% (17-55) | -1.69 | -2.26 | -47 |  |
| (0.316, 0.527] | 20 | 65% (43-82) | +0.62 | -0.07 | -1 | ▲ |
| (0.527, 1.14] | 20 | 40% (22-61) | -2.15 | -3.10 | -62 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.16%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 81, trail_stop 68, time_stop 29, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0962] | 60 | 30% | 28% | 40% |
| (0.0962, 0.145] | 60 | 50% | 43% | 5% |
| (0.145, 0.392] | 60 | 55% | 42% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
