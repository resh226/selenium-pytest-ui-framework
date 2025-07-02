# 🧪 my_first_seleniumpytest_project

A beginner-friendly Selenium UI Automation Framework project built with Python and Pytest.  
This repository is part of a real-world QA portfolio to showcase hands-on skills in test automation and best practices in framework design.

---

## 🔄 Project Status

🚧 This project is currently in progress. Core framework structure and search scenario logic have been implemented. Browser configuration and dynamic waits are now functional via external config files.

---

## ✅ Progress So Far

### ✅ Initial Setup:
- `pipenv` used for virtual environment and dependency management  
- `webdriver-manager` installed to auto-download ChromeDriver and GeckoDriver  
- `conftest.py` added with reusable browser fixture using `yield` for setup and teardown  
- `test_search.py` updated to use browser fixture

### ✅ Page Object Model (POM) Implemented:
- Created `pages/` folder with `__init__.py` to define it as a package  
- `search.py`: `DuckDuckGoSearchPage` with methods `load()` and `search(phrase)`  
- `result.py`: `DuckDuckGoResultPage` with methods `result_link_titles()`, `search_input_value()`, and `title()`  
- Used `By.ID` and `By.CSS_SELECTOR` locators

### ✅ Functional Test Implemented:
- `test_search.py`:
  - Initializes both page objects
  - Executes a complete search and asserts:
    - Page title contains search term  
    - Input field retains search value  
    - First result contains search phrase  
  - Uses list comprehension for text extraction

### ✅ Explicit Waits Added:
- Integrated `WebDriverWait` and `expected_conditions` (EC) for dynamic synchronization  
- Used `EC.title_contains(phrase)` to replace `time.sleep()`

### ✅ Configuration Management:
- Created `config.json` at root level to define:
  - Browser type (`Chrome`, `Firefox`, or `Headless Chrome`)  
  - Implicit wait time (in seconds)
- Updated `conftest.py` to:
  - Load and validate `config.json` using a session-scoped fixture  
  - Read browser type and wait dynamically  
  - Support multiple browsers using `if-else` logic  
  - Add browser maximization for full-screen testing

---

📂 Project Structure (current)

```
my_first_seleniumpytest_project/
├── Pipfile
├── config.json # External config for browser and wait settings
├── .gitignore
├── pages/
│ ├── init.py # Declares the folder as a Python package
│ ├── search.py # DuckDuckGoSearchPage (POM)
│ └── result.py # DuckDuckGoResultPage (POM)
├── tests/
│ ├── conftest.py # Fixtures for config and browser setup
│ └── test_search.py # UI test scenario using page objects
└── README.md

```
---

## ✅ Tech Stack

- Python 3.13  
- Selenium WebDriver  
- Pytest  
- WebDriver Manager  
- Pipenv  
- PyCharm IDE  

---

## 📚 Concepts Covered So Far

| Concept | Description |
|--------|-------------|
| ✅ Selenium WebDriver | Used for browser automation |
| ✅ Page Object Model (POM) | Modular and reusable test structure |
| ✅ Pytest Fixtures | Clean test setup/teardown using `yield` and shared state |
| ✅ Explicit Waits (EC) | Reliable waits for dynamic content with `WebDriverWait` |
| ✅ External Configuration | `config.json` used to pass dynamic inputs (browser, wait time) |
| ✅ Cross-Browser Execution | Supports Chrome, Firefox, and Headless Chrome |
| ✅ Dynamic Test Debugging | Used `get_attribute('value')` to inspect inputs |
| ✅ Headless Mode Support | Seamless switch to headless via config |

---

## 🪛 Debugging Notes & Fixes

- ✅ Test failed initially due to race condition between page load and assertions.
- ✅ Fixed by implementing **explicit waits** (`WebDriverWait`) instead of `time.sleep`.
- ✅ Used `EC.title_contains(phrase)` to wait for page title update after search.
- ✅ Verified if search phrase was typed using manual observation and element value extraction via `get_attribute('value')`.
- ✅ Browser not maximizing, Added `maximize_window()` in `conftest.py`

---

## 🚫 Common Errors to Avoid

| Issue                                          | How to Fix                                                                  |
|------------------------------------------------|-----------------------------------------------------------------------------|
| `ModuleNotFoundError: No module named 'pages'` | Ensure `pages/` folder contains `__init__.py`                               |
| `find_element` fails too soon                  | Use `WebDriverWait` + `expected_conditions` for robust synchronization      |
| Browser closes too early                       | Add waits or use `--headed` mode during debugging                           |
| Title assertion fails                          | Add debug print statements or assert actual vs expected with clear messages |
| Browser tabs already open                      | Not an issue; each WebDriver opens its own session                          |
| Config file errors                             | Validate values in `config()` fixture before using                          |

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

