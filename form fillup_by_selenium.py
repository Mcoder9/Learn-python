from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

browser = 'firefox'
if browser == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('Give the correct path of %s' % browser)
url = 'https://www.seleniumeasy.com/test/drag-and-drop-demo.html'
driver.get(url)

'''# Facebook login'''
# driver.find_element_by_css_selector('div._6lux>input#email').send_keys('03059601725')
# driver.find_element_by_css_selector('div._6lux>input#pass').send_keys('fool_751')
# driver.find_element_by_css_selector('div._6ltg>button#u_0_b').click()


'''# Dropdown practice with Select'''
# url = 'https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html'
# day_ele = driver.find_element_by_css_selector('select.form-control') # get element
# for op in Select(day_ele).options: # loop and get options
#     print(op.text)


'''# Dropdown practice with xpath (without select)'''
# url = 'https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html'
# day_ele = driver.find_elements_by_xpath('//select[@id="select-demo"]/option') # get element
# for op in day_ele: # loop and get options
#     print(op.text)


'''# Generic method for dropdown'''
# url = 'https://jobs.tcs.com.pk/webresume/'
# def select_dropdown(option_list,value):
#     print(len(option_list))
#     for option in option_list:
#         if option.text == value:
#             option.click()
#             break
#         print(option.text)
# for_cont = driver.find_elements_by_xpath('//select[@id="ddlCurrCountry"]/option')
# select_dropdown(for_cont,'India')


'''# Generic method for Jquery dropdown'''
# url = 'https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/'
# def drop_down(option_list, value):
#     if not value[0] == 'all':
#         for option in option_list: # for getting options
#             print(option.text)
#             for i in range(len(value)): # for index of value_list
#                 if option.text == value[i]:
#                     option.click()
#                     break
#     else:
#         try:
#             for option in option_list:
#                 option.click()
#         except Exception as e:
#             print(e)
#
# value_list = ['choice 1','choice 2'] # list for select value
# driver.find_element(By.ID, 'justAnInputBox').click()
# ele = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
# drop_down(ele,value_list)

''' Context Menu/Right click'''
# ulr = 'https://swisnl.github.io/jQuery-contextMenu/demo.html'
# action_chain = ActionChains(driver)
# sources = driver.find_element(By.CSS_SELECTOR,'span.context-menu-one')
# action_chain.context_click(sources).perform()
# context_menu = driver.find_elements(By.CSS_SELECTOR,'li.context-menu-icon')
# for context in context_menu:
#     print(context.text)

''