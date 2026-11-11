"""
drop_check.py

Diagnoses a sharp one-day DROP on a ticker that Fin is about to push, and
labels it one of three ways instead of leaving the decision to you:

  STAY AWAY    -- a company-specific negative event was found (an offering
                  prospectus or bearish 8-K item filed on SEC EDGAR in the
                  last few days, or a bearish company headline in the last
                  48 hours). Stocks that fall on company news tend to keep
                  drifting, so the drop is treated as information.
  POSSIBLE DIP -- no bad news or filings found, the long-term trend is intact
                  (above the 200-day average), and EITHER the whole market is
                  selling off (SPY) OR the stock is closing in the upper half
                  of today's range (buyers stepping in).
  UNCLEAR      -- anything else, or a data source failed so "no bad news"
                  could not be confirmed. Wait.

DISPLAY-ONLY in this version: it adds a warning/label bullet to the push and
logs the inputs to DROP_LOG_FILE so the verdicts can be backtested later.
It never changes ranking. Every failure path returns None / "unclear" -- this
module must never be able to break the push.

Honest limits:
  * "No bad news found" is not proof there is none: EDGAR and Finnhub only
    cover what they cover.
  * Uses daily bars, so a premarket gap is invisible until the session opens.
  * Volume/candle checks use the in-progress bar when run mid-session.
"""

import json
import os
import sys
import urllib.request
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import pandas as pd
import yfinance as yf

from config import FINNHUB_API_KEY
from news_scan import classify_headline_sentiment

ET = ZoneInfo("America/New_York")

# ---- Tunables ---------------------------------------------------------------
DROP_ATR_MULT = 1.5          # trigger: down >= this many ATRs vs prior close ...
DROP_MIN_PCT = 5.0           # ... OR down >= this many percent
NEWS_LOOKBACK_DAYS = 2       # company-news window
FILING_LOOKBACK_DAYS = 3     # EDGAR window
SPY_DOWN_PCT = -1.0          # SPY down at least this much = "market selloff"
SPY_RELATIVE_BUFFER = 3.0    # stock must not be > this many pts worse than SPY
REBOUND_CLV = 0.5            # close location value: 0 = at low, 1 = at high
DROP_LOG_FILE = "drop_checks.jsonl"
HTTP_TIMEOUT = 20

# SEC requires a descriptive User-Agent with contact info. Set the
# SEC_USER_AGENT env var / workflow secret to e.g. "Fin Greg you@email.com".
SEC_USER_AGENT = os.environ.get("SEC_USER_AGENT") or "Fin stock screener contact@example.com"

# 424B4 / 424B5 = prospectus (supplement) for an underwritten or shelf offering.
OFFERING_FORMS = {"424B4", "424B5"}

# 8-K items that usually mean bad news. 5.02 can be a benign appointment, so
# it is worded as "check".
BEARISH_8K_ITEMS = {
    "1.03": "bankruptcy filing",
    "1.05": "cybersecurity incident",
    "2.05": "restructuring / exit costs",
    "2.06": "material impairment",
    "3.01": "delisting notice",
    "4.01": "auditor change",
    "4.02": "non-reliance on prior financials",
    "5.02": "executive/director change (check)",
}

_TICKER_TO_CIK = None   # cached per run
_SPY_PCT_CACHE = {}     # cached per run


# ---- Small helpers ----------------------------------------------------------
def _http_json(url: str, headers: dict | None = None):
    req = urllib.request.Request(url, headers=headers or {"User-Agent": "personal-stock-scanner"})
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _flatten(df: pd.DataFrame) -> pd.DataFrame:
    if isinstance(df.columns, pd.MultiIndex):
        df = df.copy()
        df.columns = df.columns.get_level_values(0)
    return df


def _download(symbol: str, period: str) -> pd.DataFrame | None:
    try:
        df = yf.download(tickers=symbol, period=period, interval="1d",
                         progress=False, timeout=HTTP_TIMEOUT)
        if df is None or df.empty:
            return None
        df = _flatten(df).dropna(subset=["Close"])
        return df if not df.empty else None
    except Exception as e:
        print(f"[drop_check] {symbol} download failed: {e}", file=sys.stderr)
        return None


# ---- Catalyst checks --------------------------------------------------------
def _cik_for(symbol: str) -> int | None:
    global _TICKER_TO_CIK
    if _TICKER_TO_CIK is None:
        data = _http_json("https://www.sec.gov/files/company_tickers.json",
                          {"User-Agent": SEC_USER_AGENT})
        _TICKER_TO_CIK = {row["ticker"].upper(): int(row["cik_str"]) for row in data.values()}
    return _TICKER_TO_CIK.get(symbol.upper())


