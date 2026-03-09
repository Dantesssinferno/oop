from selenium.webdriver.common.by import By

class InventoryLocators:
    # ===== ЛОКАТОРЫ СТРАНИЦЫ КАТАЛОГА =====
    # Каждый локатор — это кортеж (By, value)
    # Они ОПИСЫВАЮТ элементы, но не ищут их напрямую

    # Название первого товара в каталоге
    FIRST_PRODUCT_TITLE = (By.XPATH, "//a[@id='item_4_title_link']")

    # Цена первого товара
    FIRST_PRODUCT_PRICE = (By.XPATH, "//div[@class='inventory_item_price'][1]")

    # Кнопка "Add to cart" для первого товара
    ADD_PRODUCT_TO_CART_BUTTON = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")

    # Ссылка (иконка) корзины в шапке страницы
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")

    # Локатор кнопки "OK" на попапе (может быть RU/EN разный)
    PASSWORD_POPUP_OK = (By.XPATH, "//button[.='ОК' or .='Ok' or .='OK']")