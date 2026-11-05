# Scalp signal analysis (trail exits)

_232 tagged trades, 25 trading days (2026-10-01 to 2026-11-04). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 232 | 40% (34-47) | -0.73 | -2.38 | -551 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 40 | +2 | +0.06 | 192 | -553 | -2.88 | -2 |
| skip first 30 min | 2 | -3 | -1.70 | 230 | -548 | -2.38 | +3 |
| skip when SPY is down on the day | 89 | -281 | -3.16 | 143 | -270 | -1.89 | +281 |
| skip when SPY is below its VWAP | 99 | -330 | -3.33 | 133 | -221 | -1.66 | +330 |
| skip when SPY fell over the last 15 min | 85 | -189 | -2.22 | 147 | -362 | -2.46 | +189 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 58 | -228 | -3.93 | 174 | -323 | -1.86 | +228 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 195 | -470 | -2.41 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 49 | -221 | -4.52 | 183 | -330 | -1.80 | +221 |
| skip volume spikes above 5x average | 43 | -172 | -3.99 | 189 | -379 | -2.01 | +172 |
| skip when the stop is inside normal noise (range > stop) | 17 | -35 | -2.04 | 215 | -516 | -2.40 | +35 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.67%) | 28 | -60 | -2.16 | 204 | -491 | -2.41 | +60 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 115 | -410 | -3.57 | 117 | -141 | -1.20 | +410 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 93 | 37% (27-47) | -1.17 | -2.58 | -240 |  |
| 240-375 | 65 | 35% (25-48) | -1.93 | -3.84 | -249 |  |
| 375-390 | 40 | 48% (33-63) | +1.72 | +0.06 | +2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 37% (23-53) | -1.17 | -2.57 | -98 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 77 | 48% (37-59) | +0.68 | -1.03 | -79 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 99 | 32% (24-42) | -1.54 | -3.33 | -330 |  |
| above VWAP | 133 | 46% (38-54) | -0.12 | -1.66 | -221 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 78 | 37% (27-48) | -0.29 | -1.68 | -131 |  |
| (0.136, 0.377] | 77 | 52% (41-63) | -0.24 | -1.79 | -138 | ▲ |
| (0.377, 2.096] | 77 | 31% (22-42) | -1.66 | -3.67 | -282 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.108] | 77 | 47% (36-58) | +0.44 | -0.82 | -63 |  |
| (0.108, 0.418] | 76 | 41% (30-52) | -0.96 | -2.89 | -220 |  |
| (0.418, 2.453] | 77 | 32% (23-44) | -1.66 | -3.44 | -265 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.348] | 78 | 41% (31-52) | -1.11 | -2.97 | -232 |  |
| (-0.348, 0.401] | 77 | 48% (37-59) | +0.77 | -0.40 | -31 |  |
| (0.401, 4.204] | 77 | 31% (22-42) | -1.84 | -3.74 | -288 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0558] | 78 | 41% (31-52) | -1.00 | -2.45 | -191 |  |
| (0.0558, 0.124] | 77 | 43% (32-54) | +0.21 | -1.34 | -103 |  |
| (0.124, 0.924] | 77 | 36% (27-48) | -1.40 | -3.33 | -257 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.211] | 78 | 45% (34-56) | +0.27 | -0.85 | -67 |  |
| (0.211, 0.326] | 77 | 40% (30-51) | -1.03 | -2.82 | -217 |  |
| (0.326, 2.663] | 77 | 35% (25-46) | -1.45 | -3.47 | -267 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.337] | 78 | 41% (31-52) | -0.61 | -2.15 | -168 |  |
| (2.337, 3.632] | 77 | 47% (36-58) | +0.54 | -1.14 | -88 |  |
| (3.632, 18.762] | 77 | 32% (23-44) | -2.12 | -3.84 | -295 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0986] | 78 | 47% (37-58) | +0.38 | -0.36 | -28 |  |
| (0.0986, 0.15] | 77 | 42% (31-53) | -1.24 | -2.41 | -185 |  |
| (0.15, 0.392] | 77 | 31% (22-42) | -1.34 | -4.38 | -338 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.913] | 36 | 36% (22-52) | -2.05 | -2.89 | -104 |  |
| (-0.913, 0.452] | 35 | 54% (38-70) | +0.08 | -0.47 | -16 |  |
| (0.452, 5.599] | 35 | 57% (41-72) | +0.03 | -0.72 | -25 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.518] | 39 | 51% (36-66) | -0.20 | -0.82 | -32 |  |
| (0.518, 0.748] | 36 | 47% (32-63) | -1.36 | -2.12 | -76 |  |
| (0.748, 1.75] | 38 | 47% (32-63) | -0.86 | -1.68 | -64 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.8] | 38 | 47% (32-63) | -1.28 | -1.81 | -69 |  |
| (0.8, 1.235] | 37 | 49% (33-64) | -0.60 | -1.33 | -49 |  |
| (1.235, 5.866] | 38 | 50% (35-65) | -0.49 | -1.43 | -54 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.354] | 38 | 45% (30-60) | -0.70 | -1.27 | -48 |  |
| (0.354, 0.564] | 37 | 59% (43-74) | -0.34 | -1.08 | -40 | ▲ |
| (0.564, 2.726] | 38 | 42% (28-58) | -1.33 | -2.21 | -84 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.15%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 103, trail_stop 93, time_stop 29, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0986] | 78 | 32% | 31% | 31% |
| (0.0986, 0.15] | 77 | 51% | 44% | 4% |
| (0.15, 0.392] | 77 | 51% | 45% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
