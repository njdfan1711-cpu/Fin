# Scalp signal analysis (fixed exits)

_104 tagged trades, 7 trading days (2026-10-01 to 2026-10-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 104 | 38% (29-47) | +0.06 | -1.91 | -198 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 37 | -8 | -0.22 | 67 | -190 | -2.84 | +8 |
| skip first 30 min | 27 | -4 | -0.16 | 77 | -194 | -2.52 | +4 |
| skip when SPY is down on the day | 32 | -34 | -1.06 | 72 | -165 | -2.29 | +34 |
| skip when SPY is below its VWAP | 33 | -77 | -2.35 | 71 | -121 | -1.70 | +77 |
| skip when SPY fell over the last 15 min | 29 | -48 | -1.67 | 75 | -150 | -2.00 | +48 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 19 | -53 | -2.80 | 85 | -145 | -1.71 | +53 |
| skip stock not beating SPY over 15 min | 10 | -35 | -3.52 | 94 | -163 | -1.74 | +35 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 56 | -180 | -3.22 | 48 | -18 | -0.37 | +180 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 27 | 41% (25-59) | +0.91 | -0.16 | -4 |  |
| 15-60 | 11 | 64% (35-85) | +3.20 | +0.25 | +3 |  |
| 60-240 | 34 | 29% (17-46) | -0.86 | -2.59 | -88 |  |
| 240-375 | 22 | 27% (13-48) | -2.06 | -4.76 | -105 |  |
| 375-390 | 10 | 50% (24-76) | +2.11 | -0.38 | -4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 9 | 33% (12-65) | +0.01 | -2.10 | -19 | few trades |
| -0.2 to 0 | 23 | 48% (29-67) | +1.78 | -0.65 | -15 |  |
| 0 to 0.2 | 40 | 30% (18-45) | -0.87 | -2.34 | -94 |  |
| > 0.2 | 32 | 41% (26-58) | +0.01 | -2.22 | -71 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 33 | 36% (22-53) | -0.02 | -2.35 | -77 |  |
| above VWAP | 71 | 38% (28-50) | +0.10 | -1.70 | -121 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 26 | 35% (19-54) | -0.89 | -2.59 | -67 |  |
| (0.136, 0.372] | 25 | 36% (20-55) | -0.87 | -3.30 | -83 |  |
| (0.372, 1.123] | 26 | 38% (22-57) | +1.03 | -1.70 | -44 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.719, 0.189] | 26 | 46% (29-65) | +0.58 | -1.10 | -29 |  |
| (0.189, 0.41] | 25 | 24% (11-43) | -1.31 | -4.03 | -101 |  |
| (0.41, 1.022] | 26 | 38% (22-57) | -0.02 | -2.48 | -65 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-2.266, -0.0575] | 35 | 37% (23-54) | +0.14 | -2.59 | -91 |  |
| (-0.0575, 0.34] | 34 | 35% (21-52) | -0.34 | -1.74 | -59 |  |
| (0.34, 2.633] | 35 | 40% (26-56) | +0.38 | -1.39 | -49 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.0029, 0.0563] | 35 | 49% (33-64) | +1.20 | -0.50 | -18 |  |
| (0.0563, 0.142] | 34 | 29% (17-46) | -1.39 | -3.17 | -108 |  |
| (0.142, 0.786] | 35 | 34% (21-51) | +0.34 | -2.09 | -73 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.153, 0.215] | 35 | 46% (30-62) | +0.65 | -0.58 | -20 |  |
| (0.215, 0.441] | 34 | 29% (17-46) | -0.78 | -3.90 | -132 |  |
| (0.441, 3.871] | 35 | 37% (23-54) | +0.29 | -1.31 | -46 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0060000000000002, 2.562] | 35 | 46% (30-62) | +1.35 | -0.88 | -31 |  |
| (2.562, 5.133] | 34 | 35% (21-52) | -0.58 | -2.66 | -91 |  |
| (5.133, 18.76] | 35 | 31% (19-48) | -0.61 | -2.20 | -77 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0973] | 35 | 46% (30-62) | +0.57 | -0.15 | -5 |  |
| (0.0973, 0.151] | 34 | 35% (21-52) | +0.04 | -1.33 | -45 |  |
| (0.151, 0.392] | 35 | 31% (19-48) | -0.42 | -4.22 | -148 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 29% of trades
- Reached +0.5% at some point: 11% of trades
- Reached +0.75% at some point: 5% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 53, target 30, time_stop 21

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0973] | 35 | 37% | 23% | 40% |
| (0.0973, 0.151] | 34 | 56% | 32% | 12% |
| (0.151, 0.392] | 35 | 60% | 31% | 9% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
