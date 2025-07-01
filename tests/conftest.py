import pytest  # Pytest is used for writing test cases and fixtures
from selenium import webdriver  # Selenium WebDriver API
from webdriver_manager.chrome import ChromeDriverManager  # Auto-downloads ChromeDriver
from selenium.webdriver.chrome.service import Service as ChromeService  # Manages ChromeDriver service

@pytest.fixture  # This decorator tells pytest this is a reusable fixture
def browser():
    # 🛠 SETUP PHASE: Prepare things before the test starts

    # 1. Automatically download the correct version of ChromeDriver
    #    Wrap it with ChromeService so Selenium can use it properly
    service = ChromeService(ChromeDriverManager().install())

    # 2. Open a new Chrome browser with that service
    b = webdriver.Chrome(service=service)

    # 3. Set a wait time: try to find elements for up to 10 seconds
    b.implicitly_wait(10)

    #  YIELD: Give this browser to the test function
    yield b

    #  CLEANUP PHASE: Run this after the test finishes
    # 4. Close the browser completely (including all windows/tabs)
    b.quit()
