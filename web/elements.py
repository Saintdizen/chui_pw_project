import abc
import allure
from allure_commons.types import AttachmentType
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

    def __init(self):
        self.timeout = settings.timeout * 1000
        self.page = Browsers.page
        self.page.wait_for_load_state(timeout=self.timeout)

    @property
    def __web_element(self):
        self.__init()
        element = self.page.locator(self.xpath)
        states = ["attached", "visible"]
        for state in states:
            element.wait_for(timeout=self.timeout, state=state)
        return element

    def screenshot(self):
        allure.attach(
            self.__web_element.screenshot(timeout=self.timeout),
            name=self.xpath,
            attachment_type=AttachmentType.PNG,
        )

    def wait_visible(self):
        states = ["attached", "visible"]
        for state in states:
            self.__web_element.wait_for(timeout=self.timeout, state=state)
        return self

    def click(self):
        self.__web_element.click(timeout=self.timeout)

    def fill(self, text):
        self.__web_element.fill(value=text, timeout=self.timeout)

    def check_text(self, text):
        check_txt = self.__web_element.text_content(timeout=self.timeout).strip()
        assert check_txt == text, f"Текст не совпадает"

    def get_value(self) -> str:
        return self.__web_element.input_value(timeout=self.timeout)

    def clear(self):
        self.__web_element.clear(timeout=self.timeout)

    def get_attribute(self, attribute) -> str:
        return self.__web_element.get_attribute(attribute, timeout=self.timeout).strip()

    # ===
    def is_visible(self) -> bool:
        return self.__web_element.is_visible(timeout=self.timeout)

    def is_hidden(self) -> bool:
        return self.__web_element.is_hidden(timeout=self.timeout)

    def is_checked(self) -> bool:
        return self.__web_element.is_checked(timeout=self.timeout)

    def is_enabled(self) -> bool:
        return self.__web_element.is_enabled(timeout=self.timeout)

    def is_disabled(self) -> bool:
        return self.__web_element.is_disabled(timeout=self.timeout)


@dataclass
class Element(WebElement):
    def __init__(self, xpath):
        super(Element, self).__init__(xpath)

    def __post_init__(self):
        self.xpath = self.xpath


