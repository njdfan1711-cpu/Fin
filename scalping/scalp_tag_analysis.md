# Scalp signal analysis (fixed exits)

_114 tagged trades, 7 trading days (2026-10-01 to 2026-10-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 114 | 39% (31-49) | +0.29 | -1.64 | -187 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 37 | -8 | -0.22 | 77 | -179 | -2.32 | +8 |
| skip first 30 min | 27 | -4 | -0.16 | 87 | -182 | -2.10 | +4 |
| skip when SPY is down on the day | 35 | -26 | -0.74 | 79 | -161 | -2.04 | +26 |
| skip when SPY is below its VWAP | 36 | -76 | -2.12 | 78 | -110 | -1.42 | +76 |
| skip when SPY fell over the last 15 min | 36 | -54 | -1.49 | 78 | -133 | -1.71 | +54 |
| skip over-extended (30-min run in top quarter, > 0.45%) | 22 | -61 | -2.79 | 92 | -125 | -1.36 | +61 |
| skip stock not beating SPY over 15 min | 10 | -35 | -3.52 | 104 | -152 | -1.46 | +35 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 59 | -184 | -3.12 | 55 | -2 | -0.05 | +184 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 27 | 41% (25-59) | +0.91 | -0.16 | -4 |  |
| 15-60 | 12 | 58% (32-81) | +2.44 | -0.33 | -4 |  |
| 60-240 | 40 | 38% (24-53) | +0.11 | -1.47 | -59 |  |
| 240-375 | 25 | 28% (14-48) | -1.86 | -4.64 | -116 |  |
| 375-390 | 10 | 50% (24-76) | +2.11 | -0.38 | -4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 11 | 36% (15-65) | +0.01 | -1.82 | -20 |  |
| -0.2 to 0 | 24 | 50% (31-69) | +2.12 | -0.25 | -6 |  |
| 0 to 0.2 | 43 | 33% (20-47) | -0.48 | -1.88 | -81 |  |
| > 0.2 | 36 | 42% (27-58) | +0.07 | -2.23 | -80 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 36 | 39% (25-55) | +0.08 | -2.12 | -76 |  |
| above VWAP | 78 | 40% (30-51) | +0.38 | -1.42 | -110 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 29 | 38% (23-56) | -0.54 | -2.12 | -61 |  |
| (0.136, 0.374] | 29 | 45% (28-62) | +0.27 | -2.00 | -58 |  |
| (0.374, 1.123] | 29 | 34% (20-53) | +0.56 | -2.17 | -63 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.193] | 29 | 48% (31-66) | +0.87 | -0.71 | -20 |  |
| (0.193, 0.405] | 29 | 31% (17-49) | -0.51 | -2.93 | -85 |  |
| (0.405, 1.022] | 29 | 38% (23-56) | -0.07 | -2.65 | -77 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.089] | 38 | 42% (28-58) | +0.89 | -1.68 | -64 |  |
| (-0.089, 0.339] | 38 | 37% (23-53) | -0.16 | -1.46 | -56 |  |
| (0.339, 2.726] | 38 | 39% (26-55) | +0.13 | -1.78 | -68 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.0029, 0.0606] | 38 | 50% (35-65) | +1.45 | -0.21 | -8 |  |
| (0.0606, 0.141] | 38 | 37% (23-53) | -0.47 | -2.29 | -87 |  |
| (0.141, 0.786] | 38 | 32% (19-47) | -0.12 | -2.42 | -92 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.153, 0.22] | 38 | 50% (35-65) | +1.30 | +0.10 | +4 |  |
| (0.22, 0.422] | 38 | 34% (21-50) | -0.23 | -3.13 | -119 |  |
| (0.422, 3.871] | 38 | 34% (21-50) | -0.20 | -1.89 | -72 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.546] | 38 | 50% (35-65) | +1.75 | -0.37 | -14 |  |
| (2.546, 5.131] | 38 | 39% (26-55) | +0.03 | -1.91 | -73 |  |
| (5.131, 18.76] | 38 | 29% (17-45) | -0.92 | -2.63 | -100 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0951] | 38 | 50% (35-65) | +1.03 | +0.33 | +13 |  |
| (0.0951, 0.146] | 38 | 39% (26-55) | +0.68 | -0.62 | -24 |  |
| (0.146, 0.392] | 38 | 29% (17-45) | -0.85 | -4.63 | -176 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 29% of trades
- Reached +0.5% at some point: 10% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 56, target 33, time_stop 25

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0951] | 38 | 32% | 21% | 47% |
| (0.0951, 0.146] | 38 | 53% | 37% | 11% |
| (0.146, 0.392] | 38 | 63% | 29% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
