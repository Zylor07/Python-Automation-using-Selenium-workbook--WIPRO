from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, settings):
        self.driver = driver
        self.settings = settings
        self.wait = WebDriverWait(driver, settings.wait_seconds)

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def open_route(self, route):
        self.driver.get(f"{self.settings.base_url}index.php?route={route}")
