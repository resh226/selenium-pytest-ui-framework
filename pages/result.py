"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""
import allure

from locators.result_locators import DuckDuckGoResultLocators as Loc
# for importing helper functions for explicit waits mentioned in wait_utils.py
from utils.wait_utils import (wait_for_element_visible,wait_for_element_clickable,wait_for_url_to_change)
from base.base_page import BasePage   #inheritace

class DuckDuckGoResultPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)  #super() → Finds parent BasePage

    @allure.step("Get all visible search result titles")
    def result_link_titles(self):
        """
        Gets all visible search result link titles from the results page.

        :return: List of visible result link texts.
        :raises AssertionError: If no results are visible within timeout.
        """
        wait_for_element_visible(self.browser, Loc.RESULT_TITLES)

        # Get all result link elements
        result_elements = self.browser.find_elements(*Loc.RESULT_TITLES)

        # Filter only visible links and extract their text
        visible_titles = [link.text for link in result_elements if link.is_displayed()]

        # Assert at least one visible search result exists
        assert visible_titles, "No visible search result titles found."

        return visible_titles

    @allure.step("Get current value from the search input field")
    def search_input_value(self):
        """
        Returns the current value entered in the search input field.

        :return: String value from the search input field.
        """
        wait_for_element_visible(self.browser, Loc.SEARCH_INPUT)
        input_field = self.browser.find_element(*Loc.SEARCH_INPUT)
        return input_field.get_attribute('value')

    @allure.step("Get current page title")
    def title(self):
        return self.get_title() # Return the title of the current page displayed in the browser tab

    @allure.step("Get count of search result links")
    def result_count(self):
        """
           Returns the number of search result links on the page for gibberish query.
           If no results are found, returns 0.
           """
        try:
            # Look for all result links (if any)
            links = self.browser.find_elements(*Loc.RESULT_TITLES)
            count = len(links)
            return count
        except:
            # In case the container exists but no links
            return 0

    @allure.step("Check for long query error message")
    def long_query_result_page(self):
        """
        Checks if the results page is loaded with error for long query search results.
        """
        long_query_message = self.browser.find_element(*Loc.LONG_QUERY_ERROR)
        error_text = long_query_message.text
        return error_text

    @allure.step("Click first visible search result link")
    def click_first_result(self):
        """
        Clicks the first visible search result link.
        """
        starting_url = self.browser.current_url
        first_link = wait_for_element_clickable(self.browser, Loc.FIRST_RESULT_LINK)
        first_link.click()

        # Wait for URL to change after navigation
        wait_for_url_to_change(self.browser, starting_url)