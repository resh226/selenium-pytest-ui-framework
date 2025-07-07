"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
import allure
from selenium.webdriver import Keys
from locators.search_locators import DuckDuckGoSearchLocators as Loc
from utils.wait_utils import WaitUtils             # for importing helper functions for explicit waits mentioned in wait_utils.py
from base.base_page import BasePage  #inheritance

class DuckDuckGoSearchPage(BasePage):

    #constructor
    def __init__(self, browser, config):
            super().__init__(browser)   #super() → Finds parent BasePage
            self.url = config['base_url']

    @allure.step("Load DuckDuckGo home page")
    def load(self):
        self.navigate(self.url) # loads page
        # Wait until the search input is visible before continuing
        WaitUtils.wait_for_element_visible(self.browser, Loc.SEARCH_INPUT)

    @allure.step("Search for phrase: {phrase}")
    def search(self, phrase):
        # Wait until the search input is clickable
        search_input = WaitUtils.wait_for_element_clickable(self.browser, Loc.SEARCH_INPUT)
        search_input.clear()
        # types and presses Enter (Keys.RETURN simulates pressing Enter)
        search_input.send_keys(phrase + Keys.RETURN)

    @allure.step("Wait for search results to load")
    def search_result_wait(self):
        # WAIT: Ensure results have loaded
        WaitUtils.wait_for_element_visible(self.browser, Loc.SEARCH_RESULTS,90)

    @allure.step("Wait for long query search results to load")
    def search_result_long_query_wait(self):
        # WAIT: Ensure results for long query have loaded
        WaitUtils.wait_for_element_visible(self.browser, Loc.LONG_QUERY_SEARCH_RESULT)

    @allure.step("Wait for gibberish search results to load")
    def search_result_gibberish_wait(self):
        # WAIT: Ensure results for gibberish query have loaded
        WaitUtils.wait_for_element_visible(self.browser, Loc.GIBBERISH_SEARCH_RESULT)