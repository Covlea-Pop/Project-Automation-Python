from selenium import webdriver
from selenium.webdriver.common import by
from behave import *
from selenium.webdriver.common.by import By
import time


@when('when i click on DOM')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/")
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[5]/a").click()


@when('i click on blue')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/a[1]").click()


@when('i click on red')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/a[2]").click()


@when('i click on green')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/a[3]").click()
