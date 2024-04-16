import abc
import time
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

    def check_page_contains_text(self, *texts):
        self.page.wait_for_load_state()
        for text in texts:
            if len(self.page.get_by_text(text).all_text_contents()) == 0:
                assert False, f"Текст '{text}' не найден"
