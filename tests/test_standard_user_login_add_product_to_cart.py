# Импорт Page Object страницы логина.
# Тесты работают ТОЛЬКО с Page Object'ами,
# они не знают о Selenium, локаторах и ожиданиях.
from pages.login_page import LoginPage


def test_standard_user_add_product_to_cart(driver):
    """
    Тестовый сценарий (семантика):
    1. Открыть страницу логина
    2. Залогиниться стандартным пользователем
    3. Получить название и цену товара из каталога
    4. Добавить товар в корзину
    5. Перейти в корзину
    6. Сравнить данные товара в корзине с исходными

    Важно:
    - driver передаётся автоматически через pytest fixture
    - тест НЕ создаёт браузер и НЕ управляет ожиданиями
    """

    # ===== ШАГ 1. ОТКРЫТИЕ СТРАНИЦЫ ЛОГИНА =====

    # Создаём Page Object страницы логина.
    # driver — это WebDriver, созданный в фикстуре.
    #
    # .open() загружает BASE_URL
    # и возвращает self (LoginPage),
    # чтобы можно было продолжать цепочку вызовов.
    login = LoginPage(driver).open()

    # ===== ШАГ 2. АВТОРИЗАЦИЯ =====

    # login.login(...) выполняет ввод логина и пароля
    # и кликает кнопку Login.
    #
    # Семантически важно:
    # - после логина пользователь оказывается на странице каталога
    # - поэтому метод возвращает InventoryPage
    inventory = login.login("standard_user", "secret_sauce")

    # ===== ШАГ 3. ЧТЕНИЕ ДАННЫХ ТОВАРА =====

    # get_product_1_info() — query-метод:
    # - ничего не кликает
    # - не меняет состояние страницы
    # - просто читает данные
    #
    # Возвращает (title, price)
    title, price = inventory.get_product_1_info()

    # ===== ШАГ 4–5. ДОБАВЛЕНИЕ В КОРЗИНУ И ПЕРЕХОД =====

    # add_product_1_to_cart():
    # - кликает "Add to cart"
    # - страница НЕ меняется → возвращает self (InventoryPage)
    #
    # open_cart():
    # - кликает по иконке корзины
    # - происходит переход → возвращается CartPage
    cart = inventory.add_product_1_to_cart().open_cart()

    # ===== ШАГ 6. ЧТЕНИЕ ДАННЫХ ИЗ КОРЗИНЫ =====

    # get_cart_product_1_info() — снова query-метод:
    # - читает название и цену товара в корзине
    # - возвращает (cart_title, cart_price)
    cart_title, cart_price = cart.get_cart_product_1_info()

    # ===== ШАГ 7. ПРОВЕРКИ (ASSERTIONS) =====

    # Assert'ы живут ТОЛЬКО в тестах.
    # Page Object'ы НИЧЕГО не проверяют.
    assert cart_title == title, \
        f"Title mismatch. Catalog = '{title}', Card = '{cart_title}'"
    assert cart_price == price, \
        f"Price mismatch. Catalog = '{price}', Cart = {cart_price}"