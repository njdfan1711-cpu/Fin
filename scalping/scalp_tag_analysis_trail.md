# Scalp signal analysis (trail exits)

_151 tagged trades, 15 trading days (2026-10-01 to 2026-10-21). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 151 | 34% (27-42) | -0.95 | -3.10 | -468 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 22 | +4 | +0.20 | 129 | -472 | -3.66 | -4 |
| skip first 30 min | 1 | -6 | -6.31 | 150 | -461 | -3.08 | +6 |
| skip when SPY is down on the day | 58 | -254 | -4.39 | 93 | -213 | -2.29 | +254 |
| skip when SPY is below its VWAP | 60 | -273 | -4.55 | 91 | -195 | -2.14 | +273 |
| skip when SPY fell over the last 15 min | 59 | -180 | -3.05 | 92 | -288 | -3.13 | +180 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 38 | -180 | -4.73 | 113 | -288 | -2.55 | +180 |
| skip stock not beating SPY over 15 min | 22 | -60 | -2.71 | 129 | -408 | -3.16 | +60 |
| skip afternoon entries (2:00-3:45 PM) | 33 | -187 | -5.65 | 118 | -281 | -2.38 | +187 |
| skip volume spikes above 5x average | 27 | -137 | -5.06 | 124 | -331 | -2.67 | +137 |
| skip when the stop is inside normal noise (range > stop) | 4 | -2 | -0.40 | 147 | -466 | -3.17 | +2 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.55%) | 8 | -24 | -3.02 | 143 | -443 | -3.10 | +24 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 91 | -361 | -3.96 | 60 | -107 | -1.78 | +361 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 20 | 50% (30-70) | +0.07 | -2.52 | -50 |  |
| 60-240 | 65 | 29% (20-41) | -1.46 | -3.17 | -206 |  |
| 240-375 | 44 | 32% (20-47) | -2.44 | -4.91 | -216 |  |
| 375-390 | 22 | 36% (20-57) | +2.58 | +0.20 | +4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 32% (16-53) | -1.38 | -3.24 | -71 |  |
| -0.2 to 0 | 36 | 28% (16-44) | -2.38 | -5.09 | -183 |  |
| 0 to 0.2 | 43 | 33% (20-47) | -1.19 | -2.82 | -121 |  |
| > 0.2 | 50 | 40% (28-54) | +0.46 | -1.84 | -92 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 60 | 23% (14-35) | -2.03 | -4.55 | -273 |  |
| above VWAP | 91 | 41% (31-51) | -0.24 | -2.14 | -195 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 51 | 31% (20-45) | +0.01 | -1.66 | -85 |  |
| (0.132, 0.37] | 50 | 42% (29-56) | -1.19 | -3.30 | -165 |  |
| (0.37, 1.555] | 50 | 28% (17-42) | -1.70 | -4.37 | -218 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 50 | 32% (21-46) | -0.21 | -2.08 | -104 |  |
| (0.147, 0.404] | 50 | 38% (26-52) | -0.71 | -2.98 | -149 |  |
| (0.404, 1.192] | 50 | 32% (21-46) | -1.84 | -4.17 | -209 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.257] | 51 | 31% (20-45) | -1.47 | -3.95 | -202 |  |
| (-0.257, 0.364] | 50 | 48% (35-61) | +1.06 | -0.32 | -16 | ▲ |
| (0.364, 2.726] | 50 | 22% (13-35) | -2.45 | -4.99 | -250 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 51 | 35% (24-49) | -1.55 | -3.37 | -172 |  |
| (0.0521, 0.122] | 50 | 36% (24-50) | +0.42 | -1.51 | -76 |  |
| (0.122, 0.678] | 50 | 30% (19-44) | -1.72 | -4.41 | -220 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.197] | 51 | 45% (32-59) | +0.44 | -0.89 | -46 |  |
| (0.197, 0.307] | 50 | 28% (17-42) | -1.56 | -3.97 | -199 |  |
| (0.307, 0.875] | 50 | 28% (17-42) | -1.76 | -4.47 | -223 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.408] | 51 | 35% (24-49) | -0.89 | -3.02 | -154 |  |
| (2.408, 3.502] | 50 | 42% (29-56) | +0.87 | -1.14 | -57 |  |
| (3.502, 18.76] | 50 | 24% (14-37) | -2.85 | -5.12 | -256 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0946] | 51 | 43% (31-57) | +0.42 | -0.33 | -17 |  |
| (0.0946, 0.147] | 50 | 32% (21-46) | -1.77 | -3.25 | -163 |  |
| (0.147, 0.392] | 50 | 26% (16-40) | -1.54 | -5.76 | -288 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -1.439] | 9 | 44% (19-73) | -1.87 | -2.90 | -26 | few trades |
| (-1.439, 0.134] | 8 | 0% (0-32) | -4.78 | -5.29 | -42 | few trades |
| (0.134, 5.305] | 8 | 75% (41-93) | +1.28 | +0.80 | +6 | few trades |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.457] | 11 | 27% (10-57) | -2.66 | -3.37 | -37 |  |
| (0.457, 0.691] | 10 | 30% (11-60) | -2.87 | -3.69 | -37 |  |
| (0.691, 1.74] | 11 | 64% (35-85) | -0.59 | -1.34 | -15 | ▲ |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.261, 0.763] | 11 | 36% (15-65) | -1.90 | -2.39 | -26 |  |
| (0.763, 1.164] | 10 | 40% (17-69) | -1.99 | -2.88 | -29 |  |
| (1.164, 3.566] | 11 | 45% (21-72) | -2.14 | -3.05 | -34 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.302] | 11 | 9% (2-38) | -3.57 | -4.24 | -47 |  |
| (0.302, 0.495] | 10 | 60% (31-83) | -0.89 | -1.51 | -15 |  |
| (0.495, 0.815] | 11 | 55% (28-79) | -1.48 | -2.45 | -27 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.17%
- Reached +0.175% at some point: 42% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 71, trail_stop 56, time_stop 23, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0946] | 51 | 33% | 29% | 35% |
| (0.0946, 0.147] | 50 | 56% | 38% | 6% |
| (0.147, 0.392] | 50 | 52% | 44% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
