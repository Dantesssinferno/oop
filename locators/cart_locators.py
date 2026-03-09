from selenium.webdriver.common.by import By

class CartLocators:
    # ===== ЛОКАТОРЫ СТРАНИЦЫ КОРЗИНЫ =====
    # Каждый локатор — это кортеж (By, value)
    # Они не ищут элементы сами по себе, а только описывают,
    # как Selenium должен их найти

    # Название первого товара в корзине
    FIRST_CART_PRODUCT_TITLE = (By.XPATH, "//div[@class='inventory_item_name'][1]")

    # Цена первого товара в корзине
    FIRST_CART_PRODUCT_PRICE = (By.XPATH, "//div[@class='inventory_item_price'][1]")