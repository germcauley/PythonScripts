from selenium import webdriver
import time
import os, sys
from selenium.webdriver.common.action_chains import ActionChains
from ScreenShotCompare import ScreenAnalysis
#set up driver
driver = webdriver.Firefox()

def TestMegaMenu(urls):
    ##########################NEED TO RUN ON STG AND LIVE
    for url in urls:
        driver.get(url)
        print('Running tests on '+ str(url))
        path = '/Users/gmcauley/PycharmProjects/PageObjectModelExample'
        #os.makedirs(path+url)
        #open window
        # driver.execute_script("window.open('https://twitter.com')")
        # print (driver.current_window_handle)

        #Mega menu
        mm = driver.find_element_by_class_name('c-mm-condensed__container').find_element_by_class_name('c-mm-condensed__top-items')

        lis = mm.find_elements_by_tag_name('li')
        #print(mm.get_attribute('innerHTML'))
        #item is the first part of menu under 'Products'
        #nth-child(x)  is the sub menu

        item=mm.find_elements_by_tag_name("ul > li")
        # item[2-11] give us all headings under Products

        # item=mm.find_elements_by_tag_name("ul > li:nth-child(1)")

        element = driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[2]')
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()

        time.sleep(2)
        # Display choices under Products
        for x in range(2,12):
            # print('PRINTING ITEM '+str(x)+ (item[x].get_attribute('innerHTML')))
            #print('PRINTING ITEM ' + str(x) + (item[x].get_attribute('innerHTML')))
            item[x].click()
            #TAKE SCREENSHOT

            try:
                driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),'screenshots','ProductsImage'+str(x)+'.png'))
                driver.get_screenshot_as_png()
                print("Done.")
                time.sleep(0.8)
            except:
                print('failure!')

        ######################################
        #Services hover
        Service_element = driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[3]')
        hov = ActionChains(driver).move_to_element(Service_element)
        hov.perform()
        # TAKE SCREENSHOT
        try:
            driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'screenshots','ServiceImage.png'))
            driver.get_screenshot_as_png()
            print("Done.")
            time.sleep(0.5)
        except:
            print('failure!')
        time.sleep(0.5)

        #Life Moments
        LM_element = driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[4]')
        hov = ActionChains(driver).move_to_element(LM_element)
        hov.perform()
        # TAKE SCREENSHOT
        try:
            driver.save_screenshot(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), 'screenshots', 'LifeMomentsImage.png'))
            driver.get_screenshot_as_png()
            print("Done.")
            time.sleep(0.5)
        except:
            print('failure!')
        time.sleep(1)
########REQUIRES REFACTOR####################
        #Way to Bank
        WTB_element = driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[5]')
        hov = ActionChains(driver).move_to_element(WTB_element)
        hov.perform()
        screenShot('WaysToBankImage1.png')
        menu_item2 = driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[5]/div/div[1]/ul/li[2]')
        menu_item2.click()
        screenShot('WaysToBankImage2.png')
        time.sleep(0.8)
        menu_item3 = driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[5]/div/div[1]/ul/li[3]/a')
        menu_item3.click()
        screenShot('WaysToBankImage3.png')
        time.sleep(0.8)

        ##############################

##Ways to bank screenshot

def screenShot(name):
     # TAKE SCREENSHOT
            try:
                driver.save_screenshot(
                    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'screenshots', name))
                driver.get_screenshot_as_png()
                print("Done.")
                time.sleep(0.5)
            except:
                print('failure!')
            time.sleep(0.5)





urls = ['https://stg.bankofireland.com/','https://stg.bankofireland.com/']
TestMegaMenu(urls)
driver.quit()


# CALL SCREENSHOT COMPARISON ON STG AND LIVE IMAGEs
THING = ScreenAnalysis('/Users/gmcauley/PycharmProjects/PageObjectModelExample/screenshots/ProductsImage2.png','/Users/gmcauley/PycharmProjects/PageObjectModelExample/screenshots/ProductsImage5.png')
THING.analyze()