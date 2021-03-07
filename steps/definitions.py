from behave import step
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


@step('Navigate to Google')
def test(context):
  driver=webdriver.Chrome()
  driver.get("https://www.google.com/")
  driver.quit()


@step('Open eBay.com')
def some_test_impl(context):
    context.browser=webdriver.Chrome()
    context.browser.get("https://www.ebay.com/")

@step('Search for "dress"')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("dress")

@step('Search for "dress1"')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("dress1")

@step('Search for "dress#"')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("dress#")

@step('Search for "dres"')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("dres")

@step('Click the Search button')
def click_the_search_btn(context):
    srch_btn = context.browser.find_element_by_xpath("//input[@id='gh-btn']")
    srch_btn.click()
    sleep(5) #5 seconds

@step('All items are dresses')
def verify_search_result(context):
    item=context.browser.find_element_by_xpath("//h3[text()='Women Ladies Long Maxi Dress Boho Holiday Beach Party Cocktail Summer Sundress']")

@step('Close the Chrome browser')
def close_the_browser(context):
    context.browser.close()


@step('Push button "Search"')
def click_the_search_btn(context):
    srch_btn = context.browser.find_element_by_xpath("//input[@type='submit']")
    srch_btn.click()
    sleep(5)

@step('All categories are displayed')
def verify_all_categories(context):
    image=context.browser.find_element_by_xpath("//h1[text()='All Categories']")

@step('Press Enter/Return')
def submit_search(context):
    srch_combo_box = context.browser.find_element_by_xpath("//input[@type='submit']")
    srch_combo_box.send_keys(Keys.RETURN)
    sleep(5)

@step('Category Dresses displayed')
def category_displayed(context):
    category=context.browser.find_element_by_xpath("//span[text()='Dresses']/span[@class='clipped' and text()='Selected category']")

@step('There is also a suggestion to search for "dres" instead')
def verifying_content_dres(context):
    pseudolink=context.browser.find_element_by_xpath("//span[@class='PSEUDOLINK' and text()='dres']")

@step('Stats show large number dresses')
def search_ver_dresses(context):
    text_dresses=context.browser.find_element_by_xpath("//h1[text()=' results for ']//span[@class='BOLD' and text()='dress']")

@step('Press space key in Search combo box')
def press_space_key(context):
    space_key_btn=context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    space_key_btn.send_keys(Keys.SPACE)

@step('Enter some special characters')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("@!#$%^&*()-_=+`~|]}[{'/.>,<?")
