import allure
from allure_commons.types import AttachmentType
from contextlib import contextmanager

from web.browsers import Browsers, RemoteBrowsers


def make_screen(name):
    try:
        browser = Browsers.page
    except:
        browser = RemoteBrowsers.page
    allure.attach(
        browser.screenshot(),
        name=name,
        attachment_type=AttachmentType.PNG,
    )


@contextmanager
def t_step(name):
    with allure.step(name):
        try:
            yield
            make_screen("screen")
        except Exception:
            make_screen("error")
            raise
