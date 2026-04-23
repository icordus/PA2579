from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")
    LOGO = (By.CLASS_NAME, "login_logo")

    def login(self, username: str, password: str) -> InventoryPage:
        self.type(*self.USERNAME, text=username)
        self.type(*self.PASSWORD, text=password)
        self.click(*self.LOGIN_BUTTON)
        return InventoryPage(self.driver)

    def error_message(self) -> str:
        return self.text_of(*self.ERROR)

    def is_loaded(self) -> bool:
        return self.is_visible(*self.LOGO)
