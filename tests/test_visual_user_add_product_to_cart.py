import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException

class TestLogin_2:
    # Standard User Login
    LOGIN_VISUAL_USER = 'visual_user'
    # Password
    PASSWORD_UNIVERSAL = 'secret_sauce'

    # Product 1: title and price (локаторы в виде кортежей)
    PRODUCT_1_XPATH = (By.XPATH,"//a[@id='item_4_title_link']")
    PRICE_PROD_1_XPATH = (By.XPATH, "//div[@class='inventory_item_price'][1]")
    # Select btn
    SELECT_PROD_1_XPATH = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    # Cart
    CART_LINK_XPATH = (By.XPATH, "//a[@class='shopping_cart_link']")
    CART_PRODUCT_1_XPATH = (By.XPATH, "//div[@class='inventory_item_name'][1]")
    CART_PRICE_PROD_1_XPATH = (By.XPATH, "//div[@class='inventory_item_price'][1]")
    # Cart checkout
    CART_CHECKOUT_XPATH = (By.XPATH, "//button[@id='checkout']")

    def close_password_leak_popup(self, driver):
        try:
            # Кнопка "ОК" на попапе (может отличаться, подбирается по локатору)
            ok_buttons = driver.find_elements(By.XPATH, "//button[.='ОК' or .='Ok' or .='OK']")
            if ok_buttons:
                ok_buttons[0].click()
                print("Закрыл попап смены пароля")
        except NoSuchElementException:
            pass

    def test_select_and_check_product(self, driver):
        """
        Сценарий:
        1.Открыть сайт Swag Labs.
        2.Залогиниться стандартным пользователем.
        3.Прочитать название и цену первого товара.
        4.Добавить товар в корзину.
        5.Открыть корзину.
        6.Сравнить название и цену в корзине с исходными значениями.
        """
        wait = WebDriverWait(driver, 10)

        # 1. Открываем сайт
        base_url = "https://www.saucedemo.com/"
        driver.get(base_url)
        print("Start Test")
        time.sleep(2)

        #2. Логинимся через Page Object
        login_page = LoginPage(driver)
        login_page.authorization(self.LOGIN_VISUAL_USER, self.PASSWORD_UNIVERSAL)

        # Закрыть Pop-Up смены пароля
        self.close_password_leak_popup(driver)

        # 3. Читаем данные по продукту
        title, price = self.read_product_1(driver, wait, self.PRODUCT_1_XPATH, self.PRICE_PROD_1_XPATH)

        # 4. Выбираем продукт, добавляем в корзину
        self.select_prod(driver, wait, self.SELECT_PROD_1_XPATH)

        # 5. Открываем корзину
        self.open_cart(driver, wait, self.CART_LINK_XPATH)

        # 6. Сверяем цену и название товара в корзине
        cart_title, cart_price = self.cart_info(driver, wait, self.CART_PRODUCT_1_XPATH, self.CART_PRICE_PROD_1_XPATH)
        # 7. Сравниваем значения
        print(f"Ожидаемое значение: {title}, в корзине: {cart_title}")
        print(f"Ожидаемое значение: {price}, в корзине: {cart_price}")

        assert cart_title == title, \
        "Название товара в корзине не совпадает с названием на странице"
        assert cart_price == price, \
        "Цена товара в корзине не совпадает с ценой на странице"
        # self.driver.quit()

    def read_product_1(self, driver, wait: WebDriverWait, title_xpath: tuple, price_xpath: tuple) -> tuple[str, str]:
        """Считать название и цену товара на странице каталога."""
        # Ждем, пока появится заголовок продукта
        wait.until(EC.presence_of_element_located(title_xpath))
        title_el = driver.find_element(*title_xpath)
        value_title = title_el.text
        print(f"Шаг: 2 Product title: {value_title}")

        # Ждём, пока появится цена продукта
        wait.until(EC.presence_of_element_located(price_xpath))
        price_el = driver.find_element(*price_xpath)
        value_price = price_el.text
        print(f"Шаг: 2.1 Product price: {value_price}")

        return value_title, value_price

    def select_prod(self, driver, wait:WebDriverWait, select_btn_xpath: tuple) -> None:
        """Нажать на кнопку добавления товара в корзину."""
        wait.until(EC.element_to_be_clickable(select_btn_xpath))
        driver.find_element(*select_btn_xpath).click()
        print(f"Шаг: 3: Selected prod: Passed")

        time.sleep(3)

    def open_cart(self, driver, wait:WebDriverWait, cart_xpath: tuple) -> None:
        """Открыть корзину."""
        wait.until(EC.element_to_be_clickable(cart_xpath))
        driver.find_element(*cart_xpath).click()
        print(f"Шаг: 4: Enter cart: Passed")

    def cart_info(self, driver, wait:WebDriverWait, title_xpath: tuple, price_xpath: tuple) -> tuple[str, str]:
        """Считать название и цену товара в корзине."""
        wait.until(EC.presence_of_element_located(title_xpath))
        cart_title_el = driver.find_element(*title_xpath)
        cart_title = cart_title_el.text
        print(f"Шаг: 5 Cart product title: {cart_title}")

        wait.until(EC.presence_of_element_located(price_xpath))
        cart_price_el = driver.find_element(*price_xpath)
        cart_price = cart_price_el.text
        print(f"Шаг: 6 Cart product price: {cart_price}")

        return cart_title, cart_price

    def checkout_cart(self, driver, wait: WebDriverWait, cart_checkout_xpath: tuple) -> None:
        """Нажать кнопку Checkout в корзине."""
        wait.until(EC.element_to_be_clickable(cart_checkout_xpath))
        driver.find_element(*cart_checkout_xpath).click()
        print(f"Шаг: 7: Checkout button clicked : success")
        time.sleep(1)