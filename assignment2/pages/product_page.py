from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ProductPage(BasePage):
    """Page object for the product details dialog."""
    DIALOG = (By.CSS_SELECTOR, "mat-dialog-container")
    NAME = (By.CSS_SELECTOR, "mat-dialog-content h1")
    PRICE = (By.CSS_SELECTOR, "mat-dialog-content .item-price")
    CLOSE = (By.CSS_SELECTOR, "button[aria-label='Close Dialog']")

    def name(self) -> str:
        """Return the product name shown in the dialog."""
        return self.text_of(*self.NAME)

    def price(self) -> str:
        """Return the product price shown in the dialog."""
        return self.text_of(*self.PRICE)

    def close(self) -> None:
        """Close the details dialog and wait until hidden."""
        self.click(*self.CLOSE)
        self.wait.until(EC.invisibility_of_element_located(self.DIALOG))

    def is_open(self) -> bool:
        """Check whether the details dialog is visible."""
        return self.is_visible(*self.DIALOG)
