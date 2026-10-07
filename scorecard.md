# Fin swing-track scorecard
_Generated: 2026-10-07 UTC_  
_Window: 2026-08-19 to 2026-09-30 (31 push days). 1055 ticker-days (341 distinct tickers), from 6240 raw push records._

**How to read this.** One sample per ticker per day. Avg R is the headline (stop = -1R, full target = +2R, otherwise marked at the day-7 close). Win% is the share with R > 0, with a 95% Wilson interval. Anything under 30 samples is *insufficient data*. ▲/▼ means the win% interval excludes the baseline -- treat as a hypothesis, not a finding: with this many features tested, a few will look significant by chance, the sample is a few weeks of one market regime, and same-ticker repeats on consecutive days are correlated. Don't retune thresholds from this yet.

**Baseline (all):** n=1055, stop 30%, target 5%, avg R -0.04, win 44% (41-47%)

## Conviction
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cats:2` | 565 | 148 | 31 | 5 | -0.01 | +0.04 | 46 (42-50) |  |
| `cats:3` | 490 | 225 | 30 | 5 | -0.09 | -0.04 | 42 (38-46) |  |

## Signal categories
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cat:news` | 490 | 225 | 30 | 5 | -0.09 | -0.04 | 42 (38-46) |  |

## Technical findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `tech:outperform_sp500` | 897 | 268 | 31 | 5 | -0.05 | -0.00 | 44 (41-47) |  |
| `tech:above_rising_50_200ma` | 749 | 190 | 28 | 5 | +0.00 | +0.05 | 46 (43-50) |  |
| `tech:rsi_overbought` | 449 | 145 | 37 | 4 | -0.15 | -0.10 | 40 (35-44) |  |
| `tech:rs_line_new_high` | 339 | 111 | 35 | 4 | -0.10 | -0.05 | 41 (36-47) |  |
| `tech:52wk_high_below_ath` | 220 | 84 | 38 | 6 | -0.12 | -0.07 | 40 (34-47) |  |
| `tech:all_time_high` | 157 | 56 | 29 | 1 | -0.06 | -0.02 | 44 (36-52) |  |
| `tech:rsi_oversold` | 93 | 69 | 28 | 9 | +0.00 | +0.05 | 45 (35-55) |  |
| `tech:macd_bullish_cross` | 72 | 50 | 35 | 7 | -0.10 | -0.05 | 42 (31-53) |  |
| `tech:52wk_high_vol_confirmed` | 47 | 36 | 49 | 2 | -0.36 | -0.31 | 28 (17-42) | ▼ |
| `tech:volume_spike` | 45 | 36 | 36 | 7 | -0.16 | -0.11 | 38 (25-52) |  |
| `tech:ma_20_50_cross` | 31 | 25 | 39 | 3 | -0.17 | -0.12 | 42 (26-59) |  |

## Fundamental findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `fund:revenue_growth` | 818 | 241 | 30 | 5 | -0.01 | +0.03 | 46 (43-50) |  |
| `fund:eps_growth` | 758 | 223 | 29 | 5 | +0.00 | +0.05 | 47 (43-50) |  |
| `fund:quality_passed` | 595 | 159 | 30 | 6 | +0.01 | +0.05 | 45 (41-49) |  |
| `fund:analyst_improving` | 215 | 63 | 23 | 2 | +0.01 | +0.05 | 47 (41-54) |  |
| `fund:earnings_beat` | 50 | 30 | 26 | 6 | -0.05 | -0.00 | 44 (31-58) |  |

## Volatility (ATR % of price)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `atr:mid(3-4.5%)` | 436 | 152 | 35 | 5 | -0.08 | -0.04 | 40 (36-45) |  |
| `atr:high(>=4.5%)` | 367 | 134 | 23 | 5 | +0.03 | +0.07 | 51 (46-56) | ▲ |
| `atr:low(<3%)` | 252 | 102 | 34 | 5 | -0.09 | -0.04 | 41 (35-47) |  |

## Cautions
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `caut:high_on_light_volume` | 370 | 109 | 32 | 5 | -0.05 | -0.00 | 44 (39-49) |  |
| `caut:extended_above_ma` | 206 | 71 | 43 | 3 | -0.28 | -0.23 | 32 (26-38) | ▼ |
| `caut:negative_net_margin` | 117 | 44 | 32 | 6 | -0.06 | -0.01 | 44 (35-53) |  |
| `caut:analyst_deteriorating` | 58 | 32 | 34 | 2 | -0.29 | -0.25 | 28 (18-40) | ▼ |
| `caut:earnings_today` | 37 | 32 | 51 | 5 | -0.32 | -0.28 | 27 (15-43) | ▼ |
| `caut:earnings_soon` | 29 | 18 | 55 | 7 | -0.37 | -0.33 | 24 (12-42) | insufficient data |
| `caut:news_caution` | 2 | 2 | 50 | 0 | -0.74 | -0.70 | 0 (0-66) | insufficient data |

## Volume at 52-wk high (time-adjusted)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `volhi:low_adj(<0.8x)` | 111 | 61 | 34 | 5 | -0.17 | -0.12 | 37 (29-46) |  |
| `volhi:normal_adj(0.8-1.5x)` | 104 | 58 | 28 | 6 | -0.04 | +0.01 | 43 (34-53) |  |
| `volhi:high_adj(>=1.5x)` | 70 | 47 | 44 | 9 | -0.22 | -0.18 | 36 (26-47) |  |

## Push timing (ET)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `time:midday` | 559 | 257 | 33 | 6 | -0.13 | -0.09 | 40 (36-45) |  |
| `time:pre_open` | 208 | 102 | 25 | 4 | +0.21 | +0.25 | 57 (50-64) | ▲ |
| `time:open_hour` | 149 | 107 | 26 | 3 | +0.00 | +0.05 | 46 (38-54) |  |
| `time:after_close` | 86 | 71 | 35 | 5 | -0.18 | -0.13 | 37 (28-48) |  |
| `time:late_session` | 53 | 45 | 30 | 8 | -0.04 | +0.01 | 40 (28-53) |  |

## Take-profit check (entries with path data)
- Take-profit touched before the stop: 84/97 (87%, 95% CI 78-92%); stop first: 7 (7%)
- Median best price in window: +7.6% vs entry

_40 distinct features tracked; always-present (hidden): cat:fundamentals, cat:technical, tier:STRONG. Raw push records without recoverable features are excluded._
