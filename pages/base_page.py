from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import DEFAULT_TIMEOUT
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from typing import Tuple


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    """Method open current url"""
    def open(self, url: str) -> None:
        self.driver.get(url)

    """Method scroll to target element"""
    def scroll_to(self, locator: Tuple[str, str]) -> None:
        element = self.find_present(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    """Method find visible element"""
    def find_visible(self, locator: Tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    """Method find present element"""
    def find_present(self, locator: Tuple[str, str]) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    """Method click element"""
    def click(self, locator: Tuple[str, str], retries: int = 3) -> None:
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

    """Method click if present"""
    def click_if_present(self, locator: Tuple[str, str], timeout: int = 3) -> bool:
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
            return True
        except TimeoutException:
            return False

    """Method type text if element is visible"""
    def type(self, locator: Tuple[str, str], text: str, clear: bool = True) -> None:
        el = self.find_visible(locator)
        if clear:
            el.clear()
        el.send_keys(text)

    """Method GET text from locator"""
    def text(self, locator: Tuple[str, str]) -> str:
        return self.find_visible(locator).text

    """Method GET visible element"""
    def is_visible(self, locator: Tuple[str, str]) -> bool:
        try:
            self.find_visible(locator)
            return True
        except TimeoutException:
            return False
