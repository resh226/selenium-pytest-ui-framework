"""
This module contains shared fixtures for pytest.
"""

import os

import pytest                  # Pytest is used for writing test cases and fixtures
import selenium.webdriver      # Selenium WebDriver API

from utils.file_utils import FileUtils  # importing file_utils.py to use helper functions to read json data fron file

# For Chrome browser automation
from selenium.webdriver.chrome.service import Service as ChromeService # Manages ChromeDriver service
from webdriver_manager.chrome import ChromeDriverManager # Auto-downloads ChromeDriver

# For Firefox browser automation
from selenium.webdriver.firefox.service import Service as FirefoxService # Manages ChromeDriver service
from webdriver_manager.firefox import GeckoDriverManager # Auto-downloads ChromeDriver



# ---------------------------
# CONFIG FIXTURE
# ---------------------------

# This decorator tells pytest this is a reusable fixture
# This ensures each test runs in its own browser instance.
@pytest.fixture(scope="session")
def config():
    """
    Loads the configuration from config.json once per test session.
    Validates expected keys and returns the config dictionary.
    """
    # Step 1: Read the config.json file from root directory
    config = FileUtils.read_json('config/config.json')

    # Step 2: Validate that the expected values are present and correct
    assert config['browser'] in ['Chrome', 'Firefox', 'Headless Chrome'], "Unsupported browser type in config.json"  #if assert is false then the custom error message wll be displayed "unsupported....."
    assert isinstance(config['implicit_wait'], int), "implicit_wait must be an integer"
    assert config['implicit_wait'] > 0, "implicit_wait must be greater than 0"
    assert 'base_url' in config, "Missing 'base_url' in config.json"
    assert isinstance(config['base_url'], str), "'base_url' must be a string"
    assert config['base_url'].strip(), "'base_url' cannot be empty"
    # Step 3: Return config dictionary for use in other fixtures
    return config

# ---------------------------
# BROWSER FIXTURE
# ---------------------------
# This decorator tells pytest this is a reusable fixture
# Scope = function, ensures each test runs in its own browser instance.
@pytest.fixture(scope="function")
def browser(config):

    # 🛠 SETUP PHASE: Prepare things before the test starts

    """
    Initializes the WebDriver instance based on the browser specified in config.json.
    Applies implicit wait time and ensures proper cleanup after test execution.
    """

    # Read the values from config.json
    browser_type = config['browser']
    wait_time = config['implicit_wait']

    # Step 1: Initialize the correct WebDriver based on browser type
    if browser_type == 'Chrome':
        # Automatically download the correct version of ChromeDriver and Wrap it with ChromeService so Selenium can use it properly
        service = ChromeService(ChromeDriverManager().install())
        # Open a new Chrome browser with that service
        b = selenium.webdriver.Chrome(service=service)

    elif browser_type == 'Firefox':
        # Automatically download the correct version of firefoxdriver and Wrap it with Firefoxservice so Selenium can use it properly
        service = FirefoxService(GeckoDriverManager().install())
        # Open a new Firefox browser with that service
        b = selenium.webdriver.Firefox(service=service)

    elif browser_type == 'Headless Chrome':
        options = selenium.webdriver.ChromeOptions()
        #.add_argument() is a method of ChromeOptions (or FirefoxOptions) used to customize the browser behavior when Selenium launches it.
        options.add_argument("--headless=new")  # more stable than old "headless"
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")

        service = ChromeService(ChromeDriverManager().install())
        b = selenium.webdriver.Chrome(service=service, options=options)

    else:
        raise Exception(f"Unsupported browser: {browser_type}")

    # Step 2: Apply implicit wait time from config.json which try to find elements for up to 10 seconds
    b.implicitly_wait(wait_time)

    # Maximize browser window
    b.maximize_window()

    # Step 3: Give this browser to the test function
    yield b

    # Step 4: Cleanup phase — close the browser after test
    b.quit()

#---------------------------------------------------------------------------------
#            SCREENSHOTS FOR PASSED AND FAILED TEST Cases
#---------------------------------------------------------------------------------

import allure                                # For attaching screenshots to Allure
from datetime import datetime                # For timestamped filenames

# 📂 Define separate folders for passed and failed screenshots
passed_dir = os.path.join(os.getcwd(), "reports", "screenshots","passed")
failed_dir = os.path.join(os.getcwd(), "reports", "screenshots","failed")
os.makedirs(passed_dir, exist_ok=True)       # Create folder if it doesn’t exist
os.makedirs(failed_dir, exist_ok=True)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    📸 Pytest hook to:
    ✅ Take screenshot on test failure or success
    ✅ Save in separate folders for Pass/Fail
    ✅ Attach screenshots to Allure reports
    """

    outcome = yield                          # Run the test and get result
    report = outcome.get_result()            # Get result object (pass/fail/skip)

    if report.when == "call":  # Only after test body (not setup/teardown)
        browser = item.funcargs.get("browser")  # Get browser fixture

        if browser:  # Proceed only if browser exists
            # 🕒 Timestamp for unique filenames
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # 📝 Descriptive filename: test name + outcome + timestamp
            test_name = report.nodeid.replace("::", "_").replace("/", "_")
            screenshot_name = f"{test_name}_{timestamp}.png"

            # 📂 Choose folder based on test outcome
            if report.when == "call":
                if report.outcome == "failed":
                    folder = failed_dir
                else:
                    folder = passed_dir

            # 📦 Full path to save screenshot
            screenshot_path = os.path.join(folder, screenshot_name)

            # 📸 Save screenshot
            browser.save_screenshot(screenshot_path)

            # 📎 Attach screenshot to Allure report
            allure.attach.file(
                screenshot_path,
                name=f"{test_name}_{report.outcome}",
                attachment_type=allure.attachment_type.PNG
            )

            # 📝 Print to console for reference
            print(f"📸 Screenshot saved: {screenshot_path} (Test {report.outcome.upper()})")
