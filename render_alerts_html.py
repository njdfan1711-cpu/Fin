"""
render_alerts_html.py -- turns latest_alerts.md into latest_alerts.html.

The markdown file stays the single source of truth (compose_alerts.py writes
it exactly as before); this script only re-presents it. Any new bullet that
compose_alerts.py starts writing shows up automatically: unknown labels fall
back to a generic row, they are never dropped.

Standalone:   python render_alerts_html.py            (reads latest_alerts.md,
                                                        writes latest_alerts.html)
From code:    render_alerts_html.write_html(md_text, "latest_alerts.html")

Look and feel: ntfy-style notification cards (tier-colored stripe, warning
callouts) on the blue/white/gray palette and pill-and-rounded-card shapes used
in the Yarrow EHR and Survivor apps. Self-contained: no external fonts,
scripts or images, so it works from GitHub Pages or a downloaded file.
Light and dark mode follow the phone's setting.
"""
import html
import re
import sys

MD_PATH = "latest_alerts.md"
HTML_PATH = "latest_alerts.html"
EXPAND_TOP_N = 20          # cards this far down the ranking start expanded

# "Fresh" / "Extended" are display-only filters taken from the swing scorecard
# (scorecard.md): first-day alerts did best, alerts that had already run 5%+
# since their first push or were 5+ days old did worst, and the extended-above-
# MA and RSI-overbought cautions were the weakest tagged buckets. They use only
# data that exists for EVERY ticker (cautions, signals, streak tag) -- the
# price-based chase caution simply adds to it when a price check was made.
FRESH_MAX_DAY = 4                 # streak day at or below this still counts as young
EXTENDED_RUNUP_PCT = 5.0          # up this much since the first alert = already moved

_CARD_RE = re.compile(r"^## (\d+)\. (.+?)(?: -- \[([A-Z]+)\] (\d+) signals?, strength (-?[\d.]+)"
                      r"(?: \(raw (-?[\d.]+), (\d+) extension flags?\))?(?: \u00B7 (.+))?)?$")
_NAME_SYM_RE = re.compile(r"^(.*) \(([A-Z0-9.\-]+)\)$")
_BULLET_RE = re.compile(r"^- (\u26A0\uFE0F )?\*\*(.+?)\*\*: (.*)$")
# Sharp-drop diagnosis bullet written by compose_alerts.py (see drop_check.py). Its icon
# is not always the warning sign, so it needs its own pattern.
_DROP_RE = re.compile(r"^- (\u26A0\uFE0F|\u26D4|\U0001F7E2|\U0001F7E1) \*\*(SHARP DROP.+?)\*\*: (.*)$")
# "Score breakdown" bullet (compose_alerts.format_score_breakdown): categories split on " || ",
# findings on " ;; ", each finding ends with {+0.00}.
_PTS_RE = re.compile(r"^(.*) \{([+-]\d+\.\d\d)\}$")
_CAT_RE = re.compile(r"^(.+?) ([+-]\d+\.\d\d)(?: = (.*))?$")
_PENALTY_RE = re.compile(r"minus ([\d.]+) per extension flag")
_PLAN_RE = re.compile(
    r"entry \$([\d.,]+)-\$([\d.,]+), take-profit \$([\d.,]+) \(([+-][\d.]+)%\), "
    r"stop \$([\d.,]+), full target \$([\d.,]+) \(~(\d+) sh, ~\$([\d.,]+) at risk\)")


def _e(s) -> str:
    return html.escape(str(s), quote=True)


