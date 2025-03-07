from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I open browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('i click on the AB Testing link')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(1) > a").click()


@when('a new page is opened')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#content > div > h3").is_displayed()


@then('i quit the page')
def step_impl(context):
    context.driver.quit()