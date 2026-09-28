from selenium.webdriver.common.by import By

class HomePage:
    HEADING_LOCATOR = (By.XPATH, "//h1[contains(text(),'Automation Testing Practice')]")

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def get_page_url(self):
        return self.driver.current_url

    def get_heading(self):
        return self.driver.find_element(*self.HEADING_LOCATOR)

    def is_heading_displayed(self):
        return self.get_heading().is_displayed()