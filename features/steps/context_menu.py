from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


@when('I select Context Menu')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.maximize_window()
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(7) > a").click()


@when('I right click on image')
def step_impl(context):
    source = context.driver.find_element(By.CSS_SELECTOR, "#hot-spot")
    action = ActionChains(context.driver).context_click()
    action.context_click(source).perform()
    alert = context.driver.switch_to.alert
    time.sleep(2)
    alert.accept()

@when('I click on image')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#hot-spot").click()


@then('i go back')
def step_impl(context):
    context.driver.back()
