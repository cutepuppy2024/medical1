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

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accept-Language":"en-US,en;q=0.9,ko;q=0.8"}

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://www.yanolja.com/search/%ED%98%B8%ED%85%94?keyword=%ED%98%B8%ED%85%94&searchKeyword=%25ED%2598%25B8%25ED%2585%2594"
browser.get(url)
time.sleep(2)

# 1. 야놀자 홈페이지 이동
# elem = browser.find(By.CLASS_NAME,'gLFyf')
# elem.send_keys("야놀자")
# elem.click()
# time.sleep(2)

# 2. 호텔입력
# elem = browser.find(By.CLASS_NAME,'HomeSearchBar_searchBoxPlaceholder__3_zPf')
# elem.click()
# elem.send_keys("호텔")
# time.sleep(2)

# 3. 날짜 선택 후 6월 5일, 6일 클릭
elem = browser.find(By.XPATH,'//td[text()="5"]')
elem.click()
elem = browser.find(By.XPATH,'//td[text()="6"]')
elem.click()
time.sleep(2)

# 4. 확인버튼
elem = browser.find(By.CLASS_NAME,'//button[text()="확인"]')
elem.click()
time.sleep(2)

# 5. 검색창 클릭 > enter키 입력
# 6. 검색 진행
elem = browser.find(By.CLASS_NAME,'SearchInput_button__tUMEN SearchInput_buttonSubmit__3D83k')
elem.click()
time.sleep(2)


# 7. 스크롤 이동 반복

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollT0(0,document.body,scrollHeight)")
    curr_height = browser.execute_script("return document.body.scrollHeight")
    
    if prev_height == curr_height:
        break
    
    print("현재 스크롤위치 :", curr_height)
    
    
# 8. 정보창이 띄워지면 이미지, 제목, 평점, 평가수, 금액 저장하시오

soup = BeautifulSoup(browser.page_source,'lxml')

with open("yanolja.html","w",encoding="utf8") as f:
    f.write(soup.prettify())
   
hotel_lists = soup.find_all("div",{"class":"PlaceListItemText_container__fUIgA text-unit"})
print(len(hotel_lists))

for i, hotel in enumerate(hotel_lists):
    img = hotel.find("div",{"class":"PlaceListImage_imageText__2XEMn"})["style"]
    loc = img.find("http")
    print("이미지 링크 :",img[loc:-3])
    
    title = hotel.find("strong",{"class":"PlaceListTitle_text__2511B"}).text
    print("제목 :",title)
    
    grade = hotel.find("span",{"class":"PlaceListScore_rating__3Glxf"}).text
    grade = float(grade)
    print("평점 :",grade )
    
    grade_num = hotel.find("span",{"class":"PlaceListScore_reviewInfo__3QSCU"}).text[1:-1].replace(",","")
    grade_num = int(grade_num)
    print("평가자수 :",grade_num )
    
    price = hotel.find("div",{"class":"PlacePriceInfoV2_bottomInfo__2h62q"}).text[:-2].replace(",","")
    
    if type(price) == str:
        price = 0
    else:
        price = int(price)
    
    print("금액 :",price) 
    print("-"*50)
    
    # yanolja테이블
    # yno,img,title,grade, grade_num, price

    sql = f"insert into yanolja values (yanolja_seq.nextval,'{img}',{grade},{grade_num},{price})"
    cursor.execute(sql)
    print("-"*50)
    
cursor.execute("commit")  
cursor.close()
conn.close()
    


# url = ""
# url[28:]
# loc = url.find("http")
# print("위치값 :", loc)

# print(url[loc:])