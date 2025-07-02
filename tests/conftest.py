"""
This module contains shared fixtures for pytest.
"""

import json                    # To read and parse the config.json file
import pytest                  # Pytest is used for writing test cases and fixtures
import selenium.webdriver      # Selenium WebDriver API

# For Chrome browser automation
from selenium.webdriver.chrome.service import Service as ChromeService # Manages ChromeDriver service
from webdriver_manager.chrome import ChromeDriverManager # Auto-downloads ChromeDriver

# For Firefox browser automation
from selenium.webdriver.firefox.service import Service as FirefoxService # Manages ChromeDriver service
from webdriver_manager.firefox import GeckoDriverManager # Auto-downloads ChromeDriver

# ---------------------------
# CONFIG FIXTURE
# ---------------------------
@pytest.fixture(scope="session")   # This decorator tells pytest this is a reusable fixture
def config():
    """
    Loads the configuration from config.json once per test session.
    Validates expected keys and returns the config dictionary.
    """
    # Step 1: Read the config.json file from root directory
    with open('config.json') as f:
        config = json.load(f) #This line reads and parses a JSON file and stores its contents as a Python dictionary.

    # Step 2: Validate that the expected values are present and correct
    assert config['browser'] in ['Chrome', 'Firefox', 'Headless Chrome'], "Unsupported browser type in config.json"  #if assert is false then the custom error message wll be displayed "unsupported....."
    assert isinstance(config['implicit_wait'], int), "implicit_wait must be an integer"
    assert config['implicit_wait'] > 0, "implicit_wait must be greater than 0"

    # Step 3: Return config dictionary for use in other fixtures
    return config

# ---------------------------
# BROWSER FIXTURE
# ---------------------------
@pytest.fixture  # This decorator tells pytest this is a reusable fixture
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
        options.add_argument("headless")  # Enables headless mode (no UI)
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
