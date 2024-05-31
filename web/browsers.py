import time
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
    __har_path: str = None

    @staticmethod
    def __set_timeout(sec):
        return sec*1000

    @staticmethod
    def __set_name_har_file():
        return datetime.now().strftime("%d-%m-%Y_%H:%M:%S")

    def __new__(cls, playwright: Playwright, ws=None):
        screen = {"width": cls.__width, "height": cls.__height}
        if settings.mobile_version:
            if settings.write_har:
                cls.__har_path = f'{cls.__set_name_har_file()}_log.har'
            devices = playwright.devices['Pixel 5']
            if settings.remote:
                cls.browser = playwright.chromium.connect_over_cdp(ws)
                cls.browser.new_browser_cdp_session()
            else:
                cls.browser = playwright.chromium.launch(headless=False)
            cls.context = cls.browser.new_context(**devices, record_har_path=cls.__har_path, no_viewport=False)
            cls.context.set_default_timeout(cls.__set_timeout(cls.__timeout))
            cls.context.set_default_navigation_timeout(cls.__set_timeout(cls.__timeout))
            cls.page = cls.context.new_page()
            return cls
        else:
            if settings.write_har:
                cls.__har_path = f'{cls.__set_name_har_file()}_log.har'
            if settings.remote:
                cls.browser = playwright.chromium.connect_over_cdp(ws)
                cls.browser.new_browser_cdp_session()
                cls.context = cls.browser.new_context(screen=screen, record_har_path=cls.__har_path, no_viewport=True)
            else:
                cls.browser = playwright.chromium.launch(headless=False)
                cls.context = cls.browser.new_context(viewport=screen, record_har_path=cls.__har_path)
            cls.context.set_default_timeout(cls.__set_timeout(cls.__timeout))
            cls.context.set_default_navigation_timeout(cls.__set_timeout(cls.__timeout))
            cls.page = cls.context.new_page()
            return cls
