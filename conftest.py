import pytest
import random
import string
from selenium import webdriver
from locators.auth_locators import AuthLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import REGISTER_URL, LOGIN_URL, CONSTRUCTOR_URL


@pytest.fixture(scope="function", params=['chrome', 'firefox'])
def browser(request):
    browser_name = request.param
    
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
        
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def generate_test_user():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return {
        'name': f'TestUser_{random_string}',
        'email': f'testuser_{random_string}@example.com',
        'password': 'TestPassword123!'
    }

@pytest.fixture(scope="function")
def registered_user(browser, generate_test_user):
    user = generate_test_user
    
    base_page = BasePage(browser, REGISTER_URL)
    base_page.open()
    
    base_page.wait_for_presence(AuthLocators.FORM_INPUTS)
    
    base_page.find_element(AuthLocators.NAME_INPUT).send_keys(user['name'])
    base_page.find_element(AuthLocators.EMAIL_INPUT).send_keys(user['email'])
    base_page.find_element(AuthLocators.PASSWORD_INPUT).send_keys(user['password'])
    
    register_button = base_page.find_element(AuthLocators.REGISTER_BUTTON)
    base_page.safe_click(register_button)
    
    base_page.wait_for_url(LOGIN_URL)
    
    return user

@pytest.fixture(scope="function")
def auth_user(browser, registered_user):
    user = registered_user
    
    base_page = BasePage(browser, LOGIN_URL)
    base_page.open()
    
    base_page.wait_for_presence(AuthLocators.FORM_INPUTS)
    
    base_page.find_element(AuthLocators.EMAIL_INPUT).send_keys(user['email'])
    base_page.find_element(AuthLocators.PASSWORD_INPUT).send_keys(user['password'])
    
    login_button = base_page.find_element(AuthLocators.LOGIN_BUTTON)
    base_page.safe_click(login_button)
    
    base_page.wait_for_url(CONSTRUCTOR_URL)
    
    yield user
    
    browser.delete_all_cookies()

    