def parse_md(md_text: str) -> dict:
    """-> {"title", "run", "cards": [...], "spec_note", "spec": [...]}"""
    out = {"title": "Latest Alerts", "run": "", "cards": [], "spec_note": "", "spec": [], "v2": False, "penalty": 0.5}
    section = "main"
    cur = None
    for raw in md_text.splitlines():
        line = raw.rstrip()
        if not line:
            continue
        if line.startswith("# Latest Alerts"):
            out["title"] = line[2:]
            continue
        if line.startswith("# Speculative"):
            section = "spec"
            out["spec_title"] = line[2:]
            cur = None
            continue
        if line.startswith("_Run:"):
            out["run"] = line.strip("_").replace("Run:", "").strip()
            continue
        if line.startswith("_Scoring:"):
            out["v2"] = True      # new scoring: flags come from the "Extension flags" bullet
            pm_ = _PENALTY_RE.search(line)
            if pm_:
                out["penalty"] = float(pm_.group(1))
            continue
        if line.startswith("_") and line.endswith("_") and section == "spec" and cur is None:
            out["spec_note"] = line.strip("_")
            continue
        m = _CARD_RE.match(line)
        if line.startswith("## ") and m:
            rank, label, tier, count, strength, raw, _nflags, streak = m.groups()
            ns = _NAME_SYM_RE.match(label)
            name, sym = (ns.group(1), ns.group(2)) if ns else ("", label)
            cur = {"rank": int(rank), "name": name, "sym": sym, "tier": tier or "",
                   "count": count or "", "strength": strength or "", "raw": raw or "",
                   "streak": streak or "", "flags": [], "v2": out["v2"], "penalty": out["penalty"], "breakdown": {},
                   "signals": [], "warnings": [], "plan": None, "plan_raw": "",
                   "news": [], "other": [], "drops": []}
            (out["cards"] if section == "main" else out["spec"]).append(cur)
            continue
        if cur is None:
            continue
        d = _DROP_RE.match(line)
        if d:
            cur["drops"].append(d.groups())
            continue
        b = _BULLET_RE.match(line)
        if not b:
            # Speculative entries are plain "- detail" lines.
            if line.startswith("- "):
                cur["other"].append(("", line[2:]))
            continue
        warn, label, text = b.groups()
        up = label.upper()
        if up == "EXTENSION FLAGS":
            cur["flags"] = _split_items(text)
        elif up == "SCORE BREAKDOWN":
            cur["breakdown"] = _parse_breakdown(text)
        elif warn:
            cur["warnings"].append((label, text))
        elif up.startswith("TRADE PLAN"):
            cur["plan_raw"] = text
            pm = _PLAN_RE.search(text)
            if pm:
                cur["plan"] = pm.groups()
        elif up.startswith("NEWS") and "CONTEXT" in up:
            cur["news"].append(text)
        else:
            cur["signals"].append((label, text))
    return out


def _parse_breakdown(text: str) -> dict:
    """-> {"Fundamentals": (subtotal, [(detail, points) ...]), ...}; findings may be missing."""
    out = {}
    for block in text.split(" || "):
        m = _CAT_RE.match(block.strip())
        if not m:
            continue
        name, total, rest = m.group(1), m.group(2), m.group(3)
        items = []
        for it in (rest or "").split(" ;; "):
            pm = _PTS_RE.match(it.strip())
            if pm:
                items.append((pm.group(1), pm.group(2)))
        out[name] = (total, items)
    return out


def _score_tag(label: str, text: str, penalty: float) -> str:
    """Short note on how a warning bullet affects the score. Only the extension flags change
    the ranking (they subtract `penalty`); everything else is display-only."""
    up, t = label.upper(), text
    if up == "EARNINGS REACTION" and not t.lower().startswith("earnings scheduled"):
        return f"rank \u2212{penalty:.2f}"
    if up == "CAUTION" and (t.startswith("Extended") or t.startswith("up ") or "RSI overbought" in t):
        return f"rank \u2212{penalty:.2f}"
    return "not scored"


def _warning_severity(label: str, text: str) -> str:
    t = text.lower()
    if label.upper() == "CAUTION" and t.startswith("up "):
        return "alert"          # chase risk: the one that matters most at entry
    if t.startswith("earnings scheduled"):
        return "info"
    return "warn"


_STREAK_DAY_RE = re.compile(r"Day (\d+)(?: \(([+-][\d.]+)% since 1st alert\))?")


