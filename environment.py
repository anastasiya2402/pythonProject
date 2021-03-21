from selenium import webdriver
import re
from time import sleep


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    sleep(2)


def before_all(context):
    context.url='https://www.ebay.com/'


def after_step(context,step):
    if step.status=='failed':
        step_name =re.sub('[^a-zA-Z \n\.]', '', step.name)
        context.browser.save_screenshot(step_name)