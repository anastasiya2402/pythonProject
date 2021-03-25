from behave import step
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import warnings

@step('Open eBay.com')
def some_test_impl(context):
    context.browser.get(context.url)


@step('In search bar type "{name_of_search}"')
def search_smth(context, name_of_search):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys(f"{name_of_search}")


@step('Search results are "{search}" related')
def verify_search_result(context, search):
    items = context.browser.find_elements_by_xpath("//li[starts-with(@class,'s-item')]//h3")
    sleep(3)
    if not items:
        raise ValueError(f'BUG:\n\n Not all {search}es found by xPaths are on the page!')

    items[0].click()
    sleep(2)

    back_to_search = context.browser.find_element_by_xpath("//span[@class='gspr vi-bkto-arrnewred']").click()
    sleep(2)

    items = context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')]//h3")
    mismatches = []

    for each_item in items:
        for word in search.split():
            if word.lower() not in each_item.text.lower():
                  mismatches.append(each_item.text)
                  break

    while True:
        next_page = context.browser.find_element_by_xpath("//a[@class='pagination__next']")
        if next_page.get_attribute("aria-disabled") == 'true':
            break
        next_page.click()
        result_items = context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')][.//span[contains(text(),'Buy It Now')]][.//span[contains(text(),'Free shipping')]]//h3")
        sleep(5)
        if not result_items:
            raise ValueError(f'BUG:\n\n Not all {search} found by xPaths are on the page!')

        for each_item in result_items:
            for word in search.split():
                if word.lower() not in each_item.text.lower():
                    mismatches.append(each_item.text)
                    break

    if mismatches:
        print(mismatches)
        raise ValueError(f'BUG: Some items do not contain the word {search}!')



@step('Verifying that all items are "{search}" related')
def verifying_result(context,search):
     result_items=context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')][.//span[text()='Buy It Now' or text()='or Best Offer']][.//span[contains(text(),'Free shipping')]]//h3")
     if not result_items:
         raise ValueError(f'BUG:\n\n Not all {search} found by xPaths are on the page!')

     result_items[0].click()
     sleep(2)
     back_to_search = context.browser.find_element_by_xpath("//span[@class='gspr vi-bkto-arrnewred']").click()
     sleep(2)
     result_items = context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')][.//span[contains(text(),'Buy It Now')]][.//span[contains(text(),'Free shipping')]]//h3")
     mismatches=[]

     for each_item in result_items:
         for word in search.split():
             if word.lower() not in each_item.text.lower():
                 mismatches.append(each_item.text)
                 break

     pages = context.browser.find_elements_by_xpath("//a[@class='pagination__item']")
     count_number = len(pages)
     print(count_number)
     top_value = count_number + 1

     for page in range(2, top_value):
         context.browser.find_element_by_xpath(f"//a[@class='pagination__item' and text()='{page}']").click()
         items = context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')]//h3")
         sleep(5)
         if not items:
             raise ValueError(f'BUG:\n\n Not all {search}es found by xPaths are on the page!')

         for each_item in items:
             for word in each_item.text:
                 if word.lower() not in each_item.text.lower():
                     mismatches.append(each_item.text)
                     break

     if mismatches:
         print(mismatches)
         raise ValueError(f'BUG: \n\n Some items do not contain the word {search}!')


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

