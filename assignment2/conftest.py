from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import Optional

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.checkout_page import RegisterPage

BASE_URL = os.getenv("JUICE_SHOP_URL", "https://demo.owasp-juice.shop/").rstrip("/")
_RESOLVED_BASE_URL: Optional[str] = None
ADMIN_EMAIL = "admin@juice-sh.op"
ADMIN_PASSWORD = "admin123"
WRONG_EMAIL = "notauser@example.com"
WRONG_PASSWORD = "wrongpassword"
ARTIFACTS_DIR = Path("artifacts")


def _url_candidates() -> list[str]:
    """Return Juice Shop base URLs to try, in priority order."""
    candidates = [
        BASE_URL,
        "https://demo.owasp-juice.shop",
        "https://juice-shop.herokuapp.com",
    ]
    # Preserve order and remove duplicates.
    return list(dict.fromkeys(url.rstrip("/") for url in candidates if url))


def _resolve_base_url(driver) -> str:
    """Pick the first host that loads the login page correctly."""
    global _RESOLVED_BASE_URL
    if _RESOLVED_BASE_URL:
        return _RESOLVED_BASE_URL

    page = LoginPage(driver)
    for base_url in _url_candidates():
        page.open(f"{base_url}/#/login")
        page.dismiss_overlays()

        if "application error" in driver.title.lower():
            continue

        if page.is_loaded():
            _RESOLVED_BASE_URL = base_url
            return _RESOLVED_BASE_URL

    raise RuntimeError(
        "Could not load Juice Shop login page from any known host. "
        f"Tried: {_url_candidates()}. Last URL: {driver.current_url}. Title: {driver.title}"
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
    base_url = _resolve_base_url(driver)
    page = LoginPage(driver)
    page.open(f"{base_url}/#/login")
    page.dismiss_overlays()
    return page


@pytest.fixture
def register_page(driver):
    """Open the registration page and return a ready-to-use page object."""
    base_url = _resolve_base_url(driver)
    page = RegisterPage(driver)
    page.open(f"{base_url}/#/register")
    page.dismiss_overlays()
    return page
