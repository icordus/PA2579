from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Base page with reusable wait and browser helpers."""

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        """Navigate the browser to the given URL."""
        self.driver.get(url)

    def dismiss_overlays(self) -> None:
        """Dismiss the cookie consent banner and any open dialogs (welcome banner, etc.)."""
        # Dismiss welcome banner when present.
        for selector in [
            "button[aria-label='Close Welcome Banner']",
            "button[aria-label='close-dialog']",
        ]:
            try:
                buttons = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if buttons and buttons[0].is_displayed():
                    buttons[0].click()
            except Exception:
                pass

        # Accept/dismiss cookie message across UI variants.
        for selector in [
            "a[aria-label='allow cookies']",
            "a[aria-label='dismiss cookie message']",
        ]:
            try:
                cookie_btns = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if cookie_btns and cookie_btns[0].is_displayed():
                    cookie_btns[0].click()
            except Exception:
                pass

        # Dismiss any open mat-dialog (welcome banner, challenge notifications) with Escape
        try:
            body = self.driver.find_element(By.TAG_NAME, "body")
            body.send_keys(Keys.ESCAPE)
        except Exception:
            pass

    def find(self, by: By, value: str) -> WebElement:
        """Wait for and return a visible element."""
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def click(self, by: By, value: str) -> None:
        """Wait for and click an element."""
        self.wait.until(EC.element_to_be_clickable((by, value))).click()

    def type(self, by: By, value: str, text: str) -> None:
        """Clear an input field and type text into it."""
        field = self.find(by, value)
        field.clear()
        field.send_keys(text)

    def text_of(self, by: By, value: str) -> str:
        """Return visible text from an element."""
        return self.find(by, value).text

    def elements(self, by: By, value: str):
        """Return matching elements after at least one is present."""
        self.wait.until(lambda d: len(d.find_elements(by, value)) > 0)
        return self.driver.find_elements(by, value)

    def is_visible(self, by: By, value: str) -> bool:
        """Check whether an element is currently visible."""
        try:
            self.find(by, value)
            return True
        except Exception:
            return False
