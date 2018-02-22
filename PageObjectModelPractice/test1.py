from search_pages_qa import Page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from locators import *

#separate class for tests?
class SimpleTest(Page):

    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)  # Python3 version

    def check_page_loads(self):
        return True if self.find_element(*self.locator.SEARCH) else False

    def search_item(self):
        self.find_element(*self.locator.SEARCH).send_keys("programming")
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        #return self.find_element(*self.locator.SEARCH_LIST).text
        return self.get_url()






