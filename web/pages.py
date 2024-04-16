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

    def check_page_contains_text(self, *texts):
        self.page.wait_for_load_state()
        errors = []
        for text in texts:
            xpath = f"//body//*[contains(normalize-space(.), '{text}')]"
            visible_list = list(filter(lambda x: x.is_visible() is True, self.page.locator(xpath).all()))
            if len(visible_list) == 0:
                errors.append(text)
        assert errors == 0, f"Текст '{errors}' не найден на странице"
