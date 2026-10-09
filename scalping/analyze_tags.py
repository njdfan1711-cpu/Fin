"""
analyze_tags.py -- judges candidate rules (see IDEAS.md) from the tagged
signals in scalp_signals_tagged.csv, WITHOUT changing the strategy.

Run from the scalping/ folder (the backtest workflow does this after each
backtest):  python analyze_tags.py [fixed|trail]     (default: fixed)
Writes scalp_tag_analysis.md (fixed) or scalp_tag_analysis_trail.md (trail).

Costs are re-computed from gross P&L with the measured spreads in
measured_spreads.csv (same rule as scalp_backtest.py: max(1c, price x median
spread %) per share, flat 2c fallback for symbols with no measurement).

Reading the results: a good rule removes mostly LOSERS; a bad rule removes
winners too. Every table is a hypothesis, not a finding -- many features are
tested, samples are small, and trades cluster in time and in a few symbols.
Do not retune thresholds from a handful of days.
"""
import csv
import math
import os
import sys
import warnings

warnings.filterwarnings("ignore")
import pandas as pd

TAGS_FILE = "scalp_signals_tagged.csv"
SPREADS_FILE = "measured_spreads.csv"
OUT_FILES = {"fixed": "scalp_tag_analysis.md", "trail": "scalp_tag_analysis_trail.md"}
FLAT_CENTS = 2.0
MIN_TICK = 0.01
TIGHT_PCT = 0.03
MIN_BUCKET = 10          # buckets smaller than this are labelled insufficient


def load_spreads() -> dict:
    t = {}
    if os.path.exists(SPREADS_FILE):
        with open(SPREADS_FILE, newline="") as f:
            for r in csv.DictReader(f):
                try:
                    t[r["symbol"].strip().upper()] = float(r["median_pct"])
                except (KeyError, ValueError):
                    pass
    return t


def wilson(w: int, n: int, z: float = 1.96):
    if n == 0:
        return 0.0, 0.0
    p = w / n
    den = 1 + z * z / n
    c = p + z * z / (2 * n)
    a = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - a) / den * 100, (c + a) / den * 100


def load(mode: str) -> pd.DataFrame:
    if not os.path.exists(TAGS_FILE):
        raise SystemExit(f"{TAGS_FILE} not found -- run scalp_backtest.py first.")
    df = pd.read_csv(TAGS_FILE)
    df = df[df["mode"] == mode].copy()
    if df.empty:
        raise SystemExit(f"No '{mode}' rows in {TAGS_FILE} yet.")
    spreads = load_spreads()
    pct = df["symbol"].map(spreads)
    cps = (df["entry_price"] * pct / 100).clip(lower=MIN_TICK)
    cps = cps.where(pct.notna(), FLAT_CENTS / 100)
    df["cost"] = df["shares"] * cps
    df["net"] = df["gross_pnl"] - df["cost"]
    df["win"] = df["net"] > 0
    df["spread_pct_used"] = pct
    df["date"] = df["entry_time"].str[:10]
    return df


def stats(d: pd.DataFrame) -> dict:
    n = len(d)
    w = int(d["win"].sum())
    lo, hi = wilson(w, n)
    return {"n": n, "win": 100 * w / n if n else 0, "lo": lo, "hi": hi,
            "gross": d["gross_pnl"].mean() if n else 0,
            "net": d["net"].mean() if n else 0, "total": d["net"].sum() if n else 0}


def row(label: str, d: pd.DataFrame, base: dict) -> str:
    s = stats(d)
    if s["n"] == 0:
        return f"| {label} | 0 | | | | | |"
    flag = ""
    if s["n"] < MIN_BUCKET:
        flag = "few trades"
    elif s["lo"] > base["win"]:
        flag = "▲"
    elif s["hi"] < base["win"]:
        flag = "▼"
    return (f"| {label} | {s['n']} | {s['win']:.0f}% ({s['lo']:.0f}-{s['hi']:.0f}) | "
            f"{s['gross']:+.2f} | {s['net']:+.2f} | {s['total']:+.0f} | {flag} |")


HEADER = ("| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |\n"
          "|---|--:|---|--:|--:|--:|---|")


def bucket_table(df, col, title, base, bins=None, labels=None):
    d = df[df[col].notna()].copy()
    if len(d) < MIN_BUCKET * 2:
        return f"### {title}\n_Not enough tagged trades with this value yet ({len(d)})._\n"
    if bins is not None:
        d["_b"] = pd.cut(d[col], bins=bins, labels=labels, right=False)
    else:
        try:
            d["_b"] = pd.qcut(d[col], 3, duplicates="drop")
        except ValueError:
            return f"### {title}\n_Values too similar to split._\n"
    lines = [f"### {title}", HEADER]
    for b, g in d.groupby("_b", observed=True):
        lines.append(row(str(b), g, base))
    return "\n".join(lines) + "\n"


