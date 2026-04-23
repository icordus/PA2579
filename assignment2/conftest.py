from __future__ import annotations

import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com/"
STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PASSWORD = "secret_sauce"
ARTIFACTS_DIR = Path("artifacts")


def pytest_configure() -> None:
    ARTIFACTS_DIR.mkdir(exist_ok=True)


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")

    if os.getenv("CI"):
        options.add_argument("--disable-extensions")

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(0)
    yield browser
    browser.quit()


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open(BASE_URL)
    return page
