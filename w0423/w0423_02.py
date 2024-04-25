from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

# selenium 정보 가져오기
browser = webdriver.Chrome()
browser.get("https://comic.naver.com/bestChallenge")
time.sleep(3)
soup = BeautifulSoup(browser.page_source, "lxml")
# with open("webtoons2.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print("완료")

# requests 정보 가져오기
# url = "https://comic.naver.com/bestChallenge"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

# with open("webtoons1.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
    
# print("완료")


# browser = webdriver.Chrome()
# browser.get("http://www.naver.com/")

# time.sleep(10)

# elem = browser.find_element("MyView-module__link_login___HpHMW")
# elem
# elem.click()


ul_box = soup.find("ul",{"class":"AsideList__content_list--FXDvm AsideList__challenge--HeKuU"})
# print(ul_box)

lis = ul_box.find_all("li")
# print(len(lis))


for i,li in enumerate(lis):
    print("[ ",i ,"번째 작품 ]")
    w_rank = li.find("strong",{"class":"AsideList__ranking--sNPZy"}).text
    title = li.find("span",{"class":"text"}).text
    writer = li.find("a",{"class":"ContentAuthor__author--CTAAP"}).text
    print("등수 : ", w_rank)
    print("제목 : ", title)
    print("작가 : ", writer) 
    img_url = li.find("img",{"class":"Poster__image--d9XTI"})['src']
    print("이미지링크 : ",img_url)
    img_poster = requests.get(img_url,headers=headers)
    # 이미지파일 저장방법
    with open("webtoons_{}.jpeg".format(w_rank),"wb") as f:
        f.write(img_poster.content)
    
    print("-"*40)
        


        