def check_edgar(symbol: str) -> tuple[bool, list[str]]:
    """(check_succeeded, findings). Findings are short human-readable strings."""
    try:
        cik = _cik_for(symbol)
        if cik is None:
            return False, []
        sub = _http_json(f"https://data.sec.gov/submissions/CIK{cik:010d}.json",
                         {"User-Agent": SEC_USER_AGENT})
        recent = sub.get("filings", {}).get("recent", {})
        forms = recent.get("form", [])
        dates = recent.get("filingDate", [])
        items = recent.get("items", [])
        cutoff = (datetime.now(ET).date() - timedelta(days=FILING_LOOKBACK_DAYS)).isoformat()
        findings = []
        for i, form in enumerate(forms):
            filed = dates[i] if i < len(dates) else ""
            if filed < cutoff:
                continue
            if form in OFFERING_FORMS:
                findings.append(f"offering prospectus ({form}) filed {filed}")
            elif form in ("8-K", "8-K/A"):
                raw = items[i] if i < len(items) else ""
                for code in [c.strip() for c in raw.split(",") if c.strip()]:
                    if code in BEARISH_8K_ITEMS:
                        findings.append(f"8-K item {code}: {BEARISH_8K_ITEMS[code]} ({filed})")
        return True, findings
    except Exception as e:
        print(f"[drop_check] {symbol} EDGAR check failed: {e}", file=sys.stderr)
        return False, []


def check_company_news(symbol: str) -> tuple[bool, list[str]]:
    """(check_succeeded, bearish headlines) from Finnhub company news."""
    if not FINNHUB_API_KEY:
        return False, []
    try:
        today = datetime.now(ET).date()
        start = today - timedelta(days=NEWS_LOOKBACK_DAYS)
        url = (f"https://finnhub.io/api/v1/company-news?symbol={symbol}"
               f"&from={start.isoformat()}&to={today.isoformat()}&token={FINNHUB_API_KEY}")
        articles = _http_json(url)
        bearish = []
        for a in articles:
            headline = a.get("headline", "")
            if classify_headline_sentiment(headline) == "bearish":
                bearish.append(headline[:90])
        return True, bearish
    except Exception as e:
        print(f"[drop_check] {symbol} company-news check failed: {e}", file=sys.stderr)
        return False, []


# ---- Market / technical context ---------------------------------------------
def _spy_pct() -> float | None:
    if "v" in _SPY_PCT_CACHE:
        return _SPY_PCT_CACHE["v"]
    pct = None
    df = _download("SPY", "5d")
    if df is not None and len(df) >= 2:
        if pd.Timestamp(df.index[-1]).date() >= datetime.now(ET).date():
            last, prev = float(df["Close"].iloc[-1]), float(df["Close"].iloc[-2])
            pct = (last - prev) / prev * 100
    _SPY_PCT_CACHE["v"] = pct
    return pct


def read_bars(df: pd.DataFrame | None, price: float) -> dict:
    """above200 / rvol / clv from daily bars. Values are None when unknowable."""
    out = {"above200": None, "rvol": None, "clv": None}
    if df is None or df.empty:
        return out
    if len(df) >= 200:
        out["above200"] = bool(price > float(df["Close"].tail(200).mean()))
    session_today = pd.Timestamp(df.index[-1]).date() >= datetime.now(ET).date()
    if session_today:
        last = df.iloc[-1]
        hi, lo, close = float(last["High"]), float(last["Low"]), float(last["Close"])
        if hi > lo:
            out["clv"] = (close - lo) / (hi - lo)
        if len(df) >= 21 and "Volume" in df.columns:
            avg_vol = float(df["Volume"].iloc[-21:-1].mean())
            if avg_vol > 0:
                out["rvol"] = float(last["Volume"]) / avg_vol
    return out


