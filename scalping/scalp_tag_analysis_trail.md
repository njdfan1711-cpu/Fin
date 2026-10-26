# Scalp signal analysis (trail exits)

_160 tagged trades, 18 trading days (2026-10-01 to 2026-10-26). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 160 | 35% (28-43) | -0.93 | -2.99 | -478 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 24 | +13 | +0.52 | 136 | -490 | -3.61 | -13 |
| skip first 30 min | 1 | -6 | -6.31 | 159 | -471 | -2.97 | +6 |
| skip when SPY is down on the day | 62 | -254 | -4.09 | 98 | -224 | -2.29 | +254 |
| skip when SPY is below its VWAP | 66 | -276 | -4.18 | 94 | -202 | -2.14 | +276 |
| skip when SPY fell over the last 15 min | 63 | -169 | -2.68 | 97 | -309 | -3.19 | +169 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 40 | -187 | -4.66 | 120 | -291 | -2.43 | +187 |
| skip stock not beating SPY over 15 min | 26 | -52 | -2.02 | 134 | -425 | -3.17 | +52 |
| skip afternoon entries (2:00-3:45 PM) | 34 | -193 | -5.68 | 126 | -285 | -2.26 | +193 |
| skip volume spikes above 5x average | 28 | -143 | -5.10 | 132 | -335 | -2.54 | +143 |
| skip when the stop is inside normal noise (range > stop) | 6 | -9 | -1.42 | 154 | -469 | -3.05 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.55%) | 10 | -31 | -3.11 | 150 | -447 | -2.98 | +31 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -368 | -4.00 | 68 | -110 | -1.61 | +368 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 23 | 57% (37-74) | +0.47 | -1.83 | -42 | ▲ |
| 60-240 | 67 | 28% (19-40) | -1.59 | -3.27 | -219 |  |
| 240-375 | 46 | 30% (19-45) | -2.59 | -4.98 | -229 |  |
| 375-390 | 24 | 42% (24-61) | +2.74 | +0.52 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 38 | 32% (19-47) | -2.18 | -4.78 | -182 |  |
| 0 to 0.2 | 46 | 33% (21-47) | -1.30 | -2.88 | -132 |  |
| > 0.2 | 52 | 40% (28-54) | +0.46 | -1.76 | -92 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 66 | 27% (18-39) | -1.85 | -4.18 | -276 |  |
| above VWAP | 94 | 40% (31-51) | -0.29 | -2.14 | -202 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 54 | 33% (22-47) | +0.13 | -1.45 | -78 |  |
| (0.122, 0.368] | 53 | 43% (31-57) | -1.18 | -3.12 | -165 |  |
| (0.368, 1.555] | 53 | 28% (18-42) | -1.77 | -4.42 | -234 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.145] | 53 | 36% (24-49) | +0.05 | -1.69 | -90 |  |
| (0.145, 0.404] | 53 | 38% (26-51) | -0.82 | -3.01 | -160 |  |
| (0.404, 1.281] | 53 | 32% (21-45) | -1.94 | -4.19 | -222 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.239] | 54 | 31% (21-45) | -1.46 | -3.85 | -208 |  |
| (-0.239, 0.401] | 53 | 51% (38-64) | +1.08 | -0.26 | -14 | ▲ |
| (0.401, 2.726] | 53 | 23% (13-36) | -2.41 | -4.84 | -256 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 54 | 35% (24-49) | -1.57 | -3.32 | -179 |  |
| (0.0521, 0.122] | 53 | 38% (26-51) | +0.43 | -1.39 | -74 |  |
| (0.122, 0.678] | 53 | 32% (21-45) | -1.65 | -4.24 | -225 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 54 | 44% (32-58) | +0.35 | -0.95 | -52 |  |
| (0.198, 0.301] | 53 | 34% (23-47) | -1.42 | -3.65 | -193 |  |
| (0.301, 0.875] | 53 | 26% (16-40) | -1.75 | -4.40 | -233 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 54 | 35% (24-49) | -0.92 | -2.85 | -154 |  |
| (2.389, 3.421] | 53 | 43% (31-57) | -0.38 | -2.44 | -129 |  |
| (3.421, 18.76] | 53 | 26% (16-40) | -1.50 | -3.68 | -195 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0971] | 54 | 41% (29-54) | +0.07 | -0.72 | -39 |  |
| (0.0971, 0.147] | 53 | 38% (26-51) | -1.24 | -2.60 | -138 |  |
| (0.147, 0.392] | 53 | 26% (16-40) | -1.65 | -5.69 | -301 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.913] | 12 | 33% (14-61) | -2.86 | -3.83 | -46 |  |
| (-0.913, 0.134] | 11 | 27% (10-57) | -2.74 | -3.23 | -36 |  |
| (0.134, 5.305] | 11 | 73% (43-90) | +1.30 | +0.84 | +9 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.488] | 14 | 21% (8-48) | -2.92 | -3.68 | -52 |  |
| (0.488, 0.597] | 13 | 46% (23-71) | -1.50 | -2.03 | -26 |  |
| (0.597, 1.74] | 14 | 64% (39-84) | -0.66 | -1.50 | -21 | ▲ |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.763] | 14 | 43% (21-67) | -1.35 | -1.76 | -25 |  |
| (0.763, 1.164] | 13 | 46% (23-71) | -1.44 | -2.26 | -29 |  |
| (1.164, 3.566] | 14 | 43% (21-67) | -2.30 | -3.20 | -45 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 15 | 20% (7-45) | -3.22 | -3.85 | -58 |  |
| (0.315, 0.495] | 12 | 58% (32-81) | -0.30 | -0.83 | -10 |  |
| (0.495, 1.14] | 14 | 57% (33-79) | -1.27 | -2.23 | -31 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.17%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 75, trail_stop 61, time_stop 23, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0971] | 54 | 37% | 28% | 33% |
| (0.0971, 0.147] | 53 | 51% | 43% | 6% |
| (0.147, 0.392] | 53 | 53% | 43% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
