"""
wait_utils.py
==============

This module provides utility functions for explicit waits using Selenium WebDriver.

It centralizes WebDriverWait logic for visibility, presence, clickability,
URL changes, and title updates—improving readability and maintainability
across page objects and tests.

Typical usage:
--------------
from utils.wait_utils import WaitUtils

# Wait for visible element (user-facing UI)
element = WaitUtils.wait_for_element_visible(browser, locator)

# Wait for presence in DOM (even if hidden)
element = WaitUtils.wait_for_element_presence(browser, locator)

# Wait for clickable element
clickable = WaitUtils.wait_for_element_clickable(browser, locator)

# Wait for URL change
WaitUtils.wait_for_url_to_change(browser, starting_url)

# Wait for title to contain text
WaitUtils.wait_for_title_contains(browser, "Welcome")

#Wait for search input to contain: '{text}'
wait_for_input_contains(browser, locator, text, timeout=10):

"""
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WaitUtils:

    @staticmethod
    @allure.step("Wait for element visible: {locator} (timeout={timeout}s)")
    @staticmethod
    def wait_for_element_visible(browser, locator, timeout=90, retries=2):
        """
        Waits for the element to be visible (present in DOM and not hidden).
        Retries if TimeoutException occurs.
        Returns the WebElement if successful.
        """
        attempt = 0
        while attempt < retries:
            try:
                return WebDriverWait(browser, timeout).until(
                    EC.visibility_of_any_elements_located(locator)
                )
            except TimeoutException:
                print(f"⚠️ Attempt {attempt + 1}: Element {locator} not visible after {timeout}s")
                attempt += 1
                if attempt == retries:
                    raise AssertionError(f"❌ Element {locator} not visible after {timeout * retries}s")

    @staticmethod
    @allure.step("Wait for element presence: {locator} (timeout={timeout}s)")
    def wait_for_element_presence(browser, locator, timeout=90):
        """
        Waits for the element to be present in the DOM (visibility not required).
        Returns the WebElement if successful.
        """
        try:
            return WebDriverWait(browser, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"❌ Element {locator} not present in DOM after {timeout}s")

    @staticmethod
    @allure.step("Wait for element clickable: {locator} (timeout={timeout}s)")
    def wait_for_element_clickable(browser, locator, timeout=90):
        """
        Waits for the element to be clickable (visible and enabled).
        Returns the WebElement if successful.
        """
        try:
            return WebDriverWait(browser, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise AssertionError(f"❌ Element {locator} not clickable after {timeout}s")

    @staticmethod
    @allure.step("Wait for URL to change from: {starting_url} (timeout={timeout}s)")
    def wait_for_url_to_change(browser, starting_url, timeout=90):
        """
        Waits for the URL to change from the starting URL after navigation.
        """
        try:
            WebDriverWait(browser, timeout).until(
                EC.url_changes(starting_url)
            )
        except TimeoutException:
            raise AssertionError(f"❌ URL did not change from '{starting_url}' after {timeout}s")

    @staticmethod
    @allure.step("Wait for title to contain: '{text}' (timeout={timeout}s)")
    def wait_for_title_contains(browser, text, timeout=90):
        """
        Waits until the page title contains the specified text (case-insensitive).
        """
        try:
            WebDriverWait(browser, timeout).until(
                lambda d: text.lower() in d.title().lower(),
                message=f"Timed out waiting for text '{text}' in page title."
            )
        except TimeoutException:
            raise AssertionError(f"❌ Page title did not contain '{text}' after {timeout}s")

    @staticmethod
    @allure.step("Wait for search input to contain: '{text}' (timeout={timeout}s)")
    def wait_for_input_contains(browser, locator, text, timeout=10):
        """
        Wait until the input field's value contains the given text.
        """
        try:
            WebDriverWait(browser, timeout).until(
                lambda d: text.lower() in d.find_element(*locator).get_attribute('value').lower(),
                message=f"Timed out waiting for input to contain '{text}'"
            )
        except TimeoutException:
            raise AssertionError(f"❌ Input field did not contain '{text}' after {timeout}s")
