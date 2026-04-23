from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver):
        """Initialize page with driver and wait."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        """Click element, fallback to JS if needed."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, value, clear_first=True):
        """Type text into element."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()
        if clear_first:
            try:
                element.clear()
            except Exception:
                pass
        element.send_keys(value)

    def visible(self, locator):
        """Return visible element."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def visibles(self, locator):
        """Return all visible elements."""
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def present(self, locator):
        """Return element present in DOM."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def count(self, locator):
        """Return number of matching elements."""
        return len(self.driver.find_elements(*locator))

    def is_visible(self, locator, timeout=5):
        """Check if element is visible."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def text_of(self, locator):
        """Return element text."""
        return self.visible(locator).text.strip()

    def scroll_into_view(self, locator):
        """Scroll element into view."""
        element = self.present(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        return element

    def wait_for_url_contains(self, text):
        """Wait until URL contains text."""
        self.wait.until(EC.url_contains(text))
