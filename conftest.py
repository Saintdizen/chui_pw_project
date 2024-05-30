from _pytest.fixtures import fixture
from playwright.sync_api import Playwright
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from web.browsers import Browsers, MobileBrowsers


@fixture
def chrome(playwright: Playwright):
    capabilities = {
        "browserName": "chrome",
        "selenoid:options": {
            "enableVideo": False,
            "enableVNC": True,
            "name": "test",
            "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"],
            "timezone": "Europe/Moscow",
        }
    }
    driver = webdriver.Remote(desired_capabilities=capabilities, command_executor='http://127.0.0.1:4444/wd/hub')
    driver.maximize_window()
    ws = f"ws://127.0.0.1:4444/devtools/{driver.session_id}"
    browser = Browsers(playwright, ws)
    driver.close()
    yield browser
    browser.context.close()
    browser.page.close()
    browser.browser.close()
    driver.quit()


@fixture
def mobile(playwright: Playwright):
    browser = MobileBrowsers(playwright)
    yield browser
    browser.context.close()
    browser.page.close()
    browser.browser.close()
