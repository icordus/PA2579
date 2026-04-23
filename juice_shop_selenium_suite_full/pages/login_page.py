from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "loginButton")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error")
    ACCOUNT_BUTTON = (By.ID, "navbarAccount")
    LOGOUT_BUTTON = (By.ID, "navbarLogoutButton")

    def login(self, email: str, password: str) -> None:
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def error_text(self) -> str:
        return self.text_of(self.ERROR_MESSAGE)

    def logout(self) -> None:
        self.click(self.ACCOUNT_BUTTON)
        self.click(self.LOGOUT_BUTTON)
