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

time.sleep(1)
# // 전체문서 b
# 출발지 선택
elem = browser.find_element(By.XPATH,'//b[text()="ICN"]')
time.sleep(1)
elem.click()

# 국내부분 클릭
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(2)

# 김포국제공항 선택
elem = browser.find_element(By.XPATH,'//i[contains(text(),"김포국제공항")]')
elem.click() 
time.sleep(2)

# 도착지 선택
elem = browser.find_element(By.XPATH,'//b[text()="도착"]')
time.sleep(1)
elem.click()

# 국내부분 클릭
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(2)

# 제주국제공항 선택
elem = browser.find_element(By.XPATH,'//i[contains(text(),"제주국제공항")]')
elem.click()

# 가는날 부분 선택
elem = browser.find_element(By.XPATH,'//button[text()="가는 날"]').click()
time.sleep(1)

# 가는날짜 선택
elem = browser.find_elements(By.XPATH,'//b[text()="14"]')
print("14일의 개수 :",len(elem))
time.sleep(1)
elem[1].click()

# 오는날짜 선택
elem = browser.find_elements(By.XPATH,'//b[text()="15"]')
print("15일의 개수 :",len(elem))
time.sleep(1)
elem[1].click()

# 인원수 선택
browser.find_element(By.XPATH,'//button[contains(text(),"성인")]').click()
time.sleep(1)

# 1명 추가 선택
browser.find_element(By.XPATH,'//button[@class="searchBox_outer__9n6IB"]').click()
time.sleep(1)

# 인원선택창 닫기
browser.find_element(By.XPATH,'//span[contains(text(),"항공권 검색")]').click()

# 항공권 검색 선택
browser.find_element(By.XPATH,'//span[contains(text(),"항공권 검색")]').click()

# 대기시간
# time.sleep(7)
elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="domestic_Flight__sK0eA"]')))
print(elem)
print(elem[0].text)

# 화면 스크롤 내리기
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 : ", prev_height)

while True:
    browser.execute_script("window.strollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    
    curr_height = browser.execute_script("return document.body.scrollHeight")
    
    if prev_height == curr_height :
        break
    
    print("현재 높이 :",curr_height)
        

# 웹스크래핑을 하면 됨

soup = BeautifulSoup(browser.page_source,'lxml')
with open("flight.html","w",encoding="utf8") as f:
    f.write(soup.prettify())
    
input("Enter키를 입력하면 프로그램을 종료합니다.")

browser.quit()


# 실제구문 1개 가져오기
# elem = browser.find_element(By.XPATH,'//i[text()="김포국제공항"]')

# 실제구문 여러개 가져오기
# elem = browser.find_elements(By.XPATH,'//b[text()="15"]')

# 문자열과 일치할 때 선택방법
# elem = browser.find_element('//i[text()="김포국제공항")]')
# 문자열이 포함되어 있을 때 선택방법
# elem = browser.find_element('//i[contains(text(),"김포국제공항")]')
# id를 가지고 선택방법
# elem = browser.find_element('//i[@id ="_next"]')
# class를 가지고 선택방법
# elem = browser.find_element('//class[@id ="_next"]')


