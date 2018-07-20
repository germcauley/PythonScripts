import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import datetime,time,sys

class WWW_Test_Cases(unittest.TestCase):
    capabilities = None
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Remote(desired_capabilities=self.capabilities)
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

    def test_Share_Price_Widget_Date_Display(self):
        # CHECK CURRENT DATE IS DISPLAYED IN SHARE PRICE WIDGET
        self.driver.get("")
        widget = self.driver.find_element_by_class_name("c-two-col-widgets__col2")
        sharePrice_Header = widget.find_element_by_class_name("c-share-price-wdgt").find_element_by_class_name("c-share-price-wdgt__header")

        #-------------DATE SECTION-----------------
        date = sharePrice_Header.find_element_by_tag_name('span')
        # get month
        month = datetime.date.today().strftime("%B")
        # truncate
        month = month[:-1]
        # build current date string
        current_date = str(datetime.date.today().strftime("%d")) + " " + month + " " + str(
            datetime.date.today().strftime("%Y"))
        # date displayed in widget
        date_in_widget = str(date.get_attribute('innerHTML'))

        def widgetDateDisplay(date, widgetDate):
            if current_date in date_in_widget:
                return True
            else:
                return False
        Datechecker = widgetDateDisplay(current_date, date_in_widget)
        self.assertTrue(Datechecker)

    def test_Share_Price_Widget_Arrows_Display(self):
        #CHECK THAT ARROW CLASS IS PRESENT IN WIDGET
        # urls = ["
        self.driver.get("")
        # find widget
        widget_container = self.driver.find_element_by_class_name('c-two-col-widgets')
        widget = self.driver.find_element_by_class_name("c-two-col-widgets__col2")
        sharePrice_Header = widget.find_element_by_class_name("c-share-price-wdgt").find_element_by_class_name(
            "c-share-price-wdgt__header")
        sharePrice_Body = widget.find_element_by_class_name("c-share-price-wdgt").find_element_by_class_name(
            "c-share-price-wdgt__body")
        dublin_row = sharePrice_Body.find_element_by_class_name('dublin')
        london_row = sharePrice_Body.find_element_by_class_name('london')

        # -------------------------Dublin Stock arrow----------------
        dublin_stock_arrow = str(dublin_row.find_element_by_xpath('div[2]').find_element_by_tag_name('span').find_element_by_tag_name('i').get_attribute('class'))
        # --------------------------London Stock Arrow-------------------------
        london_stock_arrow = str(london_row.find_element_by_xpath('div[2]').find_element_by_tag_name('span').find_element_by_tag_name('i').get_attribute('class'))

        # -------CHECK THAT UP/DOWN ARROW CLASS DISPLAYS for Dublin and London markets
        def arrow_present(stock_arrow_class):
            if "fa-arrow-down" in stock_arrow_class:
                return True
            elif "fa-arrow-up" in stock_arrow_class:
                return True
            else:
                return False

        self.assertTrue(arrow_present(dublin_stock_arrow))
        self.assertTrue(arrow_present(london_stock_arrow))

    def test_Share_Price_Widget_Price_Display(self):
        self.driver.get("")
        # find widget
        widget = self.driver.find_element_by_class_name("c-two-col-widgets__col2")

        sharePrice_Body = widget.find_element_by_class_name("c-share-price-wdgt").find_element_by_class_name("c-share-price-wdgt__body")
        dublin_row = sharePrice_Body.find_element_by_class_name('dublin')
        london_row = sharePrice_Body.find_element_by_class_name('london')

        # -------------------------Dublin Price and name----------------------
        dublin_price_text = dublin_row.find_element_by_xpath('div[1]').find_element_by_class_name('c-share-price-wdgt__value')
        dublin_price_text = str(dublin_price_text.get_attribute('innerHTML')[1:])

        # --------------------------London Price and name ----------------
        london_price_text = london_row.find_element_by_xpath('div[1]').find_element_by_class_name('c-share-price-wdgt__value')
        london_price_text = str(london_price_text.get_attribute('innerHTML')[1:])

        # ----CHECK THAT PRICE TEXT ELEMENTS CAN BE PARSED TO FLOAT
        assert float(london_price_text)
        assert float(dublin_price_text)

    def te
        self.driver.get("")
        # find widget
        widget = self.driver.find_element_by_class_name("c-two-col-widgets__col2")
        sharePrice_Body = widget.find_element_by_class_name("c-share-price-wdgt").find_element_by_class_name("c-share-price-wdgt__body")
        dublin_row = sharePrice_Body.find_element_by_class_name('dublin')
        london_row = sharePrice_Body.find_element_by_class_name('london')

        # -------------------------Dublin Price and name----------------------
        dublin_price_text = dublin_row.find_element_by_xpath('div[1]').find_element_by_class_name('c-share-price-wdgt__value')
        dublin_stock_name = str(dublin_row.find_element_by_xpath('div[1]').find_element_by_class_name('c-share-price-wdgt__stockmarket').get_attribute('innerHTML'))
        dublin_price_text = str(dublin_price_text.get_attribute('innerHTML')[1:])

        # --------------------------London Price and name ----------------
        london_price_text = london_row.find_element_by_xpath('div[1]').find_element_by_class_name('c-share-price-wdgt__value')
        london_stock_name = str(london_row.find_element_by_xpath('div[1]').find_element_by_class_name('c-share-price-wdgt__stockmarket').get_attribute('innerHTML'))

        expectedDub = "Dublin BIRG"
        expectedLon = "London BIRG"
        self.assertEqual(dublin_stock_name,expectedDub)
        self.assertEqual(london_stock_name,expectedLon)

    def test_Search(self):
        #TEST THAT CARDS IS DISPLAYE ON SEARCH RESULTS PAGE
        self.driver.get("")
        self.search_field=self.driver.find_element_by_class_name("c-mm-condensed__search-form-input")
        self.search_field.click()
        self.search_field.send_keys("cards")
        self.search_field.send_keys(Keys.ENTER)

        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "heroRegion"))
        )
        expected = "e"  # need correct url here once code is on stg and live
        actual = self.driver.current_url
        print(actual)
        self.assertEqual(expected,actual,'Error, urls are not equal :'+actual)


    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    WWW_Test_Cases.capabilities = {
        "browserName": sys.argv[1],
        "platform": sys.argv[2],
    }
    del sys.argv[1:]
    unittest.main()
