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
