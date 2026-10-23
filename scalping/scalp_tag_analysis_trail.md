# Scalp signal analysis (trail exits)

_152 tagged trades, 16 trading days (2026-10-01 to 2026-10-22). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 152 | 34% (27-42) | -0.91 | -3.04 | -462 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 23 | +10 | +0.43 | 129 | -472 | -3.66 | -10 |
| skip first 30 min | 1 | -6 | -6.31 | 151 | -456 | -3.02 | +6 |
| skip when SPY is down on the day | 59 | -249 | -4.22 | 93 | -213 | -2.29 | +249 |
| skip when SPY is below its VWAP | 61 | -267 | -4.38 | 91 | -195 | -2.14 | +267 |
| skip when SPY fell over the last 15 min | 59 | -180 | -3.05 | 93 | -282 | -3.04 | +180 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 38 | -180 | -4.73 | 114 | -283 | -2.48 | +180 |
| skip stock not beating SPY over 15 min | 23 | -54 | -2.35 | 129 | -408 | -3.16 | +54 |
| skip afternoon entries (2:00-3:45 PM) | 33 | -187 | -5.65 | 119 | -276 | -2.32 | +187 |
| skip volume spikes above 5x average | 27 | -137 | -5.06 | 125 | -325 | -2.60 | +137 |
| skip when the stop is inside normal noise (range > stop) | 4 | -2 | -0.40 | 148 | -461 | -3.11 | +2 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.55%) | 8 | -24 | -3.02 | 144 | -438 | -3.04 | +24 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 91 | -361 | -3.96 | 61 | -101 | -1.66 | +361 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 20 | 50% (30-70) | +0.07 | -2.52 | -50 |  |
| 60-240 | 65 | 29% (20-41) | -1.46 | -3.17 | -206 |  |
| 240-375 | 44 | 32% (20-47) | -2.44 | -4.91 | -216 |  |
| 375-390 | 23 | 39% (22-59) | +2.72 | +0.43 | +10 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 23 | 35% (19-55) | -1.06 | -2.86 | -66 |  |
| -0.2 to 0 | 36 | 28% (16-44) | -2.38 | -5.09 | -183 |  |
| 0 to 0.2 | 43 | 33% (20-47) | -1.19 | -2.82 | -121 |  |
| > 0.2 | 50 | 40% (28-54) | +0.46 | -1.84 | -92 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 61 | 25% (16-37) | -1.90 | -4.38 | -267 |  |
| above VWAP | 91 | 41% (31-51) | -0.24 | -2.14 | -195 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 51 | 31% (20-45) | +0.09 | -1.56 | -80 |  |
| (0.126, 0.369] | 50 | 44% (31-58) | -1.04 | -3.06 | -153 |  |
| (0.369, 1.555] | 51 | 27% (17-41) | -1.78 | -4.50 | -230 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.146] | 51 | 33% (22-47) | -0.09 | -1.93 | -98 |  |
| (0.146, 0.403] | 50 | 38% (26-52) | -0.71 | -2.98 | -149 |  |
| (0.403, 1.192] | 50 | 32% (21-46) | -1.84 | -4.17 | -209 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.254] | 51 | 31% (20-45) | -1.47 | -3.95 | -202 |  |
| (-0.254, 0.377] | 50 | 48% (35-61) | +1.06 | -0.32 | -16 | ▲ |
| (0.377, 2.726] | 51 | 24% (14-37) | -2.28 | -4.79 | -244 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0519] | 51 | 35% (24-49) | -1.45 | -3.27 | -167 |  |
| (0.0519, 0.122] | 50 | 38% (26-52) | +0.56 | -1.38 | -69 |  |
| (0.122, 0.678] | 51 | 29% (19-43) | -1.80 | -4.44 | -227 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.197] | 51 | 45% (32-59) | +0.44 | -0.89 | -46 |  |
| (0.197, 0.305] | 50 | 30% (19-44) | -1.49 | -3.85 | -193 |  |
| (0.305, 0.875] | 51 | 27% (17-41) | -1.68 | -4.39 | -224 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.405] | 51 | 35% (24-49) | -0.82 | -2.95 | -150 |  |
| (2.405, 3.475] | 50 | 42% (29-56) | -0.43 | -2.44 | -122 |  |
| (3.475, 18.76] | 51 | 25% (16-39) | -1.47 | -3.72 | -190 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.095] | 51 | 43% (31-57) | +0.42 | -0.33 | -17 |  |
| (0.095, 0.147] | 50 | 34% (22-48) | -1.54 | -3.02 | -151 |  |
| (0.147, 0.392] | 51 | 25% (16-39) | -1.62 | -5.77 | -294 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -1.264] | 9 | 44% (19-73) | -1.87 | -2.90 | -26 | few trades |
| (-1.264, 0.129] | 8 | 12% (2-47) | -3.34 | -3.86 | -31 | few trades |
| (0.129, 5.305] | 9 | 67% (35-88) | +0.52 | +0.04 | +0 | few trades |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.465] | 11 | 27% (10-57) | -2.66 | -3.37 | -37 |  |
| (0.465, 0.645] | 11 | 36% (15-65) | -2.07 | -2.86 | -31 |  |
| (0.645, 1.74] | 11 | 64% (35-85) | -0.59 | -1.34 | -15 | ▲ |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.261, 0.769] | 11 | 36% (15-65) | -1.90 | -2.39 | -26 |  |
| (0.769, 1.15] | 11 | 45% (21-72) | -1.27 | -2.12 | -23 |  |
| (1.15, 3.566] | 11 | 45% (21-72) | -2.14 | -3.05 | -34 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.307] | 11 | 9% (2-38) | -3.57 | -4.24 | -47 |  |
| (0.307, 0.483] | 11 | 64% (35-85) | -0.27 | -0.88 | -10 | ▲ |
| (0.483, 0.815] | 11 | 55% (28-79) | -1.48 | -2.45 | -27 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.17%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 47%
- Exit mix: stop 71, trail_stop 57, time_stop 23, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.095] | 51 | 33% | 29% | 35% |
| (0.095, 0.147] | 50 | 54% | 40% | 6% |
| (0.147, 0.392] | 51 | 53% | 43% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
