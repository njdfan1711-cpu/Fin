# Scalp signal analysis (fixed exits)

_158 tagged trades, 17 trading days (2026-10-01 to 2026-10-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 158 | 37% (30-44) | -0.29 | -2.36 | -374 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 23 | -21 | -0.92 | 135 | -352 | -2.61 | +21 |
| skip first 30 min | 1 | -6 | -6.31 | 157 | -367 | -2.34 | +6 |
| skip when SPY is down on the day | 62 | -145 | -2.34 | 96 | -228 | -2.38 | +145 |
| skip when SPY is below its VWAP | 65 | -190 | -2.93 | 93 | -183 | -1.97 | +190 |
| skip when SPY fell over the last 15 min | 61 | -148 | -2.42 | 97 | -226 | -2.33 | +148 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 39 | -167 | -4.28 | 119 | -207 | -1.74 | +167 |
| skip stock not beating SPY over 15 min | 25 | -22 | -0.90 | 133 | -351 | -2.64 | +22 |
| skip afternoon entries (2:00-3:45 PM) | 34 | -184 | -5.41 | 124 | -190 | -1.53 | +184 |
| skip volume spikes above 5x average | 28 | -134 | -4.79 | 130 | -240 | -1.84 | +134 |
| skip when the stop is inside normal noise (range > stop) | 6 | -11 | -1.76 | 152 | -363 | -2.39 | +11 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 10 | -21 | -2.12 | 148 | -352 | -2.38 | +21 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -305 | -3.32 | 66 | -68 | -1.03 | +305 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 22 | 59% (39-77) | +2.81 | +0.42 | +9 | ▲ |
| 60-240 | 67 | 34% (24-46) | -0.59 | -2.27 | -152 |  |
| 240-375 | 46 | 26% (16-40) | -2.17 | -4.56 | -210 |  |
| 375-390 | 23 | 43% (26-63) | +1.37 | -0.92 | -21 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 38 | 37% (23-53) | -0.44 | -3.03 | -115 |  |
| 0 to 0.2 | 45 | 36% (23-50) | +0.04 | -1.56 | -70 |  |
| > 0.2 | 51 | 35% (24-49) | -0.84 | -3.10 | -158 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 65 | 35% (25-48) | -0.56 | -2.93 | -190 |  |
| above VWAP | 93 | 38% (28-48) | -0.10 | -1.97 | -183 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 53 | 36% (24-49) | -0.24 | -1.84 | -98 |  |
| (0.126, 0.368] | 52 | 38% (26-52) | -0.45 | -2.42 | -126 |  |
| (0.368, 1.555] | 53 | 36% (24-49) | -0.18 | -2.83 | -150 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.146] | 53 | 38% (26-51) | -0.34 | -2.11 | -112 |  |
| (0.146, 0.405] | 52 | 42% (30-56) | +0.94 | -1.28 | -66 |  |
| (0.405, 1.281] | 52 | 31% (20-44) | -1.37 | -3.64 | -189 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.246] | 53 | 38% (26-51) | -0.10 | -2.52 | -134 |  |
| (-0.246, 0.399] | 52 | 44% (32-58) | +0.72 | -0.64 | -33 |  |
| (0.399, 2.726] | 53 | 28% (18-42) | -1.47 | -3.90 | -207 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0519] | 53 | 38% (26-51) | -0.60 | -2.36 | -125 |  |
| (0.0519, 0.122] | 52 | 44% (32-58) | +0.69 | -1.18 | -61 |  |
| (0.122, 0.678] | 53 | 28% (18-42) | -0.94 | -3.53 | -187 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.197] | 53 | 45% (33-59) | +0.18 | -1.11 | -59 |  |
| (0.197, 0.301] | 52 | 33% (22-46) | -0.41 | -2.70 | -140 |  |
| (0.301, 0.875] | 53 | 32% (21-45) | -0.64 | -3.29 | -174 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 53 | 34% (23-47) | -0.25 | -2.20 | -116 |  |
| (2.389, 3.475] | 52 | 48% (35-61) | +0.84 | -1.26 | -65 |  |
| (3.475, 18.76] | 53 | 28% (18-42) | -1.44 | -3.62 | -192 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0966] | 53 | 43% (31-57) | -0.04 | -0.83 | -44 |  |
| (0.0966, 0.147] | 52 | 33% (22-46) | -0.52 | -1.92 | -100 |  |
| (0.147, 0.392] | 53 | 34% (23-47) | -0.31 | -4.34 | -230 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -1.264] | 11 | 27% (10-57) | -2.04 | -3.07 | -34 |  |
| (-1.264, 0.0841] | 10 | 20% (6-51) | -1.85 | -2.34 | -23 |  |
| (0.0841, 5.305] | 11 | 55% (28-79) | +1.57 | +1.09 | +12 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.482] | 13 | 23% (8-50) | -2.64 | -3.37 | -44 |  |
| (0.482, 0.645] | 13 | 31% (13-58) | -1.39 | -2.06 | -27 |  |
| (0.645, 1.74] | 13 | 46% (23-71) | +0.86 | +0.05 | +1 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.769] | 13 | 38% (18-64) | +0.11 | -0.34 | -4 |  |
| (0.769, 1.15] | 13 | 38% (18-64) | -0.08 | -0.91 | -12 |  |
| (1.15, 3.566] | 13 | 23% (8-50) | -3.20 | -4.13 | -54 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.314] | 13 | 15% (4-42) | -2.66 | -3.31 | -43 |  |
| (0.314, 0.483] | 13 | 54% (29-77) | +0.47 | -0.08 | -1 |  |
| (0.483, 1.14] | 13 | 31% (13-58) | -0.98 | -1.98 | -26 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 53%
- Exit mix: stop 83, target 39, time_stop 35, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0966] | 53 | 38% | 15% | 45% |
| (0.0966, 0.147] | 52 | 60% | 29% | 12% |
| (0.147, 0.392] | 53 | 60% | 30% | 9% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
