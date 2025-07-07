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
# Import helper functions
from utils.file_utils import FileUtils
from utils.wait_utils import WaitUtils  # <-- NEW: import our wait utility

#import locator
from locators.result_locators import DuckDuckGoResultLocators as Loc

# setup for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load test data from JSON file
test_data = FileUtils.read_json('test_data/basic_cases.json')
search_phrases = test_data['search_phrases']


@allure.feature("DuckDuckGo Search")
@allure.story("Basic Search Functionality")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('phrase', search_phrases)  # Data-driven testing
@pytest.mark.smoke                # Core functionality, run first
@pytest.mark.order(1)             # Execution order
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

    # WAIT: Ensure results block is visible
    search_page.search_result_wait()
    logger.info("Search results appeared on the page.")

    # WAIT: Ensure page title contains search phrase
    WaitUtils.wait_for_title_contains(browser, phrase, timeout=30)

    # THEN: Verify the page title contains the search phrase
    actual_title = DuckDuckGoResultPage(browser).title()
    assert phrase.lower() in actual_title.lower(), \
        f"Expected phrase '{phrase}' in page title, got '{actual_title}'"
    logger.info("Verified page title contains the phrase.")

    # WAIT: Ensure search input contains search phrase
    WaitUtils.wait_for_input_contains(browser, Loc.SEARCH_INPUT, phrase, timeout=30)

    actual_input = DuckDuckGoResultPage(browser).search_input_value()
    # AND: Verify the search input still contains the search phrase
    assert phrase.lower() in actual_input.lower(), \
        f"Expected '{phrase}' in search input, but got '{actual_input}'"
    logger.info("Verified search input retains the phrase.")

    # AND: Verify result links contain the search phrase
    titles = DuckDuckGoResultPage(browser).result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0, f"No search results contain the phrase '{phrase}'."
    assert matches, f"No search result titles contained the phrase '{phrase}'. Found: {titles}"
    logger.info("Verified at least one result link contains the phrase.")

    logger.info("Test for search phrase '%s' completed successfully.", phrase)
