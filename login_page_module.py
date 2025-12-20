import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage():
    # Login XPATH
    LOGIN_FIELD_XPATH = (By.XPATH, "//input[@name='user-name']")
    PASS_FIELD_XPATH = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON_XPATH = (By.XPATH, "//input[@id='login-button']")
    def __init__(self,driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def authorization(self, username: str, password: str) -> None:
          # Ждем поле логина
          self.wait.until(EC.presence_of_element_located(self.LOGIN_FIELD_XPATH))
          user_name_el = self.driver.find_element(*self.LOGIN_FIELD_XPATH)
          user_name_el.clear()
          user_name_el.send_keys(username)
          print('Шаг: 1: Input Login : success')
          # Ждём поле пароля
          self.wait.until(EC.presence_of_element_located(self.PASS_FIELD_XPATH))
          user_pass_el = self.driver.find_element(*self.PASS_FIELD_XPATH)
          user_pass_el.send_keys(password)
          print('Шаг: 1.1: Input password : success')
          # Ждём кнопку логина и кликаем
          self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON_XPATH))
          self.driver.find_element(*self.LOGIN_BUTTON_XPATH).click()
          print('Шаг: 1.2: Login button clicked : success')

          time.sleep(1)
