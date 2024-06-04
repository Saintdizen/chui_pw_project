import json
import this

from _pytest.fixtures import fixture
from playwright.sync_api import Playwright

from web.browsers import Browsers, RemoteBrowsers
from settings import settings
import inspect


@fixture
def mobile():
    Browsers.mobile_mode = True
    RemoteBrowsers.mobile_mode = True


@fixture
def chrome(playwright: Playwright, request):
    if settings.remote:
        browser = RemoteBrowsers(playwright, request)
    else:
        browser = Browsers(playwright)
    yield browser
    browser.context.close()
    browser.page.close()
    browser.browser.close()
    if settings.remote:
        browser.driver.quit()
