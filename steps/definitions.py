from behave import step
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
import warnings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@step('Open eBay.com')
def some_test_impl(context):
    context.browser.get(context.url)


@step('In search bar type "{name_of_search}"')
def search_smth(context, name_of_search):
    # search_inpt=context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt =WebDriverWait(context.browser,5).until(EC.visibility_of_element_located((By.XPATH,
    "//input[@id='gh-ac']" )), message='Search has not found')

    search_inpt.send_keys(f"{name_of_search}")


@step('Search results are "{search}" related')
def verify_search_result(context, search):

    items_visible=WebDriverWait(context.browser, 8).until(EC.visibility_of_all_elements_located((By.XPATH,
    "//li[starts-with(@class,'s-item')]//h3")), message='Search has not been found')

    if not items_visible:
        raise ValueError(f'BUG:\n\n Not all {search}es found by xPaths are on the page!')

    items_visible[0].click()

    context.browser.back()

    items_visible = WebDriverWait(context.browser, 12).until(EC.presence_of_all_elements_located((By.XPATH,
    "//li[starts-with(@class,'s-item')]//h3")), message='Search has not been found')

    mismatches = []

    for each_item in items_visible:
        for word in search.split():
            if word.lower() not in each_item.text.lower():
                  mismatches.append(each_item.text)
                  break

    while True:
        next_page = WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
        "//a[@class='pagination__next']")), message = 'Search has not been found')

        if next_page.get_attribute("aria-disabled") == 'true':
            break
        next_page.click()

        items_visible = WebDriverWait(context.browser, 8).until(EC.presence_of_all_elements_located((By.XPATH,
        "//li[starts-with(@class,'s-item')]//h3")), message='Search has not been found')

        if not items_visible:
            raise ValueError(f'BUG:\n\n Not all {search} found by xPaths are on the page!')

        for each_item in items_visible:
            for word in search.split():
                if word.lower() not in each_item.text.lower():
                    mismatches.append(each_item.text)
                    break

    try:
       xpath_visible=WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
       "//div[contains(text(),'We're unable to show you more than 10,000 results. Please refine your search to narrow your results.')]")),
       message='Search has not been found')

       print("We're unable to show you more than 10,000 results. Please refine your search to narrow your results.")
    except:
       print(f"Search {search} is completed")

    if mismatches:
        print(mismatches)
        raise ValueError(f'BUG: Some items do not contain the word {search}!')


@step('Verifying that all items are "{search}" related')
def verifying_result(context,search):
     result_items_visible=WebDriverWait(context.browser,10).until(EC.presence_of_all_elements_located((By.XPATH,
      "//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'Buy It Now') or contains(text(),'Best Offer')]][.//span[contains(text(),'shipping')]]//h3")),
     message='Search has not been found')

     if not result_items_visible:
         raise ValueError(f'BUG:\n\n Not all {search} found by xPaths are on the page!')

     result_items_visible[0].click()

     context.browser.back()

     result_items_visible = WebDriverWait(context.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,
     "//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'Buy It Now') or contains(text(),'Best Offer')]][.//span[contains(text(),'shipping')]]//h3")),
     message='Search has not been found')

     mismatches=[]

     for each_item in result_items_visible:
         for word in search.split():
             if word.lower() not in each_item.text.lower():
                 mismatches.append(each_item.text)
                 break

     pages = WebDriverWait(context.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,
     "//a[@class='pagination__item']")), message='Search has not been found')

     count_number = len(pages)
     print(count_number)
     top_value = count_number + 1

     for page in range(2, top_value):

         new_page = WebDriverWait(context.browser, 8).until(EC.element_to_be_clickable((By.XPATH,
         f"//a[@class='pagination__item' and text()='{page}']")), message='Search has not been found').click()

         result_items_visible = WebDriverWait(context.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,
         "//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'Buy It Now') or contains(text(),'Best Offer')]][.//span[contains(text(),'shipping')]]//h3")),
         message='Search has not been found')

         if not result_items_visible:
             raise ValueError(f'BUG:\n\n Not all {search}es found by xPaths are on the page!')

         for each_item in result_items_visible:
             for word in each_item.text:
                 if word.lower() not in each_item.text.lower():
                     mismatches.append(each_item.text)
                     break

     if mismatches:
         print(mismatches)
         raise ValueError(f'BUG: \n\n Some items do not contain the word {search}!')


