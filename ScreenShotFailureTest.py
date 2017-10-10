#searches for latest news about 'stocks' and takes a screen shot

import unittest
from selenium import webdriver

class ScreenSotOnFailure(unittest.TestCase):
    def SetUp(self):
        self.driver = webdriver.Firefox()

    def test_example_1(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        try:
            driver.get('https://www.google.ie/search?biw=1280&bih=632&tbm=nws&q=stocks&oq=stocks&gs_l=psy-ab.3..0l4.3113.8765.0.9340.8.8.0.0.0.0.123.409.3j1.6.0....0...1.1.64.psy-ab..2.4.408.0...97.fKpNb97lzXs')
            driver.save_screenshot('screenie.png')
        except:
            print("Not successful")


    def tearDown(self):
        self.driver = webdriver.Firefox()
        self.driver.quit()


if __name__=="__main__":
    unittest.main()

