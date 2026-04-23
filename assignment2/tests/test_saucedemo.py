from __future__ import annotations

from conftest import LOCKED_OUT_USER, PASSWORD, STANDARD_USER
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestSauceDemo:
    """
    10 test scenarios designed to demonstrate maintainability, reusability,
    modularity, readability, and proper synchronization.
    """

    def test_01_login_with_valid_credentials_opens_inventory(self, login_page: LoginPage) -> None:
        inventory = login_page.login(STANDARD_USER, PASSWORD)
        assert inventory.title_text() == "Products"
        assert inventory.product_count() == 6

    def test_02_locked_out_user_sees_error_message(self, login_page: LoginPage) -> None:
        login_page.login(LOCKED_OUT_USER, PASSWORD)
        assert "locked out" in login_page.error_message().lower()

    def test_03_inventory_contains_expected_number_of_products(self, login_page: LoginPage) -> None:
        inventory = login_page.login(STANDARD_USER, PASSWORD)
        assert inventory.product_count() == 6
        assert "Sauce Labs Backpack" in inventory.product_names()

    def test_04_product_details_page_displays_expected_information(self, login_page: LoginPage) -> None:
        inventory = login_page.login(STANDARD_USER, PASSWORD)
        product = inventory.open_product_details("Sauce Labs Backpack")
        assert product.name() == "Sauce Labs Backpack"
        assert product.price() == "$29.99"
        assert len(product.description()) > 20

    def test_05_adding_a_single_product_updates_the_cart_badge(self, login_page: LoginPage) -> None:
        inventory = login_page.login(STANDARD_USER, PASSWORD)
        inventory.add_product_to_cart("sauce-labs-backpack")
        assert inventory.cart_badge_count() == 1

    def test_06_cart_keeps_added_items_and_allows_removal(self, login_page: LoginPage) -> None:
        inventory = login_page.login(STANDARD_USER, PASSWORD)
        inventory.add_product_to_cart("sauce-labs-backpack")
        inventory.add_product_to_cart("sauce-labs-bike-light")

        cart = inventory.open_cart()
        assert cart.title_text() == "Your Cart"
        assert cart.item_count() == 2
        assert set(cart.item_names()) == {"Sauce Labs Backpack", "Sauce Labs Bike Light"}

        cart.remove_product("sauce-labs-bike-light")
        assert cart.item_count() == 1
        assert cart.item_names() == ["Sauce Labs Backpack"]

    def test_07_sorting_by_price_low_to_high_reorders_inventory(self, login_page: LoginPage) -> None:
        inventory = login_page.login(STANDARD_USER, PASSWORD)
        inventory.sort_by_visible_text("Price (low to high)")
        prices = inventory.product_prices()
        assert prices == sorted(prices)

    def test_08_checkout_requires_mandatory_information(self, login_page: LoginPage) -> None:
        inventory = login_page.login(STANDARD_USER, PASSWORD)
        inventory.add_product_to_cart("sauce-labs-backpack")
        checkout = inventory.open_cart().checkout()
        checkout.continue_checkout()
        assert "first name is required" in checkout.error_message().lower()

    def test_09_successful_checkout_displays_order_confirmation(self, login_page: LoginPage) -> None:
        inventory = login_page.login(STANDARD_USER, PASSWORD)
        inventory.add_product_to_cart("sauce-labs-backpack")
        checkout = inventory.open_cart().checkout()
        checkout.fill_information("Ilie", "Cordus", "19164")
        checkout.continue_checkout()
        assert checkout.title_text() == "Checkout: Overview"
        assert "Total:" in checkout.summary_total()
        checkout.finish_checkout()
        assert checkout.complete_message() == "Thank you for your order!"

    def test_10_logout_returns_user_to_login_page(self, login_page: LoginPage) -> None:
        inventory = login_page.login(STANDARD_USER, PASSWORD)
        inventory.logout()
        reloaded_login = LoginPage(inventory.driver)
        assert reloaded_login.is_loaded()
