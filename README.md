# 🚀 Selenium Pytest UI Automation Framework

![Sequential Workflow](https://github.com/<username>/<repo>/actions/workflows/docker-selenium-grid.yml/badge.svg)
![Parallel Workflow](https://github.com/<username>/<repo>/actions/workflows/pytest-markers-parallel.yml/badge.svg)

---

## 📖 Overview

This is a **Selenium UI Automation Framework** using Python and Pytest. It supports:

✅ Page Object Model (POM) for clean, maintainable code
✅ Parallel & marker-based test execution in GitHub Actions CI/CD
✅ Rich Allure Reports with screenshots and logs
✅ Designed for Chrome browser testing in both local and CI environments
✅ Two CI/CD workflows: one using Dockerized Selenium Grid and one running directly without Docker

*Note:* Local runs were performed using the Pytest framework **without Docker**, as Docker had setup issues locally. In CI, Dockerized Selenium Grid was used only for Chrome due to GitHub runner memory constraints.

---

## 🏗 Framework Highlights

| Feature                     | Details                                                                |
| --------------------------- | ---------------------------------------------------------------------- |
| **Page Object Model (POM)** | Encapsulated locators & actions in `pages/` for reusability            |
| **Fixtures & Scopes**       | Session & function scoped fixtures for setup/teardown in `conftest.py` |
| **Explicit Waits**          | `utils/wait_utils.py` handles dynamic elements reliably                |
| **Markers**                 | `@pytest.mark.smoke`, `@pytest.mark.regression`, `@pytest.mark.flow`   |
| **Parallel Execution**      | `pytest-xdist` enabled multi-core runs                                 |
| **Pytest Hooks**            | Screenshots on test pass/fail, Allure step logging                     |
| **Allure Reporting**        | Full HTML reports with screenshots and metadata                        |
| **CI/CD Workflows**         | Dockerized Grid (Chrome-only) and non-Docker workflows                 |

---

## 🧪 Core Scenarios Covered

* ✅ **Basic Search Verification**: Home → Search → Validate title & links
* ✅ **Edge Cases**: Blank searches, special characters, long inputs
* ✅ **Flow Tests**: Multi-step workflows across pages
* ✅ **Negative Tests**: Intentional failures to verify error handling & screenshots

---

## 📂 Folder Structure

```bash
selenium-pytest-ui-framework/
│
├── config/                # Test configs (e.g., implicit_wait, browser settings)
├── locators/              # Page locators
├── pages/                 # POM classes (SearchPage, ResultPage)
├── tests/                 # Organized tests (smoke, regression, flow)
├── utils/                 # Helper utilities (waits, file ops, constants)
├── reports/               # Allure results and HTML reports
├── .github/workflows/     # CI/CD pipelines (docker & non-docker)
├── Dockerfile
├── docker-compose.yml
├── wait-for-grid.sh
├── requirements.txt
└── README.md
```

---

## 🖼️ Test Flow Diagram
```
🚀 Workflow 1 – Dockerized Selenium Grid (docker-selenium-grid.yml)

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

```

⚡ Workflow 2 – Non-Docker (pytest-markers-parallel.yml)

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

## 🐳 Docker & CI/CD Highlights

### 🚀 Docker Compose (CI Only)

* Hub + Chrome node defined in `docker-compose.yml`
* Healthcheck logic with retries via `wait-for-grid.sh`

### 📦 GitHub Actions Workflows

* **docker-selenium-grid.yml** → Sequential Docker Grid runs (Chrome only)
* **pytest-markers-parallel.yml** → Parallel marker-based runs (non-Docker)
* Allure reports & screenshots uploaded as artifacts
* Docker layer caching for faster builds

---

## 🛠 Setup Instructions

### 🖥 Run Locally (Non-Docker)

```bash
# Create virtualenv & install dependencies
pip install -r requirements.txt

# Run tests
pytest -m smoke

# View Allure Report
allure serve reports/allure-results
```

### 🌐 Run in CI/CD

Push to `main` branch to trigger workflows:

* Sequential Docker Grid: docker-selenium-grid.yml
* Parallel Non-Docker: pytest-markers-parallel.yml

---

## 🪝 Debugging Notes & Fixes

| Issue                          | Fix                                                     |
| ------------------------------ | ------------------------------------------------------- |
| `allure: not recognized`       | Used `allure.bat` or added Allure bin to PATH           |
| Selenium Grid healthcheck fail | Added `wait-for-grid.sh` retry logic                    |
| GitHub Runner OOM (7GB limit)  | Reduced Hub/node memory, limited parallel workers       |
| Large Allure artifacts         | Synced reports via Docker volume mapping                |
| Flaky tests on Grid            | Added explicit waits and retry logic in `wait_utils.py` |

---

## 📸 Allure Report (GIF)

![Allure Report Demo](https://github.com/<username>/<repo>/assets/allure-report-demo.gif)

---

## 📋 What I Learned

* Advanced Pytest (markers, fixtures, hooks, parallel runs)
* Dockerized Selenium Grid (Chrome-only, CI optimized)
* Debugging CI/CD memory issues on GitHub runners
* Allure Reporting integration
* Artifact management and caching in workflows

---

## 🌟 Future Improvements

* Resolve local Docker setup issues for cross-browser testing
* Integrate Jenkins pipeline
* Add Playwright for API testing
* Cloud Grid (BrowserStack/SauceLabs)

---

## 👩‍💻 Quick Recap for Interviews

* Framework: POM, fixtures, explicit waits, hooks, markers
* Docker: Hub + Chrome node (CI only), healthcheck
* CI/CD: Dockerized and non-Docker workflows, artifacts, caching
* Debugging: Solved Grid issues, memory limits, flaky tests

---

## 🏷 Badges

![Sequential Workflow](https://github.com/<username>/<repo>/actions/workflows/docker-selenium-grid.yml/badge.svg)
![Parallel Workflow](https://github.com/<username>/<repo>/actions/workflows/pytest-markers-parallel.yml/badge.svg)

(Replace `<username>` and `<repo>` with your GitHub details)

---


