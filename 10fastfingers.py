#!/usr/bin/env python

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

val = float(input("Enter a value between 0 and 2: \n"))
browser = webdriver.Chrome(executable_path=r"/usr/lib/chromium/chromedriver")
browser.get('https://10fastfingers.com/typing-test/english')
html = browser.page_source
soup = BeautifulSoup(html,'html.parser')
words = (soup.find('div',{'id':'wordlist'}).text).split('|')
for i in words:
    browser.find_element_by_id("inputfield").send_keys(i)
    browser.find_element_by_id("inputfield").send_keys(Keys.SPACE)
    sleep(val)
