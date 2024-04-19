from _pytest.fixtures import fixture
from playwright.sync_api import Playwright

from web.browsers import Browsers


@fixture
def chrome(playwright: Playwright):
    test = Browsers(playwright)
    yield test
    test.context.close()
    test.page.close()
    test.browser.close()
