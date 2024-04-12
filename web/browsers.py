from dotenv import load_dotenv
from playwright.sync_api import Page, Browser, Playwright, BrowserContext
from pydantic import BaseSettings

from settings import settings

load_dotenv()


class Browsers(BaseSettings):
    browser: Browser = None
    page: Page = None
    __context: BrowserContext = None
    __timeout: int = settings.timeout
    __width: int = settings.browser_width
    __height: int = settings.browser_height

    @staticmethod
    def set_timeout(sec):
        return sec*1000

    def __new__(cls, playwright: Playwright):
        print(cls.set_timeout(cls.__timeout))
        cls.browser = playwright.chromium.launch(headless=False)
        # context
        cls.__context = cls.browser.new_context(
            viewport={"width": cls.__width, "height": cls.__height}
        )
        cls.__context.set_default_timeout(cls.set_timeout(cls.__timeout))
        cls.__context.set_default_navigation_timeout(cls.set_timeout(cls.__timeout))
        # page
        cls.page = cls.__context.new_page()
        # return
        return cls
