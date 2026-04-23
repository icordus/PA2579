from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage


class HomePage(BasePage):
    """Page object for the Juice Shop home page."""

    DISMISS_WELCOME_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Close Welcome Banner']")
    DISMISS_COOKIE_BUTTON = (By.CSS_SELECTOR, "a[aria-label='dismiss cookie message']")

    ACCOUNT_BUTTON = (By.ID, "navbarAccount")
    LOGIN_BUTTON = (By.ID, "navbarLoginButton")

    SEARCH_BUTTON = (
        By.XPATH,
        "//button[contains(@aria-label,'search') or contains(@aria-label,'Search')]",
    )
    SEARCH_INPUT = (By.ID, "searchQuery")

    PRODUCT_CARDS = (By.CSS_SELECTOR, "mat-card")
    PRODUCT_NAMES = (By.CSS_SELECTOR, "mat-card .item-name")

    BASKET_COUNT = (By.CSS_SELECTOR, "span.fa-layers-counter")
    BASKET_BUTTON = (
        By.XPATH,
        "//button[contains(@aria-label,'shopping cart') "
        "or contains(@aria-label,'Shopping Cart') "
        "or contains(@routerlink,'basket')]",
    )

    SNACKBAR = (By.CSS_SELECTOR, "simple-snack-bar")

    def dismiss_welcome_banner_if_present(self) -> None:
        """Close welcome banner if visible."""
        if self.is_visible(self.DISMISS_WELCOME_BUTTON, timeout=8):
            self.click(self.DISMISS_WELCOME_BUTTON)

    def dismiss_cookie_banner_if_present(self) -> None:
        """Close cookie banner if visible."""
        if self.is_visible(self.DISMISS_COOKIE_BUTTON, timeout=8):
            self.click(self.DISMISS_COOKIE_BUTTON)

    def open_login(self) -> None:
        """Open login page."""
        self.click(self.ACCOUNT_BUTTON)
        self.click(self.LOGIN_BUTTON)

    def product_count(self) -> int:
        """Return number of products."""
        return len(self.visibles(self.PRODUCT_CARDS))

    def get_product_names(self) -> list[str]:
        """Return list of product names."""
        return [e.text.strip() for e in self.visibles(self.PRODUCT_NAMES) if e.text.strip()]

    def first_product_name(self) -> str:
        """Return first product name."""
        names = self.get_product_names()
        if not names:
            raise AssertionError("No products found.")
        return names[0]

    def search_for(self, query: str) -> None:
        """Search for a product."""
        if self.count(self.SEARCH_INPUT) == 0:
            self.click(self.SEARCH_BUTTON)

        search_input = self.visible(self.SEARCH_INPUT)
        self.driver.execute_script("arguments[0].focus();", search_input)
        try:
            search_input.clear()
        except Exception:
            self.driver.execute_script("arguments[0].value = '';", search_input)
        search_input.send_keys(query)

    def open_basket(self) -> None:
        """Open basket page."""
        self.click(self.BASKET_BUTTON)
        self.wait_for_url_contains("basket")

    def basket_count_text(self) -> str:
        """Return basket counter text."""
        return self.text_of(self.BASKET_COUNT)

    def add_product_to_basket_by_name(self, product_name: str) -> None:
        """Add product to basket by name."""
        card = (
            By.XPATH,
            f"//mat-card[.//div[contains(@class,'item-name') and normalize-space()='{product_name}']]",
        )
        button = (
            By.XPATH,
            f"//mat-card[.//div[contains(@class,'item-name') and normalize-space()='{product_name}']]"
            f"//button[.//span[contains(normalize-space(),'Add to Basket')] "
            f"or contains(@aria-label,'Basket') "
            f"or contains(@aria-label,'basket') "
            f"or .//mat-icon[normalize-space()='add_shopping_cart']]",
        )

        card_element = self.scroll_into_view(card)
        ActionChains(self.driver).move_to_element(card_element).perform()
        self.click(button)

    def open_product_details(self, product_name: str) -> None:
        """Open product details dialog."""
        locator = (
            By.XPATH,
            f"//mat-card[.//div[contains(@class,'item-name') and normalize-space()='{product_name}']]",
        )
        self.scroll_into_view(locator)
        self.click(locator)

    def snackbar_message(self) -> str:
        """Return snackbar message."""
        return self.text_of(self.SNACKBAR)