@step('Verifying that all items are "{name_of_link}" with above filters')
def all_items(context,name_of_link):
    result_items=context.browser.find_elements_by_xpath("//div[contains(@class,'s-item')][.//span[contains(text(),'Buy It Now') or contains(text(),'or Best Offer')]][.//span[text()='Free shipping']][.//span[text()='Brand New']]//h3")
    if not result_items:
        raise ValueError(f'BUG:\n\n Not all {name_of_link} found by xPath are on the page!')

    result_items[0].click()
    sleep(2)
    back_to_search = context.browser.find_element_by_xpath("//span[@class='gspr vi-bkto-arrnewred']").click()
    sleep(2)

    result_items = context.browser.find_elements_by_xpath("//div[contains(@class,'s-item')][.//span[contains(text(),'Buy It Now') or contains(text(),'or Best Offer')]][.//span[text()='Free shipping']][.//span[text()='Brand New']]//h3")
    mismatches = []
    for each_item in result_items:
        for word in name_of_link.split():
            if word.lower() not in each_item.text.lower():
                mismatches.append(each_item.text)
                break

    pages = context.browser.find_elements_by_xpath("//a[@class='pagination__item']")
    count_number = len(pages)
    print(count_number)
    top_value = count_number + 1
    for page in range(2, top_value):
        sleep(2)
        context.browser.find_element_by_xpath(f"//a[@class='pagination__item' and text()='{page}']").click()
        result_items=context.browser.find_elements_by_xpath("//div[contains(@class,'s-item')][.//span[contains(text(),'Buy It Now') or contains(text(),'or Best Offer')]][.//span[text()='Free shipping']][.//span[text()='Brand New']]//h3")
        sleep(5)

        if not result_items:
            raise ValueError(f'BUG:\n\n Not all {name_of_link} found by xPath are on the page!')

        for each_item in result_items:
            for word in name_of_link.split():
                if word.lower() not in each_item.text.lower():
                    mismatches.append(each_item.text)
                    break

    if mismatches:
       print(mismatches)
       raise ValueError(f'BUG: \n\n Not all results contain the word {name_of_link}!')


@step('From chosen 60 checkbox {name_of_link} starting with Brand, choose filters: "0", "5", "6", "16"')
def filters_checkboxes(context,name_of_link):
    checkboxes=context.browser.find_elements_by_xpath("//span[@class='checkbox cbx x-refine__multi-select-checkbox ']/parent::div[@class='x-refine__select__svg']")
    count_number=len(checkboxes)
    print(count_number)

    if not checkboxes:
     raise ValueError(f'BUG:\n\n Not all {name_of_link} found by xPath are on the page!')

    checkboxes[0].click()
    sleep(4)
    checkboxes = context.browser.find_elements_by_xpath("//span[@class='checkbox cbx x-refine__multi-select-checkbox ']/parent::div[@class='x-refine__select__svg']")
    checkboxes[5].click()
    sleep(3)
    checkboxes = context.browser.find_elements_by_xpath("//span[@class='checkbox cbx x-refine__multi-select-checkbox ']/parent::div[@class='x-refine__select__svg']")
    checkboxes[6].click()
    sleep(3)
    checkboxes = context.browser.find_elements_by_xpath("//span[@class='checkbox cbx x-refine__multi-select-checkbox ']/parent::div[@class='x-refine__select__svg']")
    sleep(3)
    context.browser.execute_script("window.scrollTo(0,700);")
    sleep(1)
    checkboxes[16].click()
    context.browser.execute_script("window.scrollTo(0,700);")
    sleep(3)

@step('"{name_of_link}":From 11 groups containing checkboxes choose something')
def filters_checkboxes(context,name_of_link):
    checkboxes=context.browser.find_elements_by_xpath("//span[@class='checkbox cbx x-refine__multi-select-checkbox ']/parent::div[@class='x-refine__select__svg']")
    count_number=len(checkboxes)
    print(count_number)
    groups_checkboxes=context.browser.find_elements_by_xpath("//li[@class='x-refine__main__list '][.//span[@class='checkbox cbx x-refine__multi-select-checkbox ']/parent::div[@class='x-refine__select__svg']]")
    groups_checkboxes[0].click()

    if not checkboxes:
     raise ValueError(f'BUG:\n\n Not all {name_of_link} found by xPath are on the page!')

    checkboxes[0].click()
    sleep(4)
    checkboxes = context.browser.find_elements_by_xpath("//span[@class='checkbox cbx x-refine__multi-select-checkbox ']/parent::div[@class='x-refine__select__svg']")
    checkboxes[5].click()
    sleep(3)
    checkboxes = context.browser.find_elements_by_xpath("//span[@class='checkbox cbx x-refine__multi-select-checkbox ']/parent::div[@class='x-refine__select__svg']")
    checkboxes[6].click()
    sleep(3)
    checkboxes = context.browser.find_elements_by_xpath("//span[@class='checkbox cbx x-refine__multi-select-checkbox ']/parent::div[@class='x-refine__select__svg']")
    sleep(3)
    context.browser.execute_script("window.scrollTo(0,700);")
    sleep(1)
    checkboxes[16].click()
    context.browser.execute_script("window.scrollTo(0,700);")
    sleep(3)


