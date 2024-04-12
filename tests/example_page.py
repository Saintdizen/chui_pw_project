from web.elements import Element
from web.pages import BasePage


class ExamplePage(BasePage):
    url = 'https://www.google.com/'

    input_search = Element('//*[@title="Поиск"]')
    btn_search = Element('(//*[@value="Мне повезёт!"])[1]')
    text_h1 = Element("(//h1)[2]")
