import json
import this

from _pytest.fixtures import fixture
from playwright.sync_api import Playwright
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from web.browsers import Browsers
from settings import settings
import inspect


@fixture
def mobile():
    Browsers.mobile_mode = True


@fixture
def chrome(playwright: Playwright, request):
    driver = None
    if settings.remote:
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
        driver = webdriver.Remote(desired_capabilities=capabilities, command_executor=settings.selenoid_url())
        driver.maximize_window()
        browser = Browsers(playwright, settings.selenoid_ws(driver.session_id))
        driver.close()
    else:
        browser = Browsers(playwright)
    yield browser
    browser.context.close()
    browser.page.close()
    browser.browser.close()
    if settings.remote:
        driver.quit()
