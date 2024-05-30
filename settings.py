from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    timeout: int = 20
    browser_width: int = 1600
    browser_height: int = 900
    write_har: bool = False
    #
    remote: bool = False
    selenoid_host: str = None
    selenoid_ws: str = None


settings = Settings()
