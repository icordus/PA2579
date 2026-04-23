from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class RegisterPage(BasePage):
    """Page object for registration form validation checks."""
    EMAIL = (By.ID, "emailControl")
    PASSWORD = (By.ID, "passwordControl")
    REPEAT_PASSWORD = (By.ID, "repeatPasswordControl")
    REGISTER_BUTTON = (By.ID, "registerButton")
    ERRORS = (By.CSS_SELECTOR, "mat-error")

    def fill_email_and_blur(self, email: str) -> None:
        """Type an email value and move focus away to trigger Angular form validation."""
        field = self.find(*self.EMAIL)
        field.clear()
        field.send_keys(email)
        field.send_keys(Keys.TAB)

    def has_email_error(self) -> bool:
        """Return True if any validation error is currently visible."""
        errors = self.driver.find_elements(*self.ERRORS)
        return len(errors) > 0

    def error_messages(self) -> list[str]:
        """Return non-empty validation error messages."""
        return [e.text for e in self.driver.find_elements(*self.ERRORS) if e.text]


# Backward-compatible alias kept for import compatibility
CheckoutPage = RegisterPage
