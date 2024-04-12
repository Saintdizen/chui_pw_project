import allure

from tests.example_page import ExamplePage
from web.allure.allure import allure_step


@allure.feature('Какая-то фича')
@allure.story('Какое-то стори')
def test_title(chrome):
    """
    Описание
    """

    page = ExamplePage(chrome.page)

    with allure_step("Открыть страницу"):
        page.open()

    with allure_step("Заполнить поля"):
        page.input_search.fill("Вот так вот")
        page.btn_search.click()

    with allure_step("Проверить текст"):
        page.text_h1.check_text("Невский: Вот так вот")
