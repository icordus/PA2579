from __future__ import annotations

import os
import shutil
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.checkout_page import RegisterPage

BASE_URL = os.getenv("JUICE_SHOP_URL", "https://demo.owasp-juice.shop/").rstrip("/")
ADMIN_EMAIL = "admin@juice-sh.op"
ADMIN_PASSWORD = "admin123"
WRONG_EMAIL = "notauser@example.com"
WRONG_PASSWORD = "wrongpassword"
ARTIFACTS_DIR = Path("artifacts")


def _ensure_demo_available(driver) -> None:
    """Validate that the configured Juice Shop demo host is serving the login page."""
    page = LoginPage(driver)
    page.open(f"{BASE_URL}/#/login")
    page.dismiss_overlays()
    if "application error" in driver.title.lower() or not page.is_loaded():
        raise RuntimeError(
            "Juice Shop demo host is unavailable right now. "
            f"URL: {BASE_URL}/#/login, current URL: {driver.current_url}, title: {driver.title}"
        )


def pytest_configure() -> None:
    """Create the artifacts directory before test execution."""
    ARTIFACTS_DIR.mkdir(exist_ok=True)


@pytest.fixture
def driver():
    """Provide a fresh headless Chrome WebDriver for each test."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--no-zygote")

    browser_binary = (
        shutil.which("google-chrome")
        or shutil.which("chromium-browser")
        or shutil.which("chromium")
    )
    if browser_binary:
        options.binary_location = browser_binary

    if os.getenv("CI"):
        options.add_argument("--disable-extensions")

    local_chromedriver = shutil.which("chromedriver")

    try:
        if local_chromedriver:
            service = Service(local_chromedriver)
            browser = webdriver.Chrome(service=service, options=options)
        else:
            service = Service(ChromeDriverManager().install())
            browser = webdriver.Chrome(service=service, options=options)
    except WebDriverException:
        # Fallback for environments where system chromedriver is incompatible.
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)

    browser.implicitly_wait(0)
    yield browser
    browser.quit()


@pytest.fixture
def login_page(driver):
    """Open the login page and return a ready-to-use page object."""
    _ensure_demo_available(driver)
    page = LoginPage(driver)
    page.open(f"{BASE_URL}/#/login")
    page.dismiss_overlays()
    return page


@pytest.fixture
def register_page(driver):
    """Open the registration page and return a ready-to-use page object."""
    _ensure_demo_available(driver)
    page = RegisterPage(driver)
    page.open(f"{BASE_URL}/#/register")
    page.dismiss_overlays()
    return page
