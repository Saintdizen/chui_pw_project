import abc
from dataclasses import dataclass

from playwright.sync_api import Page


@dataclass
class BasePage(abc.ABC):
    page: Page
    url = None

    class Elements:
        pass

    def open(self, url: str = None):
        self.page.goto(url or self.url)
        self.page.wait_for_load_state()

    def get_title(self):
        self.page.wait_for_load_state()
        return self.page.title()
