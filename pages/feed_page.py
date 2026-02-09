import allure
from selenium.webdriver.support import expected_conditions as EC  
from locators.feed_page_locators import FeedPageLocators
from .base_page import BasePage


class FeedPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)    
        
    @allure.step("Получить счетчик 'Выполнено за все время'")
    def get_total_orders_all_time(self, timeout=10):
        element = self.find_element(FeedPageLocators.TOTAL_ORDERS_ALL_TIME, timeout=timeout)
        return int(element.text.replace(' ', ''))
    
    @allure.step("Получить счетчик 'Выполнено за сегодня'")
    def get_total_orders_today(self, timeout=10):
        element = self.find_element(FeedPageLocators.TOTAL_ORDERS_TODAY, timeout=timeout)
        return int(element.text.replace(' ', ''))
    
    @allure.step("Получить заказы в работе")
    def get_orders_in_progress(self, timeout=10):
        elements = self.find_elements(FeedPageLocators.IN_PROGRESS_ORDER_NUMBERS, timeout=timeout)
        return [element.text.strip() for element in elements]
    
    @allure.step("Ожидать увеличения счетчика 'Выполнено за все время'")
    def wait_for_all_time_counter_to_increase(self, before_value, timeout=15):
        self._wait(
            lambda driver: int(driver.find_element(*FeedPageLocators.TOTAL_ORDERS_ALL_TIME).text.replace(' ', '')) > before_value,
            timeout=timeout
        )  
    
    @allure.step("Ожидать увеличения счетчика 'Выполнено за сегодня'")
    def wait_for_today_counter_to_increase(self, before_value, timeout=15):
        self._wait(
            lambda driver: int(driver.find_element(*FeedPageLocators.TOTAL_ORDERS_TODAY).text.replace(' ', '')) > before_value,
            timeout=timeout
        )  
    
    @allure.step("Ожидать появления раздела 'В работе'")
    def wait_for_in_progress_section(self, timeout=15):
        self._wait(
            EC.presence_of_element_located(FeedPageLocators.IN_PROGRESS_SECTION),
            timeout=timeout
        )  