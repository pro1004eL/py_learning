from all_lessons.lesson_27.sausedemo.locators.login_page import LoginPageLocators
from all_lessons.lesson_27.sausedemo.pages.base_page import BasePage
from all_lessons.lesson_27.sausedemo.pages.product_page import ProductPage
from settings import settings


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)  # викликаємо метод ініт у батьківського (BasePage) класу
        self.url = settings.SAUCEDEMO_URL
        self.locators = LoginPageLocators()

    def _user_name_input(self):
        return self._input_field(self.locators.user_name_input_locator, message='Can`t find user name input at Login Page')

    def _user_pwd_input(self):
        return self._input_field(self.locators.user_pwd_input_locator, message='Can`t find user pwd input at Login Page')
    def _login_btn(self):
        return self._btn(self.locators.login_btn_locator, message='Can`t find login btn at Login Page', timeout=3)

    def set_user_name(self, user_name):
        self._user_name_input().send_keys(user_name)
        return self

    def set_user_pwd(self, user_pwd):
        self._user_pwd_input().send_keys(user_pwd)
        return self

    def click_login_btn(self):
        self._login_btn().click()
        return self

    # positive cases
    def login_user(self, user_name, user_pwd) -> ProductPage:
        self.set_user_name(user_name).set_user_pwd(user_pwd).click_login_btn()
        return ProductPage(self._driver)

    def error_h3_text_wrong_name_or_pwd(self):
        return self._present_text(self.locators.error_text_element,
                                  'Epic sadface: Username and password do not match any user in this service')



