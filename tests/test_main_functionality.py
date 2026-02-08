import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators



@allure.feature("Основная функциональность Stellar Burgers")
class TestMainFunctionality:
    
    @allure.title("1. Переход по клику на «Конструктор»")
    def test_main_navigate_to_constructor(self, browser):
        page = MainPage(browser)
        
        with allure.step("Открыть страницу ленты заказов"):
            browser.get(MainPageLocators.FEED_URL)
        
        with allure.step("Проверить наличие кнопки 'Конструктор'"):
            assert page.is_element_displayed(MainPageLocators.CONSTRUCTOR_BUTTON)
        
        with allure.step("Кликнуть на кнопку 'Конструктор'"):
            page.click_constructor()
        
        with allure.step("Проверить переход на главную страницу"):
            assert page.is_on_main_page()
    
    @allure.title("2. Переход по клику на раздел «Лента заказов»")
    def test_main_navigate_to_order_feed(self, browser):
        page = MainPage(browser)
        
        with allure.step("Открыть главную страницу"):
            page.open()
        
        with allure.step("Проверить наличие кнопки 'Лента Заказов'"):
            assert page.is_element_displayed(MainPageLocators.FEED_BUTTON)
        
        with allure.step("Кликнуть на кнопку 'Лента Заказов'"):
            page.click_feed()
        
        with allure.step("Проверить переход на страницу ленты заказов"):
            assert page.is_on_feed_page()
    
    @allure.title("3. Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_main_ingredient_modal_opens(self, browser):
        page = MainPage(browser)
        
        with allure.step("Открыть главную страницу"):
            page.open()
        
        with allure.step("Кликнуть на ингредиент"):
            page.click_first_ingredient()
        
        with allure.step("Проверить появление модального окна"):
            assert page.is_modal_visible()
    
    @allure.title("4. Всплывающее окно закрывается кликом по крестику")
    def test_main_ingredient_modal_closes(self, browser):
        page = MainPage(browser)
        
        with allure.step("Открыть главную страницу"):
            page.open()
        
        with allure.step("1. Открыть модальное окно с деталями ингредиента"):
            page.click_first_ingredient()
            assert page.is_modal_visible()
        
        with allure.step("2. Кликнуть на кнопку закрытия (крестик)"):
            page.close_modal()
        
        with allure.step("3. Проверить, что модальное окно закрыто"):
            assert page.is_modal_closed()
    
    @allure.title("5.1 Увеличение счётчика булки при добавлении в заказ")
    def test_main_bun_counter_increases(self, browser, auth_user):
        """Проверка счетчика для булки"""
        main_page = MainPage(browser)
        
        with allure.step("1. Открыть главную страницу"):
            main_page.open()
        
        with allure.step("2. Запомнить начальное значение счетчика у булки"):
            initial_counter = main_page.get_counter_value(MainPageLocators.FIRST_BUN_COUNTER)
        
        with allure.step("3. Перетащить булку в конструктор"):
            main_page.drag_ingredient_to_constructor(MainPageLocators.FIRST_BUN)
            
            WebDriverWait(browser, 3).until(
                lambda driver: main_page.get_counter_value(MainPageLocators.FIRST_BUN_COUNTER) != initial_counter
            )
        
        with allure.step("4. Проверить, что счётчик увеличился в 2 раза"):
            final_counter = main_page.get_counter_value(MainPageLocators.FIRST_BUN_COUNTER)
            
            assert final_counter == initial_counter + 2, \
                f"Счетчик булки не увеличился в 2 раза. Было: {initial_counter}, стало: {final_counter}"
    
    @allure.title("5.2 Счетчик соусов и начинок увеличивается на 1")
    @pytest.mark.parametrize("ingredient_name, ingredient_locator, counter_locator", [
        ("соус", MainPageLocators.FIRST_SAUCE, MainPageLocators.FIRST_SAUCE_COUNTER),
        ("начинка", MainPageLocators.FIRST_FILLING, MainPageLocators.FIRST_FILLING_COUNTER),
    ])
    def test_main_sauce_and_filling_counter_increases(self, browser, auth_user, 
                                                     ingredient_name, ingredient_locator, counter_locator):
        """Проверка счетчиков для соусов и начинок"""
        main_page = MainPage(browser)
        
        with allure.step("1. Открыть главную страницу"):
            main_page.open()
        
        with allure.step(f"2. Запомнить начальное значение счетчика у {ingredient_name}"):
            initial_counter = main_page.get_counter_value(counter_locator)
        
        with allure.step(f"3. Перетащить {ingredient_name} в конструктор"):
            main_page.drag_ingredient_to_constructor(ingredient_locator)
            
            WebDriverWait(browser, 3).until(
                lambda driver: main_page.get_counter_value(counter_locator) != initial_counter
            )
        
        with allure.step(f"4. Проверить, что счётчик {ingredient_name} увеличился на 1"):
            final_counter = main_page.get_counter_value(counter_locator)
            
            assert final_counter == initial_counter + 1, \
                f"Счетчик {ingredient_name} не увеличился на 1. Было: {initial_counter}, стало: {final_counter}"