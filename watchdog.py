"""
watchdog.py

Checks whether today's Daily Foundation Scan (scan.yml) has actually
produced a run yet. Meant to run from its own scheduled workflow a
couple hours after the scan's normal ~11:07 UTC trigger time.

This exists for one specific failure mode: GitHub's scheduler can
silently drop a cron trigger under load. When that happens, scan.yml
never even shows a queued or failed run -- there's simply nothing to
see in the Actions tab, and nothing downstream (compose_alerts.py's
own error handling, retry logic, etc.) would ever catch it, since
none of that code runs either. This script is the one thing checking
from outside that pipeline.

Requires GITHUB_TOKEN (needs `actions: read` permission granted to the
calling workflow) and GITHUB_REPOSITORY, both provided automatically
by GitHub Actions -- no extra secrets beyond the existing NTFY_TOPIC.
"""

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

from notify import send_alert

SCAN_WORKFLOW_FILE = "scan.yml"


def has_scan_run_today() -> bool:
    repo = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GITHUB_TOKEN"]
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    url = (f"https://api.github.com/repos/{repo}/actions/workflows/"
           f"{SCAN_WORKFLOW_FILE}/runs?created=%3E%3D{today}&per_page=1")
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.load(resp)
    return data.get("total_count", 0) > 0


def main():
    try:
        ran = has_scan_run_today()
    except Exception as e:
        print(f"[watchdog error] Couldn't check scan run history: {e}", file=sys.stderr)
        # Fail open -- if the check itself is broken, a false-alarm push
        # beats silently telling you nothing.
        send_alert(
            title="Daily Scan Watchdog error",
            message=f"Couldn't check whether today's Daily Foundation Scan "
                     f"has run: {e}",
            priority="high",
            tags=["warning"],
        )
        sys.exit(1)

    if ran:
        print("Daily Foundation Scan has already run today -- no alert needed.")
        return

    send_alert(
        title="Daily Scan hasn't started",
        message="No Daily Foundation Scan run found yet today (normally "
                 "kicks off ~11:07 UTC / ~7am ET). The scheduled trigger "
                 "may not have fired -- check the Actions tab and consider "
                 "a manual workflow_dispatch run.",
        priority="high",
        tags=["warning"],
    )
    print("Alert sent: Daily Foundation Scan hasn't run yet today.")


if __name__ == "__main__":
    main()
