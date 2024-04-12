import abc
from dataclasses import dataclass
from typing import Union

from web.browsers import Browsers


@dataclass
class BaseElement(abc.ABC):
    xpath: Union[None, str] = None


class WebElement(BaseElement):
    def __post_init__(self):
        self.xpath = self.xpath

    def _init(self):
        self.page = Browsers.page

    @property
    def web_element(self):
        self._init()
        return self.page.locator(self.xpath)

    def click(self):
        self._init()
        self.page.wait_for_load_state()
        self.web_element.click()

    def check_text(self, text):
        self._init()
        self.page.wait_for_load_state()
        assert self.web_element.text_content().strip() == text, "Текст не совпадает"

    def fill(self, text):
        self._init()
        self.page.wait_for_load_state()
        return self.web_element.fill(text)


@dataclass
class Element(WebElement):
    def __init__(self, xpath):
        super(Element, self).__init__(xpath)

    def __post_init__(self):
        self.xpath = self.xpath


