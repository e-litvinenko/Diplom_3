from selenium.webdriver.common.by import By


class FeedPageLocators:
        
    TOTAL_ORDERS_ALL_TIME = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TOTAL_ORDERS_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    IN_PROGRESS_SECTION = (By.XPATH, "//p[contains(text(), 'В работе:')]")
    IN_PROGRESS_ORDER_NUMBERS = (By.XPATH, "//p[contains(text(), 'В работе:')]/following-sibling::ul//li")
    
    