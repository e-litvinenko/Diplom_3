import allure
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import CONSTRUCTOR_URL, FEED_URL

class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser, CONSTRUCTOR_URL)
    
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
        return self.get_current_url() == CONSTRUCTOR_URL
    
    def is_on_feed_page(self):
        return self.get_current_url() == FEED_URL
    
    @allure.step("Перетащить конкретный ингредиент в конструктор")
    def drag_ingredient_to_constructor(self, ingredient_locator):
        self.drag_and_drop_js(
            ingredient_locator,
            MainPageLocators.CONSTRUCTOR_AREA
        )
        self._wait(
            lambda driver: driver.find_element(*MainPageLocators.CONSTRUCTOR_AREA).is_displayed()
        ) 
    
    @allure.step("Получить значение счетчика")
    def get_counter_value(self, counter_locator):
        element = self.find_element(counter_locator, timeout=2)
        return int(element.text.strip())
    
    @allure.step("Получить номер заказа из модального окна")
    def get_order_number(self, timeout=15):
        self.wait_for_visibility(MainPageLocators.MODAL_CONTAINER, timeout=timeout)
        
        order_number_locator = MainPageLocators.ORDER_NUMBER
        
        self._wait(
            lambda driver: driver.find_element(*order_number_locator).text.strip() != "9999"
        )
        
        order_number_element = self.find_element(order_number_locator)
        return order_number_element.text.strip()
    
    @allure.step("Ожидать изменения счетчика")
    def wait_for_counter_change(self, counter_locator, initial_value, timeout=3):
        self._wait(
            lambda driver: self.get_counter_value(counter_locator) != initial_value
        )
    
    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)
    
    @allure.step("Дождаться видимости номера заказа")
    def wait_for_order_number_visible(self):
        self.wait_for_visibility(MainPageLocators.ORDER_NUMBER)
    
    @allure.step("Дождаться исчезновения модального окна")
    def wait_for_modal_invisible(self):
        self.wait_for_invisibility(MainPageLocators.MODAL_CONTAINER)
    
    @allure.step("Перетащить первую булку в конструктор")
    def drag_first_bun(self):
        self.drag_ingredient_to_constructor(MainPageLocators.FIRST_BUN)
    
    @allure.step("Перетащить первый соус в конструктор")
    def drag_first_sauce(self):
        self.drag_ingredient_to_constructor(MainPageLocators.FIRST_SAUCE)
    
    @allure.step("Перетащить первую начинку в конструктор")
    def drag_first_filling(self):
        self.drag_ingredient_to_constructor(MainPageLocators.FIRST_FILLING)
    
    @allure.step("Получить значение счетчика первой булки")
    def get_first_bun_counter_value(self):
        return self.get_counter_value(MainPageLocators.FIRST_BUN_COUNTER)
    
    @allure.step("Получить значение счетчика первого соуса")
    def get_first_sauce_counter_value(self):
        return self.get_counter_value(MainPageLocators.FIRST_SAUCE_COUNTER)
    
    @allure.step("Получить значение счетчика первой начинки")
    def get_first_filling_counter_value(self):
        return self.get_counter_value(MainPageLocators.FIRST_FILLING_COUNTER)
    
    @allure.step("Ожидать изменения счетчика первой булки")
    def wait_for_first_bun_counter_change(self, initial_value, timeout=3):
        self.wait_for_counter_change(MainPageLocators.FIRST_BUN_COUNTER, initial_value, timeout)
    
    @allure.step("Ожидать изменения счетчика первого соуса")
    def wait_for_first_sauce_counter_change(self, initial_value, timeout=3):
        self.wait_for_counter_change(MainPageLocators.FIRST_SAUCE_COUNTER, initial_value, timeout)
    
    @allure.step("Ожидать изменения счетчика первой начинки")
    def wait_for_first_filling_counter_change(self, initial_value, timeout=3):
        self.wait_for_counter_change(MainPageLocators.FIRST_FILLING_COUNTER, initial_value, timeout)

    @allure.step("Проверить видимость кнопки 'Конструктор'")
    def is_constructor_button_displayed(self):
        return self.is_element_displayed(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Проверить видимость кнопки 'Лента Заказов'")
    def is_feed_button_displayed(self):
        return self.is_element_displayed(MainPageLocators.FEED_BUTTON)
