from typing import Dict

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    def __init__(self, driver: WebDriver, wait: WebDriverWait) -> None:
        self.driver = driver
        self.wait = wait

    def is_opened(self) -> bool:
        self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "cart_list")))
        return "cart.html" in self.driver.current_url

    def get_product_info(self, product_name: str) -> Dict[str, str]:
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
            if name == product_name:
                return {
                    "name": name,
                    "price": item.find_element(By.CLASS_NAME, "inventory_item_price").text.strip(),
                }
        raise ValueError(f"Product '{product_name}' was not found in cart")

    def click_checkout(self) -> None:
        self.driver.find_element(By.ID, "checkout").click()