@step('Then choose more filters: "{name_of_filter}"')
def filter_adding_text(context,name_of_filter):
    context.browser.execute_script("window.scrollTo(0,1800);")
    sleep(4)
    context.browser.find_element_by_xpath(f"//span[@class='checkbox cbx x-refine__multi-select-checkbox ']/parent::div[@class='x-refine__select__svg'][.//span[text()='{name_of_filter}']]").click()
    sleep(3)
    context.browser.execute_script("window.scrollTo(0,1800);")
    sleep(4)

@step('Choose more filters: "{filter_name}"')
def filter_adding_location(context,filter_name):
    context.browser.execute_script("window.scrollTo(0,1400);")
    sleep(4)
    context.browser.find_element_by_xpath(f"//span[@class='checkbox cbx x-refine__multi-select-checkbox ']/parent::div[@class='x-refine__select__svg'][.//span[text()='{filter_name}']]").click()
    sleep(3)
    context.browser.execute_script("window.scrollTo(0,1400);")
    sleep(4)

@step('and also "{link_name}"')
def filter_by_text(context, link_name):
    context.browser.execute_script("window.scrollTo(0,2400);")
    sleep(4)
    context.browser.find_element_by_xpath(f"//span[@class='checkbox cbx x-refine__multi-select-checkbox ']/parent::div[@class='x-refine__select__svg'][.//span[text()='{link_name}']]").click()
    sleep(3)
    context.browser.execute_script("window.scrollTo(0,2400);")
    sleep(3)

@step('and also choose "{link_filter}"')
def filter_with_location(context,link_filter):
    context.browser.execute_script("window.scrollTo(0,2000);")
    sleep(4)
    context.browser.find_element_by_xpath(f"//span[@class='checkbox cbx x-refine__multi-select-checkbox ']/parent::div[@class='x-refine__select__svg'][.//span[text()='{link_filter}']]").click()
    sleep(3)
    context.browser.execute_script("window.scrollTo(0,2000);")
    sleep(3)

@step('Verifying that all items are "{search}" related and contain "{common_filter}"')
def let_us_find(context,search,common_filter):
    common_paths=context.browser.find_elements_by_xpath(f"//li[starts-with(@class,'s-item')][.//span[text()='Free 4 day shipping' or text()='{common_filter}']]")
    if not common_paths:
       raise ValueError(f'BUG:\n\n Not all {search} results found by xPath are on the page!')

    common_paths[0].click()
    sleep(2)
    back_to_search = context.browser.find_element_by_xpath("//span[@class='gspr vi-bkto-arrnewred']").click()
    sleep(2)

    common_paths = context.browser.find_elements_by_xpath(f"//li[starts-with(@class,'s-item')][.//span[text()='Free 4 day shipping' or text()='{common_filter}']]")
    mismatches = []
    for each_item in common_paths:
        for word in search.split():
            if word.lower() not in each_item.text.lower():
                mismatches.append(each_item.text)
                break

    pages=context.browser.find_elements_by_xpath("//a[@class='pagination__item']")
    count_number=len(pages)
    print(count_number)
    top_value=count_number+1
    for page in range(2, top_value):
        context.browser.find_element_by_xpath(f"//a[@class='pagination__item' and text()='{page}']").click()
        common_paths=context.browser.find_elements_by_xpath(f"//li[starts-with(@class,'s-item')][.//span[text()='Free 4 day shipping' or text()='{common_filter}']]")
        sleep(5)
        if not common_paths:
            raise ValueError(f'BUG:\n\n Not all {search} results found by xPath are on the page!')

        for each_item in common_paths:
            for word in search.split():
                if word.lower() not in each_item.text.lower():
                    mismatches.append(each_item.text)
                    break

    if mismatches:
        print(mismatches)
        raise ValueError(f'BUG: \n\n Some items do not contain the word {search}!')


@step('Click on {name_of_link}')
def link(context, name_of_link):
    change_default=context.browser.find_element_by_xpath(f"//span[text()='{name_of_link}']/parent::a")
    sleep(2)
    change_default.click()

