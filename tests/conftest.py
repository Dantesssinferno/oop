# pytest — тестовый фреймворк.
# @pytest.fixture помечает функцию как фикстуру,
# которую pytest будет автоматически подставлять в тесты.
import pytest

# tempfile используется для создания временных директорий.
# Здесь — для изолированного профиля браузера на каждый запуск.
import tempfile

# webdriver — основной API Selenium для управления браузером
from selenium import webdriver

# Options — объект конфигурации браузера Chrome
from selenium.webdriver.chrome.options import Options

# Service — объект, управляющий процессом chromedriver
from selenium.webdriver.chrome.service import Service


# ===== FIXTURE DRIVER =====
@pytest.fixture
def driver():
    """
    Фикстура driver отвечает за:
    - создание браузера
    - его конфигурацию
    - передачу WebDriver в тест
    - (опционально) закрытие браузера после теста

    Семантика:
    - тест НЕ знает, как создаётся браузер
    - тест просто получает готовый driver
    """

    # ===== 1. СОЗДАНИЕ ОБЪЕКТОВ КОНФИГУРАЦИИ =====

    # chrome_options — объект, в который мы складываем
    # все параметры запуска Chrome
    chrome_options = Options()

    # chrome_service — объект, отвечающий за процесс chromedriver
    # (через него Selenium общается с браузером)
    chrome_service = Service()

    # ===== 2. БАЗОВЫЕ НАСТРОЙКИ БРАУЗЕРА =====

    # detach=True — Chrome не закрывается автоматически,
    # если Python-процесс завершился (удобно для отладки)
    chrome_options.add_experimental_option("detach", True)

    # Язык интерфейса браузера
    chrome_options.add_argument("--lang=en")

    # ===== 3. ИЗОЛИРОВАННЫЙ ПРОФИЛЬ БРАУЗЕРА =====

    # Создаём временную директорию для профиля Chrome
    # Это гарантирует:
    # - отсутствие сохранённых паролей
    # - отсутствие кэша
    # - отсутствие влияния предыдущих тестов
    user_data_dir = tempfile.mkdtemp(prefix="selenium-chrome-profile-")

    # Указываем Chrome использовать этот профиль
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

    # Отключаем первый запуск и системные подсказки Chrome
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")

    # Отключаем синхронизацию с Google-аккаунтом
    chrome_options.add_argument("--disable-sync")

    # Инкогнито-режим:
    # - не сохраняет историю
    # - снижает влияние состояния браузера
    chrome_options.add_argument("--incognito")

    # ===== 4. НАСТРОЙКИ PREFERENCES (prefs) =====

    # prefs — это "внутренние" настройки Chrome
    # Они управляют поведением браузера без аргументов CLI
    prefs = {
        # Отключаем браузерные уведомления
        "profile.default_content_setting_values.notifications": 2,

        # Отключаем автоперевод страниц
        "translate": {"enable": False},

        # Предпочтительный язык контента
        "intl.accept_languages": "en,en_US",

        # Отключаем сервис сохранения учётных данных
        "credentials_enable_service": False,

        # Отключаем менеджер паролей
        "profile.password_manager_enabled": False,

        # Отключаем детекцию утечек паролей
        "password_manager_leak_detection": False,
    }

    # Передаём preferences в Chrome
    chrome_options.add_experimental_option("prefs", prefs)

    # ===== 5. ЖЁСТКОЕ ОТКЛЮЧЕНИЕ PASSWORD MANAGER =====

    # Эти флаги дополнительно гарантируют,
    # что попапы сохранения паролей не появятся
    chrome_options.add_argument(
        "--disable-features="
        "PasswordLeakDetection,"
        "PasswordManagerOnboarding,"
        "EnablePasswordsAccountStorage"
    )

    # Отключаем всплывающее окно сохранения пароля
    chrome_options.add_argument("--disable-save-password-bubble")

    # Отключаем расширения (ускоряет запуск и повышает стабильность)
    chrome_options.add_argument("--disable-extensions")

    # ===== 6. СОЗДАНИЕ WEB DRIVER =====

    # Создаём экземпляр Chrome WebDriver
    # На этом шаге:
    # - запускается chromedriver
    # - запускается Chrome
    # - устанавливается WebDriver-сессия
    driver = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    # Устанавливаем фиксированный размер окна,
    # чтобы верстка была предсказуемой
    driver.set_window_size(1440, 860)

    # ===== 7. ПЕРЕДАЧА DRIVER В ТЕСТ =====

    # yield — ключевой момент фикстуры:
    # всё ДО yield — setup
    # всё ПОСЛЕ yield — teardown
    yield driver

    # ===== 8. TEARDOWN (ЗАКРЫТИЕ БРАУЗЕРА) =====

    # Закрывает браузер и завершает WebDriver-сессию
    # В реальных проектах ЭТО ДОЛЖНО БЫТЬ ВКЛЮЧЕНО
    #driver.quit()