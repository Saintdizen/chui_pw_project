import time
from datetime import datetime

from dotenv import load_dotenv
from playwright.sync_api import Page, Browser, Playwright, BrowserContext
from pydantic import BaseSettings
from selenium import webdriver
from selenium.webdriver.remote.command import Command

from settings import settings

load_dotenv()


class Browsers(BaseSettings):
    mobile_mode: bool = False
    driver: webdriver.Remote = None
    browser: Browser = None
    page: Page = None
    context: BrowserContext = None

    @staticmethod
    def __set_timeout():
        return settings.timeout * 1000

    @staticmethod
    def __set_name_har_file():
        if settings.write_har:
            return f'{datetime.now().strftime("%d-%m-%Y_%H:%M:%S")}_log.har'
        else:
            return None

    @staticmethod
    def __set_screen():
        return {"width": settings.browser_width, "height": settings.browser_height}

    def _setup_locale_browser(self, playwright):
        self.browser = playwright.chromium.launch(headless=False)
        if hasattr(self, 'mobile_mode'):
            self.context = self.browser.new_context(**playwright.devices['Pixel 5'], record_har_path=self.__set_name_har_file(), no_viewport=False)
        else:
            self.context = self.browser.new_context(viewport=self.__set_screen(), record_har_path=self.__set_name_har_file())
        self.context.set_default_timeout(self.__set_timeout())
        self.context.set_default_navigation_timeout(self.__set_timeout())
        self.page = self.context.new_page()

    def _setup_remote_browser(self, playwright, request):
        capabilities = {
            "browserName": "chrome",
            "selenoid:options": {
                "enableVideo": False,
                "enableVNC": settings.selenoid_enable_vnc,
                "name": request.node.nodeid,
                "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"],
                "timezone": "Europe/Moscow",
            }
        }
        self.driver = webdriver.Remote(desired_capabilities=capabilities, command_executor=settings.selenoid_url())
        self.driver.maximize_window()
        self.browser = playwright.chromium.connect_over_cdp(settings.selenoid_ws(self.driver.session_id))
        self.browser.new_browser_cdp_session()
        if hasattr(self, 'mobile_mode'):
            self.context = self.browser.new_context(**playwright.devices['Pixel 5'], record_har_path=self.__set_name_har_file(), no_viewport=False)
        else:
            self.context = self.browser.new_context(screen=self.__set_screen(), record_har_path=self.__set_name_har_file(), no_viewport=True)
        self.context.set_default_timeout(self.__set_timeout())
        self.context.set_default_navigation_timeout(self.__set_timeout())
        self.page = self.context.new_page()
        self.driver.close()

    def __new__(cls, playwright: Playwright, ws=None, request=None):
        if settings.remote:
            cls._setup_remote_browser(cls, playwright, request)
        else:
            cls._setup_locale_browser(cls, playwright)
        return cls
