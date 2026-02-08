import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.auth_locators import AuthLocators
from locators.main_page_locators import MainPageLocators


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


def safe_click(browser, element):
    try:
        element.click()
    except Exception:
        browser.execute_script("arguments[0].click();", element)



@pytest.fixture(scope="function")
def registered_user(browser, generate_test_user):
    user = generate_test_user
    
    browser.get(AuthLocators.REGISTER_URL)
    
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input"))
    )
    
    browser.find_element(*AuthLocators.NAME_INPUT).send_keys(user['name'])
    browser.find_element(*AuthLocators.EMAIL_INPUT).send_keys(user['email'])
    browser.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(user['password'])
    
    register_button = browser.find_element(*AuthLocators.REGISTER_BUTTON)
    safe_click(browser, register_button)
    
    WebDriverWait(browser, 10).until(
        EC.url_to_be(AuthLocators.LOGIN_URL)
    )
    
    return user


@pytest.fixture(scope="function")
def auth_user(browser, registered_user):
    user = registered_user
    
    browser.get(AuthLocators.LOGIN_URL)
    
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input"))
    )
    
    browser.find_element(*AuthLocators.EMAIL_INPUT).send_keys(user['email'])
    browser.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(user['password'])
    
    login_button = browser.find_element(*AuthLocators.LOGIN_BUTTON)
    safe_click(browser, login_button)
    
    WebDriverWait(browser, 15).until(
        EC.url_to_be(MainPageLocators.CONSTRUCTOR_URL)
    )
    
    return user