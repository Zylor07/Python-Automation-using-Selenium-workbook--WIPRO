"""INI settings with opt-in environment overrides."""
import configparser
import os
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Settings:
    base_url: str
    browser: str
    headless: bool
    wait_seconds: int
    page_load_seconds: int


def load_settings() -> Settings:
    config = configparser.ConfigParser()
    if not config.read(ROOT / "config" / "settings.ini"):
        raise FileNotFoundError("Missing config/settings.ini")
    headless = os.getenv("HEADLESS", config["browser"]["headless"]).lower()
    if headless not in {"true", "false", "1", "0"}:
        raise ValueError("HEADLESS must be true/false or 1/0")
    return Settings(
        base_url=os.getenv("BASE_URL", config["application"]["base_url"]).rstrip("/") + "/",
        browser=os.getenv("BROWSER", config["browser"]["name"]).lower(),
        headless=headless in {"true", "1"},
        wait_seconds=config.getint("browser", "wait_seconds"),
        page_load_seconds=config.getint("browser", "page_load_seconds"),
    )
