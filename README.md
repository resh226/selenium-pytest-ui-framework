🧪 my_first_seleniumpytest_project  
A beginner-friendly Selenium UI Automation Framework project built with Python and Pytest.  
This repository is part of a real-world QA portfolio to showcase hands-on skills in test automation.

🔄 Project Status  
This project is currently in progress, with basic framework setup complete and test logic under active development.

✅ Progress So Far  
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
- `test_search.py` now:
  - Initializes both page objects  
  - Executes a full search scenario  
  - Uses assertions to verify title, input value, and result link text  
  - Utilizes list comprehension for result filtering and validation  

### ✅ Waits and Synchronization:
- Implemented **explicit wait** using `WebDriverWait` and `expected_conditions`:
  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC
  
  WebDriverWait(self.browser, timeout=10).until(EC.title_contains("panda"))
This ensures the test waits for the search results page to load before proceeding with validations.

📂 Project Structure (current)
my_first_seleniumpytest_project/
├── Pipfile
├── Pipfile.lock
├── .gitignore
├── pages/
│   ├── __init__.py               # Declares the folder as a Python package
│   ├── search.py                 # DuckDuckGoSearchPage implementation
│   └── result.py                 # DuckDuckGoResultPage implementation
├── tests/
│   ├── conftest.py               # Contains browser fixture using WebDriver Manager
│   └── test_search.py            # UI test using page objects and assertions
└── README.md

✅ Tech Stack

Python 3.13
Selenium WebDriver
Pytest
WebDriver Manager (for ChromeDriver)
Pipenv
PyCharm IDE

🐞 Debugging & Issue Resolution

✅ Initial ImportError for pages.result: Fixed by adding __init__.py in the pages/ folder to make it a proper Python package

✅ Test failed due to early browser close: Added time.sleep() for debugging and later replaced with WebDriverWait

✅ Phrase not typed: Investigated by inserting temporary delays and logging, then replaced with proper wait conditions

✅ Multiple browser tabs open: Confirmed it doesn’t affect test runs as each test launches its own controlled session

🚫 Common Errors to Avoid

❌ Using browser instead of self.browser inside page object methods
✅ Always use self.browser to refer to the WebDriver instance passed to the class.

# Incorrect
WebDriverWait(browser, 10).until(...)
# Correct
WebDriverWait(self.browser, 10).until(...)

❌ Using time.sleep() for waits
✅ Replace with WebDriverWait and expected_conditions for robust and reliable waiting.

❌ Accessing elements before the page loads
✅ Always wait for page elements or titles to load using proper wait strategies

📌 To-Do (Next Steps)

⏳ Finalize TODOs in page object methods
⏳ Parameterize test cases for different search phrases
⏳ Organize test data and selectors as needed
⏳ Integrate Allure Reports with test execution
⏳ Add parallel execution support and command-line flexibility
⏳ Expand test coverage with more DuckDuckGo search scenarios

