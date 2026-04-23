from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    TITLE = (By.CLASS_NAME, "title")

    def fill_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.type(*self.FIRST_NAME, text=first_name)
        self.type(*self.LAST_NAME, text=last_name)
        self.type(*self.POSTAL_CODE, text=postal_code)

    def continue_checkout(self) -> None:
        self.click(*self.CONTINUE)

    def finish_checkout(self) -> None:
        self.click(*self.FINISH)

    def error_message(self) -> str:
        return self.text_of(*self.ERROR)

    def summary_total(self) -> str:
        return self.text_of(*self.SUMMARY_TOTAL)

    def complete_message(self) -> str:
        return self.text_of(*self.COMPLETE_HEADER)

    def title_text(self) -> str:
        return self.text_of(*self.TITLE)
