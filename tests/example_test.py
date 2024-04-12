import allure

from tests.example_page import ExamplePage
from web.allure.allure import allure_step


@allure.feature('feature')
@allure.story('story')
def test_title(chrome):
    page = ExamplePage(chrome.page)
    with allure_step("1"):
        page.open()
    with allure_step("2"):
        page.input_search.fill("Вот так вот")
        page.btn_search.click()
    with allure_step("3"):
        print(page.get_title())


