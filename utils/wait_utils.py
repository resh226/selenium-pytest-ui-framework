"""
wait_utils.py
==============

This module provides utility functions for explicit waits using Selenium WebDriver.

It centralizes WebDriverWait logic for visibility and presence checks,
improving readability and maintainability across page objects and tests.

Typical usage:
--------------
from utils.wait_utils import WaitUtils

# Wait for visible element (user-facing UI)
element = WaitUtils.wait_for_element_visible(browser, locator)

# Wait for presence in DOM (even if hidden)
element = WaitUtils.wait_for_element_presence(browser, locator)

# Wait for clickable element
clickable = WaitUtils.wait_for_element_clickable(browser, locator)

# Wait for partial URL
WaitUtils.wait_for_url_to_contain(browser, partial_url)
"""
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WaitUtils:
    @staticmethod
    @allure.step("Wait for element visible: {locator} (timeout={timeout}s)")
    def wait_for_element_visible(browser, locator, timeout=30):
        """
        Waits for the element to be visible (present in DOM and not hidden).
        """
        try:
            return WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Element {locator} not visible after {timeout}s")

    @staticmethod
    @allure.step("Wait for element presence: {locator} (timeout={timeout}s)")
    def wait_for_element_presence(browser, locator, timeout=30):
        """
        Waits for the element to be present in the DOM (visibility not required).
        """
        try:
            return WebDriverWait(browser, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Element {locator} not present in DOM after {timeout}s")

    @staticmethod
    @allure.step("Wait for element clickable: {locator} (timeout={timeout}s)")
    def wait_for_element_clickable(browser, locator, timeout=30):
        """
        Waits for the element to be clickable (visible and enabled).
        """
        try:
            return WebDriverWait(browser, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Element {locator} not clickable after {timeout}s")

    @staticmethod
    @allure.step("Wait for URL to change from: {starting_url} (timeout={timeout}s)")
    def wait_for_url_to_change(browser, starting_url, timeout=30):
        """
        Waits for URL to change after navigation
        """
        try:
            WebDriverWait(browser, timeout).until(
                EC.url_changes(starting_url)
            )
        except TimeoutException:
            raise AssertionError(f"URL did not contain '{starting_url}' after {timeout}s")
