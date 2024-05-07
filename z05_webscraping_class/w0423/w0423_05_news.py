import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# # selenium 은 자동화프로그램
# browser = webdriver.Chrome()
# url = "https://news.naver.com/main/ranking/popularDay.naver"
# # 브라우저 페이지를 열기
# browser.get(url)
# soup = BeautifulSoup(browser.page_source,"lxml")

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

officeCard = soup.find("div",{"class":"_officeCard _officeCard0"})
ranks = officeCard.find_all("div",{"class":"rankingnews_box"})
print("개수 :", len(ranks))

for rank in ranks:
    lis = rank.find_all("li")
    print("제목 :", lis[0].find("a",{"class":"list_title"}).text)
    print("li 개수 :" , len(lis))
    print("-"*40)




# news_list = soup.find("ul",{"class":"rankingnews_list"})
# lis = news_list.find_all("li")

# for i,li in enumerate(lis[0:5]):
#     print("순위 :", li.find("em",{"class":"list_ranking_num"}).text)
#     print("제목 :", li.find("a",{"class":"list_title nclicks('RBP.rnknws')"}).text)
#     print("이미지링크 :", li.find("a",{"class":"list_img nclicks('RBP.rnknws')"})["href"])


