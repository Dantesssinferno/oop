from selenium.webdriver.common.by import By
from base_page import BasePage
from inventory_page import InventoryPage


class LoginPage(BasePage):
    USERNAME = (By.XPATH, "//input[@name='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BTN = (By.XPATH, "//input[@id='login-button']")

    def login(self, username: str, password: str) -> InventoryPage:
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
        return InventoryPage(self.driver, self.wait)