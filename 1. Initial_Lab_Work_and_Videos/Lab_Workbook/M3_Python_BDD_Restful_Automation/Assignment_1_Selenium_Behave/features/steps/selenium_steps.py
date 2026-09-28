from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("I open the automation practice website")
def step_open_website(context):
    context.driver.get("https://testautomationpractice.blogspot.com/")

@when("I enter my name")
def step_enter_name(context):
    name_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "name"))
    )
    name_field.send_keys("Pritam")

@when("I enter my email")
def step_enter_email(context):
    email_field = context.driver.find_element(By.ID, "email")
    email_field.send_keys("pritam@example.com")

@when("I enter my phone number")
def step_enter_phone(context):
    phone_field = context.driver.find_element(By.ID, "phone")
    phone_field.send_keys("7478396102")

@when("I select the male gender")
def step_select_gender(context):
    male_radio = context.driver.find_element(By.ID, "male")
    male_radio.click()

@then("the form data should be entered successfully")
def step_validate_form(context):
    name_value = context.driver.find_element(By.ID, "name").get_attribute("value")
    email_value = context.driver.find_element(By.ID, "email").get_attribute("value")
    phone_value = context.driver.find_element(By.ID, "phone").get_attribute("value")
    gender_selected = context.driver.find_element(By.ID, "male").is_selected()

    assert name_value == "Pritam"
    assert email_value == "pritam@example.com"
    assert phone_value == "7478396102"
    assert gender_selected