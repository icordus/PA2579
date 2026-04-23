from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def title_text(self) -> str:
        return self.text_of(*self.TITLE)

    def item_names(self) -> list[str]:
        return [item.text for item in self.elements(By.CLASS_NAME, "inventory_item_name")]

    def item_count(self) -> int:
        return len(self.elements(*self.CART_ITEMS))

    def remove_product(self, product_slug: str) -> None:
        self.click(By.ID, f"remove-{product_slug}")

    def checkout(self):
        self.click(*self.CHECKOUT)
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)

    def continue_shopping(self):
        self.click(*self.CONTINUE_SHOPPING)
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
