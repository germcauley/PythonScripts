from selenium import webdriver
import time

import csv
exampleFile = open('x.csv') #name of csv file
exampleReader =csv.reader(exampleFile)
exampleData=list(exampleReader)
i =0
errors =0

driver = webdriver.Chrome()

for row in exampleData:
    url = str(row[0])
    try:

        driver.get(url)
        for entry in driver.get_log("browser"):
            if entry['level'] == 'SEVERE':
                print(url)
                print(entry)
                print(" ")
                errors += 1
    except NameError:
        print("Error! " +url)
    # print(str(i)+" "+str(row[0]))
    i += 1

print("Finished")
