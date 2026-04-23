from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ProductDetailsPage(BasePage):
    DIALOG_TITLE = (By.CSS_SELECTOR, "mat-dialog-container h1")
    DIALOG_CLOSE = (By.CSS_SELECTOR, "button[aria-label='Close Dialog']")
    DIALOG_BODY = (By.CSS_SELECTOR, "mat-dialog-container")

    def dialog_title(self) -> str:
        return self.text_of(self.DIALOG_TITLE)

    def dialog_contains(self, text: str) -> bool:
        return text.lower() in self.text_of(self.DIALOG_BODY).lower()

    def close(self) -> None:
        self.click(self.DIALOG_CLOSE)
