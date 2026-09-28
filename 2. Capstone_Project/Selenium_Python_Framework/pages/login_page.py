from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Login']")
    ALERT = (By.CSS_SELECTOR, ".alert-danger")
    ACCOUNT_HEADING = (By.CSS_SELECTOR, "#content h2")

    def open(self):
        self.open_route("account/login")
        self.visible(self.EMAIL)
        return self

    def login(self, email: str, password: str):
        self.visible(self.EMAIL).send_keys(email)
        self.visible(self.PASSWORD).send_keys(password)
        self.clickable(self.LOGIN_BUTTON).click()
        return self

    def error_message(self):
        return self.visible(self.ALERT).text.strip()

    def is_account_open(self):
        self.wait.until(lambda driver: "route=account/account" in driver.current_url)
        return "My Account" in [h.text for h in self.driver.find_elements(*self.ACCOUNT_HEADING)]
