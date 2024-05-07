import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys



headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

url = "http://www.naver.com/"

browser = webdriver.Chrome()
browser.get(url)
elem = browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[6]/a')
elem.click()

# 새창으로 페이지 이동
browser.switch_to.window(browser.window_handles[1])

elem = browser.find_element(By.XPATH,'//*[@id="container"]/div[2]/div/div[3]/a')
elem.click()

time.sleep(100)
    
    