@step('"{link_name}" are displayed')
def verify_all_categories(context,link_name):
    # image_visible=context.browser.find_element_by_xpath(f"//h1[text()='{link_name}']")
    image_visible=WebDriverWait(context.browser,5).until(EC.presence_of_element_located((By.XPATH,f"//h1[text()='{link_name}']")),
    message='Search has not been found')

    if not image_visible:
        raise ValueError(f'BUG: \n\n {link_name} are not displayed!' )

@step('Choose filter "{link_name}"')
def choose_filter(context, link_name):
    filter_visible=WebDriverWait(context.browser,5).until(EC.element_to_be_clickable((By.XPATH,
    f"//h2[@class='srp-format-tabs-h2' and contains(text(), '{link_name}')]")),message='Search has not been found')

    filter_visible.click()

@step('Next choose more filters: "{link_name}"')
def choose_filter(context,link_name):
    new_filter=WebDriverWait(context.browser,5).until(EC.element_to_be_clickable((By.XPATH,f"//span[text()='{link_name}']")),
    message='Search has not been found')
    new_filter.click()

@step('and "{name_link}"')
def filter_again(context,name_link):
   another_filter=WebDriverWait(context.browser,8).until(EC.element_to_be_clickable((By.XPATH,
   f"//span[text()='{name_link}']/span[@class='checkbox']")),message='Search has not been found')

   another_filter.click()


@step('Push button "{link_of_the_element}"')
def click_the_search_btn(context, link_of_the_element):
     # srch_btn_clickable =WebDriverWait(context.browser,5).until(EC.element_to_be_clickable((By.XPATH,
     # f"//*[contains(@class, 'btn-') and contains(@value, '{link_of_the_element}')]")), message='Search has not been found')

    srch_btn=context.browser.find_elements_by_xpath(f"//*[contains(@class, 'btn-') and contains(@value, '{link_of_the_element}')]")
    limit=5
    while not srch_btn and limit:
        sleep(1)
        limit-=1
        srch_btn=context.browser.find_elements_by_xpath(f"//*[contains(@class, 'btn-') and contains(@value, '{link_of_the_element}')]")

    if not srch_btn:
        raise Exception("Search has not been found")

    srch_btn[0].click()


@step('Select/Copy/Paste the result')
def copy_text(context):
    field_visible=WebDriverWait(context.browser,5).until(EC.presence_of_element_located((By.XPATH,"//input[@id='gh-ac']")),
    message='Search has not been found')

    field_visible.send_keys(Keys.COMMAND + 'a')

    field_visible.send_keys(Keys.COMMAND + 'c')

    field_visible.send_keys(Keys.ARROW_RIGHT)

    field_visible.send_keys(Keys.COMMAND + 'v')


@step('And paste 5 more times(Total 315 characters)')
def paste_text(context):
    field_visible=WebDriverWait(context.browser,5).until(EC.presence_of_element_located((By.XPATH,"//input[@id='gh-ac']")),
    message='Search has not been found')

    field_visible.send_keys(Keys.COMMAND + 'v')
    field_visible.send_keys(Keys.COMMAND + 'v')
    field_visible.send_keys(Keys.COMMAND + 'v')
    field_visible.send_keys(Keys.COMMAND + 'v')
    field_visible.send_keys(Keys.COMMAND + 'v')


@step('Count # of actual elements in the field and compare with 300')
def count_number(context):
    field_visible=WebDriverWait(context.browser,5).until(EC.presence_of_element_located((By.XPATH,"//input[@id='gh-ac']")),
    message='Search has not been found')
    elem=len(field_visible.get_attribute("value"))
    assert elem==300
    print(elem)


@step('Verify the message "No exact matches found"')
def count_number(context):
    element_visible=WebDriverWait(context.browser,5).until(EC.presence_of_element_located((By.XPATH,
    "//h3[@class='srp-save-null-search__heading' and text()='No exact matches found']")),message='Search has not been found')
    if not element_visible:
        raise ValueError('No such message appeared')


@step('Click "{name_of_the_link}" header element')
def click_sell(context, name_of_the_link):
    header_action_visible=WebDriverWait(context.browser, 5).until(EC.presence_of_element_located((By.XPATH,
    f"//*[contains(@class, 'gh-') and contains(text(), '{name_of_the_link}')]")), message='Search has not been found')
    header_action_visible.click()

@step('Hover over "{link_name}" header element')
def hover_over(context, link_name):
    action=ActionChains(context.browser)
    elmt_visible=WebDriverWait(context.browser,5).until(EC.visibility_of_element_located((By.XPATH,
    f"//*[contains(@class, 'gh-') and contains(text(), '{link_name}')]")), message='Search has not been found')

    hover_elmt=action.move_to_element(elmt_visible).perform()

