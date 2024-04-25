# 메일로 전송을 시켜주는 자동화 프로그램 구성
# 1. 주식 2. 뉴스 3. 날씨

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# selenium 은 자동화프로그램

browser = webdriver.Chrome()
url = "https://www.naver.com"

# 브라우저 페이지를 열기
browser.get(url)

# 네이버 로그인 버튼을 클릭
# 로그인 : a, class, MyView-module__link_login___HpHMW
elem = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')
elem.click() # 로그인페이지로 넘어옴
time.sleep(3) # 확인용
browser.back() # 뒤로가기 browser.forward() 앞으로 가기 
browser.refresh() # 새로고침 F5





# 네이버 검색부분에 검색어를 입력
#id = query
elem = browser.find_element(By.ID,'query') # id가 query인 요소 선택
elem # 선택되어 있는 elme 요소를 보여줌.
elem.click() 
elem.send_keys("주식")



time.sleep(100)

# soup = BeautifulSoup(browser.page_source, "lxml")



