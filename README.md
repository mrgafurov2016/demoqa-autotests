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