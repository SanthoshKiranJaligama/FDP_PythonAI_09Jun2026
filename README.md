# FDP Hands-On Guide
## Python Virtual Environments, DEV/TEST Setup, CI/CD Simulation, and AI Project Demo on Windows 11

This is the single working instructions file for running the FDP demo package on a **Windows 11 laptop**.
It combines the source-code overview, setup steps, environment configuration, execution commands, testing, pipeline simulation, and troubleshooting needed to run the full demo successfully.

## Project files

- `app/predict.py` — Student risk predictor using environment-based threshold.
- `tests/test_predict.py` — Unit tests with pytest.
- `pipeline.py` — Local CI/CD simulation script.
- `deploy.py` — Deployment simulation script writing JSON output.
- `app/faq_bot.py` — Simple NLP FAQ bot with confidence threshold.
- `requirements-dev.txt` — DEV environment dependencies.
- `requirements-test.txt` — TEST environment dependencies.
- `.github/workflows/ai-pipeline.yml` — GitHub Actions version of the same pipeline.
- `README.md` — This working instructions file.

## Windows 11 setup

### 1. Install prerequisites
Install the following on your Windows 11 laptop:

1. **Python 3.11 or newer** from [python.org](https://www.python.org/downloads/windows/)
2. **VS Code** from [code.visualstudio.com](https://code.visualstudio.com/)
3. Optional but useful: **Git for Windows** from [git-scm.com](https://git-scm.com/download/win)

While installing Python, enable:
- **Add Python to PATH**
- **Install launcher for all users**

After installation, open **Command Prompt** and verify:

```cmd
python --version
pip --version
```

If `python` is not recognized, restart Command Prompt or reinstall Python with PATH enabled.

### 2. Extract the package
Extract the FDP source package to a folder such as:

```cmd
C:\FDP\ai-demo
```

Open that folder in VS Code using **File > Open Folder**.

### 3. Open terminal in VS Code
Use **Terminal > New Terminal** and select **Command Prompt** for the easiest Windows 11 demo flow.

---

## DEV environment

### 4. Create the DEV virtual environment
From the project root, run:

**Command Prompt:**
```cmd
python -m venv .venv_dev
.venv_dev\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

**PowerShell:**
```powershell
python -m venv .venv_dev
.venv_dev\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

If activation succeeds, the terminal prompt will show `(.venv_dev)`.

### 5. Run the predictor in DEV
Set the environment variables for the demo:

**Command Prompt:**
```cmd
set APP_ENV=dev
set MODEL_THRESHOLD=0.5
python app\predict.py
```

**PowerShell:**
```powershell
$env:APP_ENV="dev"
$env:MODEL_THRESHOLD="0.5"
python app\predict.py
```

Expected behavior: In an interactive terminal, the script prompts whether to use default values (Attendance=62, Internal=58, Assignment=70). Press `Enter` or type `y`/`Y` to use defaults, or type `n`/`N` to enter custom values. In non-interactive environments, it automatically runs with the defaults. Finally, it prints the current environment, configuration, inputs, computed score, and prediction label.

### 6. Run the FAQ bot in DEV
Run:

**Command Prompt:**
```cmd
set APP_ENV=dev
set FAQ_CONFIDENCE=0.20
python app\faq_bot.py
```

**PowerShell:**
```powershell
$env:APP_ENV="dev"
$env:FAQ_CONFIDENCE="0.20"
python app\faq_bot.py
```

If the script expects a query argument or interactive input, use the same query shown in the code comments or prompt.
The DEV threshold is intentionally lower so you can demonstrate a more permissive answer policy.

### 7. Run tests in DEV
Execute:

```cmd
python -m pytest -q
```

All tests should pass before moving to the TEST environment.

---

## TEST environment

### 8. Create the TEST virtual environment
Deactivate DEV if needed:

```cmd
deactivate
```

Then create and activate the TEST environment:

**Command Prompt:**
```cmd
python -m venv .venv_test
.venv_test\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements-test.txt
```

**PowerShell:**
```powershell
python -m venv .venv_test
.venv_test\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-test.txt
```

### 9. Run the predictor in TEST
Set a stricter threshold:

**Command Prompt:**
```cmd
set APP_ENV=test
set MODEL_THRESHOLD=0.7
python app\predict.py
```

**PowerShell:**
```powershell
$env:APP_ENV="test"
$env:MODEL_THRESHOLD="0.7"
python app\predict.py
```

Confirm or provide custom inputs as prompted. This shows how the same code (with same or custom inputs) can produce a different label when threshold/configuration changes.

### 10. Run the FAQ bot in TEST
Run:

**Command Prompt:**
```cmd
set APP_ENV=test
set FAQ_CONFIDENCE=0.60
python app\faq_bot.py
```

**PowerShell:**
```powershell
$env:APP_ENV="test"
$env:FAQ_CONFIDENCE="0.60"
python app\faq_bot.py
```

The higher threshold demonstrates a stricter response policy and may produce fallback output for borderline queries.

### 11. Run tests again in TEST
Execute:

```cmd
python -m pytest -q
```

The test suite should still pass in the TEST environment.

---

## CI/CD simulation

### 12. Run the local pipeline
From the project root, run:

```cmd
python pipeline.py
```

This should perform the configured stages in sequence, typically including dependency setup, tests, and deployment simulation.

### 13. Inspect deployment output
After a successful pipeline run, check for the JSON deployment artifact:

```cmd
type deployed_test.json
```

The file should contain environment information, status, configuration, and a timestamp.

### 14. Demonstrate failure handling
To show pipeline failure:
1. Open `tests\test_predict.py`
2. Change one expected assertion intentionally
3. Save the file
4. Run:

```cmd
python -m pytest -q
python pipeline.py
```

The pipeline should stop when tests fail.

Then restore the file and rerun the pipeline successfully.

---

## GitHub Actions mapping

The file `.github/workflows/ai-pipeline.yml` mirrors the same workflow in GitHub Actions.
Use it to explain how the local pipeline connects to automated cloud-based CI/CD.

Recommended explanation order for the demo:
1. Local Python script.
2. Unit test.
3. Local pipeline.
4. GitHub Actions workflow.
5. Deployment artifact.

---

## GitHub Setup for Participants

This section explains how every participant should **fork** the shared repository, work in their own copy, and follow the branch rules that protect the main codebase.

### 15. Fork the repository

Forking creates your own independent copy of the project under your GitHub account. You can freely modify it, break things, fix them, and push — without affecting the instructor's original repository.

1. Open the repository in your browser:
   ```
   https://github.com/SanthoshKiranJaligama/FDP_PythonAI_09Jun2026
   ```
2. Click the **Fork** button (top-right corner of the page).
3. On the "Create a new fork" screen, keep the default name `FDP_PythonAI_09Jun2026` and click **Create fork**.
4. You now have your own copy at:
   ```
   https://github.com/YOUR_USERNAME/FDP_PythonAI_09Jun2026
   ```

### 16. Clone your fork to your laptop

Clone **your fork** (not the instructor's original):

**Command Prompt:**
```cmd
git clone https://github.com/YOUR_USERNAME/FDP_PythonAI_09Jun2026.git
cd FDP_PythonAI_09Jun2026
```

**PowerShell:**
```powershell
git clone https://github.com/YOUR_USERNAME/FDP_PythonAI_09Jun2026.git
Set-Location FDP_PythonAI_09Jun2026
```

### 17. Create a personal practice branch

> **Rule: Never commit directly to `main`.** All your changes must go into a personal branch.

Create and switch to a new branch named with your identifier:

```cmd
git checkout -b practice/YOUR_NAME
```

For example:
```cmd
git checkout -b practice/santhosh-kiran
```

You will do all your work — edits, experiments, test breakage demos — on this branch.

### 18. Make changes, commit, and push your branch

After making any change:

```cmd
git add .
git commit -m "describe what you changed"
git push origin practice/YOUR_NAME
```

This pushes only to **your fork**, so the instructor's repository is never touched.

### 19. Keep your fork up to date with the instructor's repo

If the instructor pushes new changes to the original repository, sync them into your fork:

```cmd
git remote add upstream https://github.com/SanthoshKiranJaligama/FDP_PythonAI_09Jun2026.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

Then rebase your practice branch on top:
```cmd
git checkout practice/YOUR_NAME
git rebase main
```

### 20. Open a Pull Request (optional exploration)

To practice the PR workflow:
1. Push your practice branch to your fork.
2. Go to your fork on GitHub.
3. Click **Compare & pull request**.
4. Set the base as **your own fork's `main`** (not the instructor's).
5. Describe your changes and click **Create pull request**.
6. GitHub Actions will automatically run the CI pipeline on your PR.

---

## Branch Protection Rules

The instructor repository has branch protection rules configured on `main` to prevent accidental or unauthorized changes.

### What is protected

| Rule | Effect |
|------|--------|
| **Require pull request before merging** | No one can push commits directly to `main`. Changes must go through a PR. |
| **Require status checks to pass** | The `AI Demo CI/CD Pipeline` must succeed before a PR can be merged. |
| **Dismiss stale reviews** | If new commits are pushed to a PR, previous approvals are dismissed automatically. |
| **Block force pushes** | `git push --force` to `main` is rejected. |
| **Restrict deletions** | The `main` branch cannot be deleted. |

### Setting up branch protection on your own fork (recommended)

After forking, protect your own `main` branch too:

1. Go to your fork on GitHub.
2. Click **Settings** → **Branches**.
3. Click **Add branch protection rule**.
4. In **Branch name pattern**, type `main`.
5. Enable:
   - ✅ Require a pull request before merging
   - ✅ Require status checks to pass before merging
   - ✅ Block force pushes
6. Click **Create**.

This mirrors the instructor's protection on your own copy and gives you practice with real-world branch governance.

### How participants should work (summary)

```
Instructor repo (read-only for participants)
    ↓  fork
Your fork on GitHub  (your personal sandbox)
    ↓  clone
Your laptop
    ↓  checkout -b practice/YOUR_NAME
Your practice branch  ← all edits happen here
    ↓  push
Your fork/practice branch  ← triggers GitHub Actions on YOUR repo
    ↓  pull request (optional)
Your fork/main  ← safe merge after CI passes
```

The instructor's `main` branch is **never modified** by participants.

---

## Windows 11 troubleshooting

### Python not found
If `python` is not recognized:
- Close and reopen Command Prompt.
- Confirm Python PATH was added during installation.
- Reinstall Python if needed.

### Virtual environment activation fails
Make sure you are using **Command Prompt** and not a restricted shell.
The correct activation command is:

```cmd
.venv_dev\Scripts\activate
```

or

```cmd
.venv_test\Scripts\activate
```

### pip install problems
If package installation fails:
- Upgrade pip first.
- Check internet connectivity.
- Try running Command Prompt as a normal user first.

### DLL load failed / Application Control policy error
If running `app/faq_bot.py` fails with:
`ImportError: DLL load failed while importing _hashing_fast: An Application Control policy has blocked this file.`
- **Cause:** Your system has Windows Defender Application Control (WDAC) or AppLocker enabled, which blocks compiled binary `.dll`/`.pyd` extensions inside local/user-writable virtual environments.
- **Solution:** The FAQ bot has been updated to use a pure-Python TF-IDF and Cosine Similarity solver. This runs without compiled binary extensions, bypassing policy restrictions.

### ModuleNotFoundError: No module named 'app'
If running tests fails with `ModuleNotFoundError: No module named 'app'`:
- **Cause:** Invoking `pytest -q` directly may run a global pytest executable or execute outside the virtual environment context, failing to resolve the workspace path.
- **Solution:** Run the tests using `python -m pytest -q`. This forces Python to use the active virtual environment's libraries and adds the project root to `sys.path`.

### PowerShell behavior
If using PowerShell, activation syntax is different and you must set environment variables using the `$env:` prefix:

- **Activation command**:
  ```powershell
  .venv_dev\Scripts\Activate.ps1
  ```
- **Environment variables**:
  Instead of `set KEY=VALUE` (which sets local shell variables in PowerShell that subprocesses do not inherit), use:
  ```powershell
  $env:APP_ENV="test"
  $env:MODEL_THRESHOLD="0.7"
  ```
  *(To clear a variable: `$env:APP_ENV=$null`)*

For the FDP demo, **Command Prompt is recommended** to avoid confusion, but PowerShell works perfectly when using the `$env:` prefix.

---

## Demo flow for the FDP session

A clean live demonstration flow is:
1. Show folder structure.
2. Create DEV environment.
3. Run predictor.
4. Run FAQ bot.
5. Run tests.
6. Create TEST environment.
7. Run predictor again with stricter threshold.
8. Run FAQ bot again with stricter threshold.
9. Run pipeline.
10. Show `deployed_test.json`.
11. Break one test and show pipeline failure.
12. Restore test and rerun successfully.
13. Open the GitHub repository and show the `.github/workflows/ai-pipeline.yml` file.
14. Show the completed GitHub Actions run and the uploaded `deployed-test-receipt` artifact.
15. Each participant forks the repository to their own GitHub account.
16. Participant clones their fork and creates a `practice/YOUR_NAME` branch.
17. Participant makes a small intentional change (e.g., adjusts a threshold or adds a comment).
18. Participant commits and pushes their branch — GitHub Actions runs automatically on their fork.
19. Participant opens a pull request from their branch to their fork's `main` and watches CI results.
20. Demonstrate that a direct push to `main` is rejected by branch protection rules.

---

## Notes for teaching

- Keep DEV and TEST terminals separate if possible.
- Use the same code to demonstrate how configuration changes behavior.
- Emphasize that this is a working simulation, not a production deployment.
- Use the demo to teach curiosity, experimentation, validation, and deployment flow.