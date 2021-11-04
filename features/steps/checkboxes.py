from behave import *
from selenium.webdriver.common.by import By


@when('i access Checkboxes')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(6) > a").click()


@when('i click on checkboxes')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)").click()
    context.driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)").click()


@when('I go back on main page')
def step_impl(context):
    context.driver.back()


@then(u'I close browser')
def step_impl(context):
    context.driver.quit()
