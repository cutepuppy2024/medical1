import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 마우스를 이동할 때 쓸 수 있음
import pyautogui 


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accept-Language":"en-US,en;q=0.9,ko;q=0.8"}

url = 'https://flight.naver.com/'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# 마우스 이동
pyautogui.moveTo(100,500)

# 스크롤 이동
pyautogui.scroll(-500)

# 마우스 클릭
pyautogui.click()

# 마우스 더블클릭
pyautogui.doubleClick()

# 3초간 대기
pyautogui.sleep(3)

