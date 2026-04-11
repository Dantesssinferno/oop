from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver: WebDriver, wait: WebDriverWait) -> None:
        self.driver = driver
        self.wait = wait

    def open(self, base_url: str) -> None:
        self.driver.get(base_url)

    def login(self, username: str, password: str) -> None:
        self.wait.until(ec.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def is_opened(self) -> bool:
        return "saucedemo.com" in self.driver.current_url and self.driver.find_element(By.ID, "login-button").is_displayed()
