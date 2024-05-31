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
## [Пример](https://github.com/Saintdizen/chui_pw_project/tree/main/tests/0_example)
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