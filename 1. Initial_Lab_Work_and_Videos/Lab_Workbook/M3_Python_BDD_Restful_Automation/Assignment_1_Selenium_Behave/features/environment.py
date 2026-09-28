from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
