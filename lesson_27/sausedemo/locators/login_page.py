
from selenium.webdriver.common.by import By


class LoginPageLocators:
    user_name_input_locator = (By.ID, 'user-name')
    user_pwd_input_locator = (By.ID, 'password')
    login_btn_locator = (By.CSS_SELECTOR, '#login-button')
    error_text_element = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
