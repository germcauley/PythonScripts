import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class WWW_Test_Cases(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.title


    def test_PageLoad(self):
        self.driver.get("")

        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        self.assertTrue(element, 'Cannot locate')

    def test_Mega_Menu_Access(self):
        #Hover each section in MM and assert the mm displays for all li elements
        self.driver.get("")

        element = self.driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[2]')
        element2 = self.driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[3]')
        element3 = self.driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[4]')
        element4 = self.driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[5]')

        element_array = [element, element2, element3, element4]

        #Display megaMenu for each header
        def display_menu():
            try:
                for item in element_array:
                    hov = ActionChains(self.driver).move_to_element(item)
                    hov.perform()
                    time.sleep(1)
                return True
            except:
                return False

        self.assertTrue(display_menu(), 'Something went wrong')

    def test_Mega_Menu_Display(self):

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
