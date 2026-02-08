from selenium.webdriver.common.by import By

class MainPageLocators:
    
    CONSTRUCTOR_URL = "https://stellarburgers.education-services.ru/"
    FEED_URL = "https://stellarburgers.education-services.ru/feed"
    
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    FEED_BUTTON = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")
    
    FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    
    FIRST_BUN = (By.XPATH, "//h2[text()='Булки']/following::ul[1]//a[contains(@class, 'BurgerIngredient_ingredient')]")
    FIRST_SAUCE = (By.XPATH, "//h2[text()='Соусы']/following::ul[1]//a[contains(@class, 'BurgerIngredient_ingredient')]")
    FIRST_FILLING = (By.XPATH, "//h2[text()='Начинки']/following::ul[1]//a[contains(@class, 'BurgerIngredient_ingredient')]")
    
    FIRST_BUN_COUNTER = (By.XPATH, "//h2[text()='Булки']/following::ul[1]//p[contains(@class, 'counter_counter__num')]")
    FIRST_SAUCE_COUNTER = (By.XPATH, "//h2[text()='Соусы']/following::ul[1]//p[contains(@class, 'counter_counter__num')]")
    FIRST_FILLING_COUNTER = (By.XPATH, "//h2[text()='Начинки']/following::ul[1]//p[contains(@class, 'counter_counter__num')]")
    
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button') and text()='Оформить заказ']")
    
    MODAL_CONTAINER = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]//h2[contains(@class, 'Modal_modal__title')]")