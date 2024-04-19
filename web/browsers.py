from datetime import datetime

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
    # har
    __har_path: str = None

    @staticmethod
    def __set_timeout(sec):
        return sec*1000

    @staticmethod
    def __set_name_har_file():
        return datetime.now().strftime("%d-%m-%Y_%H:%M:%S")

    def __new__(cls, playwright: Playwright):
        if settings.write_har:
            cls.__har_path = f'{cls.__set_name_har_file()}_log.har'
        # launch
        cls.browser = playwright.chromium.launch(headless=False)
        # context
        cls.context = cls.browser.new_context(
            viewport={"width": cls.__width, "height": cls.__height},
            record_har_path=cls.__har_path
        )
        cls.context.set_default_timeout(cls.__set_timeout(cls.__timeout))
        cls.context.set_default_navigation_timeout(cls.__set_timeout(cls.__timeout))
        # page
        cls.page = cls.context.new_page()
        # cls.page.on("request", lambda request: print(request.url))
        # cls.page.on("response", lambda response: print(response.url))
        # return
        return cls


