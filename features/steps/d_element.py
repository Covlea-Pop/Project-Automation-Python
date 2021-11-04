from behave import *
from selenium.webdriver.common.by import By


@when('I select Disappearing Elements')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.maximize_window()
    context.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(9) > a").click()


@when('I can access all the buttons')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > a").click()
    context.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(9) > a").click()
    context.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > a").click()
    context.driver.back()
    context.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(3) > a").click()
    context.driver.back()
    context.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(4) > a").click()
    context.driver.back()
    context.driver.back()