def card_status(c: dict) -> dict:
    """Derive Extended / Fresh from what the alert already says about the ticker.
    Returns {"extended": bool, "chase": bool, "fresh": bool, "why": [str]}.
    With the new scoring (c["v2"]) the alert itself lists its extension flags, so
    those are used as-is; the heuristics below only serve older markdown files."""
    if c.get("v2"):
        why = list(c["flags"])
        chase = any(w.startswith("chase risk") for w in why)
        return {"extended": bool(why), "chase": chase, "fresh": not why, "why": why}
    why, chase = [], False
    for label, text in c["warnings"]:
        up, t = label.upper(), text
        if up == "CAUTION" and t.startswith("Extended"):
            why.append("extended above 50-day MA")
        elif up == "CAUTION" and t.startswith("up "):
            why.append("chase risk (big move today)")
            chase = True
        elif up == "EARNINGS REACTION":
            why.append("just reported earnings")
    if any("RSI overbought" in t for _, t in c["signals"]):
        why.append("RSI overbought")
    streak, day, runup, young = c["streak"], None, None, True
    if streak:
        m = _STREAK_DAY_RE.search(streak)
        if m and "Back" not in streak:
            day = int(m.group(1))
            runup = float(m.group(2)) if m.group(2) else None
            young = day <= FRESH_MAX_DAY
        else:
            young = False       # "Back (was Day N)" = on-again/off-again, or unparseable
    if runup is not None and runup >= EXTENDED_RUNUP_PCT:
        why.append(f"already +{runup:.1f}% since first alert")
    extended = bool(why)
    return {"extended": extended, "chase": chase, "fresh": young and not extended, "why": why}


def _split_items(text: str) -> list:
    return [p.strip() for p in text.split("; ") if p.strip()]


def _warning_items(label: str, text: str) -> list:
    # Only the combined earnings-quality caution joins unrelated findings
    # with "; ". Every other warning is one sentence that may contain a
    # semicolon, so it must not be split.
    return _split_items(text) if label.upper() == "EARNINGS QUALITY" else [text]


def _render_card(c: dict, expand: bool) -> str:
    tier = c["tier"]
    tier_cls = {"STRONG": "strong", "MODERATE": "moderate", "EXTENDED": "extended"}.get(tier, "plain")
    warn_n = len(c["warnings"]) + len(c.get("drops", []))
    sev = [_warning_severity(l, t) for l, t in c["warnings"]]
    st = card_status(c)
    # Stripe = what the data says, not the tier: red chasing, amber extended,
    # green fresh, blue neutral.
    stripe = "alert" if st["chase"] else "warn" if st["extended"] else "fresh" if st["fresh"] else "neutral"
    has_plan = 1 if c["plan"] or c["plan_raw"] else 0

    chips = []
    if tier:
        chips.append(f'<span class="badge {tier_cls}">{_e(tier.title())}</span>')
    if c["streak"]:
        chips.append(f'<span class="chip">{_e(c["streak"])}</span>')
    if st["extended"] and tier != "EXTENDED":
        chips.append('<span class="chip extchip">Extended</span>')
    elif st["fresh"]:
        chips.append('<span class="chip freshchip">Fresh</span>')
    if warn_n:
        chips.append(f'<span class="chip warnchip">\u26A0\uFE0F {warn_n}</span>')
    if not has_plan:
        chips.append('<span class="chip nocheck" title="No live price fetched for this ticker, so no trade plan or chase check">No price check</span>')

    head = (f'<summary><span class="rank">{c["rank"]}</span>'
            f'<span class="who"><span class="sym">{_e(c["sym"])}</span>'
            f'<span class="nm">{_e(c["name"])}</span></span>'
            f'<span class="chips">{"".join(chips)}</span></summary>')

    body = []
    if c["count"]:
        raw_bit = f' (raw {_e(c["raw"])})' if c["raw"] else ""
        body.append(f'<div class="meta">{_e(c["count"])} signals \u00B7 strength {_e(c["strength"])}{raw_bit}</div>')
    if st["extended"]:
        body.append('<div class="why">Extended: ' + _e(" \u00B7 ".join(st["why"]))
                    + f' <span class="tag">each flag \u2212{c.get("penalty", 0.5):.2f} rank</span></div>')

    if c["signals"]:
        rows = []
        for label, text in c["signals"]:
            bd = c.get("breakdown", {}).get(label)
            if bd and bd[1]:
                # Points from compose_alerts: strongest finding first, each with what it adds.
                items = "".join(f'<li>{_e(d)}<span class="pts">{_e(p)}</span></li>' for d, p in bd[1])
            else:
                items = "".join(f"<li>{_e(i)}</li>" for i in _split_items(text))
            sub = f'<span class="subtot">{_e(bd[0])}</span>' if bd else ""
            rows.append(f'<div class="sec"><div class="sec-h">{_e(label)}{sub}</div><ul>{items}</ul></div>')
        body.append("".join(rows))

    # Context-only headlines (not scored) sit with the signals, ahead of the warnings.
    if c["news"]:
        news = "".join(f"<li>{_e(n)}</li>" for n in c["news"])
        body.append(f'<div class="sec news"><div class="sec-h">News (context, not scored)</div><ul>{news}</ul></div>')

    # Sharp-drop diagnosis (display-only): red = stay away, blue = possible dip, amber = unclear.
    for icon, label, text in c.get("drops", []):
        cls = "alert" if icon == "\u26D4" else "info" if icon == "\U0001F7E2" else "warn"
        body.append(f'<div class="callout {cls}"><div class="callout-h">{icon} {_e(label)}'
                    f'<span class="tag">not scored</span></div><div>{_e(text)}</div></div>')

    for (label, text), sv in zip(c["warnings"], sev):
        items = "".join(f"<div>{_e(i)}</div>" for i in _warning_items(label, text))
        tag = _score_tag(label, text, c.get("penalty", 0.5))
        body.append(f'<div class="callout {sv}"><div class="callout-h">\u26A0\uFE0F {_e(label.title())}'
                    f'<span class="tag">{_e(tag)}</span></div>{items}</div>')

    for label, text in c["other"]:
        body.append(f'<div class="sec"><div>{_e(text)}</div></div>')

    # The trade plan is ALWAYS the last thing on the card.
    if c["plan"]:
        lo, hi, tp, tp_pct, stop, target, sh, risk = c["plan"]
        cells = [("Entry", f"${lo}\u2013${hi}", ""), ("Take-profit", f"${tp}", f"{tp_pct}%"),
                 ("Stop", f"${stop}", ""), ("Full target", f"${target}", ""),
                 ("Size", f"~{sh} sh", ""), ("Risk", f"~${risk}", "")]
        parts = []
        for k, v, sub in cells:
            sub_html = '<span class="sub">' + _e(sub) + '</span>' if sub else ''
            parts.append('<div class="cell"><div class="cl">' + _e(k) + '</div><div class="cv">'
                         + _e(v) + sub_html + '</div></div>')
        grid = "".join(parts)
        body.append(f'<div class="plan"><div class="sec-h">Trade plan</div><div class="grid">{grid}</div></div>')
    elif c["plan_raw"]:
        body.append(f'<div class="plan"><div class="sec-h">Trade plan</div><div>{_e(c["plan_raw"])}</div></div>')

    search = f'{c["sym"]} {c["name"]}'.lower()
    return (f'<details class="card {stripe}" data-tier="{_e(tier)}" data-plan="{has_plan}" '
            f'data-warn="{warn_n}" data-fresh="{1 if st["fresh"] else 0}" data-ext="{1 if st["extended"] else 0}" '
            f'data-search="{_e(search)}"{" open" if expand else ""}>'
            f'{head}<div class="body">{"".join(body)}</div></details>')


