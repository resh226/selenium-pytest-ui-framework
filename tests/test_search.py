"""
These tests cover DuckDuckGo searches using Page Object Model (POM).
This test is for the below testcase:-
# Given the DuckDuckGo home page is displayed
# WHEN: The user searches for the phrase "panda"
# THEN: The search result page title should include the search phrase
# AND: The search input should still contain the search phrase
# AND: The result links should include the search phrase

"""

# Importing the page object classes
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

# browser parameter passed as this is a fixture written in conftest.py
# What pytest will do anytime it sees a test case with an argument,
# it will check that argument's name against all available fixtures in the project, which will come from conftest.py.
def test_basic_duckduckgo_search(browser):

    # Create instances of our page objects with the shared browser fixture
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Define the search keyword we want to test
    phrase = "panda"


    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # WHEN: The user searches for the phrase "panda"
    search_page.search(phrase)

    # THEN: The search result page title should include the search phrase
    assert phrase in result_page.title()

    # AND: The search input should still contain the search phrase
    assert phrase == result_page.search_input_value()

    # AND: The result links should include the search phrase
    titles = result_page.result_link_titles()
    # Filter titles that contain the search phrase (case-insensitive)(uses list comprehension in python)
    matches = [t for t in titles if phrase.lower() in t.lower()]
    # Assert that at least one matching title exists
    assert len(matches) > 0

