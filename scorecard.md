# Fin swing-track scorecard
_Generated: 2026-10-03 UTC_  
_Window: 2026-08-19 to 2026-09-25 (28 push days). 958 ticker-days (329 distinct tickers), from 5220 raw push records._

**How to read this.** One sample per ticker per day. Avg R is the headline (stop = -1R, full target = +2R, otherwise marked at the day-7 close). Win% is the share with R > 0, with a 95% Wilson interval. Anything under 30 samples is *insufficient data*. ▲/▼ means the win% interval excludes the baseline -- treat as a hypothesis, not a finding: with this many features tested, a few will look significant by chance, the sample is a few weeks of one market regime, and same-ticker repeats on consecutive days are correlated. Don't retune thresholds from this yet.

**Baseline (all):** n=958, stop 32%, target 5%, avg R -0.11, win 41% (38-44%)

## Conviction
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cats:2` | 484 | 136 | 34 | 4 | -0.11 | -0.00 | 41 (37-46) |  |
| `cats:3` | 474 | 222 | 31 | 5 | -0.10 | +0.00 | 41 (36-45) |  |

## Signal categories
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cat:news` | 474 | 222 | 31 | 5 | -0.10 | +0.00 | 41 (36-45) |  |

## Technical findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `tech:outperform_sp500` | 808 | 259 | 33 | 4 | -0.12 | -0.01 | 40 (37-44) |  |
| `tech:above_rising_50_200ma` | 665 | 179 | 30 | 5 | -0.07 | +0.03 | 43 (39-46) |  |
| `tech:rsi_overbought` | 415 | 141 | 38 | 4 | -0.19 | -0.09 | 37 (33-42) |  |
| `tech:rs_line_new_high` | 321 | 108 | 34 | 4 | -0.12 | -0.01 | 40 (35-46) |  |
| `tech:52wk_high_below_ath` | 209 | 80 | 37 | 6 | -0.13 | -0.03 | 40 (33-46) |  |
| `tech:all_time_high` | 149 | 54 | 29 | 1 | -0.08 | +0.03 | 43 (35-51) |  |
| `tech:rsi_oversold` | 86 | 65 | 28 | 8 | -0.02 | +0.09 | 43 (33-54) |  |
| `tech:macd_bullish_cross` | 69 | 48 | 36 | 7 | -0.10 | +0.00 | 42 (31-54) |  |
| `tech:52wk_high_vol_confirmed` | 42 | 34 | 45 | 2 | -0.31 | -0.20 | 29 (17-44) |  |
| `tech:volume_spike` | 38 | 31 | 32 | 8 | -0.14 | -0.03 | 37 (23-53) |  |
| `tech:ma_20_50_cross` | 20 | 18 | 40 | 5 | -0.24 | -0.13 | 40 (22-61) | insufficient data |

## Fundamental findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `fund:revenue_growth` | 731 | 232 | 32 | 5 | -0.09 | +0.02 | 42 (39-46) |  |
| `fund:eps_growth` | 679 | 215 | 31 | 5 | -0.07 | +0.03 | 43 (39-46) |  |
| `fund:quality_passed` | 520 | 150 | 33 | 5 | -0.08 | +0.02 | 41 (37-45) |  |
| `fund:analyst_improving` | 187 | 60 | 27 | 2 | -0.09 | +0.01 | 42 (35-49) |  |
| `fund:earnings_beat` | 50 | 30 | 26 | 6 | -0.05 | +0.06 | 44 (31-58) |  |

## Volatility (ATR % of price)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `atr:mid(3-4.5%)` | 406 | 150 | 37 | 5 | -0.16 | -0.05 | 36 (32-41) |  |
| `atr:high(>=4.5%)` | 309 | 127 | 24 | 5 | -0.05 | +0.06 | 47 (41-52) | ▲ |
| `atr:low(<3%)` | 243 | 97 | 34 | 5 | -0.09 | +0.02 | 41 (35-47) |  |

## Cautions
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `caut:high_on_light_volume` | 353 | 105 | 32 | 5 | -0.07 | +0.03 | 43 (38-48) |  |
| `caut:extended_above_ma` | 183 | 69 | 46 | 4 | -0.36 | -0.25 | 27 (21-34) | ▼ |
| `caut:negative_net_margin` | 112 | 43 | 31 | 6 | -0.04 | +0.06 | 45 (36-54) |  |
| `caut:analyst_deteriorating` | 53 | 30 | 38 | 2 | -0.40 | -0.30 | 23 (13-36) | ▼ |
| `caut:earnings_today` | 36 | 31 | 53 | 6 | -0.32 | -0.22 | 28 (16-44) |  |
| `caut:earnings_soon` | 27 | 18 | 59 | 7 | -0.40 | -0.29 | 22 (11-41) | insufficient data |
| `caut:news_caution` | 2 | 2 | 50 | 0 | -0.74 | -0.63 | 0 (0-66) | insufficient data |

## Take-profit check (entries with path data)
_0 entries so far -- insufficient data (need 30). Path data only exists for pushes resolved after it went live._

_32 distinct features tracked; always-present (hidden): cat:fundamentals, cat:technical, tier:STRONG. Raw push records without recoverable features are excluded._
