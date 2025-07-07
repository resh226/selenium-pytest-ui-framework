"""
This module contains shared fixtures for pytest
✅ Works locally and in Docker/Selenium Grid
✅ Captures screenshots on test pass/fail
"""

import os
import pytest
import selenium.webdriver
import requests
import time
import allure
from datetime import datetime
from utils.file_utils import FileUtils

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# -----------------------------------------------------------------------------
# Wait for Selenium Grid readiness
# -----------------------------------------------------------------------------
def wait_for_grid():
    grid_url = os.getenv("GRID_URL", "http://selenium-hub:4444/wd/hub/status")
    print("🔄 Checking Selenium Grid readiness at:", grid_url)
    for i in range(10):
        try:
            response = requests.get(grid_url)
            if response.status_code == 200 and response.json()["value"]["ready"]:
                print("✅ Selenium Grid is ready!")
                return
        except Exception:
            print(f"⏳ Waiting for Selenium Grid... attempt {i+1}")
        time.sleep(5)
    raise Exception("❌ Selenium Grid was not ready after waiting 50 seconds.")

@pytest.fixture(scope="session", autouse=True)
def grid_check():
    if os.getenv("GRID_URL"):
        wait_for_grid()

# -----------------------------------------------------------------------------
# CONFIG FIXTURE
# -----------------------------------------------------------------------------
@pytest.fixture(scope="session")
def config():
    config = FileUtils.read_json('config/config.json')
    assert config['browser'] in ['Chrome', 'Firefox', 'Headless Chrome'], "Unsupported browser type"
    assert isinstance(config['implicit_wait'], int), "implicit_wait must be int"
    assert config['implicit_wait'] > 0, "implicit_wait must be > 0"
    assert 'base_url' in config and config['base_url'].strip(), "Missing or empty 'base_url'"
    return config

# -----------------------------------------------------------------------------
# BROWSER FIXTURE
# -----------------------------------------------------------------------------
@pytest.fixture(scope="function")
def browser(config):
    browser_type = config['browser']
    wait_time = config['implicit_wait']
    grid_url = os.getenv("GRID_URL", "http://selenium-hub:4444/wd/hub")
    is_grid = bool(os.getenv("GRID_URL"))

    print(f"🌐 Running on {'Selenium Grid' if is_grid else 'Local WebDriver'}")

    if is_grid:
        # Selenium Grid
        if browser_type == 'Chrome':
            capabilities = selenium.webdriver.DesiredCapabilities.CHROME.copy()
        elif browser_type == 'Firefox':
            capabilities = selenium.webdriver.DesiredCapabilities.FIREFOX.copy()
        else:
            raise ValueError(f"Unsupported browser for Grid: {browser_type}")

        b = selenium.webdriver.Remote(
            command_executor=grid_url,
            desired_capabilities=capabilities
        )
    else:
        # Local
        if browser_type == 'Chrome':
            service = ChromeService(ChromeDriverManager().install())
            b = selenium.webdriver.Chrome(service=service)
        elif browser_type == 'Firefox':
            service = FirefoxService(GeckoDriverManager().install())
            b = selenium.webdriver.Firefox(service=service)
        elif browser_type == 'Headless Chrome':
            options = selenium.webdriver.ChromeOptions()
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--window-size=1920,1080")
            service = ChromeService(ChromeDriverManager().install())
            b = selenium.webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser_type}")

    b.implicitly_wait(wait_time)
    b.maximize_window()

    yield b
    b.quit()

# -----------------------------------------------------------------------------
# SCREENSHOT HOOK
# -----------------------------------------------------------------------------
base_reports_dir = os.path.join(os.getcwd(), "reports", "screenshots")
passed_dir = os.path.join(base_reports_dir, "passed")
failed_dir = os.path.join(base_reports_dir, "failed")
os.makedirs(passed_dir, exist_ok=True)
os.makedirs(failed_dir, exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        browser = item.funcargs.get("browser", None)
        if browser:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = report.nodeid.replace("::", "_").replace("/", "_")
            screenshot_name = f"{test_name}_{timestamp}.png"
            folder = failed_dir if report.outcome == "failed" else passed_dir
            screenshot_path = os.path.join(folder, screenshot_name)
            try:
                browser.save_screenshot(screenshot_path)
                allure.attach.file(
                    screenshot_path,
                    name=f"{test_name}_{report.outcome}",
                    attachment_type=allure.attachment_type.PNG
                )
                print(f"📸 Screenshot saved: {screenshot_path} (Test {report.outcome.upper()})")
            except Exception as e:
                print(f"⚠️ Could not save screenshot: {e}")
