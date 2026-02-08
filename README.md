# QA Python Project: UI-тестирование бургерной Stellar Burgers

## Задание 3: Автотесты для UI

### Описание
Автотесты для UI-тестирования веб-приложения Stellar Burgers. Проект реализует комплексное тестирование пользовательского интерфейса с использованием паттерна Page Object, selenium, pytest и allure-pytest. Тестирование проводится в двух браузерах: Google Chrome и Mozilla Firefox.

### Тестируемая функциональность

#### Проверка основной функциональности `test_main_functionality.py`:
1. **Переход по клику на «Конструктор»** - `test_main_navigate_to_constructor`
2. **Переход по клику на раздел «Лента заказов»** - `test_main_navigate_to_order_feed`
3. **Если кликнуть на ингредиент, появится всплывающее окно с деталями** - `test_main_ingredient_modal_opens`
4. **Всплывающее окно закрывается кликом по крестику** - `test_main_ingredient_modal_closes`
5. **При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается**:
   - Для булок - `test_main_bun_counter_increases`
   - Для соусов и начинок - `test_main_sauce_and_filling_counter_increases`

#### Раздел «Лента заказов» `test_feed_functionality.py`:
1. **При создании нового заказа счётчик «Выполнено за всё время» увеличивается** - `test_feed_all_time_counter_increases`
2. **При создании нового заказа счётчик «Выполнено за сегодня» увеличивается** - `test_feed_today_counter_increases`
3. **После оформления заказа его номер появляется в разделе «В работе»** - `test_feed_order_appears_in_progress_section`

### Особенности реализации

#### Page Object Pattern
Проект организован с использованием паттерна Page Object:
locators/ # Локаторы элементов страниц
├── auth_locators.py # Локаторы для страниц авторизации
├── feed_page_locators.py # Локаторы для ленты заказов
└── main_page_locators.py # Локаторы для главной страницы

pages/ # Классы страниц
├── base_page.py # Базовый класс с общими методами
├── feed_page.py # Работа с лентой заказов
└── main_page.py # Работа с конструктором бургеров

tests/ # Тестовые сценарии
├── test_feed_functionality.py # Тесты ленты заказов
└── test_main_functionality.py # Тесты основной функциональности

#### Фикстуры для тестовых данных:
- `generate_test_user` - генерация уникальных тестовых данных пользователя
- `registered_user` - регистрация пользователя в системе
- `auth_user` - авторизация пользователя для тестов, требующих входа в систему
- `browser` - параметризованная фикстура для запуска тестов в Chrome и Firefox

### Запуск автотестов

#### 1. Установка зависимостей
```pip install -r requirements.txt```

#### 2. Запуск всех тестов
```pytest -v```

#### 3. Запуск с Allure-отчетом
```pytest --alluredir=./allure-results```

#### 4. Генерация и просмотр Allure-отчета
```allure serve allure-results```