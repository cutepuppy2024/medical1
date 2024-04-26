# https://jumin.mois.go.kr/ageStatMonth.do
# 서울특별시, 인천, 경기도 3개의 인구를 웹스크래핑해서
# 서울특별시 : 인구
# 인천광역시 : 인구
# 경기도 : 인구
# 합계 : 인구를 출력하시오

# 셀레늄 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup


browser = webdriver.Chrome()
url = "https://jumin.mois.go.kr/ageStatMonth.do"
# 브라우저 페이지를 열기
browser.get(url)
time.sleep(3)

soup = BeautifulSoup(browser.page_source,"lxml")
# with open('jumin.html',"w",encoding='utf8') as f:
#     f.write(soup.prettify())

# 테이블 검색
table = soup.find("table",{"id":"contextTable"})

# tbody 검색
tb = soup.find("tbody")
print(tb)
trs =  tb.find_all("tr") # 21개
print(len(trs))
# td 검색
tds = trs[1].find_all("td") 
seoul = tds[2].text
print("서울특별시 인구수 : ", seoul)
tds = trs[4].find_all("td") 
inchon = tds[2].text
print("인천광역시 인구수 : ", inchon)
tds = trs[9].find_all("td") 
kyunggi = tds[2].text
print("경기도 인구수 : ", kyunggi)

total = int(seoul.replace(",",""))+int(inchon.replace(",",""))+int(kyunggi.replace(",",""))
print("수도권 인구수 :", format(total,","))


# ------------------------------------------------------

# 웹 스크래핑 

# url = "https://jumin.mois.go.kr/ageStatMonth.do"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")

# table = soup.find("table",{"class":"tbl_type1"})

# cities = table.tbody.find_all("td",{"class":"td_admin th1"})

# # print(len(trs)) # 행의 개수 : 18

# # 서울
# print(cities[1].text, cities[1].find_next_sibling("td").text)
# # 인천
# print(cities[4].text, cities[4].find_next_sibling("td").text)
# # 경기도
# print(cities[9].text, cities[9].find_next_sibling("td").text)

# # 합계
# seoul_pop = int(cities[1].find_next_sibling("td").text.replace(",",""))
# incheon_pop = int(cities[4].find_next_sibling("td").text.replace(",",""))
# gyunggi_pop = int(cities[9].find_next_sibling("td").text.replace(",",""))

# total = seoul_pop + incheon_pop + gyunggi_pop
# print("합계 : ",'{0:,}'.format(total),"명")




