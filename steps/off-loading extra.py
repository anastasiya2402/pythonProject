from behave import step
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import warnings

@step('Category Dresses displayed')
def category_displayed(context):
    category=context.browser.find_element_by_xpath("//span[text()='Dresses']/span[@class='clipped' and text()='Selected category']")


@step('Stats show large number dresses')
def search_ver_dresses(context):
    text_dresses=context.browser.find_element_by_xpath("//h1[text()=' results for ']//span[@class='BOLD' and text()='dress']")

@step('All categories are displayed')
def verify_all_categories(context):
    image=context.browser.find_element_by_xpath("//h1[text()='All Categories']")


@step('There is also a suggestion to search for "dres" instead')
def verifying_content_dres(context):
    pseudolink=context.browser.find_element_by_xpath("//span[@class='PSEUDOLINK' and text()='dres']")

@step('Press Enter/Return in Search combobox field')
def submit_search(context):
    srch_combo_box = context.browser.find_element_by_xpath("//div[@id='gh-ac-box']")
    sleep(4)
    srch_combo_box.send_keys(Keys.RETURN)
    sleep(5)


@step('Enter every special character (no whitespace) in Search combo box, push Search')
def press_sp_char(context):
     sp_char = ["`"," ", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "[", "}", "]", "\\","|", ":", ";", "'", "\"", "/", "?", ",", "<", ".", ">"]
     for i in range(0, 33):
      space_key_btn = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
      space_key_btn.send_keys(sp_char[i] + Keys.RETURN)
      # sleep(3)
     #image = context.browser.find_element_by_xpath("//h1[text()='Dress']")



