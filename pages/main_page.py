import allure
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser, MainPageLocators.CONSTRUCTOR_URL)
    
    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Кликнуть на 'Лента Заказов'")
    def click_feed(self):
        self.click(MainPageLocators.FEED_BUTTON)
    
    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        self.click(MainPageLocators.FIRST_INGREDIENT)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
    
    @allure.step("Проверить видимость модального окна ингредиента")
    def is_modal_visible(self):
        try:
            return self.is_element_displayed(MainPageLocators.MODAL_CONTAINER, timeout=3)
        except TimeoutException:
            return False
    
    @allure.step("Проверить что модальное окно закрыто")
    def is_modal_closed(self):
        try:
            self.wait_for_invisibility(MainPageLocators.MODAL_CONTAINER, timeout=3)
            return True
        except TimeoutException:
            return False
    
    def is_on_main_page(self):
        return self.get_current_url() == MainPageLocators.CONSTRUCTOR_URL
    
    def is_on_feed_page(self):
        return self.get_current_url() == MainPageLocators.FEED_URL
    
    @allure.step("Перетащить конкретный ингредиент в конструктор")
    def drag_ingredient_to_constructor(self, ingredient_locator):
        self.drag_and_drop_js(
            ingredient_locator,
            MainPageLocators.CONSTRUCTOR_AREA
        )
        time.sleep(0.5)
    
    @allure.step("Получить значение счетчика")
    def get_counter_value(self, counter_locator):
        element = self.find_element(counter_locator, timeout=2)
        return int(element.text.strip())