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
# [Пример](https://github.com/Saintdizen/chui_pw_project/tree/main/tests/0_example)
## example_page.py
```python
from web.elements import Element
from web.pages import BasePage


class ExamplePage(BasePage):
    url = 'https://www.google.com/'

    class Desktop:
        input_search = Element('//*[@title="Поиск"]')
        btn_search = Element('(//*[@value="Мне повезёт!"])[1]')

    class Mobile:
        input_search = Element('//textarea[@aria-label="Поиск в Google"]')
        btn_search = Element("(//*[text()='вот так вот'])[1]")
```
## example_test_desktop.py

```python
import allure

from tests.example.example_page import ExamplePage
from web.allure.allure import t_step


@allure.feature('Какая-то фича')
@allure.story('Какое-то стори')
def test_title(chrome):
    """ Описание """
    page = ExamplePage(chrome.page)
    # Перехват запросов \ ответов
    page.on("request", lambda request: print(request.url))
    page.on("response", lambda response: print(response.url))

    with t_step("Открыть страницу"):
        page.open()

    with t_step("Заполнить поля"):
        page.Desktop.input_search.fill("Вот так вот")
        page.Desktop.btn_search.click()

    with t_step("Проверить текст"):
        page.check_page_contains_text("Невский: Вот так вот")
```
## example_test_mobile.py

```python
import allure

from tests.example.example_page import ExamplePage
from web.allure.allure import t_step


@allure.feature('Какая-то фича')
@allure.story('Какое-то стори')
def test_title(mobile, chrome):
    """ Описание """
    page = ExamplePage(chrome.page)
    # Перехват запросов \ ответов
    page.on("request", lambda request: print(request.url))
    page.on("response", lambda response: print(response.url))

    with t_step("Открыть страницу"):
        page.open()

    with t_step("Заполнить поля"):
        page.Mobile.input_search.fill("Вот так вот")
        page.Mobile.btn_search.click()

    with t_step("Проверить текст"):
        page.check_page_contains_text("Невский: Вот так вот")
```
# Запуск
## Запуск теста
```shell
pytest -s -v tests/example/example_test_desktop.py --alluredir allure --disable-pytest-warnings --clean-alluredir --continue-on-collection-errors
```
```shell
pytest -s -v tests/example/example_test_mobile.py --alluredir allure --disable-pytest-warnings --clean-alluredir --continue-on-collection-errors
```
## Генерация отчета
### linux
```shell
web/allure/bin/allure serve allure
```
### ubuntu
```shell
sudo apt-get install default-jre
wget https://github.com/allure-framework/allure2/releases/download/2.18.1/allure_2.18.1-1_all.deb
sudo dpkg -i allure_2.18.1-1_all.deb
```
### windows
```shell
web/allure/bin/allure.bat serve allure
```