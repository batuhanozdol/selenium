# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:05:36 2019

@author: Batuhan
"""

from selenium import webdriver
import time
import random

browser = webdriver.Chrome("C:/Users/CEM/Downloads/chromedriver_win32/chromedriver.exe")
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
pagecount=1
entry = []

while pagecount <=10:
    randompage = random.randint(1,1290)
    newurl = url + str(randompage)
    browser.get(newurl)
    elements = browser.find_element_by_css_selector(".content")
    for element in elements:
        entry.append(element.text)
    time.sleep(5)
    pagecount +=1
      
with open("entries.txt","w",encoding="UTF-8") as file:
    for ent in entry:
        file.write(ent+"\n")
"""browser.get(url)
# bu sadece bir sayfadaki butun entryleri toplamak için olur
time.sleep(5)

# inspect yaptığımız zaman entryler için classın content olduğunu görürüz
elements= browser.find_element_by_css_selector(".content")

for element in elements:
    print("******")
    print(element.text) # içindekini almak için text yaparız <>text</>
"""
browser.close()

