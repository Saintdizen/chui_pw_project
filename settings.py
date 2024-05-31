from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    # Основные настройки
    timeout: int = 20
    browser_width: int = 1600
    browser_height: int = 900
    write_har: bool = False
    mobile_version: bool = False
    # Удаленное управление
    remote: bool = False
    selenoid_protocol: str = "http://"
    selenoid_host: str = "127.0.0.1"
    selenoid_port: str = "4444"
    selenoid_enable_vnc: bool = False

    def selenoid_url(self):
        return f"{self.selenoid_protocol}{self.selenoid_host}:{self.selenoid_port}/wd/hub"

    def selenoid_ws(self, session_id):
        return f"ws://{self.selenoid_host}:{self.selenoid_port}/devtools/{session_id}"


settings = Settings()
