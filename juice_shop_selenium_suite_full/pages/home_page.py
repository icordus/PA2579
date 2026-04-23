from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class HomePage(BasePage):
    DISMISS_WELCOME_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Close Welcome Banner']")
    DISMISS_COOKIE_BUTTON = (By.CSS_SELECTOR, "a[aria-label='dismiss cookie message']")
    ACCOUNT_BUTTON = (By.ID, "navbarAccount")
    LOGIN_BUTTON = (By.ID, "navbarLoginButton")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Show the search bar']")
    SEARCH_INPUT = (By.ID, "searchQuery")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "mat-card")
    PRODUCT_NAMES = (By.CSS_SELECTOR, "mat-card .item-name")
    BASKET_COUNT = (By.CSS_SELECTOR, "span.fa-layers-counter")
    BASKET_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Show the shopping cart']")
    SNACKBAR = (By.CSS_SELECTOR, "simple-snack-bar")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "mat-select[aria-label='Sort by']")

    def dismiss_welcome_banner_if_present(self) -> None:
        if self.is_visible(self.DISMISS_WELCOME_BUTTON, timeout=8):
            self.click(self.DISMISS_WELCOME_BUTTON)

    def dismiss_cookie_banner_if_present(self) -> None:
        if self.is_visible(self.DISMISS_COOKIE_BUTTON, timeout=8):
            self.click(self.DISMISS_COOKIE_BUTTON)

    def open_login(self) -> None:
        self.click(self.ACCOUNT_BUTTON)
        self.click(self.LOGIN_BUTTON)

    def product_count(self) -> int:
        return len(self.visibles(self.PRODUCT_CARDS))

    def get_product_names(self):
        return [e.text.strip() for e in self.visibles(self.PRODUCT_NAMES) if e.text.strip()]

    def search_for(self, query: str) -> None:
        self.click(self.SEARCH_BUTTON)
        self.type(self.SEARCH_INPUT, query)

    def open_basket(self) -> None:
        self.click(self.BASKET_BUTTON)

    def basket_count_text(self) -> str:
        return self.text_of(self.BASKET_COUNT)

    def add_product_to_basket_by_name(self, product_name: str) -> None:
        locator = (
            By.XPATH,
            f"//mat-card[.//div[contains(@class,'item-name') and normalize-space()='{product_name}']]//button[@aria-label='Add to Basket']",
        )
        self.scroll_into_view(locator)
        self.click(locator)

    def open_product_details(self, product_name: str) -> None:
        locator = (
            By.XPATH,
            f"//mat-card[.//div[contains(@class,'item-name') and normalize-space()='{product_name}']]",
        )
        self.scroll_into_view(locator)
        self.click(locator)

    def snackbar_message(self) -> str:
        return self.text_of(self.SNACKBAR)

    def select_sort_option(self, option_text: str) -> None:
        self.click(self.SORT_DROPDOWN)
        option = (By.XPATH, f"//mat-option//span[normalize-space()='{option_text}']")
        self.click(option)
