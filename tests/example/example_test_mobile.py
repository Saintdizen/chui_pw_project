import allure

from tests.example.example_page import ExamplePage
from web.allure.allure import t_step


@allure.feature('Какая-то фича')
@allure.story('Какое-то стори')
def test_title(mobile, chrome):
    """
    Описание
    """
    page = ExamplePage(chrome.page)
    # Перехват запросов \ ответов
    # page.on("request", lambda request: print(request.url))
    # page.on("response", lambda response: print(response.url))

    # Перехват сообщений консоли
    page.on("console", lambda msg: print(msg.text))
    page.on("console", lambda msg: print(f"error: {msg.text}") if msg.type == "error" else None)

    with t_step("Открыть страницу"):
        page.open()

    with t_step("Заполнить поля"):
        page.Mobile.input_search.fill("Вот так вот")
        page.Mobile.input_search.screenshot()
        page.Mobile.btn_search.click()

    with t_step("Проверить текст"):
        page.check_page_contains_text(
            "Невский: Вот так вот"
        )
