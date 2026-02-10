import pytest
import random
import string
from selenium import webdriver
from pages.auth_page import AuthPage 
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
    
    auth_page = AuthPage(browser, REGISTER_URL)
    auth_page.open()
    auth_page.wait_for_form()
    
    auth_page.fill_name(user['name'])
    auth_page.fill_email(user['email'])  
    auth_page.fill_password(user['password'])
    auth_page.click_register()
    
    auth_page.wait_for_url(LOGIN_URL)
    
    return user

@pytest.fixture(scope="function")
def auth_user(browser, registered_user):
    user = registered_user
    
    auth_page = AuthPage(browser, LOGIN_URL)
    auth_page.open()
    auth_page.wait_for_form()
    
    auth_page.fill_email(user['email'])
    auth_page.fill_password(user['password'])
    auth_page.click_login()
    
    auth_page.wait_for_url(CONSTRUCTOR_URL)
    
    yield user
    
    browser.delete_all_cookies()