@step('and go to "{name_of_link}" items')
def choose_elmt(context,name_of_link):
    choose_next_visible=WebDriverWait(context.browser,5).until(EC.presence_of_element_located((By.XPATH,
    f"//a[text()=' {name_of_link}' and @class='gh-eb-oa thrd']")), message='Search has not been found')

    choose_next_visible.click()

@step('Verifying that all items are "{name_of_link}" with above filters')
def all_items(context,name_of_link):
    result_items_visible=WebDriverWait(context.browser,8).until(EC.presence_of_all_elements_located((By.XPATH,
    "//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'Buy It Now') or contains(text(),'Best Offer')]][.//span[contains(text(),'shipping')]][.//span[text()='Brand New']]//h3")),
    message='Search has not been found')

    if not result_items_visible:
        raise ValueError(f'BUG:\n\n Not all {name_of_link} found by xPath are on the page!')

    result_items_visible[0].click()

    context.browser.back()

    result_items_visible = WebDriverWait(context.browser, 8).until(EC.presence_of_all_elements_located((By.XPATH,
    "//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'Buy It Now') or contains(text(),'Best Offer')]][.//span[contains(text(),'shipping')]][.//span[text()='Brand New']]//h3")),
    message='Search has not been found')

    mismatches = []
    for each_item in result_items_visible:
        for word in name_of_link.split():
            if word.lower() not in each_item.text.lower():
                mismatches.append(each_item.text)
                break

    pages =WebDriverWait(context.browser,8).until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='pagination__item']")),
    message='Search has not been found')

    count_number = len(pages)
    print(count_number)
    top_value = count_number + 1

    for page in range(2, top_value):
        new_page=WebDriverWait(context.browser,8).until(EC.element_to_be_clickable((By.XPATH,
        f"//a[@class='pagination__item' and text()='{page}']")) , message='Search has not been found').click()

        result_items_visible = WebDriverWait(context.browser, 8).until(EC.presence_of_all_elements_located((By.XPATH,
        "//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'Buy It Now') or contains(text(),'Best Offer')]][.//span[contains(text(),'shipping')]][.//span[text()='Brand New']]//h3")),
        message='Search has not been found')

        if not result_items_visible:
            raise ValueError(f'BUG:\n\n Not all {name_of_link} found by xPath are on the page!')

        for each_item in result_items_visible:
            for word in name_of_link.split():
                if word.lower() not in each_item.text.lower():
                    mismatches.append(each_item.text)
                    break

    if mismatches:
       print(mismatches)
       raise ValueError(f'BUG: \n\n Not all results contain the word {name_of_link}!')


# @step('Verifying that all items are "{search}" related and contain Free {common_filter}')
# def let_us_find(context,search,common_filter):
#
#     result_items=WebDriverWait(context.browser, 8).until(EC.presence_of_all_elements_located((By.XPATH,
#     f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]//h3")),
#     message = 'Search has not been found')
#
#     if not result_items:
#        raise ValueError(f'BUG:\n\n Not all {search} results found by xPath are on the page!')
#
#     result_items[0].click()
#
#     context.browser.back()
#
#     result_items = WebDriverWait(context.browser, 5).until(EC.presence_of_all_elements_located((By.XPATH,
#     f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]//h3")),
#     message='Search has not been found')
#
#     mismatches = []
#
#     for each_item in result_items:
#         for word in search.split():
#             if word.lower() not in each_item.text.lower():
#                 mismatches.append(each_item.text)
#                 break
#
#     pages = WebDriverWait(context.browser, 5).until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='pagination__item']")),
#     message='Search has not been found')
#
#     count_number = len(pages)
#     print(count_number)
#     top_value = count_number + 1
#
#     for page in range(2, top_value):
#         try:
#             new_page = WebDriverWait(context.browser, 5).until(EC.presence_of_element_located((By.XPATH,
#             f"//a[@class='pagination__item' and text()='{page}']")), message='Search has not been found')
#
#             new_page.click()
#
#             try:
#                 result_items = WebDriverWait(context.browser, 5).until(EC.presence_of_all_elements_located((By.XPATH,
#                 f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]//h3")),
#                 message='Search has not been found')
#                 for each_item in result_items:
#                     for word in each_item.text:
#                         if word.lower() not in each_item.text.lower():
#                             mismatches.append(each_item.text)
#                             break
#             except:
#                 raise ValueError(f'BUG:\n\n Not all {search}es found by xPaths are on the page!')
#
#         except:
#             print("No more pages available")
#
#     if mismatches:
#         print(mismatches)
#         raise ValueError(f'BUG: \n\n Some items do not contain the word {search}!')


