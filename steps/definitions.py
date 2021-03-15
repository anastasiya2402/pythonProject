from behave import step
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import warnings


@step('Navigate to Google')
def test(context):
  driver=webdriver.Chrome()
  driver.get("https://www.google.com/")
  driver.quit()


@step('Open eBay.com')
def some_test_impl(context):
    context.browser=webdriver.Chrome()
    context.browser.get("https://www.ebay.com/")


@step('In search bar type "{name_of_search}"')
def search_smth(context, name_of_search):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys(f"{name_of_search}")


@step('Search results are "{link}" related')
def verify_search_result(context, link):
    item = context.browser.find_elements_by_xpath(f"//h3[contains(text(), '{link}')]")
    print(item)

    if not item:   # True
        raise ValueError(f'BUG!: \n\n Search results are not related to {link} only')

@step('"{link_name}" are displayed')
def verify_all_categories(context,link_name):
    image=context.browser.find_elements_by_xpath(f"//h1[text()='{link_name}']")

    if not image:
        raise ValueError(f'BUG: \n\n {link_name} are not displayed!' )

@step('Choose filter "{link_name}"')
def choose_filter(context, link_name):
    filter=context.browser.find_element_by_xpath(f"//h2[@class='srp-format-tabs-h2' and contains(text(), '{link_name}')]")
    sleep(3)
    filter.click()
    sleep(5)


@step('Next choose more filters: "{link_name}"')
def choose_filter(context,link_name):
    new_filter=context.browser.find_element_by_xpath(f"//span[text()='{link_name}']")
    new_filter.click()
    sleep(3)


@step('and "{name_link}"')
def filter_again(context,name_link):
   another_filter=context.browser.find_element_by_xpath(f"//span[text()='{name_link}']/span[@class='checkbox']")
   sleep(2)
   another_filter.click()


@step('Verifying that the "{link_name}es" with such filters are there on the first page')
def verify_dress(context,link_name):
    needed_dress=context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')][.//span[contains(text(),'Buy It Now')]][.//span[contains(text(),'Free shipping')]]//h3[contains(text(),'{link_name}')]")
    sleep(5)

    if not needed_dress:
     raise ValueError(f'BUG: \n\n Not all {link_name}es satisfy filters!')


@step('Push button "{link_of_the_element}"')
def click_the_search_btn(context, link_of_the_element):
    srch_btn = context.browser.find_element_by_xpath(f"//*[contains(@class, 'btn-') and contains(@value, '{link_of_the_element}')]")
    srch_btn.click()
    sleep(5)


@step('Enter some special characters')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("@!#$%^&*()-_=+`~|]}[{'/.>,<?")


@step('Verifying that the iPhone 11 you want is there')
def enter_search(context):
    search_elmt=context.browser.find_elements_by_xpath("//li[@class='s-item    '][.//span[text()='Free returns']][.//span[text()='Free shipping']][.//span[text()='Brand New']][.//span[text()='$649.00']]//h3")


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

@step('Hover over "{link_name}" header element')
def hover_over(context, link_name):
    action=ActionChains(context.browser)
    elmt=context.browser.find_element_by_xpath(f"//*[contains(@class, 'gh-') and contains(text(), '{link_name}')]")
    hover_elmt=action.move_to_element(elmt).perform()
    sleep(4)

@step('and go to "{name_of_link}" items')
def choose_elmt(context,name_of_link):
    choose_next=context.browser.find_element_by_xpath(f"//a[text()=' {name_of_link}' and @class='gh-eb-oa thrd']")
    choose_next.click()
    sleep(3)

@step('Verifying that all items are "{name_of_link}" with filters')
def all_items(context,name_of_link):
    all_items=context.browser.find_elements_by_xpath(f"//div[contains(@class,'s-item')][.//span[text()='Buy It Now' or text()='Best Offer']][.//span[text()='Free shipping']][.//span[text()='Brand New']]//h3[contains(text(),'{name_of_link}')]")
    sleep(6)

    if not all_items:
        raise ValueError(f'BUG!: \n\n Not all search results are {name_of_link} with specified filters!')





