from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    def __init__(self, driver: WebDriver, wait: WebDriverWait) -> None:
        self.driver = driver
        self.wait = wait

    def is_step_one_opened(self) -> bool:
        self.wait.until(ec.visibility_of_element_located((By.ID, "continue")))
        return "checkout-step-one.html" in self.driver.current_url

    def fill_checkout_data(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def continue_checkout(self) -> None:
        self.driver.find_element(By.ID, "continue").click()

    def is_step_two_opened(self) -> bool:
        self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "summary_info")))
        return "checkout-step-two.html" in self.driver.current_url

    def finish_checkout(self) -> None:
        self.driver.find_element(By.ID, "finish").click()

    def is_complete_opened(self) -> bool:
        self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
        return "checkout-complete.html" in self.driver.current_url

    def back_to_products(self) -> None:
        self.driver.find_element(By.ID, "back-to-products").click()

    def is_returned_to_catalog(self) -> bool:
        self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
        return "inventory.html" in self.driver.current_url
