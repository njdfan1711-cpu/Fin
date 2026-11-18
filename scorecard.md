# Fin swing-track scorecard
_Generated: 2026-11-18 UTC_  
_Window: 2026-08-19 to 2026-11-11 (61 push days). 2190 ticker-days (503 distinct tickers), from 15740 raw push records._

**How to read this.** One sample per ticker per day. Avg R is the headline (stop = -1R, full target = +2R, otherwise marked at the day-7 close). Win% is the share with R > 0, with a 95% Wilson interval. Anything under 30 samples is *insufficient data*. ▲/▼ means the win% interval excludes the baseline -- treat as a hypothesis, not a finding: with this many features tested, a few will look significant by chance, the sample is a few weeks of one market regime, and same-ticker repeats on consecutive days are correlated. Don't retune thresholds from this yet.

**Baseline (all):** n=2190, stop 35%, target 6%, avg R -0.07, win 44% (41-46%)

## Conviction
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `tier:STRONG` | 2162 | 499 | 34 | 6 | -0.07 | +0.00 | 44 (42-46) |  |
| `cats:2` | 1653 | 336 | 36 | 6 | -0.07 | +0.00 | 44 (41-46) |  |
| `cats:3` | 537 | 232 | 30 | 5 | -0.08 | -0.00 | 43 (39-47) |  |
| `tier:EXTENDED` | 28 | 20 | 39 | 0 | -0.29 | -0.22 | 32 (18-51) | insufficient data |

