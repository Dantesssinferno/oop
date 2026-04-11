from typing import Dict

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    def __init__(self, driver: WebDriver, wait: WebDriverWait) -> None:
        self.driver = driver
        self.wait = wait

    def is_opened(self) -> bool:
        self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
        return "inventory.html" in self.driver.current_url

    def _product_card_by_name(self, product_name: str):
        cards = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for card in cards:
            name = card.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
            if name == product_name:
                return card
        raise ValueError(f"Product '{product_name}' was not found in catalog")

    def add_product_to_cart(self, product_name: str) -> None:
        card = self._product_card_by_name(product_name)
        card.find_element(By.TAG_NAME, "button").click()

    def get_product_info(self, product_name: str) -> Dict[str, str]:
        card = self._product_card_by_name(product_name)
        return {
            "name": card.find_element(By.CLASS_NAME, "inventory_item_name").text.strip(),
            "price": card.find_element(By.CLASS_NAME, "inventory_item_price").text.strip(),
        }

    def get_cart_items_count(self) -> int:
        badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        return int(badge.text.strip())

    def open_cart(self) -> None:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
