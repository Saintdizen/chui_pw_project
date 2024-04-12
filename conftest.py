from _pytest.fixtures import fixture
from playwright.sync_api import Playwright

from web.browsers import Browsers


@fixture
def chrome(playwright: Playwright):
    yield Browsers(playwright)
