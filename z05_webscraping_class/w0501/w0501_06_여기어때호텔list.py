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

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accept-Language":"en-US,en;q=0.9,ko;q=0.8"}

browser = webdriver.Chrome()
browser.maximize_window()

# for i in range(5):
url = f"https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-05-01&checkOut=2024-05-02&personal=2&freeForm=true&page=2"
browser.get(url)

soup = BeautifulSoup(browser.page_source,'lxml')

# 파일저장
# with open("y_hotels.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())

# 1개
# title = soup.find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"})
# print("호텔명 : ",title.text)
# hotel_box = soup.find("div",{"class":"css-1qumol3"})

hotel_lists = soup.find_all("a",{"class":"gc-thumbnail-type-seller-card css-wels0m"})
print("호텔리스트 개수 :",len(hotel_lists))  # 20개

# 복수개
for i, hotel in enumerate(hotel_lists):
    print("[",i+1,"번째 리스트 ]")
    
    # 1. 호텔명
    title = hotel.find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"})
    title = title.text
    print("1. 호텔명 : ",title)
    
    # 2. 지역
    try:
        region = hotel.find("span",{"class":"css-1rzfout"})
        region = region.text
        print("2. 지역 : ",region)  
    except:
        region = ""
        print(f"지역 {region}")
        
    # 3. 평점
    score = hotel.find("span",{"class":"css-9ml4lz"})
    score = float(score.text)
    print("평점 : ",score)
    
    # 4. 평가자수
    member = hotel.find("span",{"class":"css-oj6onp"})
    member = int(member.text[:-4].replace(",",""))
    print("평가자수 : ",member)   
    
    # 5. 이미지링크
    try:
        img = hotel.find("img")["src"]  
        print("이미지링크 : ",img)   
    except:
        img = ""
        print(f"이미지링크 : {img}")
       
    # 6. 가격
    try:
        price = hotel.find("span",{"class":"css-5r5920"})
        price = int(price.text.replace(",",""))
        print("가격 : ",price)
    except:
        price = 0
        print(f"가격 : {price}")

    
    sql = f"insert into yeogi values(yeogi_seq.nextval,'{title}','{region}',{score},{member},'{img}',{price})"
    cursor.execute(sql) 
print("-"*30)
cursor.execute('commit')  
cursor.close()
conn.close()

















