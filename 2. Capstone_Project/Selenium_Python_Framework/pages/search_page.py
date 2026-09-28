from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    GLOBAL_SEARCH = (By.CSS_SELECTOR, "#search input[name='search']")
    GLOBAL_BUTTON = (By.CSS_SELECTOR, "#search button")
    PRODUCT_TITLES = (By.CSS_SELECTOR, "#content .product-thumb h4 a")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content p")
    HEADING = (By.CSS_SELECTOR, "#content h1")

    def open(self):
        self.driver.get(self.settings.base_url)
        self.visible(self.GLOBAL_SEARCH)
        return self

    def search(self, query: str):
        field = self.visible(self.GLOBAL_SEARCH)
        field.clear()
        field.send_keys(query)
        self.clickable(self.GLOBAL_BUTTON).click()
        self.wait.until(lambda driver: "route=product/search" in driver.current_url)
        self.visible(self.HEADING)
        return self

    def product_names(self):
        return [element.text.strip() for element in self.driver.find_elements(*self.PRODUCT_TITLES)]

    def has_no_results(self):
        return any("no product that matches the search criteria" in element.text.lower()
                   for element in self.driver.find_elements(*self.EMPTY_MESSAGE))
