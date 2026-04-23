from __future__ import annotations

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    """Page object for Juice Shop login interactions."""
    EMAIL_LOCATORS = [
        (By.ID, "email"),
        (By.CSS_SELECTOR, "input[type='email']"),
        (By.CSS_SELECTOR, "input[formcontrolname='email']"),
    ]
    PASSWORD_LOCATORS = [
        (By.ID, "password"),
        (By.CSS_SELECTOR, "input[type='password']"),
        (By.CSS_SELECTOR, "input[formcontrolname='password']"),
    ]
    LOGIN_BUTTON_LOCATORS = [
        (By.ID, "loginButton"),
        (By.CSS_SELECTOR, "button[type='submit']"),
        (By.XPATH, "//button[contains(., 'Log in') or contains(., 'Login') or @id='loginButton']"),
    ]
    ERROR_LOCATORS = [
        (By.CSS_SELECTOR, "#login-form .error"),
        (By.CSS_SELECTOR, "mat-error"),
        (By.CSS_SELECTOR, "div.error"),
    ]

    def _first_visible(self, locators: list[tuple[By, str]], timeout: int = 12) -> WebElement:
        """Return first visible element from a list of fallback locators."""
        wait = WebDriverWait(self.driver, timeout)
        for locator in locators:
            try:
                return wait.until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                continue
        raise TimeoutException(f"No visible element found for locators: {locators}")

    def login(self, email: str, password: str) -> InventoryPage:
        """Submit credentials and return the inventory page object."""
        email_field = self._first_visible(self.EMAIL_LOCATORS)
        email_field.clear()
        email_field.send_keys(email)

        password_field = self._first_visible(self.PASSWORD_LOCATORS)
        password_field.clear()
        password_field.send_keys(password)

        login_button = self._first_visible(self.LOGIN_BUTTON_LOCATORS)
        login_button.click()

        products = InventoryPage(self.driver)
        products.dismiss_overlays()
        return products

    def error_message(self) -> str:
        """Return the visible login error text."""
        for locator in self.ERROR_LOCATORS:
            elems = self.driver.find_elements(*locator)
            if elems and elems[0].is_displayed() and elems[0].text.strip():
                return elems[0].text.strip()
        return ""

    def is_loaded(self) -> bool:
        """Check whether the login form is ready."""
        try:
            self._first_visible(self.EMAIL_LOCATORS, timeout=8)
            return True
        except TimeoutException:
            return False
