import inspect

from _pytest.fixtures import fixture
from playwright.sync_api import Playwright

from web.browsers import Browsers
from settings import settings


@fixture
def mobile():
    Browsers.mobile_mode = True


@fixture
def chrome(playwright: Playwright, request):
    browser = Browsers(playwright=playwright, request=request)
    yield browser
    browser.context.close()
    browser.page.close()
    browser.browser.close()
    if settings.remote:
        browser.driver.quit()
