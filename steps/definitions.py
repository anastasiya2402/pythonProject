from behave import step
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import warnings

@step('Open eBay.com')
def some_test_impl(context):
    context.browser=webdriver.Chrome()
    context.browser.get("https://www.ebay.com/")


@step('In search bar type "{name_of_search}"')
def search_smth(context, name_of_search):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys(f"{name_of_search}")


@step('Search results are "{search}" related')
def verify_search_result(context, search):

    items = context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')]//h3")
    mismatches = []  # placeholder for bugs

    for each_item in items:  # iterate through results
        if search.lower() not in each_item.text.lower():  # TRUE or FALSE
           mismatches.append(each_item.text)

    for page in range(2,10):
        context.browser.find_element_by_xpath(f"//a[@class='pagination__item' and text()='{page}']").click()
        items = context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')]//h3")
        sleep(5)
        for each_item in items:
            if search.lower() not in each_item.text.lower():
                mismatches.append(each_item.text)

    if mismatches:
      print(mismatches)
      raise ValueError(f'BUG: Some items do not contain the word {search}!')
    if not items:
     raise ValueError(f'BUG: Not all {search}es are in the result items!')

@step('Verifying that all items are "{search}" related')
def verifying_result(context,search):
     result_items=context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')][.//span[contains(text(),'Buy It Now')]][.//span[contains(text(),'Free shipping')]]//h3")
     mismatches=[]
     for each_item in result_items:
         if search.lower() not in each_item.text.lower():
             mismatches.append(each_item.text)
             break
     for page in range(2,10):
        context.browser.find_element_by_xpath(f"//a[@class='pagination__item' and text()='{page}']").click()
        result_items = context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')][.//span[contains(text(),'Buy It Now')]][.//span[contains(text(),'Free shipping')]]//h3")
        sleep(5)
        for each_item in result_items:
            if search.lower() not in each_item.text.lower():
                mismatches.append(each_item.text)
                break
     if mismatches:
      print(mismatches)
      raise ValueError(f'BUG: Some items do not contain the word {search}!')
     if not result_items:
      raise ValueError(f'BUG: Not all {search}es are in the result items!')


@step('"{link_name}" are displayed')
def verify_all_categories(context,link_name):
    image=context.browser.find_elements_by_xpath(f"//h1[text()='{link_name}']")

    if not image:
        raise ValueError(f'BUG: \n\n {link_name} are not displayed!' )

@step('Choose filter "{link_name}"')
def choose_filter(context, link_name):
    filter=context.browser.find_element_by_xpath(f"//h2[@class='srp-format-tabs-h2' and contains(text(), '{link_name}')]")
    sleep(5)
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
   sleep(4)
   another_filter.click()


@step('Verifying that all items are "{search}es" with filters "Free shipping" and "Buy It Now"')
def verify_dress(context, search):
    result_items=context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')][.//span[contains(text(),'Buy It Now')]][.//span[contains(text(),'Free shipping')]]//h3")
    mismatches = []                 # placeholder for bugs
    for each_item in result_items:  # iterate through results
        if search.lower() not in each_item.text.lower():  # TRUE or FALSE
          mismatches.append(each_item.text)

    for page in range(2,10):
         sleep(2)
         context.browser.find_element_by_xpath(f"//a[@class='pagination__item' and text()='{page}']").click()
         result_items = context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')][.//span[contains(text(),'Buy It Now')]][.//span[contains(text(),'Free shipping')]]//h3")
         sleep(5)
         for each_item in result_items:
            if search.lower() not in each_item.text.lower():  # TRUE or FALSE
             mismatches.append(each_item.text)
    if mismatches:
     print(mismatches)
     raise ValueError(f'BUG: \n\n Not all results contain a word {search}!')
    if not result_items:
     raise ValueError(f'BUG: Not all {search}es are in the result items!')





@step('Push button "{link_of_the_element}"')
def click_the_search_btn(context, link_of_the_element):
    srch_btn = context.browser.find_element_by_xpath(f"//*[contains(@class, 'btn-') and contains(@value, '{link_of_the_element}')]")
    srch_btn.click()
    sleep(5)


@step('Enter some special characters')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("@!#$%^&*()-_=+`~|]}[{'/.>,<?")


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

@step('Verifying that all items are "{name_of_link}" with filters "Free Shipping", "Brand New" and "Buy It Now"(or Best Offer)')
def all_items(context,name_of_link):
    result_items=context.browser.find_elements_by_xpath("//div[contains(@class,'s-item')][.//span[contains(text(),'Buy It Now') or contains(text(),'or Best Offer')]][.//span[text()='Free shipping']][.//span[text()='Brand New']]//h3")
    mismatches = []  # placeholder for bugs

    for each_item in result_items:  # iterate through results
     #if (name_of_link.lower() or filter1.lower() or filter2.lower() or filter3.lower() or filter4.lower()) not in each_item.text.lower():  # TRUE or FALSE
      if name_of_link.lower() not in each_item.text.lower():
       mismatches.append(each_item.text)

    for page in range(2, 10):
        sleep(2)
        context.browser.find_element_by_xpath(f"//a[@class='pagination__item' and text()='{page}']").click()
        result_items=context.browser.find_elements_by_xpath("//div[contains(@class,'s-item')][.//span[contains(text(),'Buy It Now') or contains(text(),'or Best Offer')]][.//span[text()='Free shipping']][.//span[text()='Brand New']]//h3")
        sleep(5)
        for each_item in result_items:
            if name_of_link.lower() not in each_item.text.lower():  # TRUE or FALSE
                mismatches.append(each_item.text)

    if mismatches:
       print(mismatches)
       raise ValueError(f'BUG: \n\n Not all results contain the word {name_of_link}!')
    if not result_items:
     raise ValueError(f'BUG: Not all {name_of_link}es are in the result items!')


@step('Delete all cookies')
def clean_cookies(context):
    context.browser.delete_all_cookies()




