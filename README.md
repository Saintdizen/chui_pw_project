# Установка
```shell
git rm -r --cached "путь до файла или папки"
```
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