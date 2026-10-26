# Scalp signal analysis (trail exits)

_159 tagged trades, 17 trading days (2026-10-01 to 2026-10-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 159 | 35% (28-42) | -0.98 | -3.05 | -484 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 24 | +13 | +0.52 | 135 | -497 | -3.68 | -13 |
| skip first 30 min | 1 | -6 | -6.31 | 158 | -478 | -3.03 | +6 |
| skip when SPY is down on the day | 62 | -254 | -4.09 | 97 | -231 | -2.38 | +254 |
| skip when SPY is below its VWAP | 66 | -276 | -4.18 | 93 | -208 | -2.24 | +276 |
| skip when SPY fell over the last 15 min | 62 | -175 | -2.83 | 97 | -309 | -3.19 | +175 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 40 | -187 | -4.66 | 119 | -298 | -2.50 | +187 |
| skip stock not beating SPY over 15 min | 25 | -59 | -2.37 | 134 | -425 | -3.17 | +59 |
| skip afternoon entries (2:00-3:45 PM) | 34 | -193 | -5.68 | 125 | -291 | -2.33 | +193 |
| skip volume spikes above 5x average | 28 | -143 | -5.10 | 131 | -342 | -2.61 | +143 |
| skip when the stop is inside normal noise (range > stop) | 6 | -9 | -1.42 | 153 | -476 | -3.11 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.55%) | 10 | -31 | -3.11 | 149 | -453 | -3.04 | +31 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -368 | -4.00 | 67 | -116 | -1.74 | +368 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 22 | 55% (35-73) | +0.18 | -2.22 | -49 | ▲ |
| 60-240 | 67 | 28% (19-40) | -1.59 | -3.27 | -219 |  |
| 240-375 | 46 | 30% (19-45) | -2.59 | -4.98 | -229 |  |
| 375-390 | 24 | 42% (24-61) | +2.74 | +0.52 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 38 | 32% (19-47) | -2.18 | -4.78 | -182 |  |
| 0 to 0.2 | 46 | 33% (21-47) | -1.30 | -2.88 | -132 |  |
| > 0.2 | 51 | 39% (27-53) | +0.34 | -1.93 | -98 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 66 | 27% (18-39) | -1.85 | -4.18 | -276 |  |
| above VWAP | 93 | 40% (30-50) | -0.37 | -2.24 | -208 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 53 | 32% (21-45) | +0.00 | -1.60 | -85 |  |
| (0.129, 0.369] | 53 | 43% (31-57) | -1.18 | -3.12 | -165 |  |
| (0.369, 1.555] | 53 | 28% (18-42) | -1.77 | -4.42 | -234 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 53 | 34% (23-47) | -0.18 | -1.95 | -103 |  |
| (0.147, 0.404] | 52 | 38% (26-52) | -0.73 | -2.94 | -153 |  |
| (0.404, 1.281] | 53 | 32% (21-45) | -1.94 | -4.19 | -222 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.242] | 53 | 32% (21-45) | -1.44 | -3.86 | -205 |  |
| (-0.242, 0.41] | 53 | 49% (36-62) | +0.91 | -0.44 | -23 | ▲ |
| (0.41, 2.726] | 53 | 23% (13-36) | -2.41 | -4.84 | -256 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 53 | 34% (23-47) | -1.62 | -3.39 | -180 |  |
| (0.052, 0.122] | 53 | 38% (26-51) | +0.32 | -1.52 | -80 |  |
| (0.122, 0.678] | 53 | 32% (21-45) | -1.65 | -4.24 | -225 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 53 | 45% (33-59) | +0.33 | -0.96 | -51 |  |
| (0.198, 0.301] | 53 | 32% (21-45) | -1.52 | -3.78 | -200 |  |
| (0.301, 0.875] | 53 | 26% (16-40) | -1.75 | -4.40 | -233 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.382] | 53 | 34% (23-47) | -0.97 | -2.91 | -154 |  |
| (2.382, 3.448] | 53 | 43% (31-57) | -0.48 | -2.55 | -135 |  |
| (3.448, 18.76] | 53 | 26% (16-40) | -1.50 | -3.68 | -195 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0968] | 53 | 42% (29-55) | +0.18 | -0.60 | -32 |  |
| (0.0968, 0.147] | 53 | 36% (24-49) | -1.48 | -2.86 | -151 |  |
| (0.147, 0.392] | 53 | 26% (16-40) | -1.65 | -5.69 | -301 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -1.088] | 11 | 36% (15-65) | -2.61 | -3.64 | -40 |  |
| (-1.088, 0.125] | 11 | 27% (10-57) | -2.74 | -3.23 | -36 |  |
| (0.125, 5.305] | 11 | 64% (35-85) | +0.18 | -0.32 | -3 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.486] | 14 | 21% (8-48) | -2.92 | -3.68 | -52 |  |
| (0.486, 0.6] | 13 | 46% (23-71) | -1.87 | -2.49 | -32 |  |
| (0.6, 1.74] | 13 | 62% (36-82) | -0.86 | -1.67 | -22 | ▲ |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.775] | 14 | 43% (21-67) | -1.65 | -2.11 | -29 |  |
| (0.775, 1.178] | 13 | 46% (23-71) | -1.39 | -2.21 | -29 |  |
| (1.178, 3.566] | 13 | 38% (18-64) | -2.72 | -3.65 | -47 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 15 | 20% (7-45) | -3.22 | -3.85 | -58 |  |
| (0.315, 0.508] | 12 | 58% (32-81) | -0.71 | -1.35 | -16 |  |
| (0.508, 1.14] | 13 | 54% (29-77) | -1.51 | -2.44 | -32 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.17%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 75, trail_stop 60, time_stop 23, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0968] | 53 | 36% | 28% | 34% |
| (0.0968, 0.147] | 53 | 53% | 42% | 6% |
| (0.147, 0.392] | 53 | 53% | 43% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
