# Scalp signal analysis (trail exits)

_150 tagged trades, 15 trading days (2026-10-01 to 2026-10-21). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 150 | 33% (26-41) | -0.98 | -3.13 | -469 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 22 | +4 | +0.20 | 128 | -474 | -3.70 | -4 |
| skip first 30 min | 1 | -6 | -6.31 | 149 | -463 | -3.11 | +6 |
| skip when SPY is down on the day | 58 | -254 | -4.39 | 92 | -215 | -2.34 | +254 |
| skip when SPY is below its VWAP | 59 | -274 | -4.65 | 91 | -195 | -2.14 | +274 |
| skip when SPY fell over the last 15 min | 58 | -181 | -3.13 | 92 | -288 | -3.13 | +181 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 37 | -181 | -4.90 | 113 | -288 | -2.55 | +181 |
| skip stock not beating SPY over 15 min | 22 | -60 | -2.71 | 128 | -410 | -3.20 | +60 |
| skip afternoon entries (2:00-3:45 PM) | 32 | -188 | -5.88 | 118 | -281 | -2.38 | +188 |
| skip volume spikes above 5x average | 27 | -137 | -5.06 | 123 | -333 | -2.70 | +137 |
| skip when the stop is inside normal noise (range > stop) | 4 | -2 | -0.40 | 146 | -468 | -3.20 | +2 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 8 | -24 | -3.02 | 142 | -445 | -3.13 | +24 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 90 | -362 | -4.03 | 60 | -107 | -1.78 | +362 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 20 | 50% (30-70) | +0.07 | -2.52 | -50 |  |
| 60-240 | 65 | 29% (20-41) | -1.46 | -3.17 | -206 |  |
| 240-375 | 43 | 30% (19-45) | -2.56 | -5.06 | -217 |  |
| 375-390 | 22 | 36% (20-57) | +2.58 | +0.20 | +4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 32% (16-53) | -1.38 | -3.24 | -71 |  |
| -0.2 to 0 | 36 | 28% (16-44) | -2.38 | -5.09 | -183 |  |
| 0 to 0.2 | 42 | 31% (19-46) | -1.29 | -2.92 | -123 |  |
| > 0.2 | 50 | 40% (28-54) | +0.46 | -1.84 | -92 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 59 | 22% (13-34) | -2.12 | -4.65 | -274 |  |
| above VWAP | 91 | 41% (31-51) | -0.24 | -2.14 | -195 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 50 | 30% (19-44) | -0.02 | -1.71 | -85 |  |
| (0.129, 0.369] | 50 | 44% (31-58) | -1.04 | -3.06 | -153 |  |
| (0.369, 1.555] | 50 | 26% (16-40) | -1.88 | -4.62 | -231 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 50 | 32% (21-46) | -0.21 | -2.08 | -104 |  |
| (0.147, 0.403] | 49 | 37% (25-51) | -0.87 | -3.16 | -155 |  |
| (0.403, 1.192] | 50 | 32% (21-46) | -1.76 | -4.09 | -204 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.266] | 50 | 32% (21-46) | -1.47 | -4.00 | -200 |  |
| (-0.266, 0.364] | 50 | 46% (33-60) | +0.94 | -0.45 | -23 |  |
| (0.364, 2.726] | 50 | 22% (13-35) | -2.41 | -4.94 | -247 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 50 | 34% (22-48) | -1.60 | -3.44 | -172 |  |
| (0.052, 0.122] | 50 | 36% (24-50) | +0.38 | -1.54 | -77 |  |
| (0.122, 0.678] | 50 | 30% (19-44) | -1.72 | -4.41 | -220 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 50 | 44% (31-58) | +0.39 | -0.94 | -47 |  |
| (0.198, 0.309] | 50 | 28% (17-42) | -1.56 | -3.97 | -199 |  |
| (0.309, 0.875] | 50 | 28% (17-42) | -1.76 | -4.47 | -223 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.407] | 50 | 34% (22-48) | -0.95 | -3.12 | -156 |  |
| (2.407, 3.547] | 50 | 42% (29-56) | +0.86 | -1.14 | -57 |  |
| (3.547, 18.76] | 50 | 24% (14-37) | -2.85 | -5.12 | -256 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0946] | 51 | 43% (31-57) | +0.42 | -0.33 | -17 |  |
| (0.0946, 0.148] | 49 | 31% (20-45) | -1.87 | -3.35 | -164 |  |
| (0.148, 0.392] | 50 | 26% (16-40) | -1.54 | -5.76 | -288 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.612, -1.088] | 8 | 38% (14-69) | -2.48 | -3.46 | -28 | few trades |
| (-1.088, 0.281] | 8 | 0% (0-32) | -4.78 | -5.29 | -42 | few trades |
| (0.281, 5.305] | 8 | 75% (41-93) | +1.28 | +0.80 | +6 | few trades |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.449] | 11 | 27% (10-57) | -2.66 | -3.37 | -37 |  |
| (0.449, 0.736] | 10 | 20% (6-51) | -3.75 | -4.49 | -45 |  |
| (0.736, 1.74] | 10 | 70% (40-89) | -0.06 | -0.84 | -8 | ▲ |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.261, 0.757] | 11 | 36% (15-65) | -1.90 | -2.39 | -26 |  |
| (0.757, 1.136] | 10 | 40% (17-69) | -1.99 | -2.88 | -29 |  |
| (1.136, 3.566] | 10 | 40% (17-69) | -2.65 | -3.52 | -35 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.296] | 11 | 9% (2-38) | -3.57 | -4.24 | -47 |  |
| (0.296, 0.508] | 10 | 60% (31-83) | -0.99 | -1.62 | -16 |  |
| (0.508, 0.815] | 10 | 50% (24-76) | -1.81 | -2.74 | -27 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.17%
- Reached +0.175% at some point: 42% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 71, trail_stop 55, time_stop 23, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0946] | 51 | 33% | 29% | 35% |
| (0.0946, 0.148] | 49 | 57% | 37% | 6% |
| (0.148, 0.392] | 50 | 52% | 44% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
