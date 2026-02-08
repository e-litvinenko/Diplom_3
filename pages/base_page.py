import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    
    @allure.step("Открыть страницу")
    def open(self):
        self.browser.get(self.url)
    
    def _wait(self, condition, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(condition(locator))
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=10):
        return self._wait(EC.presence_of_element_located, locator, timeout)
    
    @allure.step("Найти элементы {locator}")
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
    
    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator, timeout=10):
        element = self._wait(EC.element_to_be_clickable, locator, timeout)
        self.execute_script("arguments[0].click();", element)
    
    @allure.step("Дождаться видимости элемента {locator}")
    def wait_for_visibility(self, locator, timeout=10):
        return self._wait(EC.visibility_of_element_located, locator, timeout)
    
    @allure.step("Дождаться исчезновения элемента {locator}")
    def wait_for_invisibility(self, locator, timeout=10):
        return self._wait(EC.invisibility_of_element_located, locator, timeout)
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.browser.current_url
    
    @allure.step("Проверить, отображается ли элемент {locator}")
    def is_element_displayed(self, locator, timeout=5):
        try:
            self.wait_for_visibility(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    @allure.step("Выполнить JavaScript")
    def execute_script(self, script, *args):
        return self.browser.execute_script(script, *args)
    
    @allure.step("Перетащить элемент из {source_locator} в {target_locator}")
    def drag_and_drop_js(self, source_locator, target_locator):
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        
        self.browser.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, source_element, target_element)