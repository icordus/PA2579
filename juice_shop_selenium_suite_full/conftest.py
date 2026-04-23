import os
import shutil
import tempfile
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pages.home_page import HomePage

BASE_URL = os.getenv("JUICE_SHOP_URL", "https://demo.owasp-juice.shop/#/")


def _build_chrome_options(profile_dir: str) -> Options:
    """Build Chrome options for tests."""
    options = Options()

    browser_binary = (
        shutil.which("google-chrome")
        or shutil.which("chromium-browser")
        or shutil.which("chromium")
    )

    if browser_binary:
        options.binary_location = browser_binary
    else:
        raise RuntimeError("No Chrome/Chromium browser found.")

    options.add_argument("--window-size=1440,1200")
    options.add_argument("--disable-notifications")
    options.add_argument("--lang=en-US")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument(f"--user-data-dir={profile_dir}")

    return options


@pytest.fixture()
def driver():
    """Create browser session for one test."""
    chromedriver_path = shutil.which("chromedriver") or "/usr/bin/chromedriver"
    service = Service(chromedriver_path)

    with tempfile.TemporaryDirectory(prefix="chrome-profile-") as profile_dir:
        driver = webdriver.Chrome(
            service=service,
            options=_build_chrome_options(profile_dir),
        )
        driver.implicitly_wait(0)
        driver.get(BASE_URL)

        home = HomePage(driver)
        home.dismiss_welcome_banner_if_present()
        home.dismiss_cookie_banner_if_present()

        yield driver
        driver.quit()
