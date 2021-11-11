from behave import *
from selenium.webdriver.common.by import By
import time


@when('I access Floating Menu page')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.maximize_window()
    context.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(19) > a").click()


@when('I can see Floating Menus when i scroll down')
def step_impl(context):
    status1 = context.driver.find_element(By.CSS_SELECTOR, "#menu > ul > li:nth-child(1) > a").is_displayed()
    assert status1 is True
    status2 = context.driver.find_element(By.CSS_SELECTOR, "#menu > ul > li:nth-child(2) > a").is_displayed()
    assert status2 is True
    status3 = context.driver.find_element(By.CSS_SELECTOR, "#menu > ul > li:nth-child(3) > a").is_displayed()
    assert status3 is True
    status4 = context.driver.find_element(By.CSS_SELECTOR, "#menu > ul > li:nth-child(4) > a").is_displayed()
    assert status4 is True
    context.driver.execute_script("window.scrollTo(0, 4509)")
    time.sleep(5)

    context.driver.back()