# Stale-page guard (2026-11-12). The ntfy push links here with ?r=<run stamp>. The push goes out
# minutes before this page is committed AND GitHub Pages finishes deploying it (observed: Intraday run
# ~10 min, then a Pages deployment of 5+ min), so the first tap can land on the PREVIOUS run's page. If the
# page's own run is older than ?r=, show a banner and poll the tiny latest_run.json (cache-busted) every
# 20 s for up to 30 min; as soon as it reports the wanted run, reload the page once with a fresh URL.
# No ?r= (or an older one, e.g. tapping an old notification) -> does nothing.
_STALE_JS = """(function(){
var m=document.querySelector('meta[name="fin-run"]');if(!m)return;
var have=m.content,p=new URLSearchParams(location.search),want=p.get('r');
if(!want||want<=have)return;
var b=document.getElementById('fin-stale'),tries=0,MAX=90,n=parseInt(p.get('n')||'0',10);
var go=window.__finGo||function(u){location.replace(u);};
function fresh(){if(n>=5){b.textContent='Still showing the '+have+' run after several reloads. Tap here to try again.';n=0;return;}
p.set('n',String(n+1));p.set('t',String(Date.now()));go(location.pathname+'?'+p.toString()+location.hash);}
b.hidden=false;b.style.cursor='pointer';b.onclick=function(){n=0;fresh();};
b.textContent='Showing the '+have+' run. The '+want+' run is still being published (GitHub Pages can take 5\\u201315 min). Checking automatically \\u2013 tap here to retry now.';
function poll(){
if(tries>=MAX){b.textContent='Still showing the '+have+' run; the '+want+' run has not appeared yet. Tap here to retry.';return;}
tries++;
fetch('latest_run.json?t='+Date.now(),{cache:'no-store'}).then(function(r){return r.ok?r.json():null;}).then(function(j){
if(j&&j.run&&j.run>=want){fresh();}else{setTimeout(poll,20000);}
}).catch(function(){setTimeout(poll,20000);});
}
setTimeout(poll,8000);
})();"""

