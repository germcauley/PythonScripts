# Use selenium to get the page and grab all the links and images from the page:
#Gerald McAuley 2017

import requests
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.politics.ie/")
#get all 'a' elements
links = driver.find_elements_by_css_selector("a")
#get all img elements
images = driver.find_elements_by_css_selector("img")


# Requests library, allow you t send http requests

#HTTP status codes
#200 – Valid Link
#404 – Link not found
#400 – Bad request
#401 – Unauthorized
#500 – Internal Error


#test all links in links list

length= len(links)
i = 0
while i < length:
    try:
        #print the link being tested
        print(links[i].get_attribute("href"))
        #print status code
        print(requests.options(links[i].get_attribute("href")))
    #error handling if the link isnt a valid url
    except:
        print("Not a valid link")
    i+=1


#Idea to expand upon script
#read from list:
# Page1,https://www.bankofireland.com
# Page2,https://www.bankofireland.com/about

#output to csv - Page1.csv
#In Page1.csv you would have: the href,the response code

#add image support



