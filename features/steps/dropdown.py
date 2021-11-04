from behave import *
from selenium.webdriver.common.by import By
import time



@when('I select Dropdown')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.maximize_window()
    context.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(11) > a").click()


@when('I can access all the options on dropdown')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#dropdown").click()
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "#dropdown > option:nth-child(2)").click()
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "#dropdown").click()
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "#dropdown").click()
    context.driver.find_element(By.CSS_SELECTOR, "#dropdown > option:nth-child(3)").click()
    time.sleep(2)
    context.driver.back()
