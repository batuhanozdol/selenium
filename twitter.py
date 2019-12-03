# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 19:50:06 2019

@author: Batuhan
"""

from selenium import webdriver
import loginInfo
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:/Users/CEM/Downloads/chromedriver_win32/chromedriver.exe")

browser.get("https://twitter.com/")
time.sleep(3)

giris_yap = browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/div[1]/a")
giris_yap.click()

time.sleep(3)

inp = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
password = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")
inp.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

login = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
login.click()

time.sleep(5)

arama_text = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
arama_text.send_keys("#sigarayazam"+ Keys.ENTER)
time.sleep(3)
arama_text.click()
time.sleep(5)     
"""
# 3 saniyede bir scroll yapma 
lenPage = browser.execute_async_script("window.scrollTo(0,document.body.scrollHeight);var lenPage=document.body.scrollHeight;return lenPage;")
match = False
while(match == False):
    lastcount = lenPage
    time.sleep(3)
    lenPage = browser.execute_async_script("window.scrollTo(0,document.body.scrollHeight);var lenPage=document.body.scrollHeight;return lenPage;")
    if lastcount == lenPage:
        match = True
time.sleep(3)

tweetler = []
#tweets = browser.find_elements_by_css_selector(".css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0")
tweets = browser.find_elements_by_xpath(".//span[@class = 'css-901oao']")
for tweet in tweets:
    tweetler.append(tweet)

with open("tweets.txt",'w',encoding = "UTF_8") as file:
    for tweet in tweetler:
        file.write(tweet+"\n")
        file.write("******* \n")
        
kalpler = browser.find_elements_by_css_selector(".r-4qtqp9.r-yyyyoo.r-1xvli5t.r-dnmrzs.r-bnwqim.r-1plcrui.r-lrvibr.r-1hdv0qi")
for kalp in kalpler:
    try:
        kalp.click()
        time.sleep(2)
    except Exception:
        print("Problem")"""
browser.close()



