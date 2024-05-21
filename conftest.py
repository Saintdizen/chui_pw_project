from _pytest.fixtures import fixture
from playwright.sync_api import Playwright

from web.browsers import Browsers


@fixture
def chrome(playwright: Playwright):
    browser = Browsers(playwright)
    yield browser
    browser.context.close()
    browser.page.close()
    browser.browser.close()
