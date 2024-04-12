from dotenv import load_dotenv
from playwright.sync_api import Page, Browser
from pydantic import BaseSettings

load_dotenv()


class Browsers(BaseSettings):
    browser: Browser = None
    page: Page = None

    def __new__(cls, playwright):
        cls.browser = playwright.chromium.launch(headless=False)
        cls.page = cls.browser.new_page()
        return cls
