import time

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
