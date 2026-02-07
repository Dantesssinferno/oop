from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import DEFAULT_TIMEOUT


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def find_visible(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_present(self, locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def type(self, locator, text: str, clear: bool = True) -> None:
        el = self.find_visible(locator)
        if clear:
            el.clear()
        el.send_keys(text)

    def text(self, locator) -> str:
        return self.find_visible(locator).text

    def is_visible(self, locator) -> bool:
        try:
            self.find_visible(locator)
            return True
        except Exception:
            return False
        