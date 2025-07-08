
import allure
import pytest
import logging

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

# importing file_utils.py to use helper functions to read json data fron file
from utils.file_utils import FileUtils

# setup for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load search phrases from JSON
test_data = FileUtils.read_json('test_data/flow_cases.json')
search_phrase = test_data['search_phrases']
expected_url_keyword = test_data['expected_url_keyword']

@allure.feature("DuckDuckGo Search")
@allure.story("Navigation to First Result")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.flow                       #End-to-end flow test
@pytest.mark.order(4)                   #execution order
def test_search_flow(browser, config):
    """
    GIVEN the DuckDuckGo home page is displayed
    WHEN the user searches for 'Selenium WebDriver'
    AND clicks the first result link
    THEN the browser navigates to a page containing 'selenium' in the URL
    """

    logger.info("Starting navigation test with search phrase: '%s'", search_phrase)

    # Navigate to DuckDuckGo first before clearing storage
    browser.get("https://duckduckgo.com")
    browser.delete_all_cookies()
    browser.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")

    search_page = DuckDuckGoSearchPage(browser, config)
    result_page = DuckDuckGoResultPage(browser)

    search_page.load()
    # Reset cookies and storage for session reuse
    browser.delete_all_cookies()
    browser.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
    logger.info("DuckDuckGo home page loaded.")

    search_page.search(search_phrase)
    logger.info("Searched for phrase: '%s'", search_phrase)

    #wait till result titles are loaded
    search_page.search_result_wait()
    logger.info("Results page loaded.")

    # Click the first result link
    result_page.click_first_result()
    logger.info("Clicked first result link.")

    current_url = browser.current_url

    assert expected_url_keyword in current_url.lower(), f"Expected '{expected_url_keyword}' in URL, got: {current_url}"
    logger.info("Verified navigation to URL: %s", current_url)
