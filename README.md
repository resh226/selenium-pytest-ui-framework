# 🚀 Selenium Pytest UI Automation Framework

![Sequential Workflow](https://github.com/<username>/<repo>/actions/workflows/docker-selenium-grid.yml/badge.svg)
![Parallel Workflow](https://github.com/<username>/<repo>/actions/workflows/pytest-markers-parallel.yml/badge.svg)

---

## 📖 Overview

This is a **Selenium UI Automation Framework** using Python and Pytest. It supports:
```
✅ Page Object Model (POM) for clean, maintainable code
✅ Parallel & marker-based test execution in GitHub Actions CI/CD
✅ Rich Allure Reports with screenshots and logs
✅ Designed for Chrome browser testing in both local and CI environments
✅ Two CI/CD workflows: one using Dockerized Selenium Grid and one running directly without Docker
```
*Note:* In CI, Dockerized Selenium Grid was used only for Chrome due to GitHub runner memory constraints. If desired, you can switch to Firefox by editing the `browser` value in `config/config.json` as Firefox (currently its set as Chrome).

---

## 💻 Tech Stack

| Technology         | Purpose                               |
| ------------------ | ------------------------------------- |
| Python 3.11        | Programming language                  |
| Pytest             | Test framework                        |
| Selenium WebDriver | Browser automation                    |
| Allure             | Reporting with screenshots & metadata |
| Docker             | Containerized Selenium Grid (CI only) |
| GitHub Actions     | CI/CD pipelines (Docker & Non-Docker) |
| pytest-xdist       | Parallel test execution               |

---

## 🏗 Framework Highlights

| Feature                     | Details                                                                                       |
| --------------------------- | --------------------------------------------------------------------------------------------- |
| **Page Object Model (POM)** | Encapsulated locators & actions in `pages/` for reusability                                   |
| **Fixtures & Scopes**       | Session & function scoped fixtures for setup/teardown in `conftest.py`                        |
| **Explicit Waits**          | `utils/wait_utils.py` handles dynamic elements reliably                                       |
| **Markers**                 | `@pytest.mark.smoke`, `@pytest.mark.regression`, `@pytest.mark.flow`, `@pytest.mark.negative` |
| **Parallel Execution**      | `pytest-xdist` enabled multi-core runs                                                        |
| **Pytest Hooks**            | Screenshots on test pass/fail, Allure step logging                                            |
| **Allure Reporting**        | Full HTML reports with screenshots and metadata                                               |
| **CI/CD Workflows**         | Dockerized Grid (Chrome-only) and non-Docker workflows                                        |
| **Configurable Browser**    | `config/config.json` allows switching between Chrome and Firefox                              |

---

## 🧪 Core Scenarios Covered

* ✅ **Basic Search Verification**: Home → Search → Validate title & links
* ✅ **Edge Cases**: Blank searches, special characters, long inputs
* ✅ **Flow Tests**: Multi-step workflows across pages
* ✅ **Negative Tests**: Intentional failures to verify error handling & screenshots

---

## 📂 Folder Structure
---
```
selenium-pytest-ui-framework/
│
├── base/                              # Base page classes
│   └── base_page.py                   # Parent class with common WebDriver methods
│
├── config/                            # Configuration files
│   └── config.json                    # Holds browser type, waits, and other configs
│
├── locators/                          # Page locators (organized per page)
│   ├── result_locators.py             # Locators for results page
│   └── search_locators.py             # Locators for search page
│
├── pages/                             # Page Object Model classes
│   ├── __init__.py                    # Marks directory as package
│   ├── result.py                      # ResultPage class methods
│   └── search.py                      # SearchPage class methods
│
├── reports/                           # Test execution reports
│   ├── failure_testcase_screenshot_captured/  # Screenshots for failed test cases
│   ├── Allure Report.PNG              # Saved Allure report screenshot
│   └── screen_recording_20250711.mp4  # Video recording of test execution in CI
│
├── test_data/                         # Data-driven test cases in JSON
│   ├── basic_cases.json               # Basic search test data
│   ├── edge_cases.json                # Edge case test data
│   ├── failure_cases.json             # Negative test data
│   └── flow_cases.json                # Flow test data
│
├── tests/                             # Pytest test files
│   ├── test_failure_scenarios.py      # Tests for negative cases
│   ├── test_search_basic.py           # Tests for basic search
│   ├── test_search_edge_cases.py      # Tests for edge cases
│   └── test_search_flow.py            # Tests for flow scenarios
│
├── utils/                             # Utility modules
│   ├── constants.py                   # Constants used across framework
│   ├── file_utils.py                  # File operations (read/write JSON)
│   └── wait_utils.py                  # Explicit wait utility methods
│
├── .github/workflows/                 # CI/CD workflow definitions
│   ├── docker-selenium-grid.yml       # Workflow for Dockerized Grid run (Chrome only)
│   └── pytest-markers-parallel.yml    # Workflow for marker-based parallel run
│
├── Dockerfile                         # Defines Docker image for running tests
├── docker-compose.yml                 # Spins up Selenium Grid (Hub + Chrome node) for CI
├── wait-for-grid.sh                   # Script to wait until Grid is ready
├── requirements.txt                   # Python dependencies for framework
└── README.md                          # Project documentation

```
---

## 📸 Allure Report Screenshot

Here’s a sample Allure Report generated:

<img width="1484" height="756" alt="image" src="https://github.com/user-attachments/assets/5a747b5b-ba84-433c-af68-38f4b2e8b25a" />

---

## 🌐 Run in CI/CD

Push to `main` branch to trigger workflows:

* **docker-selenium-grid.yml** → Sequential Docker Grid runs (Chrome only)
* **pytest-markers-parallel.yml** → Parallel marker-based runs (non-Docker)

---

## 📥 View Artifacts in GitHub Actions
# After a workflow run completes:

1. Go to the Actions tab in your repository.
2. Click on the latest workflow run (docker-selenium-grid.yml or pytest-markers-parallel.yml).
3. Scroll down to the Artifacts section.
   
# Download:

📊 allure-report.zip → Allure HTML report.
📂 allure-results.zip → Raw Allure results (JSON, attachments) for local regeneration.
📸 screenshots.zip → Captured screenshots for failed test cases.

---
## 🖼️ Test Flow Diagrams of both workflows in GitHub CI/CD

### 🚀 Workflow 1: Dockerized Selenium Grid (docker-selenium-grid.yml)
```
Pytest Runner
    ↓
Docker Compose Up (in CI)
    ↓
Selenium Grid Hub
    ↓
Chrome Node (Only)
    ↓
Test Execution
    ↓
Allure Results Generated
    ↓
Allure HTML Report
```
### ⚡ Workflow 2: Non-Docker Pytest Parallel Runs (pytest-markers-parallel.yml)
```
Pytest Runner
    ↓
Direct Browser Execution (Chrome Only)
    ↓
Test Execution (Parallel by Markers)
    ↓
Allure Results Generated
    ↓
Allure HTML Report
```
---

## 📦 Prerequisites & Setup Steps to run in your Local

Follow these steps to get the framework running from scratch:

1️⃣ Clone the Repository
```
git clone https://github.com/<username>/<repo>.git
cd <repo>
```
2️⃣ Install Python (Required)
```
Make sure Python 3.11 is installed. This project requires Python.
Download from python.org
Ensure python and pip are added to your PATH.
```
3️⃣ Install Project Dependencies
```
pip install -r requirements.txt
(This will install all necessary libraries, including Selenium, Pytest, Allure-pytest plugin, etc.)
```
4️⃣ Install Allure Commandline (CLI)
```
Download Allure from Allure Releases
Extract and place it in your project folder or any location
Add the bin folder path (e.g., C:\path\to\allure-2.xx.x\bin) to your System Environment Variables > PATH
Restart terminal or IDE.
Verify installation:
allure --version
```
5️⃣ Install Google Chrome (Latest)
```
Download from Google Chrome
ChromeDriver is auto-managed via WebDriverManager
```
7️⃣ Configure Browser (Optional)
```
Default browser is Chrome. To use Firefox, edit config/config.json:
{
  "browser": "Firefox"
}
```
8️⃣ Run Tests
```
See the section below for commands to execute tests and generate reports.
```
---
---

## 🖥 Running Tests Locally (Non-Docker)

### 🔥 Running All Tests

```
pytest --alluredir=reports/allure-results
```

### 🏷 Running by Markers

#### Smoke Tests

```
pytest -m smoke --alluredir=reports/allure-results
```

#### Regression Tests

```
pytest -m regression --alluredir=reports/allure-results
```

#### Flow Tests

```bash
pytest -m flow --alluredir=reports/allure-results
```

#### Negative Tests

```
pytest -m negative --alluredir=reports/allure-results
```

### ⚡ Running Tests in Parallel

```
pytest -n 2 --alluredir=reports/allure-results  # Run tests with 2 parallel workers
```

### 🌐 Switch Browser (Chrome/Firefox)

Edit `config/config.json`:

```json
{
  "browser": "Firefox"
}
```
Default is Chrome. Change to `Firefox` to run tests on Firefox locally or in CI.

---
### 📊 Generate Allure Report in local
After running tests with --alluredir, generate the HTML report:

```
allure generate reports/allure-results -o reports/allure-report --clean
```
Serve it in browser:

```
allure serve reports/allure-results
```
---

## 🪝 Debugging Notes & Fixes

| Issue                          | Fix                                                     |
| ------------------------------ | ------------------------------------------------------- |
| `allure: not recognized`       | Used `allure.bat` or added Allure bin to PATH           |
| Selenium Grid healthcheck fail | Added `wait-for-grid.sh` retry logic                    |
| GitHub Runner OOM (7GB limit)  | Reduced Hub/node memory, limited parallel workers       |
| Large Allure artifacts         | Synced reports via Docker volume mapping                |
| Flaky tests on Grid            | Added explicit waits and retry logic in `wait_utils.py` |
| Docker local issues            | Avoided Docker locally due to resource constraints      |

---

## 📋 What I Learned

* Advanced Pytest (markers, fixtures, hooks, parallel runs)
* Dockerized Selenium Grid (Chrome-only, CI optimized)
* Debugging CI/CD memory issues on GitHub runners
* Configurable browser setup via JSON file
* Allure Reporting integration
* Artifact management

---

## 🏷 Badges

![Sequential Workflow](https://github.com/<username>/<repo>/actions/workflows/docker-selenium-grid.yml/badge.svg)
![Parallel Workflow](https://github.com/<username>/<repo>/actions/workflows/pytest-markers-parallel.yml/badge.svg)

(Replace `<username>` and `<repo>` with your GitHub details)

---

