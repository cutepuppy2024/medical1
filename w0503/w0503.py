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

# url = 'https://flight.naver.com/'
url = 'https://flight.naver.com/flights/domestic/GMP-CJU-20240626/CJU-GMP-20240627?adult=2&fareType=YC'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)


elem = browser.find_element(By.XPATH,'//b[text()="ICN"]')
elem.click()
time.sleep(2)

elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
elem.click()
time.sleep(2)

elem = browser.find_element(By.XPATH,'//i[text()="김포국제공항"]')
elem.click()
time.sleep(2)

elem = browser.find_element(By.XPATH,'//b[text()="도착"]')
elem.click()
time.sleep(2)

elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
elem.click()
time.sleep(2)

elem = browser.find_element(By.XPATH,'//i[text()="제주국제공항"]')
elem.click()
time.sleep(2)

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[2]/button[1]')
elem.click()
time.sleep(2)

# - 6/26 ~ 6/27
elem = browser.find_elements(By.XPATH,'//b[text()="26"]')
elem[1].click()
time.sleep(2)

elem = browser.find_elements(By.XPATH,'//b[text()="27"]')
elem[1].click()
time.sleep(2)

elem = browser.find_element(By.XPATH,'//span[text()="항공권 검색"]')
elem.click()
time.sleep(2)

# 항공사 출발시간 도착시간 소요시간 금액을

soup = BeautifulSoup(browser.page_source,'lxml')

with open('flights.html','w',encoding='utf8') as f:
    f.write(soup.prettify())

flights = soup.find_all("div",{"class":"domestic_Flight__sK0eA"})
print("항공권리스트 개수 :",len(flights))

# print("항공사 :",flights[0].find("b",{"class":"airline_name__Tm2wJ"}).text)
# schedule = flights[0].find("div",{"class":"route_Route__2UInh"})
# print("출발시간 :",schedule.span[0].text)
# print("도착시간 :",schedule.span[1].text)
# print("소요시간 :",schedule.find("i",{"class":"route_info__1RhUH"}).text)

for i, flight in enumerate(flights):
    print("[ ",i+1,"번째 항공권 ]")
    airline = flight.find("b",{"class":"airline_name__Tm2wJ"}).text
    print("항공사 :",airline)
    
    schedule = flight.find("div",{"class":"route_Route__2UInh"})
    
    departure_time = schedule.span[0].text
    print("출발시간 :",departure_time)
    
    arrival_time = schedule.span[1].text
    print("도착시간 :",arrival_time)
    
    flight_time = schedule.find("i",{"class":"route_info__1RhUH"}).text
    print("소요시간 :",flight_time)
    
    price = flight.find("i",{"class":"domestic_num__2roTW"}).text
    print("가격 :",price)
    

    
    sql =f"insert into flight values (flight_seq.nextval,'{airline}','{departure_time}','{arrival_time}','{flight_time}',{price})"
    cursor.execute(sql)
    print("-"*50)
cursor.execute("commit")
cursor.close()
conn.close()    

# - db에 저장하시오.
# - db에서
# - 항공사별 그룹핑해서 출력하시오.
# - 시간 검색기능을 구현하시오.
# ( 출발하려는 시간을 입력하세요. >> )
# - 시간을 입력하면 입력된 시간 이후로 검색
# - 없으면 검색한 데이터가 없다고 나옴.