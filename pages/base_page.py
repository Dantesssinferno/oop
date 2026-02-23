from xml.sax.xmlreader import Locator

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import DEFAULT_TIMEOUT
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException

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

    def click(self, locator, retries: int = 3):
        last_exception = None

        for attempt in range(retries):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException as e:
                last_exception = e
                if attempt == retries -1:
                    # если все попытки провалились
                    raise last_exception

    def click_if_present(self, locator, timeout: int = 3) -> bool:
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
            return True
        except TimeoutException:
            return False

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
        except TimeoutException:
            return False
        