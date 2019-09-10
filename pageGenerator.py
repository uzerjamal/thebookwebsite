import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

baseUrl = 'https://manojpurohitcsharp2019.blogspot.com/'
driver = webdriver.Firefox()
driver.get(baseUrl)

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(3)
    
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    # break condition
    if new_height == last_height:
        break
    last_height = new_height