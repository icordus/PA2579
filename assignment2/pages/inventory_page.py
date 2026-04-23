from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page object for product listing and account actions."""
    PRODUCT_TILES = (By.CSS_SELECTOR, "mat-grid-tile")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".item-name")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".item-price")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Add to Basket']")
    BASKET_COUNTER = (By.CSS_SELECTOR, "span.fa-layers-counter.warn-notification")
    BASKET_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Show the shopping cart']")
    ACCOUNT_BUTTON = (By.ID, "navbarAccount")
    LOGOUT_BUTTON = (By.ID, "navbarLogoutButton")
    PRODUCT_CLICK_TARGET = (By.CSS_SELECTOR, "div.product")

    def product_count(self) -> int:
        """Return the number of product tiles currently shown."""
        return len(self.elements(*self.PRODUCT_TILES))

    def product_names(self) -> list[str]:
        """Return visible product names from the listing."""
        return [el.text for el in self.elements(*self.PRODUCT_NAMES)]

    def product_prices(self) -> list[float]:
        """Return visible product prices as floats."""
        raw = [el.text.replace("\u00a4", "").strip() for el in self.elements(*self.PRODUCT_PRICES)]
        return [float(p) for p in raw if p]

    def basket_item_count(self) -> int:
        """Return the basket counter value, or zero when hidden."""
        elems = self.driver.find_elements(*self.BASKET_COUNTER)
        if not elems:
            return 0
        text = elems[0].text.strip()
        return int(text) if text.isdigit() else 0

    def add_first_product_to_basket(self) -> None:
        """Add the first visible product and wait for counter update."""
        initial = self.basket_item_count()
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_BASKET_BUTTON)).click()
        self.wait.until(lambda _: self.basket_item_count() > initial)

    def open_basket(self):
        """Open the basket page and return its page object."""
        self.click(*self.BASKET_BUTTON)
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def open_product_details(self):
        """Open details for a product tile and return dialog object."""
        self.click(*self.PRODUCT_CLICK_TARGET)
        from pages.product_page import ProductPage
        return ProductPage(self.driver)

    def search(self, query: str) -> None:
        """Apply a search query through the search route."""
        base = self.driver.current_url.split("#")[0]
        self.driver.get(f"{base}#/search?q={query}")
        self.wait.until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, "mat-grid-tile")) > 0
            or len(d.find_elements(By.CSS_SELECTOR, ".noResultText")) > 0
        )

    def logout(self) -> None:
        """Log out through the account menu and wait for UI update."""
        self.click(*self.ACCOUNT_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BUTTON))
        self.click(*self.LOGOUT_BUTTON)
        self.wait.until(lambda _: not self.is_visible(*self.BASKET_BUTTON))

    def is_user_logged_out(self) -> bool:
        """Return True when authenticated UI controls are hidden."""
        return not self.is_visible(*self.BASKET_BUTTON)
