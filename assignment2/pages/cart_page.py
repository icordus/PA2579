from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "app-purchase-basket h1")
    PRODUCT_NAME_CELLS = (By.CSS_SELECTOR, "mat-cell.mat-column-product, td.mat-column-product")
    CHECKOUT_BUTTON = (By.ID, "checkoutButton")

    def title_text(self) -> str:
        return self.text_of(*self.TITLE)

    def item_count(self) -> int:
        try:
            self.wait.until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, "mat-cell.mat-column-product, td.mat-column-product")) > 0
            )
            cells = self.driver.find_elements(*self.PRODUCT_NAME_CELLS)
            return len([c for c in cells if c.text.strip()])
        except Exception:
            return 0

    def item_names(self) -> list[str]:
        cells = self.driver.find_elements(*self.PRODUCT_NAME_CELLS)
        return [c.text.strip() for c in cells if c.text.strip()]
