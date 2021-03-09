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
    sleep(3)

@step('Search for "dress#"')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("dress#")

@step('Search for "dres"')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("dres")

@step('All items are dresses')
def verify_search_result(context):
    item=context.browser.find_element_by_xpath("//h3[text()='Women Ladies Long Maxi Dress Boho Holiday Beach Party Cocktail Summer Sundress']")

@step('Choose filter "{link_name}"')
def choose_filter(context, link_name):
    filter=context.browser.find_element_by_xpath(f"//h2[@class='srp-format-tabs-h2' and contains(text(), '{link_name}')]")
    sleep(3)
    filter.click()
    sleep(5)

@step('Verifying that the dress you want is there')
def verify_dress(context):
    needed_dress=context.browser.find_element_by_xpath("//li[@class='s-item    '][.//span[text()='Free shipping']][.//span[text()='Free returns']][.//span[text()='Buy 1, get 1 10% off']][.//span[text()='Buy It Now']]//h3")

@step('Push button "{link_of_the_element}"')
def click_the_search_btn(context, link_of_the_element):
    srch_btn = context.browser.find_element_by_xpath(f"//*[contains(@class, 'btn-') and contains(@value, '{link_of_the_element}')]")
    srch_btn.click()
    sleep(5)

@step('All categories are displayed')
def verify_all_categories(context):
    image=context.browser.find_element_by_xpath("//h1[text()='All Categories']")

@step('Press Enter/Return in "{name_of_the_link}" field')
def submit_search(context, name_of_the_link):
    srch_combo_box = context.browser.find_element_by_xpath(f"//input[contains(@aria-label, '{name_of_the_link}') and @role='combobox']")
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
    sleep(3)

@step('Enter some special characters')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("@!#$%^&*()-_=+`~|]}[{'/.>,<?")

@step('Enter iphone 11')
def enter_text(context):
    enter_element=context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    enter_element.send_keys("iphone 11")


@step('Select/Copy/Paste the result')
def copy_text(context):
    element=context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    sleep(1)
    element.send_keys(Keys.COMMAND + 'a')
    sleep(1)
    element.send_keys(Keys.COMMAND + 'c')
    sleep(1)
    element.send_keys(Keys.ARROW_RIGHT)
    element.send_keys(Keys.COMMAND + 'v')
    sleep(1)

@step('And paste 5 more times(Total 315 characters)')
def paste_text(context):
    element=context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    element.send_keys(Keys.COMMAND + 'v')
    element.send_keys(Keys.COMMAND + 'v')
    element.send_keys(Keys.COMMAND + 'v')
    element.send_keys(Keys.COMMAND + 'v')
    element.send_keys(Keys.COMMAND + 'v')
    sleep(1)

@step('Count # of actual elements in the field and compare with 300')
def count_number(context):
    elem=len(context.browser.find_element_by_xpath("//input[@id='gh-ac']").get_attribute("value"))
    assert elem==300
    print(elem)

@step('Verify the message "No exact matches found"')
def count_number(context):
 element = context.browser.find_element_by_xpath("//h3[@class='srp-save-null-search__heading' and text()='No exact matches found']")


@step('Click "{name_of_the_link}" header element')
def click_sell(context, name_of_the_link):
    header_action=context.browser.find_element_by_xpath(f"//*[contains(@class, 'gh-') and contains(text(), '{name_of_the_link}')]")
    sleep(5)
    header_action.click()