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

for year in range(2020,2024):
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    browser.get(url)

    soup = BeautifulSoup(browser.page_source,'lxml')

    with open('daum_moive.html',"w",encoding='utf8') as f:
        f.write(soup.prettify())

    # 역대관객순 2023,2022,2021,2020까지
    # 이미지, 제목, 누적관객수, 날짜

    movie_lists = soup.find("ul",{"class":"c-list-basic ty_flow35"})
    lis = movie_lists.find_all("li")
    # print("영화개수 :",len(lis))

    for i,li in enumerate(lis):
        print(" [ ",year,"년도",i+1,"번째 영화 ]")
        title = li.find("strong",{"class":"tit-g clamp-g"}).text
        print("제목 :",title)
        
        img = li.find("img")["src"]
        # 이미지저장
        with open(f"daum_moive_{year}_{i}.html","wb") as f:
            re_img = requests.get(img)
            f.write(re_img.content)
        
        print("이미지 :",img)
        
    
        audience = li.find("p",{"class":"conts-desc clamp-g"}).text[3:-3].replace(",","")
        audience = int(audience)
        print("누적관객수 :",audience)
        
        ddate = li.find("span",{"class":"conts-subdesc clamp-g"}).text[:-2].strip().replace(".","/")
        print("날짜 :",ddate)

        sql = f"insert into daum_movie values (daum_movie_seq.nextval, '{title}', '{img}', {audience}, '{ddate}')"
        cursor.execute(sql)
        print("-"*50)

cursor.execute("commit")
cursor.close()
conn.close()

# 콘솔창에 출력하고 db에 저장
# daum_movie 테이블
# dno시퀀스, title 문자(100), img 문자(100), 누적관객수 숫자(10), 날짜(10)

# sql = "insert into score values(:1,:2,:3,:4)"
# cursor.execute(sql,(name,gender,addr,tel))