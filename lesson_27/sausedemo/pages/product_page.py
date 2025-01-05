from all_lessons.lesson_27.sausedemo.locators.product_page import ProductPageLocators
from all_lessons.lesson_27.sausedemo.pages.base_page import BasePage
from settings import settings


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)  # викликаємо метод ініт у батьківського (BasePage) класу
        self.url = f'{settings.SAUCEDEMO_URL}/inventory.html'
        self.locators = ProductPageLocators()

    def _add_to_cart_btn(self):
        return self._btn(self.locators.add_to_cart_button)

    def _remove_from_cart_btn(self):
        return self._btn(self.locators.remove_from_cart_button)

    def click_add_to_cart_btn(self):
        self._add_to_cart_btn().click()
        return self

    def click_remove_from_cart_btn(self):
        self._remove_from_cart_btn().click()
        return self
