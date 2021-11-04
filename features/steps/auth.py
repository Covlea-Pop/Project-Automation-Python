from selenium.webdriver.common.by import By
from behave import *


@when('I click on Basic Auth')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.find_element(By.CSS_SELECTOR, '#content > ul > li:nth-child(3) > a').click()


@when('I input username and password i can login')
def step_impl(context, username="admin", password="admin"):
    context.driver.get('https://' + username + ':' + password + '@' + 'the-internet.herokuapp.com/basic_auth')


@then('I go back on main page')
def step_impl(context):
    context.driver.back()
    context.driver.back()
