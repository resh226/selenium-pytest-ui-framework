"""
These tests cover DuckDuckGo searches using Page Object Model (POM).
This test verifies:
✅ GIVEN the DuckDuckGo home page is displayed
✅ WHEN the user searches for the phrase
✅ THEN the result page title and links should include the search phrase
"""

import pytest
import allure
import logging

# Importing Page Object classes
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
# importing file_utils.py to use helper functions to read json data fron file
from utils.file_utils import FileUtils

# setup for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load test data from JSON file
test_data = FileUtils.read_json('test_data/basic_cases.json')
search_phrases = test_data['search_phrases']

@allure.feature("DuckDuckGo Search")
@allure.story("Basic Search Functionality")
@allure.severity(allure.severity_level.CRITICAL)

#built-in Pytest decorator used for data-driven testing
@pytest.mark.parametrize('phrase', search_phrases)
@pytest.mark.smoke                #Core functionality, run first
@pytest.mark.order(1)             #execution order
def test_basic_duckduckgo_search(browser, config, phrase):
    """
    GIVEN the DuckDuckGo home page is displayed
    WHEN the user searches for a phrase
    THEN the title, search input, and result links should reflect the phrase
    """

    logger.info("Starting test for search phrase: '%s'", phrase)

    # GIVEN: Load the DuckDuckGo home page
    search_page = DuckDuckGoSearchPage(browser, config)
    search_page.load()
    logger.info("DuckDuckGo home page loaded.")

    # WHEN: Perform search with the provided phrase
    search_page.search(phrase)
    logger.info("Searched for phrase: '%s'", phrase)

    # WAIT: Ensure results have loaded
    search_page.search_result_wait()

    logger.info("Search results appeared on the page.")

    # THEN: Verify the page title contains the search phrase
    assert phrase in DuckDuckGoResultPage(browser).title(), f"Expected phrase '{phrase}' in page title."
    logger.info("Verified page title contains the phrase.")

    # AND: Verify the search input still contains the search phrase
    assert phrase == DuckDuckGoResultPage(browser).search_input_value(), "Search input does not retain the search phrase."
    logger.info("Verified search input retains the phrase.")

    # AND: Verify result links contain the search phrase
    titles = DuckDuckGoResultPage(browser).result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0, f"No search results contain the phrase '{phrase}'."
    logger.info("Verified at least one result link contains the phrase.")

    logger.info("Test for search phrase '%s' completed successfully.", phrase)
