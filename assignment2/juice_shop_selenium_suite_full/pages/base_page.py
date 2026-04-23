from typing import List, Tuple

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = Tuple[str, str]

class BasePage:
    """Reusable Selenium helpers built around explicit waits."""

    def __init__(self, driver: WebDriver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator: Locator, value: str, clear_first: bool = True) -> None:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if clear_first:
            element.clear()
        element.send_keys(value)

    def text_of(self, locator: Locator) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def visible(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def visibles(self, locator: Locator) -> List[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def present(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_visible(self, locator: Locator, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_url_contains(self, value: str) -> None:
        self.wait.until(EC.url_contains(value))

    def scroll_into_view(self, locator: Locator) -> None:
        element = self.present(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def count(self, locator: Locator) -> int:
        return len(self.driver.find_elements(*locator))

    def finds(self, locator: Locator):
        return self.driver.find_elements(*locator)
