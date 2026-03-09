import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import HEADLESS, KEEP_BROWSER

@pytest.fixture(scope = "function")
def driver():
    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")

    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1440, 860)

    try:
        yield driver
    finally:
        if not KEEP_BROWSER:
            driver.quit()