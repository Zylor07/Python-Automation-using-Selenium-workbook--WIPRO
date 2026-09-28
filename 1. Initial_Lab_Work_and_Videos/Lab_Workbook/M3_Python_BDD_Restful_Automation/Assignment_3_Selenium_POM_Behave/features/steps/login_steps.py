import time
from behave import given, when, then

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


@given("I open the automation practice website")
def step_open_website(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.get("https://testautomationpractice.blogspot.com/")
    context.login_page = LoginPage(context.driver)
    print("\nAutomation Practice website opened")


@when("I enter my name through the POM")
def step_enter_name(context):
    context.login_page.enter_name("Pritam")
    print("Name entered through POM")


@when("I enter my email through the POM")
def step_enter_email(context):
    context.login_page.enter_email("pritam@example.com")
    print("Email entered through POM")


@when("I enter my phone number through the POM")
def step_enter_phone(context):
    context.login_page.enter_phone("7478396102")
    print("Phone number entered through POM")


@when("I select male gender through the POM")
def step_select_gender(context):
    context.login_page.select_male_gender()
    print("Male gender selected through POM")


@then("the form details should be displayed correctly")
def step_validate_form(context):
    # Give the browser a split-second to update the DOM values
    time.sleep(1)

    # Fetch the actual values currently sitting in the form
    actual_name = context.login_page.get_name()
    actual_email = context.login_page.get_email()
    actual_phone = context.login_page.get_phone()
    is_male_selected = context.login_page.is_male_selected()

    # Asserts with explicit error messages if they fail
    assert actual_name == "Pritam", f"Name failed: Expected 'Pritam', got '{actual_name}'"
    assert actual_email == "pritam@example.com", f"Email failed: Expected 'pritam@example.com', got '{actual_email}'"
    assert actual_phone == "7478396102", f"Phone failed: Expected '7478396102', got '{actual_phone}'"
    assert is_male_selected is True, "Gender failed: Male radio button was not selected"

    print("Form validation passed")

    # Stay on the page for 5 seconds to visually confirm
    time.sleep(5)
    context.driver.quit()
    print("Browser closed")