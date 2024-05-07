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

# 순번(시퀀스), 순위, 변동 ,이미지, 곡제목, 뮤지션명, 좋아요수

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accept-Language":"en-US,en;q=0.9,ko;q=0.8"}

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(2)

# selenium
# browser.find_element(By.XPATH,'//span[text()="]')
# browser.find_element(By.XPATH,'//button[@class=""]')

soup = BeautifulSoup(browser.page_source,'lxml')

# 파일저장
# with open("melon.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())

melon_chart = soup.find("tbody")

# tr : 각 순위
trs = melon_chart.find_all("tr")
print("멜론차트의 노래개수 : ",len(trs))  # 100

# 1위 곡
# tds = trs[0].find_all("td")
# print(len(tds))  # 12개의 row

# print("순위 :",tds[1].find("span",{"class":"rank"}).text)
# print("변동 :",tds[2].find("span",{"class":"bullet_icons rank_static"}).text)
# print("이미지 :",tds[3].find("img")["src"])
# print("곡제목 :",tds[5].find("div",{"class":"ellipsis rank01"}).a.text)
# print("가수 :",tds[5].find("div",{"class":"ellipsis rank02"}).a.text)
# print("좋아요 수 :",tds[7].find("span",{"class":"cnt"}).text[3:])

# 복수개 찾기
for i, song in enumerate(trs):
    tds = trs[i].find_all("td")
    
    rank = int(tds[1].find("span",{"class":"rank"}).text)
    print("순위 :",rank)
    
    v_rank = tds[2].find("span")["title"]
    if v_rank == "순위 동일":
        v_rank = 0
        print("순위변동 :",v_rank)
    elif v_rank == "순위 진입":
        v_rank = 0
        print("순위변동 :",v_rank)    
    elif v_rank.find("상승") == 4:  # 숫자가 2자리인 경우는?
        v_rank = v_rank[:-5]
        v_rank = int(v_rank)
        print("순위변동 :",v_rank)
    elif v_rank.find("하락") == 4:
        v_rank = v_rank[:-5]
        v_rank = int(v_rank)*-1
        print("순위변동 :",v_rank)  
    else:
        print("순위변동 :",v_rank)
    
    img = tds[3].find("img")["src"]
    print("이미지 :",img)
    
    title = tds[5].find("div",{"class":"ellipsis rank01"}).a.text.replace("'","")
    print("곡제목 :",title)
    
    singer = tds[5].find("div",{"class":"ellipsis rank02"}).a.text
    print("가수 :",singer)
    
    likeNum = tds[7].find("span",{"class":"cnt"}).text[4:].strip().replace(",","")  # "none"으로 next_sibling 해도 됨
    likeNum = int(likeNum)
    print("좋아요 수 :",likeNum)
    
    sql = f"insert into melon values (melon_seq.nextval,{rank},{v_rank},'{img}','{title}','{singer}',{likeNum})"
    cursor.execute(sql)
    print("-"*50)
    
cursor.execute("commit")  
cursor.close()
conn.close()
    

    
