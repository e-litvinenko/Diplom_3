import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from locators.feed_page_locators import FeedPageLocators
from locators.main_page_locators import MainPageLocators


class TestFeedFunctionality:
    
    @allure.title("Раздел «Лента заказов»: при создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_feed_all_time_counter_increases(self, browser, auth_user):
        
        with allure.step("Открыть ленту заказов и получить начальное значение счетчика"):
            feed_page = FeedPage(browser, MainPageLocators.FEED_URL)
            wait = WebDriverWait(browser, 15)
            feed_page.open()
            before_value = feed_page.get_total_orders_all_time()
        
        with allure.step("Перейти на страницу конструктора"):
            main_page = MainPage(browser)
            main_page.open()
        
        with allure.step("Создать заказ: перетащить булку, соус, начинку"):
            main_page.drag_ingredient_to_constructor(MainPageLocators.FIRST_BUN)
            main_page.drag_ingredient_to_constructor(MainPageLocators.FIRST_SAUCE)
            main_page.drag_ingredient_to_constructor(MainPageLocators.FIRST_FILLING)
        
        with allure.step("Нажать кнопку 'Оформить заказ'"):
            main_page.click(MainPageLocators.ORDER_BUTTON)
        
        with allure.step("Закрыть модальное окно заказа"):
            main_page.wait_for_visibility(MainPageLocators.ORDER_NUMBER)
            main_page.close_modal()
            main_page.wait_for_invisibility(MainPageLocators.MODAL_CONTAINER)
        
        with allure.step("Вернуться на страницу 'Лента заказов' и получить новое значение счетчика"):
            feed_page.open()
            wait.until(
                lambda driver: int(driver.find_element(*FeedPageLocators.TOTAL_ORDERS_ALL_TIME).text.replace(' ', '')) > before_value
            )
            after_value = feed_page.get_total_orders_all_time()
        
        with allure.step("Проверить, что новое значение счетчика больше начального"):
            assert after_value > before_value, f"Счетчик не увеличился: было {before_value}, стало {after_value}"
        
        with allure.step("Очистить куки (выход из системы)"):
            browser.delete_all_cookies()
    
    @allure.title("Раздел «Лента заказов»: при создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_feed_today_counter_increases(self, browser, auth_user):
        
        with allure.step("Открыть ленту заказов и получить начальное значение счетчика 'за сегодня'"):
            feed_page = FeedPage(browser, MainPageLocators.FEED_URL)
            wait = WebDriverWait(browser, 15)
            feed_page.open()
            before_value = feed_page.get_total_orders_today()
        
        with allure.step("Перейти на страницу конструктора"):
            main_page = MainPage(browser)
            main_page.open()
        
        with allure.step("Создать заказ: перетащить булку, соус, начинку"):
            main_page.drag_ingredient_to_constructor(MainPageLocators.FIRST_BUN)
            main_page.drag_ingredient_to_constructor(MainPageLocators.FIRST_SAUCE)
            main_page.drag_ingredient_to_constructor(MainPageLocators.FIRST_FILLING)
        
        with allure.step("Нажать кнопку 'Оформить заказ'"):
            main_page.click(MainPageLocators.ORDER_BUTTON)
        
        with allure.step("Закрыть модальное окно заказа"):
            main_page.wait_for_visibility(MainPageLocators.ORDER_NUMBER)
            main_page.close_modal()
            main_page.wait_for_invisibility(MainPageLocators.MODAL_CONTAINER)
        
        with allure.step("Вернуться на страницу 'Лента заказов' и получить новое значение счетчика 'за сегодня'"):
            feed_page.open()
            wait.until(
                lambda driver: int(driver.find_element(*FeedPageLocators.TOTAL_ORDERS_TODAY).text.replace(' ', '')) > before_value
            )
            after_value = feed_page.get_total_orders_today()
        
        with allure.step("Проверить, что новое значение счетчика 'за сегодня' больше начального"):
            assert after_value > before_value, f"Счетчик 'за сегодня' не увеличился: было {before_value}, стало {after_value}"
        
        with allure.step("Очистить куки (выход из системы)"):
            browser.delete_all_cookies()
    
    @allure.title("Раздел «Лента заказов»: после оформления заказа его номер появляется в разделе «В работе»")
    def test_feed_order_appears_in_progress_section(self, browser, auth_user):
        
        with allure.step("Перейти на страницу конструктора"):
            main_page = MainPage(browser)
            main_page.open()
            wait = WebDriverWait(browser, 15)
        
        with allure.step("Создать заказ: перетащить булку, соус, начинку"):
            main_page.drag_ingredient_to_constructor(MainPageLocators.FIRST_BUN)
            main_page.drag_ingredient_to_constructor(MainPageLocators.FIRST_SAUCE)
            main_page.drag_ingredient_to_constructor(MainPageLocators.FIRST_FILLING)
        
        with allure.step("Нажать кнопку 'Оформить заказ'"):
            main_page.click(MainPageLocators.ORDER_BUTTON)
        
        with allure.step("Получить номер созданного заказа из модального окна"):
            main_page.wait_for_visibility(MainPageLocators.MODAL_CONTAINER)
            
            order_number_locator = MainPageLocators.ORDER_NUMBER
            
            wait.until(
                lambda driver: driver.find_element(*order_number_locator).text.strip() != "9999"
            )
            
            order_number_element = browser.find_element(*order_number_locator)
            order_number = order_number_element.text.strip()
        
        with allure.step("Закрыть модальное окно заказа"):
            main_page.close_modal()
            main_page.wait_for_invisibility(MainPageLocators.MODAL_CONTAINER)
        
        with allure.step("Перейти на страницу 'Лента заказов'"):
            feed_page = FeedPage(browser, MainPageLocators.FEED_URL)
            feed_page.open()
        
        with allure.step("Найти номер заказа в разделе «В работе»"):
            wait.until(EC.presence_of_element_located(FeedPageLocators.IN_PROGRESS_SECTION))
            
            orders_in_progress = feed_page.get_orders_in_progress()
        
        with allure.step(f"Проверить, что номер заказа '{order_number}' присутствует в списке «В работе»"):
            order_found = any(order_number in found_number for found_number in orders_in_progress)
            
            assert order_found, (
                f"Номер заказа '{order_number}' не найден ни в одном из номеров в разделе 'В работе'. "
                f"Найдены: {orders_in_progress}"
            )
        
        with allure.step("Очистить куки (выход из системы)"):
            browser.delete_all_cookies()