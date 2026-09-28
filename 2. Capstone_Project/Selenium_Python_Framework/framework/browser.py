"""Fresh browser for each test; Selenium Manager resolves the driver."""
from selenium import webdriver
from framework.config import Settings


def create_driver(settings: Settings):
    browser = settings.browser
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if settings.headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,900")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if settings.headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        if settings.headless:
            options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported BROWSER={browser!r}; use chrome, firefox or edge")
    driver.set_page_load_timeout(settings.page_load_seconds)
    return driver
