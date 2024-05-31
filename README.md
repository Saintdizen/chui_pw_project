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
## Пример
* [tests/example_page.py](https://github.com/Saintdizen/chui_pw_project/blob/main/tests/example_page.py)
* [tests/example_test_desktop.py](https://github.com/Saintdizen/chui_pw_project/blob/main/tests/example_test_desktop.py)
* [tests/example_test_mobile.py](https://github.com/Saintdizen/chui_pw_project/blob/main/tests/example_test_mobile.py)
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