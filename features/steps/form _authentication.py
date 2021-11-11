import time

from behave import *
from selenium.webdriver.common.by import By


@when(u'I access Login  page')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.maximize_window()
    context.driver.find_element(By.CSS_SELECTOR, "#content > ul > li:nth-child(21) > a").click()


@when(u'I can login with valid username and pwd')
def step_impl(context):
    text1 = context.driver.find_element(By.CSS_SELECTOR,"#username")
    text1.send_keys("tomsmith")
    time.sleep(2)
    text2 = context.driver.find_element(By.CSS_SELECTOR,"#password")
    text2.send_keys("SuperSecretPassword!")
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "#login > button > i").click()
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "#content > div > a > i").click()
    context.driver.back()