def what_if(df, name, mask, base_total, base_n) -> str:
    removed, kept = df[mask], df[~mask]
    r_net = removed["net"].sum()
    return (f"| {name} | {len(removed)} | {r_net:+.0f} | "
            f"{removed['net'].mean() if len(removed) else 0:+.2f} | {len(kept)} | "
            f"{kept['net'].sum():+.0f} | {kept['net'].mean() if len(kept) else 0:+.2f} | "
            f"{kept['net'].sum() - base_total:+.0f} |")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "fixed"
    df = load(mode)
    base = stats(df)
    out = [f"# Scalp signal analysis ({mode} exits)\n",
           f"_{len(df)} tagged trades, {df['date'].nunique()} trading days "
           f"({df['date'].min()} to {df['date'].max()}). Costs: measured median spread "
           f"per symbol (flat {FLAT_CENTS:.0f}c fallback)._\n",
           "**Hypotheses, not findings.** Many features are tested on a small sample from "
           "a few days of one market regime, and trades cluster in time and in a few "
           "symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune "
           "thresholds from this yet.\n",
           "## Baseline", HEADER, row("all trades", df, base), ""]

    # --- what-if filters: judged by what the REMOVED trades earned ---
    out.append("## What-if filters (judged by what they would have removed)\n")
    out.append("A rule helps when the *removed* trades have a clearly negative "
               "average net and the total net of the kept trades improves.\n")
    out.append("| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |\n"
               "|---|--:|--:|--:|--:|--:|--:|--:|")
    t, n0 = df["net"].sum(), len(df)
    m = df["minutes_since_open"]
    out.append(what_if(df, "skip first 15 min and last 15 min", (m < 15) | (m >= 375), t, n0))
    out.append(what_if(df, "skip first 30 min", m < 30, t, n0))
    sp = df["spy_ret_open_pct"]
    out.append(what_if(df, "skip when SPY is down on the day", sp < 0, t, n0))
    out.append(what_if(df, "skip when SPY is below its VWAP", df["spy_vs_vwap_pct"] < 0, t, n0))
    out.append(what_if(df, "skip when SPY fell over the last 15 min", df["spy_ret_15m_pct"] < 0, t, n0))
    if df["ext30_pct"].notna().sum() >= 20:
        q = df["ext30_pct"].quantile(0.75)
        out.append(what_if(df, f"skip over-extended (30-min run in top quarter, > {q:.2f}%)",
                           df["ext30_pct"] > q, t, n0))
    out.append(what_if(df, "skip stock not beating SPY over 15 min", df["rs15_vs_spy_pct"] < 0, t, n0))
    out.append(what_if(df, f"trade only tight spreads (<= {TIGHT_PCT}%) -- unmeasured symbols kept",
                       df["spread_pct_used"] > TIGHT_PCT, t, n0))
    out.append("")

    # --- feature buckets ---
    out.append("## Results by market condition\n")
    out.append(bucket_table(df, "minutes_since_open", "Minutes since the open", base,
                            bins=[0, 15, 60, 240, 375, 391],
                            labels=["0-15", "15-60", "60-240", "240-375", "375-390"]))
    out.append(bucket_table(df, "spy_ret_open_pct", "SPY return since the open (%)", base,
                            bins=[-100, -0.2, 0, 0.2, 100],
                            labels=["< -0.2", "-0.2 to 0", "0 to 0.2", "> 0.2"]))
    out.append(bucket_table(df, "spy_vs_vwap_pct", "SPY vs its VWAP (%)", base,
                            bins=[-100, 0, 100], labels=["below VWAP", "above VWAP"]))
    out.append(bucket_table(df, "rs15_vs_spy_pct", "Stock minus SPY, last 15 min (%)", base))
    out.append(bucket_table(df, "ext30_pct", "Stock move over the last 30 min (%) -- how extended", base))
    out.append(bucket_table(df, "ext_from_open_pct", "Stock move since its day open (%)", base))
    out.append(bucket_table(df, "vwap_dist_pct", "Entry distance above VWAP (%)", base))
    out.append(bucket_table(df, "mom3_pct", "3-minute momentum at entry (%)", base))
    out.append(bucket_table(df, "volume_ratio", "Volume vs 20-minute average (x)", base))
    out.append(bucket_table(df, "range20_pct", "Recent volatility (avg 1-min range, % of price)", base))

    # --- exits: what price did the trades do after entry? ---
    d = df[df["max_up_pct"].notna() & df["max_down_pct"].notna()]
    if len(d) >= MIN_BUCKET:
        out.append("## Price path after entry (for tuning exits)\n")
        out.append(f"- Median best price reached: {d['max_up_pct'].median():+.2f}% | "
                   f"median worst: {d['max_down_pct'].median():+.2f}%")
        for lvl in (0.175, 0.35, 0.5, 0.75):
            out.append(f"- Reached +{lvl}% at some point: {100 * (d['max_up_pct'] >= lvl).mean():.0f}% of trades")
        out.append(f"- Fell to -0.20% or worse at some point: {100 * (d['max_down_pct'] <= -0.2).mean():.0f}%")
        out.append(f"- Exit mix: " + ", ".join(
            f"{k} {v}" for k, v in df['exit_reason'].value_counts().items()))
        v = df[df["range20_pct"].notna()].copy()
        if len(v) >= MIN_BUCKET * 2:
            try:
                v["_b"] = pd.qcut(v["range20_pct"], 3, duplicates="drop")
                out.append("\nStop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):\n")
                out.append("| volatility bucket | trades | stopped out | hit target / trail | timed out |\n|---|--:|--:|--:|--:|")
                for b, g in v.groupby("_b", observed=True):
                    er = g["exit_reason"]
                    out.append(f"| {b} | {len(g)} | {100 * (er == 'stop').mean():.0f}% | "
                               f"{100 * er.isin(['target', 'trail_stop']).mean():.0f}% | "
                               f"{100 * (er == 'time_stop').mean():.0f}% |")
            except ValueError:
                pass
        out.append("")

    out.append("_Limits: tags exist only for trades found since tagging began (yfinance keeps "
               "7 days of 1-minute bars). The backtest allows one position per symbol at a "
               "time, while the live bot will hold one position in total, so competing "
               "simultaneous signals are all counted here._")
    out_file = OUT_FILES.get(mode, f"scalp_tag_analysis_{mode}.md")
    with open(out_file, "w") as f:
        f.write("\n".join(out) + "\n")
    print(f"Wrote {out_file} ({len(df)} trades, mode={mode}).")


if __name__ == "__main__":
    main()
