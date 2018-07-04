# Open Personal Banking homepage
# Verify mega menu sections
# Life Moments section is displayed in mega menu
from selenium import webdriver
import time, os, sys, unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#need to refactor these and use POM as quite a bit of locators duplicaiton etc

class Life_Moments_Navigation(unittest.TestCase):
    @classmethod#only run on the class instead of method
    # set up driver
    def setUpClass(inst):
        # create a Firefox session
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get('https://stg.bankofireland.com/')
        #inst.driver.get('https://personalbanking.bankofireland.com/life-moments/lifestyle/getting-married/')
        inst.driver.title


    # #Test that Life Moments is displayed
    # def test_LifeMoments_display_in_MM(self):
    #     # Life Moments section displays
    #     LM_element = self.driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[4]/a')
    #     actual= LM_element.get_attribute('innerHTML')
    #     expected = 'Life Moments'
    #     self.assertEqual(actual, expected)#assert that 'Life Moments' is displayed
    #
    #
    # #Test that certain content is displayed
    # def test_Mega_Menu_Content(self):
    #     #Hover Life Moments
    #     LM_element = self.driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[4]/a')
    #     hov = ActionChains(self.driver).move_to_element(LM_element)
    #     hov.perform()
    #     time.sleep(2)
    #     LM_element.click()
    #     GM_element = self.driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[4]/div/div/div/div[1]/ul/li[1]')
    #     hov2 = ActionChains(self.driver).move_to_element(GM_element)
    #     hov2.perform()
    #     a_element = GM_element.find_element_by_tag_name('a')
    #     GM_actual = a_element.get_attribute('text')
    #     GM_expected = "Getting married"
    #     # Verify contents 'Getting Married'
    #     self.assertEqual(GM_actual, GM_expected)


    #Click Getting married redirects to
    def test_Click_Getting_Married_and_Redirect_and_breadcrumb(self):
        LM_element = self.driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[4]/a')
        hov = ActionChains(self.driver).move_to_element(LM_element)
        hov.perform()
        time.sleep(2)
        LM_element.click()
        GM_element = self.driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[4]/div/div/div/div[1]/ul/li[1]')
        hov2 = ActionChains(self.driver).move_to_element(GM_element)
        hov2.perform()
        a_element = GM_element.find_element_by_tag_name('a')
        text = a_element.get_attribute('text')
        print(text)
        a_element.click()
        # driver.quit()
        time.sleep(8)

        body = self.driver.find_element_by_css_selector('body')
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

        # wait for page to load and assert url is as expected
        # try:
        #     WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        #     print("Page is ready!")
        # except TimeoutException:
        #     print("Loading took too much time!")

        #test urls
        getting_married_url = 'https://personalbanking.bankofireland.com/life-moments/lifestyle/getting-married/'
        actual_gm_url = str(self.driver.current_url)
        print('Comparing : '+ getting_married_url, actual_gm_url)
        # try:
        #     self.assertEqual(getting_married_url,actual_gm_url, 'Urls do not match!')
        # except:
        #     print('Failure')


        # Drill down to breadcrumbs
        breadcrumb = self.driver.find_element_by_id('page').find_element_by_id('content').find_element_by_id(
            'life-moments-articles').find_element_by_css_selector('div:nth-child(2)'). \
            find_element_by_class_name('c-life-moments-breadcrumb').find_element_by_tag_name('div')


        # set breadcrumb elements
        homepage = breadcrumb.find_element_by_css_selector('li:nth-child(1)').find_element_by_tag_name(
            'a').get_attribute('text')
        life_moments = breadcrumb.find_element_by_css_selector('li:nth-child(2)').find_element_by_tag_name(
            'a').get_attribute('text')
        lifestyle = breadcrumb.find_element_by_css_selector('li:nth-child(3)').find_element_by_tag_name(
            'a').get_attribute('text')
        getting_married = breadcrumb.find_element_by_css_selector('li:nth-child(4)').find_element_by_tag_name(
            'a').get_attribute('text')

        # define test data
        home = 'Home'
        lm = 'Life Moments'
        ls = 'Lifestyle'
        gm = 'Getting Married'

        self.assertEqual(homepage.strip(), home)
        self.assertEqual(life_moments.strip(), lm)
        self.assertEqual(lifestyle.strip(), ls)
        self.assertEqual(getting_married.strip(), gm)





    @classmethod
    def tearDownClass(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

