import allure
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