import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# selenium 은 자동화프로그램
browser = webdriver.Chrome()
url = "https://finance.naver.com/"

# 브라우저 페이지를 열기
browser.get(url)
time.sleep(3)
# elem = browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[6]/a') # 주식 아이콘 위치점
# elem.click()
# time.sleep(3)
elem = browser.find_element(By.XPATH,'//*[@id="container"]/div[2]/div/div[3]/a/em') # 더보기 위치점
elem.click()
time.sleep(3)
soup  = BeautifulSoup(browser.page_source,"lxml")
print(soup.prettify())
with open("stock.html","w",encoding="utf8") as f:
    f.write(soup.prettify())
time.sleep(100)