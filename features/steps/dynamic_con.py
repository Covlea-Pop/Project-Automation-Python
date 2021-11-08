import time

from behave import *
from selenium.webdriver.common.by import By



@when('I access Dynamic Controls page')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.maximize_window()
    context.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(13) > a").click()
    time.sleep(2)


@when('I can use all features from Dynamic Control')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#checkbox > input[type=checkbox]").click()
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button").click()
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button").click()
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "#checkbox").click()
    time.sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, "#input-example > button").click()
    time.sleep(3)
    textfield = context.driver.find_element(By.CSS_SELECTOR, "#input-example > input[type=text]")
    textfield.send_keys("Test")
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "#input-example > button").click()
    time.sleep(5)
    context.driver.back()
