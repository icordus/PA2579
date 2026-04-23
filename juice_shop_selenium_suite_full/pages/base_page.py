from typing import List, Tuple

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


Locator = Tuple[str, str]


class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver: WebDriver, timeout: int = 15):
        """Initialize page with driver and wait."""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator: Locator) -> None:
        """Click element, fallback to JS if needed."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator: Locator, value: str, clear_first: bool = True) -> None:
        """Type text into element."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].focus();", element)

        if clear_first:
            try:
                element.clear()
            except Exception:
                self.driver.execute_script("arguments[0].value = '';", element)

        element.send_keys(value)

    def text_of(self, locator: Locator) -> str:
        """Return element text."""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def visible(self, locator: Locator) -> WebElement:
        """Return visible element."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def visibles(self, locator: Locator) -> List[WebElement]:
        """Return all visible elements."""
        self.wait.until(EC.visibility_of_any_elements_located(locator))
        return self.driver.find_elements(*locator)

    def present(self, locator: Locator) -> WebElement:
        """Return element present in DOM."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_visible(self, locator: Locator, timeout: int = 5) -> bool:
        """Check if element is visible."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_url_contains(self, value: str) -> None:
        """Wait until URL contains text."""
        self.wait.until(EC.url_contains(value))

    def scroll_into_view(self, locator: Locator) -> WebElement:
        """Scroll element into view."""
        element = self.present(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        return element

    def count(self, locator: Locator) -> int:
        """Return number of matching elements."""
        return len(self.driver.find_elements(*locator))

    def finds(self, locator: Locator):
        """Return matching elements."""
        return self.driver.find_elements(*locator)
