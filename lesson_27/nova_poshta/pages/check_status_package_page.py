from all_lessons.lesson_27.nova_poshta.locators.check_status_page import CheckStatusPageLocators
from all_lessons.lesson_27.nova_poshta.pages.base_page import BasePage
from settings import settings


class CheckStatusPackage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)  # викликаємо метод ініт у батьківського (BasePage) класу
        self.url = settings.SAUCEDEMO_URL
        self.locators = CheckStatusPageLocators()