_CSS = """
:root{--bg:#f3f5f9;--card:#fff;--ink:#0f1b2d;--muted:#5b6778;--line:#dfe5ee;--blue:#1f5fbf;--blue-soft:#e8f0fd;
--green:#138a4b;--green-soft:#e4f6ec;--red:#c8372d;--red-soft:#fdecea;--amber:#9a6200;--amber-soft:#fff4dc;--shadow:0 1px 2px rgba(15,27,45,.06)}
@media (prefers-color-scheme:dark){:root{--bg:#0b1220;--card:#141d2e;--ink:#e8eefb;--muted:#93a1b8;--line:#25324a;--blue:#6ea3ff;--blue-soft:#18284a;
--green:#4cc785;--green-soft:#12301f;--red:#ff7b70;--red-soft:#3a1816;--amber:#f2b657;--amber-soft:#3a2c10;--shadow:none}}
*{box-sizing:border-box}html{color-scheme:light dark}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:760px;margin:0 auto;padding:0 12px 48px}
header.top{position:sticky;top:0;z-index:5;background:var(--bg);padding:12px 0 8px;border-bottom:1px solid var(--line)}
h1{font-size:20px;margin:0 0 2px;letter-spacing:-.01em}.run{color:var(--muted);font-size:13px}
.stats{display:flex;gap:8px;margin:10px 0;flex-wrap:wrap}
.stat{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:6px 12px;font-size:13px;color:var(--muted);box-shadow:var(--shadow)}
.stat b{display:block;font-size:18px;color:var(--ink)}
.controls{display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.pill{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:6px 12px;font:inherit;font-size:13px;cursor:pointer}
.pill.on{background:var(--blue);border-color:var(--blue);color:#fff}
input[type=search]{flex:1 1 140px;min-width:120px;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:7px 14px;font:inherit;font-size:14px}
.count{color:var(--muted);font-size:13px;margin:10px 2px}
details.card{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--line);border-radius:14px;margin:8px 0;box-shadow:var(--shadow);overflow:hidden}
details.card.fresh{border-left-color:var(--green)}details.card.neutral{border-left-color:var(--blue)}
details.card.warn{border-left-color:#e0a02e}details.card.alert{border-left-color:var(--red)}
summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:10px;padding:11px 12px}
summary::-webkit-details-marker{display:none}
.rank{flex:0 0 auto;min-width:30px;text-align:center;background:var(--blue-soft);color:var(--blue);border-radius:999px;padding:2px 8px;font-size:12px;font-weight:700}
.who{flex:1 1 auto;min-width:0;display:flex;flex-direction:column}.sym{font-weight:800;font-size:16px;letter-spacing:.01em}
.nm{color:var(--muted);font-size:12px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.chips{flex:0 0 auto;display:flex;gap:5px;flex-wrap:wrap;justify-content:flex-end;max-width:48%}
.badge,.chip{border-radius:999px;padding:2px 9px;font-size:11px;font-weight:700;white-space:nowrap}
.badge.strong{background:var(--green-soft);color:var(--green)}.badge.moderate{background:var(--blue-soft);color:var(--blue)}
.badge.extended{background:var(--amber-soft);color:var(--amber)}
.badge.plain,.chip{background:var(--bg);color:var(--muted);border:1px solid var(--line)}
.chip.warnchip,.chip.extchip{background:var(--amber-soft);color:var(--amber);border-color:transparent}
.chip.freshchip{background:var(--green-soft);color:var(--green);border-color:transparent}
.chip.nocheck{font-weight:600;border-style:dashed}
.why{font-size:13px;color:var(--amber);margin:2px 0 6px}
#fin-stale{position:sticky;top:0;z-index:20;background:var(--amber-soft);color:var(--amber);border-bottom:1px solid var(--line);padding:9px 14px;font-size:13px;font-weight:700;text-align:center}#fin-stale[hidden]{display:none}.why.muted{color:var(--muted)}
.legend{color:var(--muted);font-size:12px;margin:8px 2px 0}
.titlerow{display:flex;justify-content:space-between;align-items:flex-start;gap:10px}
#fold{flex:0 0 auto;white-space:nowrap}
#filters[hidden]{display:none}
.pill[aria-pressed=true]{background:var(--blue);border-color:var(--blue);color:#fff}
.body{padding:0 12px 12px}.meta{color:var(--muted);font-size:12px;margin:0 0 8px}
.sec{margin:8px 0}.sec-h{font-size:11px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-bottom:3px}
ul{margin:0;padding-left:18px}li{margin:1px 0;font-size:14px}
.callout{border-radius:12px;padding:9px 11px;margin:8px 0;font-size:14px}
.callout-h{font-weight:800;font-size:12px;letter-spacing:.04em;text-transform:uppercase;margin-bottom:2px}
.callout.warn{background:var(--amber-soft);color:var(--amber)}.callout.alert{background:var(--red-soft);color:var(--red)}
.callout.info{background:var(--blue-soft);color:var(--blue)}
.plan{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:9px 11px;margin:8px 0}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.cell .cl{font-size:11px;color:var(--muted)}.cell .cv{font-weight:700}.sub{font-weight:600;color:var(--green);font-size:12px;margin-left:5px}
.news{opacity:.8;font-size:13px}
.subtot{float:right;color:var(--blue);font-weight:800;letter-spacing:0;font-size:12px}
.pts{display:inline-block;margin-left:7px;padding:0 6px;border-radius:8px;background:var(--blue-soft);color:var(--blue);font-size:11px;font-weight:800;vertical-align:1px}
.tag{float:right;font-weight:700;font-size:11px;letter-spacing:0;text-transform:none;opacity:.85}
h2.spec{font-size:16px;margin:26px 0 4px}.specnote{color:var(--muted);font-size:13px;margin-bottom:8px}
footer{color:var(--muted);font-size:12px;text-align:center;margin-top:24px}
@media (max-width:420px){.grid{grid-template-columns:repeat(2,1fr)}.chips{max-width:42%}}
"""

