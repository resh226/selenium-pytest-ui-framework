"""
This module contains all locators for the DuckDuckGo Result Page.
Organized as constants for easy maintenance and reuse.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoResultLocators:
    """
    Locators for the DuckDuckGo Result Page.
    """
    RESULT_TITLES = (By.CSS_SELECTOR, "ol.react-results--main li[data-layout='organic'] a")  # Search result links
    SEARCH_INPUT = (By.ID, 'search_form_input')       # Search input box on result page
    LONG_QUERY_ERROR = (By.XPATH, "//p[contains(text(), 'Search query entered was too long')]")  # Error for long queries
    FIRST_RESULT_LINK = (By.XPATH, "//article[@id='r1-0']//a[@data-testid='result-title-a']")
    CAPTCHA_DIV = (By.CSS_SELECTOR, "div.captcha__container")