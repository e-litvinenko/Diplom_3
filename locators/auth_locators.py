from selenium.webdriver.common.by import By

class AuthLocators:
    
    REGISTER_URL = "https://stellarburgers.education-services.ru/register"
    LOGIN_URL = "https://stellarburgers.education-services.ru/login"
    
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/parent::div//input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/parent::div//input[@type='password']")
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/parent::div//input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")