from behave import *
from selenium.webdriver.common.by import By


@when('I select Add/Remove')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(2) > a").click()


@when('I select add element')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#content > div > button").click()


@when('I select delete')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#elements > button").click()


@then(u'i close window')
def step_impl(context):
    context.driver.quit()
