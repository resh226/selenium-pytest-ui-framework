"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
import selenium

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class DuckDuckGoSearchPage:

    url = 'http://duckduckgo.com/'
    #locators
    searchbox_input = (By.ID, 'searchbox_input')

    #constructor
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url) # loads page

    def search(self, phrase):
        search_input = self.browser.find_element(*self.searchbox_input) #unpacks the tuple (By, value)
        search_input.send_keys(phrase + Keys.RETURN) # types and presses Enter (Keys.RETURN simulates pressing Enter)
        #explicit wait using webdriverwait and expected conditions
        WebDriverWait(self.browser, 10).until(EC.title_contains("panda")) #This waits up to 10 seconds for the page title to contain "panda".