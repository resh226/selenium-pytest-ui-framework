"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""
from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:

    #locators
    result_titles = (By.CSS_SELECTOR, 'a.result__a')
    search_input = (By.ID, 'search_form_input')

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        result_of_titles = self.browser.find_elements(*self.result_titles) #gets all matching elements,*->unpacks the tuple (By, value)
        return [link.text for link in result_of_titles] #List comprehension returns their text

    def search_input_value(self):
        input_value = self.browser.find_element(*self.search_input) #gets matching elements,*->unpacks the tuple (By, value)
        return input_value.get_attribute('value') #.get_attribute('value') is used for input fields (since .text returns empty)

    def title(self):
        return self.browser.title     # Return the title of the current page displayed in the browser tab