@step('Click on {name_of_link}')
def link(context, name_of_link):
    change_default_visible=WebDriverWait(context.browser,5).until(EC.element_to_be_clickable((By.XPATH,
    f"//span[text()='{name_of_link}']/parent::a")), message='Search has not been found')

    change_default_visible.click()

@step('Choose {filter_group} {filter_size}')
def size_filter(context,filter_group, filter_size):
    try:
        size_of_shoe_visible=WebDriverWait(context.browser,5).until(EC.presence_of_element_located((By.XPATH,
        f"//a[@class='size-component__square' and text()='{filter_size}']")), message='Search has not been found')
        size_of_shoe_visible.click()

    except:
        see_all_located = WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
        f"//span[text()='see all']/parent::button[contains(@aria-label,'see all - {filter_group} - opens dialog')]")),
        message='Search has not been found')

        see_all_located.click()

        new_window_pops = WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
        f"//span[@class='clipped']/parent::span[text()='{filter_size}']")), message='Search has not been found')

        new_window_pops.click()

        button_push = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
        "//span[@aria-hidden='true' and text()='Apply']")), message='Search has not been found').click()


@step('From {color_group}, choose {color_choice}')
def color_filter(context,color_group,color_choice):
    try:
        desired_color = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
        f"//span[@class='clipped' and text()='{color_choice}']/parent::a")), message='Search has not been found')

        desired_color.click()

    except:
        see_all_located = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
        f"//span[text()='see all']/parent::button[starts-with(@aria-label,'see all - {color_group} - opens dialog')]")),
        message='Search has not been found')

        see_all_located.click()

        new_window_pops = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
        f"//span[@class='clipped']/parent::span[text()='{color_choice}']")), message='Search has not been found')

        new_window_pops.click()

        button_push = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
        "//span[@aria-hidden='true' and text()='Apply']")),message='Search has not been found').click()


@step('We choose from {color_group}, {color_choice}')
def color_filter(context,color_group,color_choice):
    try:
        desired_color = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
        f"//span[@class='clipped']/parent::span[text()='{color_choice}']")), message='Search has not been found')

        desired_color.click()

    except:
        see_all_located = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
        f"//span[text()='see all']/parent::button[starts-with(@aria-label,'see all - {color_group} - opens dialog')]")),
        message='Search has not been found')

        see_all_located.click()

        new_window_pops = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
        f"//span[@class='clipped']/parent::span[text()='{color_choice}']")), message='Search has not been found')

        new_window_pops.click()

        button_push = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
        "//span[@aria-hidden='true' and text()='Apply']")),message='Search has not been found').click()


@step('In {group} choose {kind}')
def choose_kind_in_group(context,group, kind):
    desired_group_visible = WebDriverWait(context.browser, 15).until(EC.element_to_be_clickable((By.XPATH,
    f"//li[@class='x-refine__main__list '][.//h3[contains(text(),'{group}')]]//div[@role='button']")),
    message='Search has not been found')

    # desired_group_visible = WebDriverWait(context.browser, 15).until(EC.element_to_be_clickable((By.XPATH,
    # f"//div[@role='button' and @class='x-refine__item--toggle']/h3[contains(text(),'{group}')]")),message='Search has not been found')

    if desired_group_visible.get_attribute('aria-expanded') == 'false':
        desired_group_visible.click()

    try:
        desired_checkbox = WebDriverWait(context.browser, 15).until(EC.presence_of_element_located((By.XPATH,
        f"//li[@class='x-refine__main__list '][.//h3[contains(text(),'{group}')]]//div[@class='x-refine__select__svg'][.//span[contains(text(),'{kind}')]]//input")),
        message='Search has not been found')

        special_char = f"//li[@class='x-refine__main__list '][.//h3[text()=\''s\']]"

        desired_checkbox.click()

    except:
        see_all_located = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
        f"//span[text()='see all']/parent::button[starts-with(@aria-label,'see all - {group} - opens dialog')]")),
        message='Search has not been found')

        see_all_located.click()

        new_window_pops = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
        f"//span[@class='clipped']/parent::span[text()='{kind}']")),
         message='Search has not been found')

        new_window_pops.click()

        button_push = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
        "//span[@aria-hidden='true' and text()='Apply']")), message='Search has not been found').click()


@step('Text as a variable')
def text_as_a_variable(context):
    my_variable=context.text
    print(my_variable)


