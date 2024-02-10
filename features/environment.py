# from features.browser import Browser
from selenium import webdriver

def before_all(context):
    try:
        context.browser = webdriver.Chrome()
    except Exception as e:
        print("Error initializing WebDriver:", e)

def after_all(context):
    if hasattr(context, 'browser') and context.browser:
        context.browser.quit()