_JS = """
const cards=[...document.querySelectorAll('details.card[data-tier]')];
const q=document.getElementById('q'),cnt=document.getElementById('cnt');
const on=new Set();
function pass(c){
 const tiers=['STRONG','MODERATE','WATCH'].filter(t=>on.has(t));   // tiers combine as "either"
 if(tiers.length&&!tiers.includes(c.dataset.tier))return false;
 if(on.has('fresh')&&c.dataset.fresh!=='1')return false;   // everything else combines as "and"
 if(on.has('ext')&&c.dataset.ext!=='1')return false;
 if(on.has('plan')&&c.dataset.plan!=='1')return false;
 if(on.has('clean')&&c.dataset.warn!=='0')return false;
 const t=q.value.trim().toLowerCase();
 return !t||c.dataset.search.includes(t);}
function apply(){let n=0;cards.forEach(c=>{const ok=pass(c);c.style.display=ok?'':'none';if(ok)n++;});
 cnt.textContent=n+' of '+cards.length+' shown';foldLabel();}
function setBtn(b,v){b.setAttribute('aria-pressed',v?'true':'false');}
const fold=document.getElementById('fold'),panel=document.getElementById('filters');
function foldLabel(){const n=on.size+(q.value.trim()?1:0);
 fold.textContent=panel.hidden?('Show filters \u25BC'+(n?' ('+n+' on)':'')):'Hide filters \u25B2';
 fold.setAttribute('aria-expanded',panel.hidden?'false':'true');}
fold.addEventListener('click',()=>{panel.hidden=!panel.hidden;foldLabel();
 try{localStorage.setItem('finFiltersHidden',panel.hidden?'1':'0');}catch(e){}});
try{if(localStorage.getItem('finFiltersHidden')==='1')panel.hidden=true;}catch(e){}
document.querySelectorAll('.pill[data-f]').forEach(b=>b.addEventListener('click',()=>{
 const f=b.dataset.f,v=!on.has(f);v?on.add(f):on.delete(f);setBtn(b,v);
 if(v&&(f==='fresh'||f==='ext')){const o=f==='fresh'?'ext':'fresh';on.delete(o);   // fresh and extended are opposites
  setBtn(document.querySelector('.pill[data-f='+o+']'),false);}
 apply();}));
document.getElementById('clr').addEventListener('click',()=>{on.clear();q.value='';
 document.querySelectorAll('.pill[data-f]').forEach(b=>setBtn(b,false));apply();});
q.addEventListener('input',apply);
document.getElementById('exp').addEventListener('click',e=>{const o=e.target.dataset.open!=='1';
 e.target.dataset.open=o?'1':'0';e.target.textContent=o?'Collapse all':'Expand all';
 cards.forEach(c=>{if(c.style.display!=='none')c.open=o;});});
apply();
"""


