#!/usr/bin/env python

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import sys

try:
    val = float(input("Enter a value between 0 and 2: \n"))
except ValueError as e:
    print("Invalid input")
    sys.exit()

browser = webdriver.Chrome(executable_path=r"/usr/lib/chromium/chromedriver")
browser.get('https://10fastfingers.com/typing-test/english')
sleep(10) #to wait because of cloudflare implementation
html = browser.page_source
soup = BeautifulSoup(html,'html.parser')
try:
    words = (soup.find('div',{'id':'wordlist'}).text).split('|')
except AttributeError as e:
    print("Error, website could not load.")
    browser.quit()
    sys.exit()

for i in words:
    browser.find_element_by_id("inputfield").send_keys(i)
    browser.find_element_by_id("inputfield").send_keys(Keys.SPACE)
    sleep(val)