@step('Apply following filters')
def filters_from_table(context):
    for filter in context.table.rows:
        header = filter['Filter']
        checks_label=filter['value']
        checks_text = filter['text']
        clicks_size=filter['size']
        checks_title = filter['title']
        clicks_color=filter['color']

        desired_group_visible=WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
        f"//li[@class='x-refine__main__list '][.//h3[contains(text(),'{header}')]]//div[@role='button']")), message ='Search has not been found')

        if desired_group_visible.get_attribute('aria-expanded') == 'false':
            desired_group_visible.click()

        try:
            desired_checkbox=WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
            f"//li[@class='x-refine__main__list '][.//h3[contains(text(),'{header}')]]//div[@class='x-refine__select__svg'][.//span[contains(text(),'{checks_label}')]]//input")),
            message= 'Search has not been found')

            special_char=f"//li[@class='x-refine__main__list '][.//h3[text()=\'Let's\']]"

            desired_checkbox.click()

        except:
            see_all_located = WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
            f"//span[text()='see all']/parent::button[starts-with(@aria-label,'see all - {header} - opens dialog')]")),
            message='Search has not been found')

            see_all_located.click()

            new_window_pops = WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
            f"//span[@class='clipped']/parent::span[text()='{checks_label}']")), message='Search has not been found')

            new_window_pops.click()

            button_push = WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
            "//span[@aria-hidden='true' and text()='Apply']")), message='Search has not been found').click()

        try:
            desired_size =WebDriverWait(context.browser,8).until(EC.presence_of_element_located((By.XPATH,
            f"//a[@class='size-component__square' and text()='{clicks_size}']")), message='Search has not been found')

            desired_size.click()

        except:
            see_all_located = WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
            f"//span[text()='see all']/parent::button[contains(@aria-label,'see all - {checks_text} - opens dialog')]")),
            message='Search has not been found')

            see_all_located.click()

            new_window_pops = WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
            f"//span[@class='clipped']/parent::span[text()='{clicks_size}']")), message='Search has not been found')

            new_window_pops.click()

            button_push = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
            "//span[@aria-hidden='true' and text()='Apply']")),message='Search has not been found').click()

        try:
            desired_color =WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
            f"//span[@class='clipped' and text()='{clicks_color}']/parent::a")), message='Search has not been found')

            desired_color.click()

        except:
            see_all_located=WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
            f"//span[text()='see all']/parent::button[starts-with(@aria-label,'see all - {checks_title} - opens dialog')]")),
            message='Search has not been found')

            see_all_located.click()

            new_window_pops=WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
            f"//span[@class='clipped']/parent::span[text()='{clicks_color}']")), message='Search has not been found')

            new_window_pops.click()

            button_push =WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
            "//span[@aria-hidden='true' and text()='Apply']")), message='Search has not been found').click()


@step('Apply the following filters')
def filters_from_table(context):
    for filter in context.table.rows:
        header = filter['Items']
        checks_label = filter['value']

        desired_group_appeared = WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
        f"//li[@class='x-refine__main__list '][.//h3[text()='{header}']]//div[@role='button']")), message='Search has not been found')

        if desired_group_appeared.get_attribute('aria-expanded') == 'false':

            desired_group_appeared.click()

        try:
            desired_checkbox=WebDriverWait(context.browser, 5).until(EC.presence_of_element_located((By.XPATH,
            f"//li[@class='x-refine__main__list '][.//h3[text()='{header}']]//div[@class='x-refine__select__svg'][.//span[starts-with(text(),'{checks_label}')]]//input")),
            message='Search has not been found')
            special_char = f"//li[@class='x-refine__main__list '][.//h3[text()=\'Let's\']]"
            desired_checkbox.click()

        except:
            see_all_located=WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
            f"//span[text()='see all']/parent::button[starts-with(@aria-label,'see all - {header} - opens dialog')]")), message='Search has not been found')

            see_all_located.click()

            new_window_pops=WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
            f"//span[@class='clipped']/parent::span[text()='{checks_label}']")), message='Search has not been found')

            new_window_pops.click()

            button_push =WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH,
            "//span[@aria-hidden='true' and text()='Apply']")), message='Search has not been found').click()


