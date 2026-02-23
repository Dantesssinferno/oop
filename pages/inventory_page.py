# By — перечисление стратегий поиска элементов в DOM
# (XPATH, ID, CSS_SELECTOR и т.д.)
from selenium.webdriver.common.by import By
from wait.decorator import timeout

# BasePage — базовый Page Object:
# содержит driver, wait и общие методы работы с элементами
from pages.base_page import BasePage

# CartPage — Page Object страницы корзины,
# на которую мы перейдём после клика по иконке корзины
from pages.cart_page import CartPage


# InventoryPage — Page Object страницы каталога товаров
# Наследуется от BasePage, поэтому имеет:
# - self.driver (WebDriver)
# - self.wait (WebDriverWait)
# - методы click(), text(), type() и т.д.
class InventoryPage(BasePage):

    # ===== ЛОКАТОРЫ СТРАНИЦЫ КАТАЛОГА =====
    # Каждый локатор — это кортеж (By, value)
    # Они ОПИСЫВАЮТ элементы, но не ищут их напрямую

    # Название первого товара в каталоге
    PRODUCT_1_TITLE = (By.XPATH, "//a[@id='item_4_title_link']")

    # Цена первого товара
    PRODUCT_1_PRICE = (By.XPATH, "//div[@class='inventory_item_price'][1]")

    # Кнопка "Add to cart" для первого товара
    ADD_PRODUCT_1 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")

    # Ссылка (иконка) корзины в шапке страницы
    CART_LINK = (By.XPATH, "//a[@class='shopping_cart_link']")

    # Локатор кнопки "OK" на попапе (может быть RU/EN разный)
    PASSWORD_POPUP_OK = (By.XPATH, "//button[.='ОК' or .='Ok' or .='OK']")



    def close_password_leak_popup_if_present(self) -> "InventoryPage":
        """

        Закрывает попап, если он появился.
        Не падает, если попапа нет.
        """
        clicked = self.click_if_present(self.PASSWORD_POPUP_OK, timeout=2)
        if clicked:
            print("Закрыл попап смены пароля")
        return self

    # ===== МЕТОД ЧТЕНИЯ ДАННЫХ ТОВАРА =====
    def get_product_1_info(self) -> tuple[str, str]:
        """
        Возвращает информацию о первом товаре в каталоге.

        Семантика:
        - метод НИЧЕГО не кликает
        - он только читает данные со страницы
        - используется для сравнений в тесте

        Возвращает:
        - кортеж (title, price)
        """

        # self.text — метод BasePage:
        # 1. ждёт, пока элемент станет видимым
        # 2. возвращает его текстовое содержимое
        title = self.text(self.PRODUCT_1_TITLE)

        # Читаем цену товара аналогичным образом
        price = self.text(self.PRODUCT_1_PRICE)

        # Возвращаем данные как единое логическое целое
        return title, price

    # ===== МЕТОД ДОБАВЛЕНИЯ ТОВАРА В КОРЗИНУ =====
    def add_product_1_to_cart(self) -> "InventoryPage":
        """
        Добавляет первый товар в корзину.

        Семантика:
        - метод выполняет ДЕЙСТВИЕ (click)
        - страница при этом НЕ МЕНЯЕТСЯ
        - поэтому возвращаем self (InventoryPage)

        Это позволяет писать цепочки вызовов:
        inventory.add_product_1_to_cart().open_cart()
        """

        # self.click — метод BasePage:
        # 1. ждёт, пока кнопка станет кликабельной
        # 2. кликает по ней
        self.click(self.ADD_PRODUCT_1)

        # Возвращаем текущую страницу,
        # потому что пользователь всё ещё находится в каталоге
        return self

    # ===== ПЕРЕХОД В КОРЗИНУ =====
    def open_cart(self) -> CartPage:
        """
        Переходит на страницу корзины.

        Семантика:
        - после клика пользователь оказывается на ДРУГОЙ странице
        - поэтому возвращаем новый Page Object — CartPage
        """

        # Кликаем по иконке корзины
        self.click(self.CART_LINK)
        print(self.driver.current_url)
        # Создаём и возвращаем Page Object корзины
        # Передаём driver, потому что браузер тот же самый
        return CartPage(self.driver)
