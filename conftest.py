from _pytest.fixtures import fixture
from playwright.sync_api import Playwright
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from web.browsers import Browsers, MobileBrowsers
from settings import settings


@fixture
def chrome(playwright: Playwright):
    driver = None
    if settings.remote:
        capabilities = {
            "browserName": "chrome",
            "selenoid:options": {
                "enableVideo": False,
                "enableVNC": settings.selenoid_enable_vnc,
                "name": "test",
                "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"],
                "timezone": "Europe/Moscow",
            }
        }
        driver = webdriver.Remote(desired_capabilities=capabilities, command_executor=f'{settings.selenoid_host}/wd/hub')
        driver.maximize_window()
        browser = Browsers(playwright, f"{settings.selenoid_ws}/devtools/{driver.session_id}")
        driver.close()
    else:
        browser = Browsers(playwright)
    yield browser
    browser.context.close()
    browser.page.close()
    browser.browser.close()
    if settings.remote:
        driver.quit()


@fixture
def mobile(playwright: Playwright):
    browser = MobileBrowsers(playwright)
    yield browser
    browser.context.close()
    browser.page.close()
    browser.browser.close()
