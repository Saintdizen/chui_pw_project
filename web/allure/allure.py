import allure
from allure_commons.types import AttachmentType
from contextlib import contextmanager

from web.browsers import Browsers


def make_screen(name):
    allure.attach(
        Browsers.page.screenshot(),
        name=name,
        attachment_type=AttachmentType.PNG,
    )


@contextmanager
def allure_step(name):
    with allure.step(name):
        try:
            yield
            make_screen("screen")
        except Exception:
            make_screen("error")
            raise
