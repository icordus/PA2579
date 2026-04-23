from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for the basket page."""

    BASKET_ITEM_NAMES = (By.CSS_SELECTOR, "mat-row .mat-column-Product")
    CHECKOUT_BUTTON = (By.ID, "checkoutButton")

    def item_names(self):
        """Return basket item names."""
        self.wait.until(EC.presence_of_all_elements_located(self.BASKET_ITEM_NAMES))
        return [element.text.strip() for element in self.finds(self.BASKET_ITEM_NAMES) if element.text.strip()]

    def remove_item_by_name(self, product_name: str) -> None:
        """Remove basket item by name."""
        locator = (
            By.XPATH,
            f"//mat-row[.//mat-cell[contains(@class,'mat-column-Product') and contains(.,'{product_name}')]]"
            f"//button[contains(@aria-label,'Remove')]",
        )
        self.scroll_into_view(locator)
        self.click(locator)

    def proceed_to_checkout(self) -> None:
        """Proceed to checkout."""
        self.scroll_into_view(self.CHECKOUT_BUTTON)
        self.click(self.CHECKOUT_BUTTON)
