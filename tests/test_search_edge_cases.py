"""
Edge Case Tests for DuckDuckGo search using Page Object Model (POM).

These tests verify:
✅ Searching gibberish returns no results
✅ Searching a very long string doesn’t break the site
"""


import allure
import pytest
import logging

# Import Page Object classes
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

# importing file_utils.py to use helper functions to read json data fron file
from utils.file_utils import FileUtils

# setup for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load gibberish and long query from JSON
test_data = FileUtils.read_json('test_data/edge_cases.json')
long_query = test_data['long_query']
phrase = test_data['gibberish']


@allure.feature("DuckDuckGo Search")
@allure.story("Edge Case: No Results")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression                 #Covers boundary & negative scenarios
@pytest.mark.order(2)             #execution order
def test_search_no_results(browser, config):
    """
    GIVEN the DuckDuckGo home page is displayed
    WHEN the user searches for gibberish text
    THEN no results should be displayed
    """

    logger.info("Starting 'No Results' test with phrase: '%s'", phrase)

    search_page = DuckDuckGoSearchPage(browser, config)
    result_page = DuckDuckGoResultPage(browser)

    search_page.load()
    logger.info("DuckDuckGo home page loaded.")

    search_page.search(phrase)
    logger.info("Searched for gibberish phrase: '%s'", phrase)

    search_page.search_result_gibberish_wait()
    logger.info("Results page (or no results message) loaded.")

    result_count = result_page.result_count()
    logger.info("Result count: %s", result_count)

    assert result_count == 0, "Expected zero results for gibberish search."
    logger.info("Verified no results displayed for gibberish search.")


@allure.feature("DuckDuckGo Search")
@allure.story("Edge Case: Long String")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression                        #Covers boundary & negative scenarios
@pytest.mark.order(3)             #execution order
def test_search_long_string(browser, config):
    """
    GIVEN the DuckDuckGo home page is displayed
    WHEN the user searches with a very long string
    THEN the results page should load without errors
    """

    logger.info("Starting 'Long String' test with query length: %d", len(long_query))

    search_page = DuckDuckGoSearchPage(browser, config)
    result_page = DuckDuckGoResultPage(browser)

    search_page.load()
    logger.info("DuckDuckGo home page loaded.")

    search_page.search(long_query)
    logger.info("Searched with very long string.")

    search_page.search_result_long_query_wait()
    logger.info("Page loaded for long query search.")

    # Get the error message text from Page Object
    error_text = result_page.long_query_result_page()

    # Assert the expected text is present
    assert "Search query entered was too long" in error_text, f"Expected error message not found. Actual message: '{error_text}'"

    logger.info("Verified long query error message successfully.")

