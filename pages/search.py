"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
import os
import random
import time

import allure
from selenium.webdriver import Keys
from locators.search_locators import DuckDuckGoSearchLocators as Loc
from utils.constants import get_default_timeout
# for importing helper functions for explicit waits mentioned in wait_utils.py
from utils.wait_utils import wait_for_element_visible
from utils.wait_utils import wait_for_element_clickable
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

        wait_for_element_visible(self.browser, Loc.SEARCH_INPUT, timeout = get_default_timeout())

    @allure.step("Search for phrase: {phrase}")
    def search(self, phrase):
        # Wait until the search input is clickable
        search_input = wait_for_element_clickable(self.browser, Loc.SEARCH_INPUT,timeout = get_default_timeout())
        search_input.clear()
        """
           Types the text character by character with a random delay,
           and waits explicitly for the search button/input to be interactable.this is done as step for CAPTHA
           prevention for anti bot detection when running in docker +Selenium grid
        """
        grid_url = os.getenv("GRID_URL", "http://selenium-hub:4444")
        IS_GRID = "selenium-hub" in grid_url or "localhost" in grid_url or "4444" in grid_url
        TYPING_DELAY = random.uniform(0.05, 0.2) if IS_GRID and random.choice([True, False]) else 0  # No delay locally
        for char in phrase:
            search_input.send_keys(char)
            if TYPING_DELAY:
                time.sleep(TYPING_DELAY)
        # types and presses Enter (Keys.RETURN simulates pressing Enter)
        search_input.send_keys(Keys.RETURN)

    @allure.step("Wait for search results to load")
    def search_result_wait(self):
        # WAIT: Ensure results have loaded
        wait_for_element_visible(self.browser, Loc.SEARCH_RESULTS, timeout = get_default_timeout())

    @allure.step("Wait for long query search results to load")
    def search_result_long_query_wait(self):
        # WAIT: Ensure results for long query have loaded
        wait_for_element_visible(self.browser, Loc.LONG_QUERY_SEARCH_RESULT,timeout = get_default_timeout())

    @allure.step("Wait for gibberish search results to load")
    def search_result_gibberish_wait(self):
        # WAIT: Ensure results for gibberish query have loaded
        wait_for_element_visible(self.browser, Loc.GIBBERISH_SEARCH_RESULT,timeout = get_default_timeout())