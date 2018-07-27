from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest,datetime,time,sys,bs4

class WWW_Test_Cases(unittest.TestCase):
    #capabilities = None
    @classmethod
    def setUpClass(self):
        #self.driver = webdriver.Remote(desired_capabilities=self.capabilities)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.title

    def test_WWW_PageLoad(self):
        self.driver.get("https://www.com/")

        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        self.assertTrue(element, 'Cannot locate')

    def test_Mega_Menu_Access(self):
        #Hover each section in MM and assert the mm displays for all li elements
        self.driver.get("https://www.com/")

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
        self.assertTrue(display_menu())

    def test_Share_Price_Widget_Date_Display(self):
        # CHECK CURRENT DATE IS DISPLAYED IN SHARE PRICE WIDGET
        self.driver.get("https://www.com/")
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
        # urls = ["stg.com","www.com"]
        self.driver.get("https://www.com/")
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
        self.driver.get("https://www.com/")
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

    def test_Share_Price_Widget_Exchange_Display(self):
        # urls = ["stg.com","www.com"]
        self.driver.get("https://www.com/")
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

    def test_SearchResults(self):
        #TEST THAT SEARCH TERM IS DISPLAYED ON SEARCH RESULTS PAGE
        self.driver.get("https://www.com/")
        self.search_field=self.driver.find_element_by_class_name("c-mm-condensed__search-form-input")
        self.search_field.click()
        searchTerm= "cards"
        self.search_field.send_keys(searchTerm)
        self.search_field.send_keys(Keys.ENTER)
        #wait for next page to load
        element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "heroRegion")))
        searchResults = self.driver.find_element_by_class_name("search-results").find_element_by_tag_name('ul').find_elements_by_tag_name('a')
        def CheckForTermInResults(element):
            ans = False
            #can modify this to check any number of search results, currently only checks first result
            i = searchResults[0]
            txt = i.get_attribute('text').lower()
            if (searchTerm in txt):
                ans = True
            else:
                ans = False
            return ans
        self.assertTrue(CheckForTermInResults(searchResults))

    def test_SearchPageRedirect(self):
        #VERIFY SEARCH FROM HOMEPAGE REDIRECTS TO /search/
        self.driver.get("https://www.com/")
        self.search_field = self.driver.find_element_by_class_name("c-mm-condensed__search-form-input")
        self.search_field.click()
        searchTerm = "cards"
        self.search_field.send_keys(searchTerm)
        self.search_field.send_keys(Keys.ENTER)
        # wait for next page to load
        element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "heroRegion")))
        #time.sleep(3)
        domain = "/search/"
        searchPgUrl = self.driver.current_url
        result = False
        if domain in searchPgUrl:
            result =True
        print(searchPgUrl)
        self.assertTrue(result)

    def test_HC_Page_Load(self):
        self.driver.get("https://www.com/help-centre/")

        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        self.assertTrue(element, 'Cannot locate')

    def test_HC_Search_Function(self):
        # TEST THAT SEARCH TERM IS DISPLAYED ON HELP CENTRE SEARCH RESULTS PAGE
        self.driver.get("https://www.com/help-centre/")
        self.search_field = self.driver.find_element_by_class_name("js-cludo-search-input")
        self.search_field.click()
        searchTerm = "mortgage"
        self.search_field.send_keys(searchTerm)
        self.search_field.send_keys(Keys.ENTER)
        # wait for next page to load
        element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, "page")))
        searchResults = self.driver.find_element_by_class_name('search-results').find_element_by_id('cludo-search-results').find_element_by_class_name('search-results').find_elements_by_tag_name('h2')
        #firstRes = searchResults[0].find_element_by_tag_name('a').get_attribute('text').lower()

        def CheckForSearchTermInResults(element):
            ans = False
            # can modify this to check any number of search results, currently only checks first result
            i = searchResults[0]
            txt = i.find_element_by_tag_name('a').get_attribute('text').lower()
            if (searchTerm in txt):
                ans = True
            else:
                ans = False
            return ans

        self.assertTrue(CheckForSearchTermInResults(searchResults))

    def test_HC_Search_Redirect(self):
        # VERIFY SEARCH FROM HC REDIRECTS TO /help-centre/search
        self.driver.get("https://www.com/help-centre/")
        self.search_field = self.driver.find_element_by_class_name("js-cludo-search-input")
        self.search_field.click()
        searchTerm = "mortgage"
        self.search_field.send_keys(searchTerm)
        self.search_field.send_keys(Keys.ENTER)
        # wait for next page to load
        #element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "heroRegion")))
        time.sleep(3)
        domain = "/help-centre/search"
        searchPgUrl = self.driver.current_url
        result = False
        if domain in searchPgUrl:
            result = True
        self.assertTrue(result)

    def test_BL_Search_Suggestions_Present(self):
        term="Dublin"
        self.driver.get("https://www.com/branch-locator/")
        searchField = self.driver.find_element_by_class_name("c-search-branch")
        searchField.click()
        input = searchField.find_element_by_class_name("search")
        #need to delay input as react has difficulty processing rapid input events
        for char in term:
            input.send_keys(char)
            time.sleep(0.3)
        suggestions = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "c-search-branch__suggestions"))
        )
        self.assertTrue(suggestions, 'Cannot locate element')

    def test_BL_Search_Suggestions_Content(self):
        term = "dublin"
        result = True
        self.driver.get("https://www.com/branch-locator/")
        searchField = self.driver.find_element_by_class_name("c-search-branch")
        searchField.click()
        input = searchField.find_element_by_class_name("search")
        # need to delay input as react has difficulty processing rapid input events
        for char in term:
            input.send_keys(char)
            time.sleep(0.3)
        suggestions = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "c-search-branch__suggestions"))
        )
        li = suggestions.find_elements_by_tag_name('li')
        if term in li[0].get_attribute('innerHTML').lower():
            result =True
        else:
            result = False
        self.assertTrue(result)

    def test_BL_Verify_Map_Interactable(self):
        self.driver.get('https://www.com/branch-locator/')
        item = self.driver.find_element_by_class_name('gmnoprint')
        item.click()
        popup = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "c-gmap__infoWindow"))
        )
        self.assertTrue(popup)

    def test_BL_Navigate_To_Branch_Info_Page(self):
        self.driver.get('https://www.com/branch-locator/')
        item = self.driver.find_element_by_class_name('gmnoprint')
        item.click()
        popup = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "c-gmap__infoWindow"))
        )
        self.driver.find_element_by_class_name("c-gmap__infoWindow__see-more").click()
        h1 = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "hero__content-title"))
        )
        expectedUrl = "https://www.com/branch-locator/tuam"
        actual = self.driver.current_url
        self.assertEqual(expectedUrl,actual,'The urls d not match!')

    def test_BL_Check_Links_To_Other_Branches(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.com/branch-locator/")
        self.driver.find_element_by_class_name("site-content").click()
        time.sleep(1)
        zoom = ActionChains(self.driver).send_keys(Keys.SHIFT + "+")
        zoom.perform()
        time.sleep(3)
        markers = self.driver.find_elements_by_class_name("gmnoprint")
        count = 0
        # for item in markers:
        #     print(str(count) + " "+ item.get_attribute('title'))
        #     count +=1
        scrollTo = ActionChains(self.driver).move_to_element(markers[26])
        scrollTo.perform()
        time.sleep(3)
        markers[26].click()
        time.sleep(3)
        popup = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "c-gmap__infoWindow"))
        )
        self.driver.find_element_by_class_name("c-gmap__infoWindow__see-more").click()
        page = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "hero__content-title"))
        )
        link = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/section/section/div/div[1]/div/div[3]/span/div/div[1]/div[2]/article/div[4]/a")
        link.click()
        page2 = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "hero__content-title"))
        )
        expectedUrl = "https://www.com/branch-locator/sligo"
        actual = self.driver.current_url
        self.assertEqual(expectedUrl,actual,"The urls do not match!")




    @classmethod
    def tearDownClass(self):
        self.driver.quit()




if __name__ == '__main__':
    #Use the below code to call from command line
    #     # WWW_Test_Cases.capabilities = {
    #     #     "browserName": sys.argv[1],
    #     #     "platform": sys.argv[2],
    #     # }
    #     # del sys.argv[1:]
    unittest.main()
