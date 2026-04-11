import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def base_url() -> str:
    return os.getenv("BASE_URL", "https://www.saucedemo.com/")


@pytest.fixture
def credentials() -> tuple[str, str]:
    username = os.getenv("SAUCE_USERNAME", "standard_user")
    password = os.getenv("SAUCE_PASSWORD", "secret_sauce")
    return username, password


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    if os.getenv("SELENIUM_HEADLESS", "1") == "1":
        options.add_argument("--headless=new")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(3)
    yield browser
    browser.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)
