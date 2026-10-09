# Scalp signal analysis (fixed exits)

_105 tagged trades, 7 trading days (2026-10-01 to 2026-10-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 105 | 37% (29-47) | +0.04 | -1.91 | -200 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 37 | -8 | -0.22 | 68 | -192 | -2.83 | +8 |
| skip first 30 min | 27 | -4 | -0.16 | 78 | -196 | -2.51 | +4 |
| skip when SPY is down on the day | 32 | -34 | -1.06 | 73 | -167 | -2.28 | +34 |
| skip when SPY is below its VWAP | 33 | -77 | -2.35 | 72 | -123 | -1.71 | +77 |
| skip when SPY fell over the last 15 min | 29 | -48 | -1.67 | 76 | -152 | -2.00 | +48 |
| skip over-extended (30-min run in top quarter, > 0.45%) | 20 | -56 | -2.81 | 85 | -144 | -1.69 | +56 |
| skip stock not beating SPY over 15 min | 10 | -35 | -3.52 | 95 | -165 | -1.74 | +35 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 56 | -180 | -3.22 | 49 | -20 | -0.41 | +180 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 27 | 41% (25-59) | +0.91 | -0.16 | -4 |  |
| 15-60 | 11 | 64% (35-85) | +3.20 | +0.25 | +3 |  |
| 60-240 | 35 | 29% (16-45) | -0.89 | -2.57 | -90 |  |
| 240-375 | 22 | 27% (13-48) | -2.06 | -4.76 | -105 |  |
| 375-390 | 10 | 50% (24-76) | +2.11 | -0.38 | -4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 9 | 33% (12-65) | +0.01 | -2.10 | -19 | few trades |
| -0.2 to 0 | 23 | 48% (29-67) | +1.78 | -0.65 | -15 |  |
| 0 to 0.2 | 41 | 29% (18-44) | -0.90 | -2.33 | -95 |  |
| > 0.2 | 32 | 41% (26-58) | +0.01 | -2.22 | -71 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 33 | 36% (22-53) | -0.02 | -2.35 | -77 |  |
| above VWAP | 72 | 38% (27-49) | +0.07 | -1.71 | -123 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.131] | 26 | 35% (19-54) | -0.73 | -2.09 | -54 |  |
| (0.131, 0.371] | 26 | 35% (19-54) | -1.07 | -3.75 | -97 |  |
| (0.371, 1.123] | 26 | 38% (22-57) | +1.03 | -1.70 | -44 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.719, 0.193] | 26 | 46% (29-65) | +0.58 | -1.10 | -29 |  |
| (0.193, 0.408] | 26 | 23% (11-42) | -1.33 | -3.95 | -103 |  |
| (0.408, 1.022] | 26 | 38% (22-57) | -0.02 | -2.48 | -65 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-2.266, -0.0515] | 35 | 37% (23-54) | +0.14 | -2.59 | -91 |  |
| (-0.0515, 0.339] | 35 | 34% (21-51) | -0.39 | -1.74 | -61 |  |
| (0.339, 2.633] | 35 | 40% (26-56) | +0.38 | -1.39 | -49 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.0029, 0.0567] | 35 | 49% (33-64) | +1.20 | -0.50 | -18 |  |
| (0.0567, 0.142] | 35 | 29% (16-45) | -1.40 | -3.13 | -110 |  |
| (0.142, 0.786] | 35 | 34% (21-51) | +0.34 | -2.09 | -73 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.153, 0.218] | 35 | 46% (30-62) | +0.65 | -0.58 | -20 |  |
| (0.218, 0.441] | 35 | 29% (16-45) | -0.81 | -3.84 | -134 |  |
| (0.441, 3.871] | 35 | 37% (23-54) | +0.29 | -1.31 | -46 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0060000000000002, 2.577] | 35 | 46% (30-62) | +1.35 | -0.88 | -31 |  |
| (2.577, 5.213] | 35 | 34% (21-51) | -0.73 | -2.78 | -97 |  |
| (5.213, 18.76] | 35 | 31% (19-48) | -0.50 | -2.07 | -72 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0964] | 35 | 46% (30-62) | +0.67 | -0.03 | -1 |  |
| (0.0964, 0.149] | 35 | 34% (21-51) | -0.12 | -1.47 | -51 |  |
| (0.149, 0.392] | 35 | 31% (19-48) | -0.42 | -4.22 | -148 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 29% of trades
- Reached +0.5% at some point: 10% of trades
- Reached +0.75% at some point: 5% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 53, target 30, time_stop 22

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0964] | 35 | 34% | 23% | 43% |
| (0.0964, 0.149] | 35 | 57% | 31% | 11% |
| (0.149, 0.392] | 35 | 60% | 31% | 9% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
