# DemoQA UI Test Automation

Автоматизированные UI-тесты для сайта [demoqa.com](https://demoqa.com) на Python + Selenium + Pytest.

## Стек технологий
- Python 3.13
- Selenium WebDriver 4
- Pytest
- Page Object Model (POM)

## Что покрыто тестами
| Страница | Сценарий |
|---|---|
| Text Box | Заполнение формы и проверка вывода данных |
| Checkbox | Раскрытие дерева и выбор одного чекбокса |
| Radio Button | Выбор разных вариантов радиокнопок |

## Архитектура
Проект построен по паттерну **Page Object Model**:
- `pages/` — классы страниц с локаторами и методами взаимодействия
- `tests/` — тестовые сценарии с проверками (assert)
- `conftest.py` — общая фикстура браузера для всех тестов

## Как запустить

```bash
git clone https://github.com//demoqa-autotests.git
cd demoqa-autotests
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
pytest
```

## Особенности реализации
- Явные ожидания (`WebDriverWait`) вместо `time.sleep()`
- Обработка `ElementClickInterceptedException` через JS-клик как запасной вариант
- Локаторы по тексту узла для динамического дерева чекбоксов (rc-tree)

## Автор
[Руслан] — QA Automation Engineer

## Генерация Allure-отчёта

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## API-тесты (DemoQA Bookstore API)
| Сценарий | Что проверяется |
|---|---|
| Получение списка книг | Возвращается непустой список |
| Создание пользователя | Успешная регистрация (201) |
| Создание со слабым паролем | Негативный кейс — отказ (400) |
| Генерация токена | Успешная авторизация |
| Добавление книги пользователю | Книга появляется в коллекции |
| Удаление книги у пользователя | Успешное удаление (204) |

## Запуск только API-тестов
```bash
pytest tests/api -v
```