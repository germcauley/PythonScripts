#A simple script that logs into facebook and checks that the facebook logo is displayed
#Gerald McAuley 2017

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://facebook.com/")

    #Main section,locates elements and populates them where necessary
    def test_Login(self):
        driver = self.driver
        #put you account name and password in the relevant fields below
        faceBookUserName ="InsertUserNameHere"
        faceBookPassword = "InsertPasswordHere"
        emailFieldID = "email"
        passFieldID ="pass"
        loginButtonXPath = "//input[@value = 'Log In']"
        fbLogoXpath = "(//a[contains(@href,'logo')])[1]"
        emailFieldElement = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id(emailFieldID))
        """webdriver wait 10 secs max for xxxxfield to display if yes it returns and saves in xxxxfield element if no it raises timeout exception"""
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXPath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(faceBookUserName)
        passFieldElement.clear()
        passFieldElement.send_keys(faceBookPassword)
        loginButtonElement.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))


    def tearDown(self):
        self.driver.quit()
        print("test has run successflly!")


if __name__ == '__main__': """run test using default unittest runner"""
unittest.main()