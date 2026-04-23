from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_APP_STATE_LINK = (By.ID, "reset_sidebar_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def title_text(self) -> str:
        return self.text_of(*self.TITLE)

    def product_count(self) -> int:
        return len(self.elements(*self.INVENTORY_ITEMS))

    def add_product_to_cart(self, product_slug: str) -> None:
        self.click(By.ID, f"add-to-cart-{product_slug}")

    def remove_product_from_cart(self, product_slug: str) -> None:
        self.click(By.ID, f"remove-{product_slug}")

    def open_cart(self):
        self.click(*self.CART_LINK)
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def cart_badge_count(self) -> int:
        if not self.driver.find_elements(*self.CART_BADGE):
            return 0
        return int(self.text_of(*self.CART_BADGE))

    def open_product_details(self, product_name: str):
        self.click(By.XPATH, f"//div[@class='inventory_item_name' and text()='{product_name}']")
        from pages.product_page import ProductPage
        return ProductPage(self.driver)

    def sort_by_visible_text(self, text: str) -> None:
        dropdown = self.find(*self.SORT_DROPDOWN)
        from selenium.webdriver.support.ui import Select
        Select(dropdown).select_by_visible_text(text)
        self.wait.until(lambda d: self.driver.find_elements(*self.PRODUCT_NAMES))

    def product_names(self) -> list[str]:
        return [element.text for element in self.elements(*self.PRODUCT_NAMES)]

    def product_prices(self) -> list[float]:
        return [float(element.text.replace("$", "")) for element in self.elements(*self.PRODUCT_PRICES)]

    def logout(self) -> None:
        self.click(*self.BURGER_MENU)
        self.wait.until(EC.visibility_of_element_located(self.LOGOUT_LINK))
        self.click(*self.LOGOUT_LINK)

    def reset_app_state(self) -> None:
        self.click(*self.BURGER_MENU)
        self.wait.until(EC.visibility_of_element_located(self.RESET_APP_STATE_LINK))
        self.click(*self.RESET_APP_STATE_LINK)
