from dotenv import load_dotenv
from playwright.sync_api import Page, Browser
from pydantic import BaseSettings

load_dotenv()


class Browsers(BaseSettings):
    browser: Browser = None
    page: Page = None
    __timeout: float = 20

    def __new__(cls, playwright):
        cls.browser = playwright.chromium.launch(headless=False)
        context = cls.browser.new_context()
        context.set_default_timeout(cls.__timeout)
        context.set_default_navigation_timeout(cls.__timeout)
        cls.page = cls.browser.new_page()
        return cls
