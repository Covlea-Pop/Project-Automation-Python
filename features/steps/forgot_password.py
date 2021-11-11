from behave import *
from selenium.webdriver.common.by import By
import time


@when('I access Forgot Password page')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.maximize_window()
    context.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(20) > a").click()
    time.sleep(2)


@when('I can reset my pwd')
def step_impl(context):
    text = context.driver.find_element(By.CSS_SELECTOR, "#email")
    text.send_keys("test@test.com")
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "#form_submit").click()
    time.sleep(2)
    context.driver.back()
    time.sleep(2)
    context.driver.back()
