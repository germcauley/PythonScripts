from selenium import webdriver
from selenium import *

def before_all(context):
    context.driver = webdriver.Chrome()

def after_all(context):
    context.driver.quit()
