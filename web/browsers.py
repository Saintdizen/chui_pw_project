import time
from datetime import datetime

from dotenv import load_dotenv
from playwright.sync_api import Page, Browser, Playwright, BrowserContext
from pydantic import BaseSettings
from selenium import webdriver

from settings import settings

load_dotenv()


class Browsers(BaseSettings):
    mobile_mode: bool = False
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
        if settings.write_har:
            cls.__har_path = f'{cls.__set_name_har_file()}_log.har'
        cls.browser = playwright.chromium.launch(headless=False)
        if hasattr(cls, 'mobile_mode'):
            devices = playwright.devices['Pixel 5']
            cls.context = cls.browser.new_context(**devices, record_har_path=cls.__har_path, no_viewport=False)
        else:
            cls.context = cls.browser.new_context(viewport=screen, record_har_path=cls.__har_path)
        cls.context.set_default_timeout(cls.__set_timeout(cls.__timeout))
        cls.context.set_default_navigation_timeout(cls.__set_timeout(cls.__timeout))
        cls.page = cls.context.new_page()
        return cls


class RemoteBrowsers(BaseSettings):
    mobile_mode: bool = False
    driver: webdriver.Remote = None
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

    def __new__(cls, playwright: Playwright, request=None):
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
        cls.driver = webdriver.Remote(desired_capabilities=capabilities, command_executor=settings.selenoid_url())
        cls.driver.maximize_window()
        screen = {"width": cls.__width, "height": cls.__height}
        if settings.write_har:
            cls.__har_path = f'{cls.__set_name_har_file()}_log.har'
        cls.browser = playwright.chromium.connect_over_cdp(settings.selenoid_ws(cls.driver.session_id))
        cls.browser.new_browser_cdp_session()
        print(cls.mobile_mode)
        if hasattr(cls, 'mobile_mode'):
            devices = playwright.devices['Pixel 5']
            cls.context = cls.browser.new_context(**devices, record_har_path=cls.__har_path, no_viewport=False)
        else:
            cls.context = cls.browser.new_context(screen=screen, record_har_path=cls.__har_path, no_viewport=True)
        cls.context.set_default_timeout(cls.__set_timeout(cls.__timeout))
        cls.context.set_default_navigation_timeout(cls.__set_timeout(cls.__timeout))
        cls.page = cls.context.new_page()
        cls.driver.close()
        return cls

