from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    NAME = (By.CLASS_NAME, "inventory_details_name")
    PRICE = (By.CLASS_NAME, "inventory_details_price")
    DESCRIPTION = (By.CLASS_NAME, "inventory_details_desc")
    BACK_TO_PRODUCTS = (By.ID, "back-to-products")

    def name(self) -> str:
        return self.text_of(*self.NAME)

    def price(self) -> str:
        return self.text_of(*self.PRICE)

    def description(self) -> str:
        return self.text_of(*self.DESCRIPTION)

    def add_to_cart(self, product_slug: str) -> None:
        self.click(By.ID, f"add-to-cart-{product_slug}")

    def back_to_products(self):
        self.click(*self.BACK_TO_PRODUCTS)
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
