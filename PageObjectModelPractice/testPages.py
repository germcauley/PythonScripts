import unittest
from selenium import webdriver
from test1 import *
from locators import *
from selenium.webdriver.common.by import By

# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()
        self.driver.get("https://www.google.ie")

    def test_page_load(self):
        page = SimpleTest(self.driver)
        self.assertTrue(page.check_page_loads())

    def test_search_results(self):
        page = SimpleTest(self.driver)
        expected_url = "https://www.google.ie/search?source=hp&ei=9OWOWqj9A4qvgAa9xoLQDg&q=programming&oq=programming&gs_l=psy-ab.3..0j0i20i263k1j0j0i20i263k1j0l6.19608.19608.0.20396.4.2.0.0.0.0.346.346.3-1.1.0....0...1..64.psy-ab..3.1.342.0...0.NL9WBBwT3UA"
        self.assertTrue(page.search_item(),expected_url)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()