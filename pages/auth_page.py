import allure
from .base_page import BasePage
from locators.auth_locators import AuthLocators

class AuthPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
    
    @allure.step("Заполнить поле 'Имя'")
    def fill_name(self, name):
        self.find_element(AuthLocators.NAME_INPUT).send_keys(name)
    
    @allure.step("Заполнить поле 'Email'")
    def fill_email(self, email):
        self.find_element(AuthLocators.EMAIL_INPUT).send_keys(email)
    
    @allure.step("Заполнить поле 'Пароль'")
    def fill_password(self, password):
        self.find_element(AuthLocators.PASSWORD_INPUT).send_keys(password)
    
    @allure.step("Нажать кнопку 'Зарегистрироваться'")
    def click_register(self):
        element = self.find_element(AuthLocators.REGISTER_BUTTON)
        self.safe_click(element)
    
    @allure.step("Нажать кнопку 'Войти'")
    def click_login(self):
        element = self.find_element(AuthLocators.LOGIN_BUTTON)
        self.safe_click(element)
    
    @allure.step("Дождаться загрузки формы")
    def wait_for_form(self):
        self.wait_for_presence(AuthLocators.FORM_INPUTS)