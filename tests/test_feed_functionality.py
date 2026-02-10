import allure
import pytest
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from urls import FEED_URL


class TestFeedFunctionality:
    
    @allure.title("Раздел «Лента заказов»: при создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_feed_all_time_counter_increases(self, browser, auth_user):
        
        with allure.step("Открыть ленту заказов и получить начальное значение счетчика"):
            feed_page = FeedPage(browser, FEED_URL)
            feed_page.open()
            before_value = feed_page.get_total_orders_all_time()
        
        with allure.step("Перейти на страницу конструктора"):
            main_page = MainPage(browser)
            main_page.open()
        
        with allure.step("Создать заказ: перетащить булку, соус, начинку"):
            main_page.drag_first_bun()
            main_page.drag_first_sauce()
            main_page.drag_first_filling()
        
        with allure.step("Нажать кнопку 'Оформить заказ'"):
            main_page.click_order_button()
        
        with allure.step("Закрыть модальное окно заказа"):
            main_page.wait_for_order_number_visible()
            main_page.close_modal()
            main_page.wait_for_modal_invisible()
        
        with allure.step("Вернуться на страницу 'Лента заказов' и получить новое значение счетчика"):
            feed_page.open()
            feed_page.wait_for_all_time_counter_to_increase(before_value)
            after_value = feed_page.get_total_orders_all_time()
        
        with allure.step("Проверить, что новое значение счетчика больше начального"):
            assert after_value > before_value, f"Счетчик не увеличился: было {before_value}, стало {after_value}"
    
    @allure.title("Раздел «Лента заказов»: при создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_feed_today_counter_increases(self, browser, auth_user):
        
        with allure.step("Открыть ленту заказов и получить начальное значение счетчика 'за сегодня'"):
            feed_page = FeedPage(browser, FEED_URL)
            feed_page.open()
            before_value = feed_page.get_total_orders_today()
        
        with allure.step("Перейти на страницу конструктора"):
            main_page = MainPage(browser)
            main_page.open()
        
        with allure.step("Создать заказ: перетащить булку, соус, начинку"):
            main_page.drag_first_bun()
            main_page.drag_first_sauce()
            main_page.drag_first_filling()
        
        with allure.step("Нажать кнопку 'Оформить заказ'"):
            main_page.click_order_button()
        
        with allure.step("Закрыть модальное окно заказа"):
            main_page.wait_for_order_number_visible()
            main_page.close_modal()
            main_page.wait_for_modal_invisible()
        
        with allure.step("Вернуться на страницу 'Лента заказов' и получить новое значение счетчика 'за сегодня'"):
            feed_page.open()
            feed_page.wait_for_today_counter_to_increase(before_value)
            after_value = feed_page.get_total_orders_today()
        
        with allure.step("Проверить, что новое значение счетчика 'за сегодня' больше начального"):
            assert after_value > before_value, f"Счетчик 'за сегодня' не увеличился: было {before_value}, стало {after_value}"
    
    @allure.title("Раздел «Лента заказов»: после оформления заказа его номер появляется в разделе «В работе»")
    def test_feed_order_appears_in_progress_section(self, browser, auth_user):
        
        with allure.step("Перейти на страницу конструктора"):
            main_page = MainPage(browser)
            main_page.open()
        
        with allure.step("Создать заказ: перетащить булку, соус, начинку"):
            main_page.drag_first_bun()
            main_page.drag_first_sauce()
            main_page.drag_first_filling()
        
        with allure.step("Нажать кнопку 'Оформить заказ'"):
            main_page.click_order_button()
        
        with allure.step("Получить номер созданного заказа из модального окна"):
            order_number = main_page.get_order_number()
        
        with allure.step("Закрыть модальное окно заказа"):
            main_page.close_modal()
            main_page.wait_for_modal_invisible()
        
        with allure.step("Перейти на страницу 'Лента заказов'"):
            feed_page = FeedPage(browser, FEED_URL)
            feed_page.open()
        
        with allure.step("Найти номер заказа в разделе «В работе»"):
            feed_page.wait_for_in_progress_section()
            orders_in_progress = feed_page.get_orders_in_progress()
        
        with allure.step(f"Проверить, что номер заказа '{order_number}' присутствует в списке «В работе»"):
            order_found = any(order_number in found_number for found_number in orders_in_progress)
            
            assert order_found, (
                f"Номер заказа '{order_number}' не найден ни в одном из номеров в разделе 'В работе'. "
                f"Найдены: {orders_in_progress}"
            )
            
            