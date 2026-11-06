# Move your trade data to a private repo — step by step

Goal: your trade log (and everything built from it) stops being visible in the public Fin repo.
Do the parts **in order**. Nothing is deleted from the public repo until Part E, so position
monitoring never has a gap.

Ignore the `__pycache__` folder inside `fin_update` if you see one. Do not upload it.

---

## Part A — Create the private repo (about 3 minutes)

1. On github.com tap **+** (top right) → **New repository**.
2. Name: `fin-private`. Choose **Private**. Tick **Add a README file** (this creates the `main` branch). Tap **Create repository**.
3. Get your current trade log: in the public **Fin** repo open `open_positions.json` → tap the download icon (or **Raw**, then save the page as a file).
4. In **fin-private**: **Add file** → **Upload files** → choose `open_positions.json` → **Commit changes**.

Check: `open_positions.json` is listed in the root of fin-private.

## Part B — Give the Fin workflows access (about 5 minutes)

1. Tap your profile photo → **Settings** → scroll to the bottom of the left menu → **Developer settings** → **Personal access tokens** → **Fine-grained tokens** → **Generate new token**.
2. Token name: `fin-private-access`. Expiration: **1 year** (the maximum). Put a reminder in your calendar for two weeks before it expires.
3. Repository access: **Only select repositories** → choose **fin-private**.
4. Permissions → **Repository permissions** → **Contents** → **Read and write**. Leave everything else alone.
5. **Generate token**. Copy it right away; GitHub shows it only once.
6. Go to the public **Fin** repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**.
   Name: `PRIVATE_REPO_TOKEN`. Secret: paste the token. **Add secret**.

If you named the private repo something other than `fin-private`, also add a **Variable** (same page, Variables tab) named `PRIVATE_REPO` with the value `your-username/your-repo-name`.

## Part C — Upload the new code

Upload everything in the `fin_update` folder to the public Fin repo, keeping the folder structure
(`.github/workflows/…` files go in that folder; `.gitignore`, `.gitattributes` and the `.py` / `.md`
files go in the repo root). It is the complete current set, so it also includes the earlier changes
from today (ranking, tiers, page) if you haven't uploaded those yet.

New or changed for this move: `config.py`, `position_monitor.py`, `trade_drawdown_report.py`,
`swing_backtest.py`, `.gitignore`, `CHANGELOG.md`, and the workflows `intraday.yml`,
`trade_drawdown.yml`, `swing_backtest.yml`.

## Part D — Test it BEFORE deleting anything

1. Public Fin repo → **Actions** → **Intraday** (the scan workflow) → **Run workflow**. Open the run when it finishes.
   - Step **Check out private trade data** should be green.
   - Step **Check open positions** should end with a line like `Checked 3 open position(s) …`.
   - It should NOT show symbols or prices, and should NOT show a yellow warning saying positions were not monitored.
2. **Actions** → **Trade drawdown report** → **Run workflow**. Then look in **fin-private**: `trade_drawdown_report.md` should appear.
3. **Actions** → **Swing backtest** → **Run workflow**. Then **fin-private** should contain `swing_backtest.md`, `swing_backtest_summary.json`, `swing_backtest_trades.csv`, `swing_backtest_my_trades.csv`.

If a step fails with "repository not found" or "bad credentials", the token or its repo access is wrong: redo Part B steps 3–6.

## Part E — Remove the files from the public repo

Only after Part D worked. In the public Fin repo, open each file below → tap the trash icon → **Commit changes**:

- `open_positions.json`
- `trade_drawdown_report.md`
- `swing_backtest_my_trades.csv`
- `swing_backtest_summary.json`
- `swing_backtest.md`
- `swing_backtest_trades.csv`

Leave `position_monitor_state.json` alone: it holds only random trade ids and condition names, no symbols.

From now on, upload your Fin Trade Log export to **fin-private**, not to Fin.

## Part F — What is still visible, and your options

Deleting a file does not erase it from the repo's history, and old logs are still online:

1. **Old versions of the files** stay in the commit history of the public repo.
2. **Old Actions logs** from earlier runs printed per-position lines (symbol, price, P&L) and the full drawdown table. They stay readable until they expire (90 days by default). You can delete individual runs (Actions → a run → ⋯ → Delete workflow run).
3. **CHANGELOG.md** names a few traded symbols in older entries (the blank-entry-date trades and the drawdown report notes).

Options, from least to most effort:

- **Accept it.** The history shows symbols, prices and dates, tied to your GitHub username.
- **Scrub the history** (rewrites every commit, then force-pushes). Doable, but destructive; do it only with a full backup, and ask me to walk you through it.
- **Start a fresh public repo** (new history, nothing old). You would re-add the secrets, the `ALERTS_PAGE_URL` variable, Pages, and point cron-job.org at the new name.

## Part G — Day to day

- The scan keeps working even if the token breaks. Only position monitoring pauses.
- If that happens you get a push notification, at most once a day: **"Position monitoring is OFF"**. Fix: make a new token (Part B) and replace the `PRIVATE_REPO_TOKEN` secret.
- When the token is a month from expiring, make a new one and replace the secret.
- Keep your trade log export in fin-private as `open_positions.json` (same name, in the root).
