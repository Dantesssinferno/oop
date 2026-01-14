import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера."""
    chrome_options = Options()
    chrome_service = Service()
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_argument('--lang=en')
    user_data_dir = tempfile.mkdtemp(prefix="selenium-chrome-profile-")
    chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
    chrome_options.add_argument('--no-first-run')
    chrome_options.add_argument('--no-default-browser-check')
    chrome_options.add_argument('--disable-sync')
    chrome_options.add_argument('--incognito')

    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "translate": {"enable": False},
        "intl.accept_languages": "en,en_US",
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option('prefs', prefs)

    chrome_options.add_argument(
        "--disable-features=PasswordLeakDetection,PasswordManagerOnboarding,EnablePasswordsAccountStorage")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.set_window_size(1440, 860)

    yield driver
    #driver.quit()