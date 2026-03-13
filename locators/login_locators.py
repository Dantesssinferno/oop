from selenium.webdriver.common.by import By

class LoginLocators:
    # ===== ЛОКАТОРЫ СТРАНИЦЫ ЛОГИНА=====
    # Каждый локатор — это кортеж (By, value)
    # Он НЕ ищет элемент, а только ОПИСЫВАЕТ, как его найти
    USERNAME_INPUT = (By.XPATH, "//input[@name='user-name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//h3[contains(text(), 'locked out')]")