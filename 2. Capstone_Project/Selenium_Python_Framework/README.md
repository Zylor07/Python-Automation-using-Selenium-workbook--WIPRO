# Selenium Python Framework — E-Commerce Login and Search

**Application:** [TutorialsNinja demo](https://tutorialsninja.com/demo/)  
**Coverage:** invalid login from CSV, product search from CSV, optional valid login with a registered account. The same page objects, browser factory, and test data are exercised through separate pytest and unittest suites. Run each suite independently; running both repeats some scenarios.

## Requirements

- Python 3.10+ and Chrome, Firefox or Edge installed.
- Internet access to the demo application and, on first use, to the browser driver's download service. Selenium Manager resolves a matching driver automatically. Public demo data may change.

## Quick start

From the folder containing `README.md`:

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest tests/pytest_tests --html=reports/pytest_report.html --self-contained-html
python run_unittest.py
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest tests/pytest_tests --html=reports/pytest_report.html --self-contained-html
python run_unittest.py
```

Open `reports/pytest_report.html` and `reports/unittest_report.html` in your browser. A failing test also saves a named PNG in `screenshots/`. The pytest report embeds its failure screenshot; the unittest report links to its screenshot, so keep `reports/` and `screenshots/` together. Reports and images are created by running the tests; none are pre-generated or claimed as passed.

### Run a single area

```bash
python -m pytest tests/pytest_tests/test_pytest_search.py --html=reports/pytest_search.html --self-contained-html
python -m pytest tests/pytest_tests/test_pytest_login.py --html=reports/pytest_login.html --self-contained-html
```

## Optional valid-login coverage

Create a personal account on the demo site and set environment variables in your own terminal. Do not write passwords to the CSV, config, logs, screenshots, or submission. The test skips unless **both** variables exist.

```powershell
$env:TEST_EMAIL="your-test-account@example.com"
$env:TEST_PASSWORD="your-test-password"
python -m pytest tests/pytest_tests --html=reports/pytest_report.html --self-contained-html
```

For macOS/Linux, use `export TEST_EMAIL='...'` and `export TEST_PASSWORD='...'`. Run `python run_unittest.py` for the equivalent unittest path.

## Configuration and data

| File | Purpose |
| --- | --- |
| `config/settings.ini` | Application URL, browser name, headless flag, explicit wait, page load timeout. |
| `data/login_cases.csv` | Invalid credential input and expected error. |
| `data/search_cases.csv` | Query, expected product or no-results condition. |
| `framework/` | Browser creation, config, CSV validation, failure screenshot utility. |
| `pages/` | Login and search page objects with explicit waits. |
| `tests/pytest_tests/` | Parametrized tests and shared browser fixture in `tests/conftest.py`. |
| `tests/unittest_tests/` | unittest cases run via `run_unittest.py`, which writes its own HTML report. |

Environment overrides: `BASE_URL`, `BROWSER` (`chrome`, `firefox`, `edge`), and `HEADLESS` (`true`/`false`). For example, PowerShell: `$env:HEADLESS="true"`; macOS/Linux: `HEADLESS=true python -m pytest ...`.

## Scenario matrix

| ID | Flow | Expected outcome |
| --- | --- | --- |
| invalid_credentials | Login with nonexistent email and incorrect password | Account warning appears. |
| empty_credentials | Login with both fields blank | Account warning appears. |
| macbook | Search MacBook | Exact product title MacBook appears. |
| iphone | Search iPhone | Exact product title iPhone appears. |
| no_results | Search unlikely unique text | No-products message appears. |
| valid_login (optional) | Login with provided personal demo account | My Account page appears. |

## Troubleshooting

- `ModuleNotFoundError`: activate the virtual environment and install requirements; run commands from this root directory.
- Driver startup error: install or update a supported browser, and ensure the first driver download can connect. Try `BROWSER=firefox` if Chrome is unavailable.
- Site timeout or changed product data: confirm the demo loads manually, examine the screenshot and HTML report, then update a CSV expectation or a page locator if the site changed.
- On Windows, if activation is disabled by local policy, run `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` then use that executable in the commands.

## Submission checklist

Submit the source ZIP. After running locally, include the two generated HTML reports and a screenshot of your passing terminal results if evidence is required. Never claim a pass before execution or include personal credentials. See `SUBMISSION_NOTES.md` for a short summary.
