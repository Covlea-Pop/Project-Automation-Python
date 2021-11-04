from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('open HA main page')
def open_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://the-internet.herokuapp.com/")


@when('The logo is on the right')
def logo(context):
    context.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > a > img").is_displayed()


@then('close browser')
def quit(context):
    context.driver.close()
