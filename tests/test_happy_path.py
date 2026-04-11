from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_happy_path_checkout_flow(driver, wait, base_url, credentials):
    login_page = LoginPage(driver, wait)
    inventory_page = InventoryPage(driver, wait)
    cart_page = CartPage(driver, wait)
    checkout_page = CheckoutPage(driver, wait)

    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
    ]

    login_page.open(base_url)
    assert login_page.is_opened(), "Login page did not open"

    username, password = credentials
    login_page.login(username, password)
    assert inventory_page.is_opened(), "Inventory page did not open after login"

    catalog_products = []
    for product_name in products_to_add:
        catalog_products.append(inventory_page.get_product_info(product_name))
        inventory_page.add_product_to_cart(product_name)

    assert inventory_page.get_cart_items_count() == len(products_to_add)

    inventory_page.open_cart()
    assert cart_page.is_opened(), "Cart page did not open"

    for catalog_product in catalog_products:
        cart_product = cart_page.get_product_info(catalog_product["name"])
        assert cart_product["name"] == catalog_product["name"]
        assert cart_product["price"] == catalog_product["price"]

    cart_page.click_checkout()
    assert checkout_page.is_step_one_opened(), "Checkout step one did not open"

    checkout_page.fill_checkout_data("Ivan", "Petrov", "101000")
    checkout_page.continue_checkout()
    assert checkout_page.is_step_two_opened(), "Checkout step two did not open"

    checkout_page.finish_checkout()
    assert checkout_page.is_complete_opened(), "Checkout complete page did not open"

    checkout_page.back_to_products()
    assert checkout_page.is_returned_to_catalog(), "Did not return to catalog page"
