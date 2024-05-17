import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import pandas as pd

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accept-Language":"en-US,en;q=0.9,ko;q=0.8"}

browser = webdriver.Chrome()
browser.maximize_window()

a1m_lists = {}

years = []
titles = []
viewers = []
ratings = []


for year in range(2019,2024):
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    browser.get(url)
    years.append(year)

    soup = BeautifulSoup(browser.page_source,'lxml')

    movie_lists = soup.find("ul",{"class":"c-list-basic ty_flow35"})
    # print(movie_lists)
    lis = movie_lists.find_all("li")
    # print(len("li"))

    title = lis[0].find("strong",{"class":"tit-g clamp-g"}).text
    titles.append(title)
    print("영화제목 : ", title)

    viewer= lis[0].find("p",{"class":"conts-desc clamp-g"}).text[3:-3].replace(",","")
    viewer = int(viewer)
    viewers.append(viewer)
    print("관객수 : ",viewer)

    elem = browser.find_element(By.CLASS_NAME,'thumb_bf')
    elem.click()
    time.sleep(2)

    soup = BeautifulSoup(browser.page_source,'lxml')
    rating = soup.find("span",{"class":"gem-star-point"}).text[2:-8]  
    ratings.append(rating)
    # rate = float(rate)
    print("평점 :",rating)
    
    
a1m_lists['year'] = years
a1m_lists['title'] = titles
a1m_lists['viewer'] = viewers
a1m_lists['ratings'] = ratings

print(a1m_lists)

m_table = pd.DataFrame(a1m_lists)

print(m_table)







