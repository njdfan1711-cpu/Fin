# Scalp signal analysis (trail exits)

_169 tagged trades, 19 trading days (2026-10-01 to 2026-10-27). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 169 | 36% (29-44) | -0.86 | -2.84 | -480 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | +12 | +0.47 | 144 | -491 | -3.41 | -12 |
| skip first 30 min | 1 | -6 | -6.31 | 168 | -473 | -2.82 | +6 |
| skip when SPY is down on the day | 63 | -254 | -4.03 | 106 | -226 | -2.13 | +254 |
| skip when SPY is below its VWAP | 71 | -287 | -4.04 | 98 | -193 | -1.97 | +287 |
| skip when SPY fell over the last 15 min | 65 | -176 | -2.71 | 104 | -304 | -2.92 | +176 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 42 | -185 | -4.40 | 127 | -295 | -2.32 | +185 |
| skip stock not beating SPY over 15 min | 28 | -48 | -1.70 | 141 | -432 | -3.06 | +48 |
| skip afternoon entries (2:00-3:45 PM) | 37 | -202 | -5.45 | 132 | -278 | -2.11 | +202 |
| skip volume spikes above 5x average | 31 | -146 | -4.70 | 138 | -334 | -2.42 | +146 |
| skip when the stop is inside normal noise (range > stop) | 7 | -9 | -1.25 | 162 | -471 | -2.91 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 13 | -43 | -3.27 | 156 | -437 | -2.80 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 95 | -362 | -3.81 | 74 | -118 | -1.60 | +362 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 24 | 54% (35-72) | +0.49 | -1.76 | -42 |  |
| 60-240 | 71 | 32% (23-44) | -1.36 | -2.98 | -212 |  |
| 240-375 | 49 | 31% (20-45) | -2.56 | -4.85 | -237 |  |
| 375-390 | 25 | 40% (23-59) | +2.61 | +0.47 | +12 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 39 | 31% (19-46) | -2.10 | -4.66 | -182 |  |
| 0 to 0.2 | 48 | 35% (23-50) | -1.15 | -2.70 | -130 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 71 | 27% (18-38) | -1.83 | -4.04 | -287 |  |
| above VWAP | 98 | 43% (34-53) | -0.15 | -1.97 | -193 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 57 | 37% (26-50) | +0.29 | -1.23 | -70 |  |
| (0.122, 0.368] | 56 | 45% (32-58) | -1.00 | -2.88 | -161 |  |
| (0.368, 1.555] | 56 | 27% (17-40) | -1.90 | -4.43 | -248 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 56 | 38% (26-51) | +0.11 | -1.59 | -89 |  |
| (0.147, 0.405] | 56 | 41% (29-54) | -0.66 | -2.75 | -154 |  |
| (0.405, 1.281] | 56 | 30% (20-43) | -1.94 | -4.11 | -230 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.25] | 57 | 33% (22-46) | -1.34 | -3.64 | -207 |  |
| (-0.25, 0.394] | 56 | 48% (36-61) | +0.93 | -0.38 | -21 |  |
| (0.394, 2.726] | 56 | 27% (17-40) | -2.16 | -4.48 | -251 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0518] | 57 | 37% (26-50) | -1.34 | -3.04 | -173 |  |
| (0.0518, 0.12] | 56 | 39% (28-52) | +0.42 | -1.33 | -75 |  |
| (0.12, 0.678] | 56 | 32% (21-45) | -1.65 | -4.14 | -232 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.2] | 57 | 44% (32-57) | +0.28 | -1.00 | -57 |  |
| (0.2, 0.301] | 56 | 39% (28-52) | -1.02 | -3.15 | -176 |  |
| (0.301, 0.875] | 56 | 25% (16-38) | -1.86 | -4.40 | -246 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.367] | 57 | 35% (24-48) | -0.86 | -2.72 | -155 |  |
| (2.367, 3.502] | 56 | 45% (32-58) | +0.87 | -1.13 | -63 |  |
| (3.502, 18.762] | 56 | 29% (18-41) | -2.59 | -4.67 | -262 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0966] | 57 | 46% (33-58) | +0.38 | -0.39 | -22 |  |
| (0.0966, 0.147] | 56 | 36% (24-49) | -1.39 | -2.72 | -152 |  |
| (0.147, 0.392] | 56 | 27% (17-40) | -1.59 | -5.46 | -306 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.911] | 15 | 33% (15-58) | -2.35 | -3.27 | -49 |  |
| (-0.911, 0.379] | 15 | 40% (20-64) | -1.51 | -1.99 | -30 |  |
| (0.379, 5.305] | 13 | 69% (42-87) | +0.90 | +0.36 | +5 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.484] | 17 | 41% (22-64) | -1.36 | -2.04 | -35 |  |
| (0.484, 0.607] | 16 | 44% (23-67) | -1.49 | -2.11 | -34 |  |
| (0.607, 1.74] | 17 | 53% (31-74) | -1.10 | -1.91 | -32 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 17 | 53% (31-74) | -0.65 | -1.05 | -18 |  |
| (0.779, 1.164] | 16 | 38% (18-61) | -1.95 | -2.74 | -44 |  |
| (1.164, 3.566] | 17 | 47% (26-69) | -1.39 | -2.30 | -39 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 17 | 29% (13-53) | -2.33 | -2.96 | -50 |  |
| (0.315, 0.521] | 16 | 62% (39-82) | +0.06 | -0.50 | -8 | ▲ |
| (0.521, 1.14] | 17 | 47% (26-69) | -1.59 | -2.50 | -42 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.16%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 77, trail_stop 65, time_stop 25, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0966] | 57 | 33% | 30% | 35% |
| (0.0966, 0.147] | 56 | 52% | 41% | 5% |
| (0.147, 0.392] | 56 | 52% | 45% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
