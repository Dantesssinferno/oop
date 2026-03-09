# By — это перечисление стратегий поиска элементов (XPATH, ID, CSS_SELECTOR и т.д.)
from selenium.webdriver.common.by import By
# LoginLocators - это локаторы на странице логин
from locators.login_locators import LoginLocators
# BASE_URL — базовый адрес приложения (хранится в config, чтобы не дублировать в тестах)
from config.settings import BASE_URL
# BasePage — базовый класс Page Object:
# в нём лежат driver, wait и общие методы (click, type, text и т.д.)
from pages.base_page import BasePage
# InventoryPage — Page Object следующей страницы,
# на которую мы попадаем после успешного логина
from pages.inventory_page import InventoryPage


# LoginPage — Page Object страницы логина
# Наследуется от BasePage, поэтому:
# - имеет self.driver
# - имеет self.wait
# - может использовать self.type(), self.click() и т.д.
class LoginPage(BasePage):

    # ===== МЕТОД ОТКРЫТИЯ СТРАНИЦЫ =====
    def open(self) -> "LoginPage":
        """
                Открывает страницу логина по BASE_URL.

                Семантика:
                - driver.get(...) загружает страницу
                - метод возвращает self, чтобы можно было писать цепочки:
                  LoginPage(driver).open().login(...)
                """
        # self.driver — это WebDriver, полученный от BasePage
        self.driver.get(BASE_URL)

        # Возвращаем текущий объект LoginPage
        # Это НЕ обязательно, но удобно для fluent-интерфейса
        return self

    # ===== МЕТОД ЛОГИНА =====
    def login(self, username: str, password: str) -> InventoryPage:
        """
                Выполняет авторизацию пользователя.

                Принимает:
                - username — логин
                - password — пароль

                Возвращает:
                - объект InventoryPage, потому что после логина
                  пользователь попадает на страницу каталога
                """
        # Вводим логин:
        # self.type — метод BasePage:
        # 1. ждёт, пока элемент станет видимым
        # 2. очищает поле
        # 3. вводит текст
        self.type(LoginLocators.USERNAME_INPUT, username)

        # Вводим пароль — логика та же самая
        self.type(LoginLocators.PASSWORD_INPUT, password)

        # Кликаем по кнопке логина:
        # self.click — метод BasePage:
        # 1. ждёт, пока кнопка станет кликабельной
        # 2. кликает по ней
        self.click(LoginLocators.LOGIN_BUTTON)

        # Возвращаем новый Page Object следующей страницы
        # Мы передаём driver, потому что браузер тот же самый
        return InventoryPage(self.driver)