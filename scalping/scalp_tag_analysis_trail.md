# Scalp signal analysis (trail exits)

_158 tagged trades, 17 trading days (2026-10-01 to 2026-10-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 158 | 34% (27-42) | -1.01 | -3.08 | -487 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 23 | +10 | +0.43 | 135 | -497 | -3.68 | -10 |
| skip first 30 min | 1 | -6 | -6.31 | 157 | -481 | -3.06 | +6 |
| skip when SPY is down on the day | 62 | -254 | -4.09 | 96 | -233 | -2.43 | +254 |
| skip when SPY is below its VWAP | 65 | -279 | -4.29 | 93 | -208 | -2.24 | +279 |
| skip when SPY fell over the last 15 min | 61 | -178 | -2.92 | 97 | -309 | -3.19 | +178 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 39 | -186 | -4.78 | 119 | -301 | -2.53 | +186 |
| skip stock not beating SPY over 15 min | 25 | -59 | -2.37 | 133 | -428 | -3.22 | +59 |
| skip afternoon entries (2:00-3:45 PM) | 34 | -193 | -5.68 | 124 | -294 | -2.37 | +193 |
| skip volume spikes above 5x average | 28 | -143 | -5.10 | 130 | -344 | -2.65 | +143 |
| skip when the stop is inside normal noise (range > stop) | 6 | -9 | -1.42 | 152 | -479 | -3.15 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 10 | -31 | -3.11 | 148 | -456 | -3.08 | +31 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -368 | -4.00 | 66 | -119 | -1.80 | +368 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 22 | 55% (35-73) | +0.18 | -2.22 | -49 | ▲ |
| 60-240 | 67 | 28% (19-40) | -1.59 | -3.27 | -219 |  |
| 240-375 | 46 | 30% (19-45) | -2.59 | -4.98 | -229 |  |
| 375-390 | 23 | 39% (22-59) | +2.72 | +0.43 | +10 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 38 | 32% (19-47) | -2.18 | -4.78 | -182 |  |
| 0 to 0.2 | 45 | 31% (20-46) | -1.40 | -3.00 | -135 |  |
| > 0.2 | 51 | 39% (27-53) | +0.34 | -1.93 | -98 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 65 | 26% (17-38) | -1.93 | -4.29 | -279 |  |
| above VWAP | 93 | 40% (30-50) | -0.37 | -2.24 | -208 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 53 | 32% (21-45) | +0.00 | -1.60 | -85 |  |
| (0.126, 0.368] | 52 | 42% (30-56) | -1.22 | -3.19 | -166 |  |
| (0.368, 1.555] | 53 | 28% (18-42) | -1.81 | -4.46 | -236 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.146] | 53 | 34% (23-47) | -0.18 | -1.95 | -103 |  |
| (0.146, 0.405] | 52 | 38% (26-52) | -0.72 | -2.94 | -153 |  |
| (0.405, 1.281] | 52 | 31% (20-44) | -2.05 | -4.32 | -225 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.246] | 53 | 32% (21-45) | -1.44 | -3.86 | -205 |  |
| (-0.246, 0.399] | 52 | 48% (35-61) | +0.90 | -0.46 | -24 | ▲ |
| (0.399, 2.726] | 53 | 23% (13-36) | -2.44 | -4.88 | -259 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0519] | 53 | 34% (23-47) | -1.62 | -3.39 | -180 |  |
| (0.0519, 0.122] | 52 | 38% (26-52) | +0.45 | -1.42 | -74 |  |
| (0.122, 0.678] | 53 | 30% (20-44) | -1.82 | -4.41 | -234 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.197] | 53 | 45% (33-59) | +0.33 | -0.96 | -51 |  |
| (0.197, 0.301] | 52 | 31% (20-44) | -1.61 | -3.91 | -203 |  |
| (0.301, 0.875] | 53 | 26% (16-40) | -1.75 | -4.40 | -233 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 53 | 34% (23-47) | -1.00 | -2.95 | -156 |  |
| (2.389, 3.475] | 52 | 42% (30-56) | -0.51 | -2.61 | -136 |  |
| (3.475, 18.76] | 53 | 26% (16-40) | -1.50 | -3.68 | -195 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0966] | 53 | 42% (29-55) | +0.18 | -0.60 | -32 |  |
| (0.0966, 0.147] | 52 | 35% (23-48) | -1.57 | -2.96 | -154 |  |
| (0.147, 0.392] | 53 | 26% (16-40) | -1.65 | -5.69 | -301 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -1.264] | 11 | 36% (15-65) | -2.61 | -3.64 | -40 |  |
| (-1.264, 0.0841] | 10 | 30% (11-60) | -2.42 | -2.92 | -29 |  |
| (0.0841, 5.305] | 11 | 55% (28-79) | -0.65 | -1.13 | -12 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.482] | 13 | 23% (8-50) | -2.69 | -3.42 | -44 |  |
| (0.482, 0.645] | 13 | 38% (18-64) | -2.57 | -3.24 | -42 |  |
| (0.645, 1.74] | 13 | 62% (36-82) | -0.86 | -1.67 | -22 | ▲ |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.769] | 13 | 38% (18-64) | -1.97 | -2.41 | -31 |  |
| (0.769, 1.15] | 13 | 46% (23-71) | -1.44 | -2.26 | -29 |  |
| (1.15, 3.566] | 13 | 38% (18-64) | -2.72 | -3.65 | -47 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.314] | 13 | 15% (4-42) | -3.38 | -4.03 | -52 |  |
| (0.314, 0.483] | 13 | 54% (29-77) | -1.13 | -1.69 | -22 |  |
| (0.483, 1.14] | 13 | 54% (29-77) | -1.61 | -2.61 | -34 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.17%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 75, trail_stop 59, time_stop 23, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0966] | 53 | 36% | 28% | 34% |
| (0.0966, 0.147] | 52 | 54% | 40% | 6% |
| (0.147, 0.392] | 53 | 53% | 43% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
