import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
url = "https://watcha.com/browse/webtoon"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# < 화면 스크롤내리기 >
# 현재 스크롤 높이 검색
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초높이 : ", prev_height)

# 스크롤 이동
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight")
    time.sleep(2)
    # 재조정된 스크롤 높이
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    
    prev_height = curr_height
    print("현재높이 :", curr_height)

# 데이터 찾기
soup = BeautifulSoup(browser.page_source,"lxml")
sections = soup.find_all("section",{"class":"custom-11ytuur e1134x5i3"})
print("section 개수 :", len(sections))
uls = sections[14].find("ul",{"class":"evjjsye0 custom-plh92q-Row e8ldpmn0"})
lis = uls.find_all("li",{"class":"w_exposed_cell e1bnpttb3 custom-vnoe9g-RowItem etpnybg1"})
print("li 개수 :", len(lis))

conts = lis[0].find("img")
print("제목 :",conts["alt"])

input("Enter키 입력시 프로그램이 종료됩니다. >>")

# 화면 닫기
browser.quit()



         
    

# < 정리 >

# 셀레늄
# elem = browser.find_element(By.CLASS_NAME,"custom-11ytuur e1134x5i3")) # section
# elem = browser.find_element(By.XPATH,"//*[@id="root"]/div[1]/main/div/section[17]/div[2]/ul/li[1]/div/a/div/div")
# elem = browser.find_element("//a[text()=""])
# elem = browser.find_element("//i[content(text,"")])

# 웹스크래핑 
# find("a",{"class":"custom-4zleql e1bnpttb2"})
# find("section",{"class":"custom-11ytuur e1134x5i3"})
# find("ul",{"class":"evjjsye0 custom-plh92q-Row e8ldpmn0"}))




