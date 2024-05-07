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

page = 1
for page in range(1,4):

    url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"

    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)

    # 제목, 이미지, 금액, 평점, 평가수

    soup = BeautifulSoup(browser.page_source,'lxml')

    notebook_box = soup.find("ul",{"id":"productList"})
    
    lis = notebook_box.find_all("li")
    # print("1페이지의 노트북 개수 :", len(lis))  # 65개

    for i, li in enumerate(lis):
        print("[",i+1,"번째 노트북 ]")

        title = li.find("div",{"class":"name"}).text.strip()  
        print("제목 :",title)

        img = li.find("img")["src"]
        print("이미지 :",img)

        price = li.find("strong",{"class":"price-value"}).text.replace(",","")
        price = int(price)
        print("금액 :",price)
        

        if li.find("em",{"class":"rating"}) == None: 
            grade = 0
            print("평점 :",grade)
            eval_num = 0
            print("평가자수 :",eval_num )
        else:  
            grade = li.find("em",{"class":"rating"}).text
            grade = float(grade)
            print("평점 :",grade)
            eval_num = li.find("span",{"class":"rating-total-count"}).text[1:-1]
            eval_num = int(eval_num)
            print("평가자수:",eval_num) 
            

        sql = f"insert into coupang values(coupang_seq.nextval,'{title}','{img}',{price},{grade},{eval_num})"
        cursor.execute(sql)
        print("-"*50)
    cursor.execute("commit")    
    cursor.close()
    conn.close()
    # 콘솔에 출력하고, db에 저장하시오.

    # prev_height = browser.execute_script("return document.body.scrollHeight")
    # while True:
    #     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        
    #     curr_height = browser.execute_script("return document.body.scrollHeight")
        
    #     if prev_height ==  curr_height:
    #         break