## Signal categories
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cat:news` | 537 | 232 | 30 | 5 | -0.08 | -0.00 | 43 (39-47) |  |

## Technical findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `tech:outperform_sp500` | 1999 | 431 | 35 | 6 | -0.08 | -0.00 | 43 (41-46) |  |
| `tech:above_rising_50_200ma` | 1613 | 290 | 34 | 5 | -0.06 | +0.01 | 45 (42-47) |  |
| `tech:rsi_overbought` | 1048 | 272 | 41 | 6 | -0.14 | -0.07 | 40 (37-43) | ▼ |
| `tech:rs_line_new_high` | 759 | 197 | 38 | 5 | -0.10 | -0.03 | 42 (38-45) |  |
| `tech:all_time_high` | 451 | 107 | 37 | 2 | -0.13 | -0.06 | 42 (37-47) |  |
| `tech:52wk_high_below_ath` | 418 | 143 | 39 | 6 | -0.10 | -0.03 | 42 (37-47) |  |
| `tech:ma_20_50_cross` | 187 | 130 | 30 | 12 | +0.07 | +0.14 | 48 (41-55) |  |
| `tech:macd_bullish_cross` | 172 | 107 | 28 | 7 | -0.00 | +0.07 | 45 (38-52) |  |
| `tech:52wk_high_vol_confirmed` | 152 | 105 | 43 | 5 | -0.21 | -0.13 | 36 (29-44) |  |
| `tech:volume_spike` | 129 | 96 | 40 | 8 | -0.16 | -0.08 | 38 (30-47) |  |
| `tech:rsi_oversold` | 110 | 82 | 28 | 7 | +0.02 | +0.09 | 46 (37-56) |  |

## Fundamental findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `fund:eps_growth` | 1820 | 368 | 34 | 6 | -0.06 | +0.02 | 45 (42-47) |  |
| `fund:revenue_growth` | 1812 | 374 | 35 | 5 | -0.08 | -0.01 | 43 (41-46) |  |
| `fund:quality_passed` | 1518 | 265 | 35 | 6 | -0.05 | +0.03 | 45 (42-47) |  |
| `fund:analyst_improving` | 377 | 93 | 32 | 4 | -0.07 | +0.01 | 44 (39-49) |  |
| `fund:earnings_beat` | 132 | 90 | 32 | 12 | +0.03 | +0.11 | 45 (36-53) |  |

## Volatility (ATR % of price)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `atr:mid(3-4.5%)` | 936 | 246 | 36 | 5 | -0.09 | -0.01 | 43 (40-46) |  |
| `atr:high(>=4.5%)` | 667 | 190 | 31 | 6 | -0.07 | +0.01 | 45 (41-48) |  |
| `atr:low(<3%)` | 587 | 180 | 36 | 6 | -0.06 | +0.01 | 44 (40-48) |  |

## Cautions
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `caut:high_on_light_volume` | 757 | 175 | 36 | 4 | -0.09 | -0.02 | 43 (40-47) |  |
| `caut:chase` | 343 | 145 | 42 | 5 | -0.14 | -0.07 | 40 (35-46) |  |
| `caut:extended_above_ma` | 328 | 100 | 46 | 5 | -0.29 | -0.21 | 32 (27-37) | ▼ |
| `caut:negative_net_margin` | 134 | 50 | 35 | 6 | -0.11 | -0.03 | 41 (33-50) |  |
| `caut:earnings_soon` | 100 | 59 | 53 | 22 | +0.00 | +0.08 | 39 (30-49) |  |
| `caut:analyst_deteriorating` | 95 | 42 | 32 | 1 | -0.18 | -0.10 | 36 (27-46) |  |
| `caut:earnings_today` | 74 | 69 | 47 | 14 | -0.09 | -0.02 | 35 (25-46) |  |
| `caut:rsi_overbought` | 9 | 6 | 44 | 0 | -0.48 | -0.41 | 22 (6-55) | insufficient data |
| `caut:post_earnings` | 4 | 4 | 75 | 0 | -0.76 | -0.69 | 0 (0-49) | insufficient data |
| `caut:news_caution` | 3 | 3 | 67 | 0 | -0.83 | -0.75 | 0 (0-56) | insufficient data |
| `caut:recent_ipo` | 1 | 1 | 100 | 0 | -1.00 | -0.93 | 0 (0-79) | insufficient data |

## Volume at 52-wk high (time-adjusted)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `volhi:low_adj(<0.8x)` | 181 | 91 | 39 | 6 | -0.19 | -0.12 | 36 (29-43) | ▼ |
| `volhi:normal_adj(0.8-1.5x)` | 137 | 86 | 28 | 5 | -0.05 | +0.02 | 44 (36-52) |  |
| `volhi:high_adj(>=1.5x)` | 99 | 76 | 42 | 10 | -0.18 | -0.11 | 36 (28-46) |  |

## Push timing (ET)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `time:pre_open` | 765 | 249 | 35 | 4 | -0.05 | +0.02 | 46 (42-49) |  |
| `time:midday` | 702 | 323 | 32 | 6 | -0.12 | -0.04 | 42 (38-45) |  |
| `time:open_hour` | 494 | 256 | 35 | 7 | -0.01 | +0.06 | 45 (40-49) |  |
| `time:after_close` | 111 | 93 | 39 | 5 | -0.20 | -0.12 | 36 (28-45) |  |
| `time:late_session` | 81 | 66 | 30 | 5 | -0.08 | -0.00 | 44 (34-55) |  |

## Signal age / run-up since first push
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `age:recurring(2-4d)` | 378 | 142 | 32 | 6 | -0.02 | +0.05 | 46 (41-51) |  |
| `age:new(1d)` | 369 | 231 | 37 | 9 | -0.03 | +0.05 | 44 (39-50) |  |
| `runup:<2%` | 295 | 131 | 37 | 5 | -0.09 | -0.01 | 44 (39-50) |  |
| `age:stale(5d+)` | 215 | 46 | 53 | 1 | -0.40 | -0.33 | 34 (28-41) | ▼ |
| `runup:2-5%` | 179 | 72 | 33 | 6 | -0.07 | +0.01 | 46 (39-54) |  |
| `runup:>=5%` | 115 | 43 | 57 | 0 | -0.48 | -0.40 | 29 (21-38) | ▼ |

## Take-profit check (entries with path data)
- Take-profit touched before the stop: 789/1232 (64%, 95% CI 61-67%); stop first: 346 (28%)
- Median best price in window: +3.4% vs entry

## Shadow score check (raw strength vs extension-adjusted)
| Group | n | tickers | stop% | target% | avg R | win% (95% CI) |
|---|--:|--:|--:|--:|--:|---|
| All logged picks | 226 | 113 | 24 | 4 | -0.07 | 41 (35-48) |
| Top third by RAW strength | 75 | 42 | 27 | 3 | -0.10 | 37 (27-49) |
| Top third by ADJUSTED strength | 75 | 46 | 27 | 4 | -0.08 | 40 (30-51) |
| Picks with 0 extension flags | 198 | 103 | 22 | 4 | -0.04 | 42 (36-49) |
| Picks with 1+ extension flags | 28 | 20 | 39 | 0 | -0.29 | 32 (18-51) |
| Tier STRONG (new) | 198 | 103 | 22 | 4 | -0.04 | 42 (36-49) |
| Tier EXTENDED (new) | 28 | 20 | 39 | 0 | -0.29 | 32 (18-51) |


_51 distinct features tracked; always-present (hidden): cat:fundamentals, cat:technical. Raw push records without recoverable features are excluded._
