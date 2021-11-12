from behave import *
from selenium.webdriver.common.by import By
import time


@when('I access Dynamic Content page')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.maximize_window()
    context.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(12) > a").click()
    time.sleep(2)


@when('I can use all features')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#content > div > p:nth-child(3) > a").click()
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "#content > div > p:nth-child(3) > a").click()
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "#content > div > p:nth-child(3) > a").click()
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "#content > div > p:nth-child(3) > a").click()
    time.sleep(5)
    context.driver.back()
    time.sleep(2)
    context.driver.back()
