"""
This module contains all locators for the DuckDuckGo Search Page.
Organized as constants for easy maintenance and reuse.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoSearchLocators:
    """
    Locators for the DuckDuckGo Search Page.
    """
    SEARCH_INPUT = (By.ID, "searchbox_input")
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'a.result__a')  # Search result links
    LONG_QUERY_SEARCH_RESULT= (By.XPATH, "//p[contains(text(), 'Search query entered was too long')]")
    GIBBERISH_SEARCH_RESULT = (By.CSS_SELECTOR, "div.results--main")