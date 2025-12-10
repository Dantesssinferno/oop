import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

# ===================================== BROWSER SETUP =====================================
def create_driver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    prefs = {
        "intl.accept_languages": "en,en_US"
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--lang=en")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver
# ===================================== PAGE OBJECT =======================================
class LoginPage: # Класс как Page Object:
    # URL страницы логина
    URL = "https://www.saucedemo.com/"

    # Локаторы - атрибуты класса
    LOGIN_FIELD = (By.XPATH, "//input[@name='user-name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")

    # Тестовые данные
    login_standard_user = "standard_user"
    password_universal = "secret_sauce"

    # действия с элементами — методы
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_login_page(self) -> None:
        """Открыть страницу логина."""
        self.driver.get(self.URL)
        print("Start Test: open login page")

    def enter_username(self, username: str) -> None:
        """Ввести логин."""
        login_input = self.wait.until(EC.visibility_of_element_located(self.LOGIN_FIELD))
        login_input.clear()
        login_input.send_keys(username)
        print("Шаг 1: Input Login: success")

    def enter_password(self, password: str) -> None:
        """Ввести пароль."""
        pass_input = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        pass_input.clear()
        pass_input.send_keys(password)
        print("Шаг 2: Input Passwodr: success")

    def click_login(self) -> None:
        """Нажать на кнопку Login."""
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()
        print("Шаг 3: login button clicked: success")
        time.sleep(1)

    def test_login_happy_path(self, username: str, password: str) -> None:
        """Полный сценарий логина одной командой."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

# ===================================== TEST RUN ==========================================

if __name__ == "__main__":
    driver = create_driver()
    login_page = LoginPage(driver)

    try:
        login_page.open_login_page()
        login_page.test_login_happy_path(LoginPage.login_standard_user, LoginPage.password_universal)
        print("Шаг 4: Login: success")
        time.sleep(10)
    finally:
        driver.quit()