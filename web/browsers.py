from dotenv import load_dotenv
from playwright.sync_api import Page, Browser, Playwright, BrowserContext
from pydantic import BaseSettings

from settings import settings

load_dotenv()


class Browsers(BaseSettings):
    browser: Browser = None
    page: Page = None
    context: BrowserContext = None
    __timeout: int = settings.timeout
    __width: int = settings.browser_width
    __height: int = settings.browser_height

    @staticmethod
    def set_timeout(sec):
        return sec*1000

    def __new__(cls, playwright: Playwright):
        cls.browser = playwright.chromium.launch(headless=False)
        # context
        cls.context = cls.browser.new_context(
            viewport={"width": cls.__width, "height": cls.__height}, record_har_path="har.har"
        )
        cls.context.set_default_timeout(cls.set_timeout(cls.__timeout))
        cls.context.set_default_navigation_timeout(cls.set_timeout(cls.__timeout))
        # page
        cls.page = cls.context.new_page()
        # cls.page.on("request", lambda request: print(request.url))
        # cls.page.on("response", lambda response: print(response.url))
        # return
        return cls


