# Fin swing-track scorecard
_Generated: 2026-11-25 UTC_  
_Window: 2026-08-19 to 2026-11-18 (66 push days). 2360 ticker-days (523 distinct tickers), from 17340 raw push records._

**How to read this.** One sample per ticker per day. Avg R is the headline (stop = -1R, full target = +2R, otherwise marked at the day-7 close). Win% is the share with R > 0, with a 95% Wilson interval. Anything under 30 samples is *insufficient data*. ▲/▼ means the win% interval excludes the baseline -- treat as a hypothesis, not a finding: with this many features tested, a few will look significant by chance, the sample is a few weeks of one market regime, and same-ticker repeats on consecutive days are correlated. Don't retune thresholds from this yet.

**Baseline (all):** n=2360, stop 35%, target 5%, avg R -0.11, win 42% (40-44%)

## Conviction
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `tier:STRONG` | 2332 | 520 | 35 | 5 | -0.10 | +0.00 | 42 (40-44) |  |
| `cats:2` | 1822 | 356 | 37 | 5 | -0.11 | -0.01 | 41 (39-44) |  |
| `cats:3` | 538 | 232 | 30 | 5 | -0.08 | +0.03 | 43 (39-47) |  |
| `tier:EXTENDED` | 28 | 20 | 39 | 0 | -0.29 | -0.18 | 32 (18-51) | insufficient data |

