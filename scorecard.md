# Fin swing-track scorecard
_Generated: 2026-11-11 UTC_  
_Window: 2026-08-19 to 2026-11-04 (56 push days). 1964 ticker-days (459 distinct tickers), from 14140 raw push records._

**How to read this.** One sample per ticker per day. Avg R is the headline (stop = -1R, full target = +2R, otherwise marked at the day-7 close). Win% is the share with R > 0, with a 95% Wilson interval. Anything under 30 samples is *insufficient data*. ▲/▼ means the win% interval excludes the baseline -- treat as a hypothesis, not a finding: with this many features tested, a few will look significant by chance, the sample is a few weeks of one market regime, and same-ticker repeats on consecutive days are correlated. Don't retune thresholds from this yet.

**Baseline (all):** n=1964, stop 36%, target 6%, avg R -0.08, win 44% (42-46%)

## Conviction
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cats:2` | 1430 | 286 | 38 | 6 | -0.07 | +0.00 | 44 (42-47) |  |
| `cats:3` | 534 | 230 | 30 | 5 | -0.08 | -0.00 | 43 (39-47) |  |

## Signal categories
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cat:news` | 534 | 230 | 30 | 5 | -0.08 | -0.00 | 43 (39-47) |  |

## Technical findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `tech:outperform_sp500` | 1785 | 388 | 36 | 6 | -0.08 | -0.00 | 44 (41-46) |  |
| `tech:above_rising_50_200ma` | 1467 | 263 | 35 | 6 | -0.05 | +0.02 | 46 (43-48) |  |
| `tech:rsi_overbought` | 1048 | 272 | 41 | 6 | -0.14 | -0.07 | 40 (37-43) | ▼ |
| `tech:rs_line_new_high` | 719 | 182 | 38 | 5 | -0.09 | -0.01 | 43 (39-46) |  |
| `tech:all_time_high` | 423 | 99 | 36 | 3 | -0.11 | -0.03 | 43 (39-48) |  |
| `tech:52wk_high_below_ath` | 396 | 132 | 39 | 7 | -0.09 | -0.02 | 42 (38-47) |  |
| `tech:ma_20_50_cross` | 152 | 108 | 36 | 12 | +0.05 | +0.13 | 48 (40-56) |  |
| `tech:macd_bullish_cross` | 145 | 88 | 30 | 8 | +0.00 | +0.08 | 46 (38-54) |  |
| `tech:52wk_high_vol_confirmed` | 138 | 95 | 44 | 6 | -0.20 | -0.12 | 37 (29-45) |  |
| `tech:volume_spike` | 106 | 80 | 41 | 8 | -0.16 | -0.09 | 38 (29-47) |  |
| `tech:rsi_oversold` | 103 | 76 | 27 | 8 | +0.03 | +0.10 | 47 (37-56) |  |

## Fundamental findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `fund:revenue_growth` | 1609 | 333 | 37 | 5 | -0.08 | -0.01 | 44 (42-47) |  |
| `fund:eps_growth` | 1601 | 327 | 36 | 6 | -0.06 | +0.02 | 45 (42-47) |  |
| `fund:quality_passed` | 1346 | 238 | 36 | 6 | -0.05 | +0.02 | 45 (42-47) |  |
| `fund:analyst_improving` | 362 | 87 | 32 | 4 | -0.07 | +0.01 | 44 (39-50) |  |
| `fund:earnings_beat` | 116 | 75 | 28 | 13 | +0.07 | +0.15 | 47 (38-56) |  |

## Volatility (ATR % of price)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `atr:mid(3-4.5%)` | 834 | 217 | 37 | 5 | -0.10 | -0.02 | 42 (39-46) |  |
| `atr:high(>=4.5%)` | 595 | 166 | 33 | 6 | -0.07 | +0.00 | 45 (41-49) |  |
| `atr:low(<3%)` | 535 | 166 | 36 | 7 | -0.04 | +0.04 | 45 (41-49) |  |

## Cautions
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `caut:high_on_light_volume` | 721 | 164 | 36 | 5 | -0.08 | -0.00 | 44 (41-48) |  |
| `caut:chase` | 332 | 140 | 42 | 5 | -0.14 | -0.07 | 40 (35-46) |  |
| `caut:extended_above_ma` | 327 | 99 | 46 | 5 | -0.29 | -0.21 | 32 (27-37) | ▼ |
| `caut:negative_net_margin` | 131 | 48 | 34 | 6 | -0.09 | -0.02 | 42 (34-51) |  |
| `caut:earnings_soon` | 92 | 56 | 54 | 22 | -0.04 | +0.03 | 37 (28-47) |  |
| `caut:analyst_deteriorating` | 90 | 40 | 32 | 1 | -0.20 | -0.12 | 33 (24-44) | ▼ |
| `caut:earnings_today` | 66 | 61 | 47 | 14 | -0.10 | -0.03 | 35 (24-47) |  |
| `caut:news_caution` | 2 | 2 | 50 | 0 | -0.74 | -0.66 | 0 (0-66) | insufficient data |

## Volume at 52-wk high (time-adjusted)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `volhi:low_adj(<0.8x)` | 174 | 86 | 39 | 6 | -0.17 | -0.10 | 37 (31-45) |  |
| `volhi:normal_adj(0.8-1.5x)` | 130 | 79 | 28 | 5 | -0.04 | +0.04 | 44 (36-52) |  |
| `volhi:high_adj(>=1.5x)` | 96 | 73 | 43 | 10 | -0.18 | -0.10 | 36 (28-46) |  |

## Push timing (ET)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `time:pre_open` | 667 | 217 | 38 | 5 | -0.06 | +0.02 | 47 (43-50) |  |
| `time:midday` | 664 | 302 | 33 | 6 | -0.11 | -0.04 | 42 (38-45) |  |
| `time:open_hour` | 419 | 218 | 36 | 8 | -0.02 | +0.06 | 45 (40-50) |  |
| `time:after_close` | 106 | 88 | 40 | 6 | -0.20 | -0.12 | 36 (27-45) |  |
| `time:late_session` | 71 | 59 | 25 | 6 | -0.01 | +0.07 | 46 (35-58) |  |

## Signal age / run-up since first push
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `age:recurring(2-4d)` | 269 | 110 | 39 | 8 | -0.02 | +0.06 | 48 (42-54) |  |
| `age:new(1d)` | 253 | 175 | 38 | 11 | +0.01 | +0.09 | 46 (40-52) |  |
| `runup:<2%` | 218 | 98 | 45 | 6 | -0.12 | -0.05 | 44 (38-51) |  |
| `age:stale(5d+)` | 214 | 45 | 54 | 1 | -0.41 | -0.33 | 34 (28-40) | ▼ |
| `runup:2-5%` | 149 | 59 | 36 | 7 | -0.05 | +0.02 | 49 (41-57) |  |
| `runup:>=5%` | 112 | 41 | 58 | 0 | -0.49 | -0.42 | 28 (20-37) | ▼ |

## Take-profit check (entries with path data)
- Take-profit touched before the stop: 658/1006 (65%, 95% CI 62-68%); stop first: 294 (29%)
- Median best price in window: +3.5% vs entry

## Shadow score check (raw strength vs extension-adjusted)
_0 picks so far with both scores logged -- insufficient data (need 90). Only picks pushed after the extension-adjusted ranking went live carry them._


_47 distinct features tracked; always-present (hidden): cat:fundamentals, cat:technical, tier:STRONG. Raw push records without recoverable features are excluded._
