import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера."""
    options = webdriver.ChromeOptions()
    # Оставить окно открытым по желанию (можно убрать, если не нужно)
    options.add_experimental_option("detach", True)
    # ВРЕМЕННЫЙ workaround вместо maximize_window()
    # driver.maximize_window()
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()
