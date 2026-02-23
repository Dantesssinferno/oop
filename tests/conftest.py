import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import HEADLESS, KEEP_BROWSER


@pytest.fixture(scope = "function")
def driver():
    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1440, 860)

    try:
        yield driver
    finally:
        if not KEEP_BROWSER:
            driver.quit()