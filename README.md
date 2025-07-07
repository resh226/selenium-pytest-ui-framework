🧪 my_first_seleniumpytest_project
A beginner-friendly Selenium UI Automation Framework project built with Python and Pytest.
This repository is part of a real-world QA portfolio showcasing hands-on skills in test automation and modern framework design.

🔄 Project Status (In Progress)
🚀 Core framework implemented with:

Page Object Model (POM)
Cross-browser configuration (Chrome, Firefox, Headless Chrome)
Test parameterization for data-driven testing
Parallel execution using pytest-xdist


✅ Features Implemented (Current)
🏁 Initial Setup
Virtual environment & dependency management with pipenv
Installed webdriver-manager for ChromeDriver & GeckoDriver auto-management
Added conftest.py with reusable browser fixture (setup & teardown using yield)
test_search.py uses fixture injection for browser management

📦 Page Object Model (POM)
Modular structure with pages/ package
search.py: DuckDuckGoSearchPage – methods: load(), search(phrase)
result.py: DuckDuckGoResultPage – methods: result_link_titles(), search_input_value(), title()
Clean locator strategy using By.ID, By.CSS_SELECTOR

🔥 Test Parameterization
Used @pytest.mark.parametrize for running the same test with multiple search phrases.

python
@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_search(browser, phrase):
    ...

⚡ Parallel Execution (pytest-xdist)
Installed pytest-xdist for faster test execution
Ran tests in parallel with:
pytest -n 2

⏳ Robust Synchronization
Replaced time.sleep() with WebDriverWait & expected_conditions
Ensures dynamic waits for faster & stable test runs.

🌐 Cross-Browser  Support
config.json controls browser choice: Chrome, Firefox

📂 Project Structure

```
my_first_seleniumpytest_project/
├── Pipfile
├── config.json              # Browser & wait settings
├── .gitignore
├── pages/
│   ├── __init__.py          # Declares as package
│   ├── search.py            # DuckDuckGoSearchPage (POM)
│   └── result.py            # DuckDuckGoResultPage (POM)
├── tests/
│   ├── conftest.py          # Fixtures for config & browser setup
│   └── test_search.py       # UI test scenario with page objects
└── README.md

```

🧰 Tech Stack
Python 3.13
Selenium WebDriver
Pytest
WebDriver Manager
pytest-xdist
Pipenv
PyCharm IDE

📚 Concepts Demonstrated
| Concept                   | Description                                              |
|---------------------------|----------------------------------------------------------|
| ✅ Selenium WebDriver      | Browser automation using Chrome/Firefox                  |
| ✅ Page Object Model (POM) | Modular and reusable test structure                      |
| ✅ Pytest Fixtures         | Clean setup/teardown with `yield`                        |
| ✅ Explicit Waits (EC)     | Dynamic waits with `WebDriverWait`                       |
| ✅ External Configuration  | `config.json` for browser & timeout management           |
| ✅ Test Parameterization   | Multiple test data inputs via `@pytest.mark.parametrize` |
| ✅ Parallel Test Execution | Faster testing using `pytest-xdist -n <num>`             |



🪛 Debugging Notes & Fixes
| Issue                               | Resolution                                          |
|-------------------------------------|-----------------------------------------------------|
| Race condition between load & assert| Added `WebDriverWait` with `EC.title_contains()`    |
| Browser not maximizing              | Added `maximize_window()` in `conftest.py`          |
| Flaky headless parallel tests       | Used explicit waits and isolated browser sessions   |
| Module import errors                | Added `__init__.py` in `pages/` folder              |


🚫 Common Pitfalls & Fixes
| Error                                       | Solution                                           |
|---------------------------------------------|----------------------------------------------------|
| ModuleNotFoundError: No module named 'pages'| Ensure `pages/__init__.py` is present              |
| Elements not found                          | Replace `time.sleep()` with `WebDriverWait` + EC   |
| Browser closing too early                   | Use `yield` fixtures and `--headed` mode for debugging|
| Title assertion fails                       | Debug actual vs expected title with print statements|
| Config file errors                          | Validate `config.json` values in the fixture       |


📌 Next Steps
📋 Integrate Allure Reports for rich test reporting
🚀 Set up CI/CD pipeline with GitHub Actions for automated parallel runs
🧪 Expand test suite with additional search scenarios and negative test cases



🙋‍♀️ About Me

Reshma Sajeev🧪 ISTQB Certified | ✅ Postman Student Expert 🔗 https://www.linkedin.com/in/reshma-sajeev-889b7215b/
⭐ This repository is part of my personal QA portfolio to demonstrate hands-on experience in Selenium UI Automation using Python and Pytest