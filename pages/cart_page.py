# By — перечисление стратегий поиска элементов в DOM
# Используется для описания локаторов (XPATH, ID, CSS и т.д.)
from selenium.webdriver.common.by import By
# CartLocators - это локаторы корзины
from locators.cart_locators import CartLocators
# BasePage — базовый Page Object:
# содержит WebDriver, WebDriverWait и общие методы работы с элементами
from pages.base_page import BasePage


# CartPage — Page Object страницы корзины
# Он ОПИСЫВАЕТ страницу корзины и предоставляет методы
# для чтения данных и взаимодействия с ней
class CartPage(BasePage):

    # ===== МЕТОД ЧТЕНИЯ ДАННЫХ ИЗ КОРЗИНЫ =====
    def get_cart_product_1_info(self) -> tuple[str, str]:
        """
        Возвращает информацию о первом товаре в корзине.

        Семантика:
        - метод НИЧЕГО не кликает
        - не меняет состояние страницы
        - используется для проверок (assert) в тесте

        Возвращает:
        - кортеж (title, price)
        """

        # self.text — метод BasePage:
        # 1. ждёт, пока элемент станет видимым
        # 2. возвращает текст элемента
        title = self.text(CartLocators.FIRST_CART_PRODUCT_TITLE)

        # Аналогично получаем цену товара
        price = self.text(CartLocators.FIRST_CART_PRODUCT_PRICE)

        # Возвращаем оба значения вместе,
        # потому что логически они относятся к одному объекту — товару
        return title, price
