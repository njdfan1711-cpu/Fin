"""
notify.py - sends a push notification via ntfy.sh (free, no account, no key).

Setup on your phone (one-time):
  1. Install the "ntfy" app (iOS App Store / Google Play)
  2. Pick a topic name that's hard to guess (it's a public system --
     anyone who knows your topic name can see your alerts), e.g.
     "yourname-stockscan-9f3k2"
  3. Subscribe to that topic in the app
  4. Set NTFY_TOPIC to that same name as a GitHub Actions secret
     (Settings -> Secrets and variables -> Actions -> New repository secret)

That's it -- no signup on ntfy.sh's website required for basic use.
"""

import json
import urllib.request
from config import NTFY_TOPIC


def send_alert(title: str, message: str, priority: str = "default",
               tags: list[str] | None = None, markdown: bool = False,
               click_url: str | None = None):
    """
    priority: one of "min", "low", "default", "high", "urgent"
    tags: emoji shortcodes shown in the notification, e.g. ["chart_with_upwards_trend"]
    markdown: if True, message is rendered with **bold**, *italics*, links,
              etc. instead of plain text (ntfy's Markdown header)
    click_url: if set, tapping the notification opens this URL (ntfy's
               Click header) -- useful for linking straight to the full
               ranked list in the repo, since long-press/inline links
               don't work reliably across all ntfy clients
    """
    if not NTFY_TOPIC:
        print(f"[notify skipped -- NTFY_TOPIC not set] {title}: {message}")
        return

    url = f"https://ntfy.sh/{NTFY_TOPIC}"
    headers = {
        "Title": title,
        "Priority": priority,
    }
    if tags:
        headers["Tags"] = ",".join(tags)
    if markdown:
        headers["Markdown"] = "yes"
    if click_url:
        headers["Click"] = click_url

    req = urllib.request.Request(
        url,
        data=message.encode("utf-8"),
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            resp.read()
    except Exception as e:
        # Don't let a failed notification crash the whole scan run
        print(f"[notify error] {title}: {e}")


def send_batch_alert(matches: list[dict]):
    """
    LEGACY / not used by the current pipeline -- compose_alerts.py builds
    its own richer, markdown-formatted message directly. Kept here in case
    it's useful for a simple one-off script later.

    matches: list of {"symbol": str, "reasons": list[str]}
    """
    if not matches:
        return

    lines = []
    for m in matches:
        reasons = ", ".join(m["reasons"])
        lines.append(f"{m['symbol']}: {reasons}")

    title = f"{len(matches)} stock alert(s)"
    message = "\n".join(lines)

    # ntfy messages have a practical length limit -- truncate gracefully
    if len(message) > 3800:
        message = message[:3800] + "\n...(truncated, check the repo log for full list)"

    send_alert(title, message, priority="high", tags=["chart_with_upwards_trend"])
