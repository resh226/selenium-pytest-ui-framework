
import allure
import logging
import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

# importing file_utils.py to use helper functions to read json data fron file
from utils.file_utils import FileUtils

# setup for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load search phrases from JSON
test_data = FileUtils.read_json('test_data/failure_case.json')
search_phrase = test_data['search_phrases']
duckduckgo_url = test_data['duckduckgo_url']

@allure.feature("Search Failure Scenarios")
@allure.story("Verify first result URL belongs to DuckDuckGo domain")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.negative                                 #Expected failures / negative paths
@pytest.mark.order(5)             #execution order
def test_first_result_url_is_duckduckgo(browser, config):
    """
    Verifies that after clicking the first search result,
    the navigated URL belongs to DuckDuckGo domain.
    This test will fail naturally because most first results are external links.
    """
    logger.info("Starting navigation test with search phrase: '%s'", search_phrase)

    search_page = DuckDuckGoSearchPage(browser, config)
    result_page = DuckDuckGoResultPage(browser)

    search_page.load()
    logger.info("DuckDuckGo home page loaded.")

    search_page.search(search_phrase)
    logger.info("Searched for phrase: '%s'", search_phrase)

    search_page.search_result_wait()
    logger.info("Results page loaded.")

    # Click the first result link
    result_page.click_first_result()
    logger.info("Clicked first result link.")

    current_url = browser.current_url

    # Assert navigated URL starts with DuckDuckGo domain
    assert current_url.startswith(duckduckgo_url), f"Expected DuckDuckGo domain, but navigated to '{current_url}'"
