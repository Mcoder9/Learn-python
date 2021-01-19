from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

browser = 'chrome'
if browser == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('Give the correct path of %s'%browser)
url = 'https://www.orangehrm.com/orangehrm-30-day-trial/'
driver.get(url)
#Facebook login
# driver.find_element_by_css_selector('div._6lux>input#email').send_keys('03059601725')
# driver.find_element_by_css_selector('div._6lux>input#pass').send_keys('fool_751')
# driver.find_element_by_css_selector('div._6ltg>button#u_0_b').click()

# url = 'https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html'
# Dropdown practice with Select
# day_ele = driver.find_element_by_css_selector('select.form-control') # get element
# for op in Select(day_ele).options: # loop and get options
#     print(op.text)

# url = 'https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html'
# Dropdown practice with xpath (without select)
# day_ele = driver.find_elements_by_xpath('//select[@id="select-demo"]/option') # get element
# for op in day_ele: # loop and get options
#     print(op.text)

# url = 'https://www.orangehrm.com/orangehrm-30-day-trial/'
# Generic method for dropdown
for_indus = driver.find_elements_by_xpath('//select[@id="Form_submitForm_Industry"]')
print(len(for_indus))
for option in for_indus:
    print(option.text)
    if option == 'Travel':
        option.click()
        break

