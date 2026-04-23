from __future__ import annotations

from conftest import ADMIN_EMAIL, ADMIN_PASSWORD, WRONG_EMAIL, WRONG_PASSWORD
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestJuiceShop:
    """
    10 test scenarios for OWASP Juice Shop demonstrating the same VGT
    Best Practices qualities as the original SauceDemo suite:
    Maintainability, Reusability, Modularity, Readability, and Synchronization.
    """

    def test_01_valid_login_opens_product_listing(self, login_page: LoginPage) -> None:
        products = login_page.login(ADMIN_EMAIL, ADMIN_PASSWORD)
        assert products.product_count() >= 1

    def test_02_invalid_login_shows_error_message(self, login_page: LoginPage) -> None:
        login_page.login(WRONG_EMAIL, WRONG_PASSWORD)
        assert login_page.error_message() != ""

    def test_03_products_page_lists_multiple_products(self, login_page: LoginPage) -> None:
        products = login_page.login(ADMIN_EMAIL, ADMIN_PASSWORD)
        assert products.product_count() >= 6
        names = products.product_names()
        assert any("Juice" in name or "Apple" in name or "Beer" in name for name in names)

    def test_04_product_detail_dialog_shows_name_and_price(self, login_page: LoginPage) -> None:
        products = login_page.login(ADMIN_EMAIL, ADMIN_PASSWORD)
        dialog = products.open_product_details()
        assert len(dialog.name()) > 0
        assert "\u00a4" in dialog.price()
        dialog.close()

    def test_05_adding_product_to_basket_updates_counter(self, login_page: LoginPage) -> None:
        products = login_page.login(ADMIN_EMAIL, ADMIN_PASSWORD)
        initial = products.basket_item_count()
        products.add_first_product_to_basket()
        assert products.basket_item_count() == initial + 1

    def test_06_basket_shows_added_product(self, login_page: LoginPage) -> None:
        products = login_page.login(ADMIN_EMAIL, ADMIN_PASSWORD)
        products.add_first_product_to_basket()
        basket = products.open_basket()
        assert "Basket" in basket.title_text()
        assert basket.item_count() >= 1

    def test_07_search_filters_product_list(self, login_page: LoginPage) -> None:
        products = login_page.login(ADMIN_EMAIL, ADMIN_PASSWORD)
        total = products.product_count()
        products.search("apple")
        filtered_names = products.product_names()
        assert len(filtered_names) >= 1
        assert len(filtered_names) < total
        assert any("apple" in name.lower() for name in filtered_names)

    def test_08_registration_validates_email_format(self, register_page) -> None:
        register_page.fill_email_and_blur("notanemail")
        assert register_page.has_email_error()

    def test_09_logout_returns_user_to_unauthenticated_state(self, login_page: LoginPage) -> None:
        products = login_page.login(ADMIN_EMAIL, ADMIN_PASSWORD)
        products.logout()
        assert products.is_user_logged_out()

    def test_10_product_detail_dialog_can_be_closed(self, login_page: LoginPage) -> None:
        products = login_page.login(ADMIN_EMAIL, ADMIN_PASSWORD)
        dialog = products.open_product_details()
        assert dialog.is_open()
        dialog.close()
        assert not dialog.is_open()
