# Документация
* https://playwright.dev/python/docs/api/class-playwright
# Установка
## Установка зависимостей
```shell
pip install -r requirements.txt
```
## Установка браузеров
```shell
playwright install
```
## Структура
* В корне проекта создать папку **tests** **( ../tests )**
* В папке **tests** создать файл **example_page.py** **( ../tests/example_page.py )**
### example_page.py
```python
from web.elements import Element
from web.pages import BasePage


class ExamplePage(BasePage):
    url = 'https://www.google.com/'

    input_search = Element('//*[@title="Поиск"]')
    btn_search = Element('(//*[@value="Мне повезёт!"])[1]')
    text_h1 = Element("(//h1)[2]")

```
* В папке **tests** создать файл **example_test.py** **( ../tests/example_test.py )**
### example_test.py
```python
import allure

from tests.example_page import ExamplePage
from web.allure.allure import t_step


@allure.feature('Какая-то фича')
@allure.story('Какое-то стори')
def test_title(chrome):
    """
    Описание
    """

    page = ExamplePage(chrome.page)
    # Перехват запросов \ ответов
    page.on("request", lambda request: print(request.url))
    page.on("response", lambda response: print(response.url))

    with t_step("Открыть страницу"):
        page.open()

    with t_step("Заполнить поля"):
        page.input_search.fill("Вот так вот")
        page.btn_search.click()

    with t_step("Проверить текст"):
        page.check_page_contains_text(
            "Невский: Вот так вот"
        )

```
# Запуск
## Запуск теста
```shell
pytest -s -v tests/example_test_desktop.py --alluredir allure
```
## Генерация отчета
### linux
```shell
web/allure/bin/allure serve allure
```
### windows
```shell
web/allure/bin/allure.bat serve allure
```