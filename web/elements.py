import abc
from dataclasses import dataclass
from typing import Union

from settings import settings
from web.browsers import Browsers


@dataclass
class BaseElement(abc.ABC):
    xpath: Union[None, str] = None


class WebElement(BaseElement):
    def __post_init__(self):
        self.xpath = self.xpath

    def _init(self):
        self.page = Browsers.page

    def __wait(self):
        self.page.wait_for_load_state()

    @property
    def web_element(self):
        self._init()
        return self.page.locator(self.xpath)

    def click(self):
        self._init()
        self.__wait()
        self.web_element.click()

    def fill(self, text):
        self._init()
        self.__wait()
        return self.web_element.fill(text)

    def check_text(self, text):
        self._init()
        self.__wait()
        assert self.web_element.text_content().strip() == text, "Текст не совпадает"

    def get_value(self) -> str:
        self._init()
        self.__wait()
        return self.web_element.input_value()

    def clear(self):
        self._init()
        self.__wait()
        return self.web_element.clear()

    def get_attribute(self, attribute) -> str:
        self._init()
        self.__wait()
        return self.web_element.get_attribute(attribute).strip()

    # ===
    def is_visible(self) -> bool:
        self._init()
        self.__wait()
        return self.web_element.is_visible()

    def is_hidden(self) -> bool:
        self._init()
        self.__wait()
        return self.web_element.is_hidden()

    def is_checked(self) -> bool:
        self._init()
        self.__wait()
        return self.web_element.is_checked()

    def is_enabled(self) -> bool:
        self._init()
        self.__wait()
        return self.web_element.is_enabled()

    def is_disabled(self) -> bool:
        self._init()
        self.__wait()
        return self.web_element.is_disabled()


@dataclass
class Element(WebElement):
    def __init__(self, xpath):
        super(Element, self).__init__(xpath)

    def __post_init__(self):
        self.xpath = self.xpath