# ---- Verdict (pure function, easy to test) ----------------------------------
def decide(day_pct, edgar_ok, edgar_hits, news_ok, news_hits,
           spy_pct, above200, clv) -> tuple[str, list[str]]:
    if edgar_hits or news_hits:
        reasons = list(edgar_hits[:2])
        if news_hits:
            reasons.append(f"bearish headline: {news_hits[0]}")
        return "stay_away", reasons

    if not (edgar_ok and news_ok):
        return "unclear", ["couldn't confirm there's no bad news or filings (data source failed)"]

    market_driven = (spy_pct is not None and spy_pct <= SPY_DOWN_PCT
                     and (day_pct - spy_pct) > -SPY_RELATIVE_BUFFER)
    rebound = clv is not None and clv >= REBOUND_CLV

    if above200 is True and (market_driven or rebound):
        reasons = ["no bad news or filings found"]
        if market_driven:
            reasons.append(f"market-wide selloff (SPY {spy_pct:+.1f}%)")
        if rebound:
            reasons.append("closing in upper half of today's range")
        reasons.append("above 200-day average")
        return "dip", reasons

    reasons = ["no bad news found, but"]
    if above200 is not True:
        reasons.append("trend broken or not enough history for 200-day check")
    if not market_driven:
        reasons.append("no market-wide selloff explaining it")
    if not rebound:
        reasons.append("no rebound yet" if clv is not None else "no session data for candle check")
    return "unclear", reasons


# ---- Logging for later backtests --------------------------------------------
def _already_logged(symbol: str, date_str: str) -> bool:
    if not os.path.exists(DROP_LOG_FILE):
        return False
    try:
        with open(DROP_LOG_FILE) as f:
            for line in f:
                if f'"symbol": "{symbol}"' in line and f'"date": "{date_str}"' in line:
                    return True
    except Exception:
        pass
    return False


def _log(record: dict):
    try:
        if _already_logged(record["symbol"], record["date"]):
            return
        with open(DROP_LOG_FILE, "a") as f:
            f.write(json.dumps(record) + "\n")
    except Exception as e:
        print(f"[drop_check] log write failed: {e}", file=sys.stderr)


# ---- Public API -------------------------------------------------------------
def assess_drop(symbol: str, price, atr, prev_close) -> dict | None:
    """Returns None unless the ticker is down sharply; never raises."""
    try:
        if not price or not atr or atr <= 0 or not prev_close:
            return None
        day_pct = (price - prev_close) / prev_close * 100
        day_atr = (price - prev_close) / atr
        if not (day_atr <= -DROP_ATR_MULT or day_pct <= -DROP_MIN_PCT):
            return None

        edgar_ok, edgar_hits = check_edgar(symbol)
        news_ok, news_hits = check_company_news(symbol)
        spy_pct = _spy_pct()
        bars = read_bars(_download(symbol, "1y"), price)

        verdict, reasons = decide(day_pct, edgar_ok, edgar_hits, news_ok, news_hits,
                                  spy_pct, bars["above200"], bars["clv"])
        info = {"symbol": symbol, "verdict": verdict, "reasons": reasons,
                "day_pct": round(day_pct, 2), "day_atr": round(day_atr, 2)}

        now = datetime.now(ET)
        _log({"date": now.date().isoformat(), "ts": now.isoformat(timespec="seconds"),
              "symbol": symbol, "price": round(float(price), 4), "day_pct": info["day_pct"],
              "day_atr": info["day_atr"], "verdict": verdict, "edgar_ok": edgar_ok,
              "edgar_hits": edgar_hits, "news_ok": news_ok, "news_hits": news_hits,
              "spy_pct": None if spy_pct is None else round(spy_pct, 2),
              "above200": bars["above200"], "rvol": bars["rvol"], "clv": bars["clv"]})
        return info
    except Exception as e:
        print(f"[drop_check] {symbol} assess failed: {e}", file=sys.stderr)
        return None


def _drop_parts(info: dict) -> tuple[str, str, str]:
    icon, label = {
        "stay_away": ("\u26D4", "Stay away"),
        "dip": ("\U0001F7E2", "Possible dip"),
    }.get(info["verdict"], ("\U0001F7E1", "Unclear, wait"))
    why = "; ".join(info["reasons"][:3])[:220]
    head = f"Sharp drop {info['day_pct']:+.1f}% today ({info['day_atr']:.1f} ATR) \u2014 {label}"
    return icon, head, why


def format_drop_caution(info: dict | None) -> str | None:
    """Push-message bullet (same two-space bullet style as the other cautions)."""
    if not info:
        return None
    icon, head, why = _drop_parts(info)
    return f"  \u2022 {icon} **{head}:** {why}"


def format_drop_md(info: dict | None) -> str | None:
    """latest_alerts.md list item (GitHub markdown wants '- ')."""
    if not info:
        return None
    icon, head, why = _drop_parts(info)
    return f"- {icon} **{head.upper()}**: {why}"