@step('Validating that all items have text "{search}", contain Free {common_filter} and satisfy the filters given below')
def check_filters(context, search, common_filter):
    for filter in context.table.rows:
        header = filter['Filter']
        checks_label = filter['value']
        checks_text = filter['text']
        clicks_output = filter['output']
        checks_title = filter['title']
        clicks_color = filter['color']

    keys=[f"{header}",f"{checks_text}",f"{checks_title}"]
    values=[f"{checks_label}",f"{clicks_output}",f"{clicks_color}"]
    our_filter=dict(zip(keys,values))
    print(our_filter)

    result_items_visible = WebDriverWait(context.browser, 8).until(EC.presence_of_all_elements_located((By.XPATH,
    f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]")),message='Search has not been found')

    current_window = context.browser.current_window_handle


    item_n_title=[]
    for item in result_items_visible:
        link = item.find_element_by_xpath("descendant::a").get_attribute("href")
        title = item.find_element_by_xpath("descendant::h3").text

        item_specs=(link,title)

        item_n_title.append(item_specs)

    suspicious_items=[]
    for link, title in item_n_title:
        context.browser.execute_script(f'window.open("{link}", "_blank");')
        sleep(2)

        # switch
        context.browser.switch_to.window(context.browser.window_handles[-1])

        # validation

        labels=context.browser.find_elements_by_xpath("//div[@class='itemAttr']//td[@class='attrLabels']")
        # values=context.browser.find_elements_by_xpath("//div[@class='itemAttr']//td[@class='attrLabels']/following-sibling::td[.//*[text()]]")
        # per_item_spec=dict(zip(labels, values))

        specs_information= {}
        for label in labels:

          specs_information[label.text.strip(':')]=label.find_element_by_xpath("following-sibling::td[.//*[text()]]").text


        for k,v in our_filter.items():
            if k in specs_information.keys():
                if our_filter[k] !=specs_information[k]:
                      suspicious_items.append(f'{link} {title} {k} is set to {specs_information[k]}, where we expected {v}')
            else:
                suspicious_items.append(f'{link} {title} does not have information about {k}')

        # switch back and close
        context.browser.close()
        context.browser.switch_to.window(current_window)

    result_items_visible = WebDriverWait(context.browser, 15).until(EC.presence_of_all_elements_located((By.XPATH,
    f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]//h3")),
    message='Search has not been found')

    if not result_items_visible:
        raise ValueError(f'BUG:\n\n Not all {search} results found by xPath are on the page!')
    result_items_visible[0].click()

    context.browser.back()

    result_items_visible = WebDriverWait(context.browser, 15).until(EC.visibility_of_all_elements_located((By.XPATH,
    f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]//h3")),
    message='Search has not been found')

    mismatches = []

    for each_item in result_items_visible:
        for word in search.split():
            if word.lower() not in each_item.text.lower():
                mismatches.append(each_item.text)
                break

    pages = WebDriverWait(context.browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='pagination__item']")),
    message='Search has not been found')

    count_number = len(pages)
    print(count_number)
    top_value = count_number + 1

    for page in range(2, 4):
        try:
            new_page = WebDriverWait(context.browser, 5).until(EC.presence_of_element_located((By.XPATH,
            f"//a[@class='pagination__item' and text()='{page}']")), message='Search has not been found')

            new_page.click()

            result_items_visible = WebDriverWait(context.browser, 8).until(EC.presence_of_all_elements_located((By.XPATH,
            f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]")), message='Search has not been found')

            current_window = context.browser.current_window_handle

            item_n_title = []
            for item in result_items_visible:
                link = item.find_element_by_xpath("descendant::a").get_attribute("href")
                title = item.find_element_by_xpath("descendant::h3").text

                item_specs = (link, title)

                item_n_title.append(item_specs)

            for link, title in item_n_title:
                context.browser.execute_script(f'window.open("{link}", "_blank");')
                sleep(2)

                # switch
                context.browser.switch_to.window(context.browser.window_handles[-1])

                # validation

                labels = context.browser.find_elements_by_xpath("//div[@class='itemAttr']//td[@class='attrLabels']")
                # values=context.browser.find_elements_by_xpath("//div[@class='itemAttr']//td[@class='attrLabels']/following-sibling::td[.//*[text()]]")
                # per_item_spec=dict(zip(labels, values))

                specs_information = {}
                for label in labels:
                    specs_information[label.text.strip(':')] = label.find_element_by_xpath(
                        "following-sibling::td[.//*[text()]]").text


                for k, v in our_filter.items():
                    if k in specs_information.keys():
                        if our_filter[k] != specs_information[k]:
                            suspicious_items.append(
                                f'{link} {title} {k} is set to {specs_information[k]}, where we expected {v}')
                    else:
                        suspicious_items.append(f'{link} {title} does not have information about {k}')

                # switch back and close
                context.browser.close()
                context.browser.switch_to.window(current_window)


            result_items_visible = WebDriverWait(context.browser, 15).until(EC.presence_of_all_elements_located((By.XPATH,
            f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]//h3")), message='Search has not been found')

            if not result_items_visible:
                raise ValueError(f'BUG:\n\n Not all {search}es found by xPaths are on the page!')

            result_items_visible[0].click()

            context.browser.back()

            result_items_visible = WebDriverWait(context.browser, 15).until(EC.visibility_of_all_elements_located((By.XPATH,
            f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]//h3")),message='Search has not been found')

            for each_item in result_items_visible:
                for word in each_item.text:
                    if word.lower() not in each_item.text.lower():
                        mismatches.extend(each_item.text)
                        break

        except:
            print("No more pages available")

    if (mismatches and suspicious_items):
       print(mismatches)
       print(len(mismatches))
       print(suspicious_items)
       print(len(suspicious_items))
       raise  ValueError(f"Some items do not contain the word:\n\t {search}!"
                         f"\n\n Along with some items do not satisfy filter criteria: {our_filter}")

    elif mismatches:
       print(mismatches)
       print(len(mismatches))
       raise ValueError(f'BUG: \n\n Some items do not contain the word {search}!')

    elif suspicious_items:
       print(suspicious_items)
       print(len(suspicious_items))
       raise ValueError(f"Following items do not satisfy filter criteria : {our_filter}")



@step('Validating the filters and the text "{search}" when the search contains Free {common_filter}')
def filtering(context, search, common_filter):
   expected_spec={row['filter']:row['value'] for row in context.table.rows}
   print(expected_spec)

   result_items_visible = WebDriverWait(context.browser, 8).until(EC.presence_of_all_elements_located((By.XPATH,
   f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]")),
   message='Search has not been found')

   current_window = context.browser.current_window_handle

   item_n_title = []
   for item in result_items_visible:
       link = item.find_element_by_xpath("descendant::a").get_attribute("href")
       title = item.find_element_by_xpath("descendant::h3").text

       item_specs = (link, title)

       item_n_title.append(item_specs)

   suspicious_items = []
   for link, title in item_n_title:
       context.browser.execute_script(f'window.open("{link}", "_blank");')
       sleep(2)

       # switch
       context.browser.switch_to.window(context.browser.window_handles[-1])

       # validation

       labels = context.browser.find_elements_by_xpath("//div[@class='itemAttr']//td[@class='attrLabels']")

       actual_spec={label.text.strip(':'): label.find_element_by_xpath("following-sibling::td[.//*[text()]]").text
       for label in labels}

       # print(actual_spec)

       for k, v in expected_spec.items():
           if k in actual_spec.keys():
               if expected_spec[k] != actual_spec[k]:
                   suspicious_items.append(
                       f'{link} {title} {k} is set to {actual_spec[k]}, where we expected {v}')
           else:
               suspicious_items.append(f'{link} {title} does not have information about {k}')

       # switch back and close

       context.browser.close()
       context.browser.switch_to.window(current_window)

   result_items_visible = WebDriverWait(context.browser, 20).until(EC.presence_of_all_elements_located((By.XPATH,
   f"//li[starts-with(@class,'s-item')][.//span[contains(text(),'{common_filter}')]]")),message='Search has not been found')

   if not result_items_visible:
       raise ValueError(f'BUG:\n\n Not all {search} results found by xPath are on the page!')

   result_items_visible[0].click()

   context.browser.back()

   result_items_visible = WebDriverWait(context.browser, 15).until(EC.presence_of_all_elements_located((By.XPATH,
   f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]")),message='Search has not been found')

   mismatches = []

   for each_item in result_items_visible:
       for word in search.split():
           if word.lower() not in each_item.text.lower():
               mismatches.append(each_item.text)
               break

   # pages = WebDriverWait(context.browser, 5).until(
   #     EC.presence_of_all_elements_located((By.XPATH, "//a[@class='pagination__item']")),
   #     message='Search has not been found')
   #
   # count_number = len(pages)
   # print(count_number)
   # top_value = count_number + 1

   for page in range(2, 3):
       try:
           new_page = WebDriverWait(context.browser, 8).until(EC.presence_of_element_located((By.XPATH,
           f"//a[@class='pagination__item' and text()='{page}']")), message='Search has not been found')

           new_page.click()

           result_items_visible = WebDriverWait(context.browser, 8).until(EC.presence_of_all_elements_located((By.XPATH,
           f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]")),
           message='Search has not been found')

           current_window = context.browser.current_window_handle

           item_n_title = []
           for item in result_items_visible:
               link = item.find_element_by_xpath("descendant::a").get_attribute("href")
               title = item.find_element_by_xpath("descendant::h3").text

               item_specs = (link, title)

               item_n_title.append(item_specs)

           for link, title in item_n_title:
               context.browser.execute_script(f'window.open("{link}", "_blank");')
               sleep(2)

               # switch

               context.browser.switch_to.window(context.browser.window_handles[-1])

               # validation

               labels = context.browser.find_elements_by_xpath("//div[@class='itemAttr']//td[@class='attrLabels']")
               values=context.browser.find_elements_by_xpath("//div[@class='itemAttr']//td[@class='attrLabels']/following-sibling::td[.//*[text()]]")

               actual_spec = {label.text.strip(':'): label.find_element_by_xpath("following-sibling::td[.//*[text()]]").text
               for label in labels}

               for k, v in expected_spec.items():
                   if k in actual_spec.keys():
                       if expected_spec[k] != actual_spec[k]:
                           suspicious_items.append(
                               f'{link} {title} {k} is set to {actual_spec[k]}, where we expected {v}')
                   else:
                       suspicious_items.append(f'{link} {title} does not have information about {k}')

               # switch back and close
               context.browser.close()
               context.browser.switch_to.window(current_window)

           result_items_visible = WebDriverWait(context.browser, 15).until(EC.presence_of_all_elements_located((By.XPATH,
           f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]//h3")),
           message='Search has not been found')

           if not result_items_visible:
               raise ValueError(f'BUG:\n\n Not all {search}es found by xPaths are on the page!')

           result_items_visible[0].click()

           context.browser.back()

           result_items_visible = WebDriverWait(context.browser, 15).until(EC.visibility_of_all_elements_located((By.XPATH,
           f"//div[@class='s-item__wrapper clearfix'][.//span[contains(text(),'{common_filter}')]]//h3")),message='Search has not been found')

           for each_item in result_items_visible:
               for word in each_item.text:
                   if word.lower() not in each_item.text.lower():
                       mismatches.extend(each_item.text)
                       break
       except:
           print("No more pages available")

   if (mismatches and suspicious_items):
       print(mismatches)
       print(len(mismatches))
       print(suspicious_items)
       print(len(suspicious_items))
       raise ValueError(f"Some items do not contain the word:\n\t {search}!"
                        f"\n\n Along with some items do not satisfy filter criteria: {expected_spec}")

   elif mismatches:
       print(mismatches)
       print(len(mismatches))
       raise ValueError(f'BUG: \n\n Some items do not contain the word {search}!')

   if suspicious_items:
       print(suspicious_items)
       print(len(suspicious_items))
       raise ValueError(f"Following items do not satisfy filter criteria : {expected_spec}")


@step('Do actions with {name} flyout menu {link} menu item')
def work_with_menu(context,link,name):
    target_menu=context.browser.find_elements_by_xpath(f"//div[@class='hl-cat-nav']//li[./a[text()='{name}']]")

    # flyout_menu =context.browser.find_elements_by_xpath("//div[@class='hl-cat-nav']//li[./a[text()='Motors']][contains(@class,'js-show')]")

    item =context.browser.find_elements_by_xpath(f"//div[@class='hl-cat-nav']//li[./a[text()='Motors']][contains(@class,'js-show')]/descendant::a[text()='{link}']")

    action=ActionChains(context.browser)

    action.move_to_element(target_menu[0])

    action.click(on_element=item)

    action.perform()


@step('Open website')
def open_website(context):
    context.browser.get("https://www.elated.com/res/File/articles/development/javascript/jquery/drag-and-drop-with-jquery-your-essential-guide/card-game.html")


@step('Drag and drop numbers to texts')
def drag_items(context):
   cards=context.browser.find_elements_by_xpath("//div[@class='ui-draggable']")


   card_map={'1':'one',
             '2':'two',
             '3':'three',
             '4':'four',
             '5':'five',
             '6':'six',
             '7':'seven',
             '8':'eight',
             '9':'nine',
             '10':'ten'}

   for card in cards:
       card_number=card.text
       card_text=card_map[card_number]
       placeholder = context.browser.find_element_by_xpath(f"//div[@class='ui-droppable'][text()='{card_text}']")
       action=ActionChains(context.browser)
       action.drag_and_drop(card,placeholder).perform()
       sleep(1)

@step('Verify a pop-up message "{link}"')
def verifying_pop_up(context,link):
    pop_up=context.browser.find_elements_by_xpath(f"//h2[text()='{link}']")
    if not pop_up:
        raise ValueError(f'Message "{link}" is not there')