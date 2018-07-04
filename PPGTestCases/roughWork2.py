from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time,bs4
from bs4 import BeautifulSoup

driver = webdriver.Firefox()

driver.get('https://personalbanking.bankofireland.com/life-moments/lifestyle/getting-married/')

body = driver.find_element_by_css_selector('body')
body.send_keys(Keys.PAGE_DOWN)
time.sleep(2)

#Drill down to breadcrumbs
breadcrumb = driver.find_element_by_id('page').find_element_by_id('content').find_element_by_id('life-moments-articles').find_element_by_css_selector('div:nth-child(2)').\
    find_element_by_class_name('c-life-moments-breadcrumb').find_element_by_tag_name('div')

homepage = breadcrumb.find_element_by_css_selector('li:nth-child(1)').find_element_by_tag_name('a').get_attribute('text')
life_moments = breadcrumb.find_element_by_css_selector('li:nth-child(2)').find_element_by_tag_name('a').get_attribute('text')
lifestyle = breadcrumb.find_element_by_css_selector('li:nth-child(3)').find_element_by_tag_name('a').get_attribute('text')
getting_married = breadcrumb.find_element_by_css_selector('li:nth-child(4)').find_element_by_tag_name('a').get_attribute('text')


home = 'Home'
life_moments = 'Life Moments'
lifestyle = 'Lifestyle'
getting_married = 'Getting Married'


assert str(homepage)== home.strip(), 'The element text is :'+ str(homepage)
assert str(life_moments)== life_moments.strip(), 'The element text is :'+ str(life_moments)
assert str(lifestyle)== lifestyle.strip(), 'The element text is :'+ str(lifestyle)
assert str(getting_married)== getting_married.strip(), 'The element text is :'+ str(getting_married)




# soup = BeautifulSoup(breadcrumb, 'html.parser')
# print(soup.prettify())


# parent_div = main_div.find_element_by_xpath('/html/body/div[2]/section[1]/div[2]/div[2]')
# breadcrumb_div = parent_div.find_element_by_class_name('life-moments-breadcrumb').find_element_by_tag_name('div').find_element_by_tag_name('ul').get_attribute('text')
#

driver.quit()
