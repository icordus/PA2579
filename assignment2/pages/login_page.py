from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")
    ERROR = (By.CSS_SELECTOR, "#login-form .error")

    def login(self, email: str, password: str) -> InventoryPage:
        self.type(*self.EMAIL, text=email)
        self.type(*self.PASSWORD, text=password)
        self.click(*self.LOGIN_BUTTON)
        products = InventoryPage(self.driver)
        products.dismiss_overlays()
        return products

    def error_message(self) -> str:
        return self.text_of(*self.ERROR)

    def is_loaded(self) -> bool:
        return self.is_visible(*self.LOGIN_BUTTON)
