"""Selenium WebDriver test suite for OWASP Juice Shop."""

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage

VALID_EMAIL = "admin@juice-sh.op"
VALID_PASSWORD = "admin123"
INVALID_PASSWORD = "wrong-password"

def open_login(driver):
    home = HomePage(driver)
    home.open_login()
    return LoginPage(driver)

def login_as_admin(driver):
    login_page = open_login(driver)
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    home = HomePage(driver)
    home.wait_for_url_contains("/#/")
    return home

def test_01_valid_login_redirects_to_home(driver):
    """Checks that a valid login returns the user to the main catalog."""
    login_page = open_login(driver)
    login_page.login(VALID_EMAIL, VALID_PASSWORD)

    home = HomePage(driver)
    home.wait_for_url_contains("/#/")
    assert home.product_count() > 0

def test_02_invalid_login_shows_error_message(driver):
    """Checks that an invalid password produces a visible error message."""
    login_page = open_login(driver)
    login_page.login(VALID_EMAIL, INVALID_PASSWORD)
    assert "Invalid email or password" in login_page.error_text()

def test_03_logout_returns_user_to_logged_out_state(driver):
    """Checks that logout returns the application to a logged-out state."""
    login_as_admin(driver)
    LoginPage(driver).logout()

    HomePage(driver).open_login()
    assert "#/login" in driver.current_url

def test_04_product_catalog_is_visible(driver):
    """Checks that the product catalog loads and displays at least one product."""
    home = HomePage(driver)
    assert home.product_count() >= 1
    assert len(home.get_product_names()) >= 1

def test_05_search_filters_products(driver):
    """Checks that searching by part of the first product name filters results."""
    home = HomePage(driver)
    original_name = home.first_product_name()
    query = original_name.split()[0]

    home.search_for(query)

    filtered_names = home.get_product_names()
    assert filtered_names
    assert any(query.lower() in name.lower() for name in filtered_names)


def test_06_add_single_item_to_basket_updates_counter(driver):
    """Checks that adding a visible product updates the basket counter."""
    home = HomePage(driver)
    product_name = home.first_product_name()

    home.add_product_to_basket_by_name(product_name)

    assert home.basket_count_text() == "1"
    assert "Placed" in home.snackbar_message()


def test_07_basket_contains_added_product(driver):
    """Checks that a visible product added from the catalog is shown in the basket."""
    home = HomePage(driver)
    product_name = home.first_product_name()

    home.add_product_to_basket_by_name(product_name)
    home.open_basket()

    cart = CartPage(driver)
    assert any(product_name in item for item in cart.item_names())


def test_08_remove_item_from_basket(driver):
    """Checks that removing an added item updates the basket contents."""
    home = HomePage(driver)
    product_name = home.first_product_name()

    home.add_product_to_basket_by_name(product_name)
    home.open_basket()

    cart = CartPage(driver)
    assert any(product_name in item for item in cart.item_names())

    cart.remove_item_by_name(product_name)

    remaining = cart.item_names() if cart.count(cart.BASKET_ITEM_NAMES) else []
    assert all(product_name not in item for item in remaining)


def test_09_open_basket_page(driver):
    """Checks that the basket page can be opened from the home page."""
    home = HomePage(driver)
    home.open_basket()

    assert "#/basket" in driver.current_url


def test_10_product_details_dialog_opens(driver):
    """Checks that product details can be opened and inspected in a dialog."""
    home = HomePage(driver)
    home.open_product_details(KNOWN_PRODUCT)

    details = ProductDetailsPage(driver)
    assert KNOWN_PRODUCT in details.dialog_title()
    assert details.dialog_contains("apple")
    details.close()
