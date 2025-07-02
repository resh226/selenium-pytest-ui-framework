# 🧪 my_first_seleniumpytest_project

A beginner-friendly Selenium UI Automation Framework project built with Python and Pytest.  
This repository is part of a real-world QA portfolio to showcase hands-on skills in test automation.

---

## 🔄 Project Status

This project is currently in progress, with basic framework setup complete and test logic under active development.

---

## ✅ Progress So Far

### ✅ Initial Setup Completed:
- `pipenv` used for virtual environment and dependency management  
- `webdriver-manager` installed for automatic browser driver handling  
- Reusable browser fixture added in `conftest.py` for clean setup/teardown  
- `test_search.py` updated to use the browser fixture  

### ✅ Page Object Model (POM) Implemented:
- Created `pages/` folder as a Python package with `__init__.py`  
- Added `DuckDuckGoSearchPage` (`search.py`) with methods: `load()` and `search(phrase)`  
- Added `DuckDuckGoResultPage` (`result.py`) with methods: `result_link_titles()`, `search_input_value()`, and `title()`  
- Locators written using `By.ID` and `By.CSS_SELECTOR`

### ✅ Functional Test Implemented:
- `test_search.py`:
  - Initializes both page objects  
  - Executes a full search scenario  
  - Uses assertions to verify title, input value, and link text matches  
  - Utilizes list comprehension for result filtering and validation  

### ✅ Explicit Waits Added:
- Integrated `WebDriverWait` and `expected_conditions` (`EC`) to replace brittle `time.sleep()`  
- Added `EC.title_contains(phrase)` to wait until page loads with dynamic content before asserting results  

---

## 📂 Project Structure (current)

my_first_seleniumpytest_project/
├── Pipfile
├── .gitignore
├── pages/
│ ├── init.py # Declares the folder as a Python package
│ ├── search.py # DuckDuckGoSearchPage implementation
│ └── result.py # DuckDuckGoResultPage implementation
├── tests/
│ ├── conftest.py # Contains browser fixture using WebDriver Manager
│ └── test_search.py # UI test using page objects and assertions
└── README.md


---

## ✅ Tech Stack

- Python 3.13  
- Selenium WebDriver  
- Pytest  
- WebDriver Manager (for ChromeDriver)  
- Pipenv  
- PyCharm IDE  

---

## 🪛 Debugging Notes & Fixes

- ✅ Test failed initially due to race condition between page load and assertions.
- ✅ Fixed by implementing **explicit waits** (`WebDriverWait`) instead of `time.sleep`.
- ✅ Used `EC.title_contains(phrase)` to wait for page title update after search.
- ✅ Verified if search phrase was typed using manual observation and element value extraction via `get_attribute('value')`.
- ✅ Refactored locator names to avoid typos (`searchbox_input`).

---

## 🚫 Common Errors to Avoid

| Issue | How to Fix |
|------|------------|
| `ModuleNotFoundError: No module named 'pages'` | Ensure `pages/` folder contains `__init__.py` |
| `find_element` fails too soon | Use `WebDriverWait` + `expected_conditions` for robust synchronization |
| Browser closes too early | Add waits or use `--headed` mode during debugging |
| Title assertion fails | Add debug print statements or assert actual vs expected with clear messages |
| Browser tabs already open | Not an issue; each WebDriver opens its own session |

---

## 📌 To-Do (Next Steps)

- ⏳ Finalize TODOs in page object methods  
- ⏳ Parameterize test cases for different search phrases  
- ⏳ Organize test data and selectors as needed  
- ⏳ Integrate Allure Reports with test execution  
- ⏳ Add parallel execution support and command-line flexibility  
- ⏳ Expand test coverage with more DuckDuckGo search scenarios  


🙋‍♀️ About Me
Reshma Sajeev🧪 ISTQB Certified | ✅ Postman Student Expert 🔗 https://www.linkedin.com/in/reshma-sajeev-889b7215b/
⭐ This repository is part of my personal QA portfolio to demonstrate hands-on experience in Selenium UI Automation using Python and Pytest

