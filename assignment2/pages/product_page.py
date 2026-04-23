from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ProductPage(BasePage):
    DIALOG = (By.CSS_SELECTOR, "mat-dialog-container")
    NAME = (By.CSS_SELECTOR, "mat-dialog-content h1")
    PRICE = (By.CSS_SELECTOR, "mat-dialog-content .item-price")
    CLOSE = (By.CSS_SELECTOR, "button[aria-label='Close Dialog']")

    def name(self) -> str:
        return self.text_of(*self.NAME)

    def price(self) -> str:
        return self.text_of(*self.PRICE)

    def close(self) -> None:
        self.click(*self.CLOSE)
        self.wait.until(EC.invisibility_of_element_located(self.DIALOG))

    def is_open(self) -> bool:
        return self.is_visible(*self.DIALOG)
