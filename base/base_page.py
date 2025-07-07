"""
BasePage
========
Minimal base class for page objects.
Handles common browser interactions.
"""

class BasePage:
    def __init__(self, browser):
        """Initialize with WebDriver instance."""
        self.browser = browser

    def navigate(self, url):
        """Navigate to a URL."""
        self.browser.get(url)

    def get_title(self):
        """Return current page title."""
        return self.browser.title
