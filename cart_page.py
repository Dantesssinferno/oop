from selenium.webdriver.common.by import By
from base_page import BasePage


class CartPage(BasePage):
    CART_PRODUCT_1_TITLE = (By.XPATH, "//div[@class='inventory_item_name'][1]")
    CART_PRODUCT_1_PRICE = (By.XPATH, "//div[@class='inventory_item_price'][1]")

    def get_cart_product_1_info(self) -> tuple[str, str]:
        title = self.text(self.CART_PRODUCT_1_TITLE)
        price = self.text(self.CART_PRODUCT_1_PRICE)
        return title, price