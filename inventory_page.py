from selenium.webdriver.common.by import By
from base_page import BasePage
from cart_page import CartPage


class InventoryPage(BasePage):
    PRODUCT_1_TITLE = (By.XPATH, "//a[@id='item_4_title_link']")
    PRODUCT_1_PRICE = (By.XPATH, "//div[@class='inventory_item_price'][1]")
    ADD_PRODUCT_1 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    CART_LINK = (By.XPATH, "//a[@class='shopping_cart_link']")

    def get_product_1_info(self) -> tuple[str, str]:
        title = self.text(self.PRODUCT_1_TITLE)
        price = self.text(self.PRODUCT_1_PRICE)
        return title, price

    def add_product_1_to_cart(self) -> None:
        self.click(self.ADD_PRODUCT_1)

    def open_cart(self) -> CartPage:
        self.click(self.CART_LINK)
        return CartPage(self.driver, self.wait)