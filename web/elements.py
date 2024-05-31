import abc
from dataclasses import dataclass
from typing import Union

from web.browsers import Browsers
from settings import settings


@dataclass
class BaseElement(abc.ABC):
    xpath: Union[None, str] = None


class WebElement(BaseElement):
    def __post_init__(self):
        self.xpath = self.xpath

    def _init(self):
        self.timeout = settings.timeout * 1000
        self.page = Browsers.page
        self.page.wait_for_load_state(timeout=self.timeout)

    @property
    def __web_element(self):
        self._init()
        element = self.page.locator(self.xpath)
        element.wait_for(timeout=self.timeout, state="visible")
        return element

    def wait_visible(self):
        self._init()
        self.__web_element.wait_for(timeout=self.timeout, state="visible")
        return self

    def click(self):
        self._init()
        self.__web_element.click()

    def fill(self, text):
        self._init()
        self.__web_element.fill(value=text)

    def check_text(self, text):
        self._init()
        check_txt = self.__web_element.text_content().strip()
        assert check_txt == text, f"Текст не совпадает"

    def get_value(self) -> str:
        self._init()
        return self.__web_element.input_value()

    def clear(self):
        self._init()
        self.__web_element.clear()

    def get_attribute(self, attribute) -> str:
        self._init()
        return self.__web_element.get_attribute(attribute).strip()

    # ===
    def is_visible(self) -> bool:
        self._init()
        return self.__web_element.is_visible()

    def is_hidden(self) -> bool:
        self._init()
        return self.__web_element.is_hidden()

    def is_checked(self) -> bool:
        self._init()
        return self.__web_element.is_checked()

    def is_enabled(self) -> bool:
        self._init()
        return self.__web_element.is_enabled()

    def is_disabled(self) -> bool:
        self._init()
        return self.__web_element.is_disabled()


@dataclass
class Element(WebElement):
    def __init__(self, xpath):
        super(Element, self).__init__(xpath)

    def __post_init__(self):
        self.xpath = self.xpath


