from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self.url = None

    def open_page(self, url=None):
        url = url or self.url
        self._driver.get(url)

    def _input_field(self, locator, timeout=1, message=''):  # locator = tuple(type_of_selector, selector) == ((By.ID, 'user-name'))
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator), message=message)

    def _btn(self, locator, timeout=1, message=''):
        return WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(locator), message=message)