def render_html(md_text: str, expand_top_n: int = EXPAND_TOP_N) -> str:
    d = parse_md(md_text)
    cards = d["cards"]
    n_strong = sum(1 for c in cards if c["tier"] == "STRONG")
    n_mod = sum(1 for c in cards if c["tier"] == "MODERATE")
    n_plan = sum(1 for c in cards if c["plan"] or c["plan_raw"])
    statuses = [card_status(c) for c in cards]
    n_fresh = sum(1 for s in statuses if s["fresh"])
    n_ext = sum(1 for s in statuses if s["extended"])
    cards_html = "".join(_render_card(c, c["rank"] <= expand_top_n) for c in cards)

    spec_html = ""
    if d["spec"]:
        items = "".join(_render_card(c, False).replace('data-tier=""', 'data-tier="SPEC"') for c in d["spec"])
        spec_html = (f'<h2 class="spec">{_e(d.get("spec_title", "Speculative"))}</h2>'
                     f'<div class="specnote">{_e(d["spec_note"])}</div>{items}')

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="fin-run" content="{_e(d['run'].split()[0] if d['run'] else '')}">
<title>Fin \u2013 {_e(d['title'])}</title><style>{_CSS}</style></head>
<body><div id="fin-stale" hidden></div><div class="wrap">
<header class="top"><div class="titlerow"><div><h1>{_e(d['title'])}</h1><div class="run">Run {_e(d['run'])}</div></div>
<button class="pill" id="fold" aria-expanded="true">Hide filters \u25B2</button></div>
<div id="filters"><div class="stats">
<div class="stat"><b>{n_fresh}</b>Fresh</div><div class="stat"><b>{n_ext}</b>Extended</div>
<div class="stat"><b>{n_strong}</b>Strong</div><div class="stat"><b>{n_mod}</b>Moderate</div>
<div class="stat"><b>{n_plan}</b>Trade plans</div></div>
<div class="controls">
<button class="pill" data-f="fresh" aria-pressed="false">Fresh setup</button>
<button class="pill" data-f="ext" aria-pressed="false">Extended</button>
<button class="pill" data-f="STRONG" aria-pressed="false">Strong</button>
<button class="pill" data-f="MODERATE" aria-pressed="false">Moderate</button>
<button class="pill" data-f="WATCH" aria-pressed="false">Watch</button>
<button class="pill" data-f="plan" aria-pressed="false">Trade plan</button>
<button class="pill" data-f="clean" aria-pressed="false">No warnings</button>
<button class="pill" id="clr">Clear</button>
<input id="q" type="search" placeholder="Search ticker or name" autocomplete="off">
<button class="pill" id="exp" data-open="0">Expand all</button></div>
<div class="legend">Tap several filters to combine them. Stripe: green = fresh, amber = extended, red = chasing a big move, blue = neither.<br>Blue numbers = points a finding adds to the ticker\u2019s strength (a category\u2019s strongest finding counts in full, the next \u00d70.6, then \u00d70.36\u2026). Order: flag-free names first, then number of signals, then strength; each extension flag subtracts points from the ranking only.</div></div></header>
<div class="count" id="cnt"></div>
{cards_html}{spec_html}
<footer>Generated from latest_alerts.md \u00B7 display only, not a recommendation</footer>
</div><script>{_JS}</script><script>{_STALE_JS}</script></body></html>"""


def write_html(md_text: str, path: str = HTML_PATH) -> int:
    page = render_html(md_text)
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)
    return len(page)


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else MD_PATH
    dst = sys.argv[2] if len(sys.argv) > 2 else HTML_PATH
    with open(src, encoding="utf-8") as f:
        size = write_html(f.read(), dst)
    print(f"Wrote {dst} ({size:,} bytes) from {src}")
