import time
from datetime import datetime

from dotenv import load_dotenv
from playwright.sync_api import Page, Browser, Playwright, BrowserContext
from pydantic import BaseSettings
from selenium import webdriver
from selenium.webdriver.remote.command import Command

from settings import settings

load_dotenv()


def set_timeout():
    return settings.timeout * 1000


def set_name_har_file():
    if settings.write_har:
        return f'{datetime.now().strftime("%d-%m-%Y_%H:%M:%S")}_log.har'
    else:
        return None


def set_screen():
    return {"width": settings.browser_width, "height": settings.browser_height}


class Browsers(BaseSettings):
    mobile_mode: bool = False
    browser: Browser = None
    page: Page = None
    context: BrowserContext = None

    def __new__(cls, playwright: Playwright, ws=None):
        cls.browser = playwright.chromium.launch(headless=False)
        if hasattr(cls, 'mobile_mode'):
            cls.context = cls.browser.new_context(**playwright.devices['Pixel 5'], record_har_path=set_name_har_file(), no_viewport=False)
        else:
            cls.context = cls.browser.new_context(viewport=set_screen(), record_har_path=set_name_har_file())
        cls.context.set_default_timeout(set_timeout())
        cls.context.set_default_navigation_timeout(set_timeout())
        cls.page = cls.context.new_page()
        return cls


class RemoteBrowsers(BaseSettings):
    mobile_mode: bool = False
    driver: webdriver.Remote = None
    browser: Browser = None
    page: Page = None
    context: BrowserContext = None

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
        cls.browser = playwright.chromium.connect_over_cdp(settings.selenoid_ws(cls.driver.session_id))
        cls.browser.new_browser_cdp_session()
        if hasattr(cls, 'mobile_mode'):
            cls.context = cls.browser.new_context(**playwright.devices['Pixel 5'], record_har_path=set_name_har_file(), no_viewport=False)
        else:
            cls.context = cls.browser.new_context(screen=set_screen(), record_har_path=set_name_har_file(), no_viewport=True)
        cls.context.set_default_timeout(set_timeout())
        cls.context.set_default_navigation_timeout(set_timeout())
        cls.page = cls.context.new_page()
        cls.driver.close()
        return cls