@step('Choose size {filter_size}')
def size_filter(context, filter_size):
    size_of_shoe=context.browser.find_element_by_xpath(f"//a[@class='size-component__square' and text()='8.5']")
    sleep(2)
    size_of_shoe.click()

@step('From Color, choose {color_choice}')
def color_filter(context,color_choice):
    context.browser.execute_script("window.scrollTo(0,600);")
    color_option=context.browser.find_element_by_xpath("//input[@aria-label='White']/parent::span")
    sleep(2)
    color_option.click()

@step('From Color options, choose {color_option}')
def color_another_construction(context,color_option):
    context.browser.execute_script("window.scrollTo(0,300);")
    color_option = context.browser.find_element_by_xpath("//span[text()='Pink']/parent::a")
    sleep(2)
    color_option.click()

@step('In {expand_it} click on {see_all}')
def choose_brand(context,expand_it, see_all):
    desired_group=context.browser.find_element_by_xpath(f"//li[@class='x-refine__main__list '][.//h3[text()='{expand_it}']]//div[@role='button']")
    sleep(4)
    context.browser.execute_script("window.scrollTo(0,1400);")
    sleep(2)
    if desired_group.get_attribute('aria-expanded') =='false':
        desired_group.click()
        sleep(5)
    see_all_choice=context.browser.find_element_by_xpath(f"//span[text()='{see_all}']/parent::button[@aria-label='see all - Brand - opens dialog']")
    sleep(4)
    see_all_choice.click()
    context.browser.execute_script("window.scrollTo(0,1400);")
    sleep(1)

@step('In New Window choose Not Specified')
def choice_in_new_window(context):
    new_window_choice=context.browser.find_element_by_xpath("//span[@class='checkbox__icon'and @hidden]/preceding-sibling::input[@aria-hidden='false' and @id='c3-subPanel-Brand_Not%20Specified-0_cbx']")
    sleep(3)
    new_window_choice.click()

@step('Push {link_button} button')
def pushing_button_hidden_before(context,link_button):
    button_push=context.browser.find_element_by_xpath("//span[@aria-hidden='true' and text()='Apply']")
    sleep(3)
    button_push.click()
    sleep(4)

@step('Text as a variable')
def text_as_a_variable(context):
    my_variable=context.text
    print(my_variable)


@step('Apply following filters')
def filters_from_table(context):
    for filter in context.table.rows:
        header = filter['Filter']
        checks_label=filter['value']
        clicks_size=filter['size']
        clicks_color=filter['color']

        desired_checkbox=context.browser.find_element_by_xpath(f"//li[@class='x-refine__main__list '][.//h3[text()='{header}']]//div[@class='x-refine__select__svg'][.//span[text()='{checks_label}']]//input")
        sleep(5)
        special_char=f"//li[@class='x-refine__main__list '][.//h3[text()=\'Let's\']]"

        if not desired_checkbox:
            raise ValueError('BUG:\n\n Checkbox not found!')

        desired_checkbox.click()
        sleep(3)

        desired_size = context.browser.find_element_by_xpath(f"//a[@class='size-component__square' and text()='{clicks_size}']")
        sleep(5)

        if not desired_size:
            raise ValueError('BUG:\n\n Checkbox not found!')

        desired_size.click()
        sleep(5)

        desired_color = context.browser.find_element_by_xpath(f"//span[@class='clipped' and text()='{clicks_color}']/parent::a")
        sleep(5)

        if not desired_color:
            raise ValueError('BUG:\n\n Checkbox not found!')

        desired_color.click()
        sleep(5)


@step('Apply the following filters')
def filters_from_table(context):
    for filter in context.table.rows:
        header = filter['Items']
        checks_label = filter['value']


        desired_checkbox=context.browser.find_element_by_xpath(f"//li[@class='x-refine__main__list '][.//h3[text()='{header}']]//div[@class='x-refine__select__svg'][.//span[contains(text(),'{checks_label}')]]//input")
        sleep(5)
        special_char=f"//li[@class='x-refine__main__list '][.//h3[text()=\'Let's\']]"

        if not desired_checkbox:
            raise ValueError('BUG:\n\n Checkbox not found!')

        sleep(2)
        desired_checkbox.click()
        sleep(5)


