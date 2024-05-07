# 기본복사

import requests
from bs4 import BeautifulSoup

url = "https://browse.auction.co.kr/list?category=22160000"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"en-US,en;q=0.9"}
res = requests.get(url,headers = headers)
res.raise_for_status()

# 데이터 불러오기
soup = BeautifulSoup(res.text,"lxml")

# print(soup.prettify())

# 파일저장
# with open("auction.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
    

# print(soup.find("div",{"class":"itemcard"}))

# items = soup.find_all("div",{"class":"section--itemcard"})
# itemdards = items.find_all()
# print(len(items)) # 100

items = soup.find("div",{"class":"section--itemcard"})
print("상품명 : ", items.find("span",{"class":"text--title"}).text)
print("이미지 : ", items.find("img",{"src":"//image.auction.co.kr/itemimage/41/63/a7/4163a77257.jpg?ver=1713767517"}))
print("가격 : ", items.find("strong",{"class":"text__price-seller"}).text)
rate = items.find("li",{"class":"item awards"})
print("평점 : ", rate.find("span",{"class":"for-a11y"}).text)

# for item in items[0:5]:
#     print("[ ", item, "번째 상품 ]")
#     print("상품명 : ", item.find("span",{"class":"text--title"}).text)
#     print("이미지 : ", item.find("img",{"src":"//image.auction.co.kr/itemimage/41/63/a7/4163a77257.jpg?ver=1713767517"}))
#     print("가격 : ", item.find("strong",{"class":"text__price-seller"}).text)
#     print("평점 : ", item.find("span",{"class":"for-a11y"}).text)
    
