"""
Shared fixtures for pytest
✅ Supports Local and Selenium Grid
✅ Captures screenshots on test pass/fail
"""

import os
import pytest
import selenium.webdriver
import allure
from datetime import datetime
from utils.file_utils import FileUtils

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from locators.result_locators import DuckDuckGoResultLocators as Loc

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

# -----------------------------------------------------------------------------
# GRID DETECTION FLAG
# -----------------------------------------------------------------------------
IS_GRID = bool(os.getenv("GRID_URL"))

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
    grid_url = os.getenv("GRID_URL", "http://selenium-hub:4444")

    print(f"🌐 Running on {'Selenium Grid' if IS_GRID else 'Local WebDriver'}")

    if IS_GRID:
        if browser_type == 'Chrome':
            options = ChromeOptions()
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--window-size=1920,1080")
        elif browser_type == 'Firefox':
            options = FirefoxOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
        else:
            raise ValueError(f"Unsupported browser for Grid: {browser_type}")

        # 🛠 Retry browser creation
        for attempt in range(3):
            try:
                print(f"🔄 Attempt {attempt + 1}: Starting browser session...")
                b = selenium.webdriver.Remote(
                    command_executor=grid_url,
                    options=options
                )
                print("✅ Browser session started successfully.")
                break
            except Exception as e:
                print(f"⚠️ Attempt {attempt + 1}: Browser failed to start - {e}")
                if attempt < 2:
                    print("⏳ Retrying in 5 seconds...")
                    import time
                    time.sleep(5)
                else:
                    print("❌ All attempts to start browser failed.")
                    raise
    else:
        if browser_type == 'Chrome':
            options = ChromeOptions()
            service = ChromeService(ChromeDriverManager().install())
            b = selenium.webdriver.Chrome(service=service, options=options)
        elif browser_type == 'Firefox':
            options = FirefoxOptions()
            service = FirefoxService(GeckoDriverManager().install())
            b = selenium.webdriver.Firefox(service=service, options=options)
        elif browser_type == 'Headless Chrome':
            options = ChromeOptions()
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

    try:
        captcha = b.find_element(*Loc.CAPTCHA_DIV)
        if captcha.is_displayed():
            print("⚠ CAPTCHA detected at global level. Skipping test.")
            import pytest
            pytest.skip("Skipped due to CAPTCHA detected on page.")
    except NoSuchElementException:
        pass  # No CAPTCHA, proceed normally

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
            except WebDriverException as e:
                if "invalid session id" in str(e).lower():
                    print("⚠️ Browser session ended before screenshot could be taken.")
                else:
                    print(f"⚠️ Could not save screenshot: {e}")
            except Exception as e:
                print(f"⚠️ Unexpected error saving screenshot: {e}")
