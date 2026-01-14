from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def open(self, url: str) -> None:
        self.driver.get(url)

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text: str, clear: bool = True) -> None:
        el = self.find_visible(locator)
        if clear:
            el.clear()
        el.send_keys(text)

    def text(self, locator) -> str:
        return self.find_visible(locator).text