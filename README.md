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
# Запуск
## Запуск теста
```shell
pytest -s -v tests/example_test.py --alluredir allure
```
## Запуск генерации отчета
```shell
web/allure/bin/allure serve allure
```