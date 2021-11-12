import time

from behave import *
from selenium.webdriver.common.by import By



@when('I access Dynamic Loading page')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.maximize_window()
    context.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(14) > a").click()
    time.sleep(2)


@when('I can use all features from Dynamic Loading')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#content > div > a:nth-child(5)").click()
    context.driver.find_element(By.CSS_SELECTOR, "#start > button").click()
    time.sleep(5)

    status = context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/h4").is_displayed()
    assert status is True

    time.sleep(2)

    context.driver.back()
    context.driver.find_element(By.CSS_SELECTOR, "#content > div > a:nth-child(8)").click()
    context.driver.find_element(By.CSS_SELECTOR, "#start > button").click()
    time.sleep(5)
    status2 = context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/h4").is_displayed()
    assert status2 is True

    context.driver.back()
    context.driver.back()