## Signal categories
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cat:news` | 538 | 232 | 30 | 5 | -0.08 | +0.03 | 43 (39-47) |  |

## Technical findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `tech:outperform_sp500` | 2162 | 449 | 36 | 5 | -0.11 | -0.01 | 41 (39-44) |  |
| `tech:above_rising_50_200ma` | 1740 | 301 | 35 | 5 | -0.09 | +0.02 | 43 (41-45) |  |
| `tech:rsi_overbought` | 1048 | 272 | 41 | 6 | -0.14 | -0.04 | 40 (37-43) |  |
| `tech:rs_line_new_high` | 773 | 202 | 38 | 5 | -0.12 | -0.01 | 41 (38-45) |  |
| `tech:all_time_high` | 463 | 111 | 37 | 2 | -0.15 | -0.04 | 41 (37-46) |  |
| `tech:52wk_high_below_ath` | 426 | 145 | 39 | 6 | -0.11 | -0.01 | 41 (37-46) |  |
| `tech:ma_20_50_cross` | 210 | 145 | 33 | 10 | -0.01 | +0.10 | 44 (38-51) |  |
| `tech:macd_bullish_cross` | 180 | 113 | 29 | 7 | -0.02 | +0.08 | 43 (36-51) |  |
| `tech:52wk_high_vol_confirmed` | 152 | 105 | 43 | 5 | -0.21 | -0.10 | 36 (29-44) |  |
| `tech:volume_spike` | 135 | 99 | 39 | 7 | -0.16 | -0.05 | 38 (30-46) |  |
| `tech:rsi_oversold` | 118 | 87 | 29 | 7 | -0.01 | +0.10 | 45 (36-54) |  |

## Fundamental findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `fund:eps_growth` | 1984 | 389 | 35 | 5 | -0.10 | +0.01 | 42 (40-44) |  |
| `fund:revenue_growth` | 1973 | 394 | 36 | 5 | -0.12 | -0.01 | 41 (39-44) |  |
| `fund:quality_passed` | 1650 | 278 | 36 | 6 | -0.09 | +0.02 | 43 (40-45) |  |
| `fund:analyst_improving` | 395 | 99 | 34 | 4 | -0.10 | +0.01 | 43 (38-47) |  |
| `fund:earnings_beat` | 132 | 90 | 32 | 12 | +0.03 | +0.14 | 45 (36-53) |  |

## Volatility (ATR % of price)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `atr:mid(3-4.5%)` | 1007 | 251 | 37 | 5 | -0.12 | -0.02 | 41 (38-44) |  |
| `atr:high(>=4.5%)` | 749 | 211 | 31 | 5 | -0.10 | +0.00 | 42 (39-46) |  |
| `atr:low(<3%)` | 604 | 183 | 37 | 6 | -0.08 | +0.02 | 43 (39-47) |  |

## Cautions
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `caut:high_on_light_volume` | 777 | 181 | 37 | 4 | -0.11 | -0.00 | 42 (39-46) |  |
| `caut:chase` | 343 | 145 | 42 | 5 | -0.14 | -0.03 | 40 (35-46) |  |
| `caut:extended_above_ma` | 328 | 100 | 46 | 5 | -0.29 | -0.18 | 32 (27-37) | ▼ |
| `caut:negative_net_margin` | 134 | 50 | 35 | 6 | -0.11 | -0.00 | 41 (33-50) |  |
| `caut:earnings_soon` | 106 | 61 | 53 | 21 | -0.02 | +0.09 | 39 (30-48) |  |
| `caut:analyst_deteriorating` | 99 | 42 | 32 | 1 | -0.20 | -0.10 | 34 (26-44) |  |
| `caut:earnings_today` | 74 | 69 | 47 | 14 | -0.09 | +0.01 | 35 (25-46) |  |
| `caut:rsi_overbought` | 9 | 6 | 44 | 0 | -0.48 | -0.37 | 22 (6-55) | insufficient data |
| `caut:news_caution` | 6 | 5 | 67 | 0 | -0.90 | -0.79 | 0 (0-39) | insufficient data |
| `caut:post_earnings` | 4 | 4 | 75 | 0 | -0.76 | -0.65 | 0 (0-49) | insufficient data |
| `caut:recent_ipo` | 2 | 2 | 100 | 0 | -1.00 | -0.89 | 0 (0-66) | insufficient data |

## Volume at 52-wk high (time-adjusted)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `volhi:low_adj(<0.8x)` | 187 | 95 | 40 | 5 | -0.21 | -0.10 | 35 (28-42) |  |
| `volhi:normal_adj(0.8-1.5x)` | 137 | 86 | 28 | 5 | -0.05 | +0.05 | 44 (36-52) |  |
| `volhi:high_adj(>=1.5x)` | 99 | 76 | 42 | 10 | -0.18 | -0.08 | 36 (28-46) |  |

## Push timing (ET)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `time:pre_open` | 864 | 272 | 37 | 4 | -0.11 | -0.00 | 43 (39-46) |  |
| `time:midday` | 721 | 329 | 32 | 5 | -0.13 | -0.02 | 41 (37-45) |  |
| `time:open_hour` | 538 | 274 | 36 | 7 | -0.06 | +0.05 | 42 (38-46) |  |
| `time:after_close` | 114 | 95 | 39 | 5 | -0.20 | -0.09 | 36 (28-45) |  |
| `time:late_session` | 86 | 71 | 33 | 5 | -0.12 | -0.01 | 43 (33-54) |  |

## Signal age / run-up since first push
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `age:recurring(2-4d)` | 480 | 162 | 35 | 5 | -0.13 | -0.03 | 40 (36-44) |  |
| `age:new(1d)` | 437 | 254 | 37 | 8 | -0.10 | +0.01 | 41 (36-45) |  |
| `runup:<2%` | 391 | 151 | 40 | 4 | -0.20 | -0.09 | 37 (33-42) |  |
| `age:stale(5d+)` | 215 | 46 | 53 | 1 | -0.40 | -0.30 | 34 (28-41) | ▼ |
| `runup:2-5%` | 185 | 74 | 34 | 6 | -0.09 | +0.02 | 45 (38-53) |  |
| `runup:>=5%` | 115 | 43 | 57 | 0 | -0.48 | -0.37 | 29 (21-38) | ▼ |

## Take-profit check (entries with path data)
- Take-profit touched before the stop: 849/1402 (61%, 95% CI 58-63%); stop first: 416 (30%)
- Median best price in window: +3.1% vs entry

## Shadow score check (raw strength vs extension-adjusted)
| Group | n | tickers | stop% | target% | avg R | win% (95% CI) |
|---|--:|--:|--:|--:|--:|---|
| All logged picks | 396 | 145 | 33 | 2 | -0.26 | 31 (27-36) |
| Top third by RAW strength | 132 | 58 | 30 | 2 | -0.22 | 33 (26-42) |
| Top third by ADJUSTED strength | 132 | 61 | 35 | 2 | -0.26 | 32 (24-40) |
| Picks with 0 extension flags | 368 | 139 | 33 | 2 | -0.26 | 31 (26-36) |
| Picks with 1+ extension flags | 28 | 20 | 39 | 0 | -0.29 | 32 (18-51) |
| Tier STRONG (new) | 368 | 139 | 33 | 2 | -0.26 | 31 (26-36) |
| Tier EXTENDED (new) | 28 | 20 | 39 | 0 | -0.29 | 32 (18-51) |


_51 distinct features tracked; always-present (hidden): cat:fundamentals, cat:technical. Raw push records without recoverable features are excluded._
