from login_page import LoginPage

def test_standard_user_add_product_to_cart(driver, wait):
    base_url = "https://www.saucedemo.com/"

    login = LoginPage(driver, wait)
    login.open(base_url)

    inventory = login.login("standard_user", "secret_sauce")

    title, price = inventory.get_product_1_info()
    inventory.add_product_1_to_cart()

    cart = inventory.open_cart()
    cart_title, cart_price = cart.get_cart_product_1_info()

    assert cart_title == title
    assert cart_price == price