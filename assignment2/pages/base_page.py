from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Base page with reusable wait and browser helpers."""

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def find(self, by: By, value: str) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def click(self, by: By, value: str) -> None:
        self.wait.until(EC.element_to_be_clickable((by, value))).click()

    def type(self, by: By, value: str, text: str) -> None:
        field = self.find(by, value)
        field.clear()
        field.send_keys(text)

    def text_of(self, by: By, value: str) -> str:
        return self.find(by, value).text

    def elements(self, by: By, value: str):
        self.wait.until(lambda d: len(d.find_elements(by, value)) > 0)
        return self.driver.find_elements(by, value)

    def is_visible(self, by: By, value: str) -> bool:
        try:
            self.find(by, value)
            return True
        except Exception:
            return False
