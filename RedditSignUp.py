from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()

driver.get('https://old.reddit.com/login?dest=https%3A%2F%2Fold.reddit.com%2Fmessage%2Funread%2F')





input_username = driver.find_element_by_id('user_reg')
input_username.send_keys('asdasd123123zxc')

input_password = driver.find_element_by_id('passwd_reg')
input_password.send_keys('1234hello')

input_password2 = driver.find_element_by_id('passwd2_reg')
input_password2.send_keys('1234hello')

input_email = driver.find_element_by_id('email_reg')
input_email.send_keys('')

time.sleep(3)


sign_up = driver.find_element_by_class_name('rc-anchor')

s1 = sign_up.find_element_by_class_name('rc-inline-block')
s2 = s1.find_element_by_class_name('rc-anchor-center-container')
s3 = s2.find_element_by_class_name('rc-anchor-checkbox-holder')

s3.click()
