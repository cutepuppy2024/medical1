import requests
from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

url ="http://www.daum.net"

# 크롬브라우저 열기
browser = webdriver.Chrome()

# 다음창 열기
browser.get(url)
# 로그인 버튼위치
elem = browser.find_element(By.CLASS_NAME,"btn_login")  
time.sleep(random.randint(2,5))
elem.click()

# 자동화 방지를 위한 자바스크립트 활용 데이터 입력
input_js = 'document.getElementById("loginId--1").value ="{id}"; \
            document.getElementById(password--2).value ="{pw}"; \
            '.format(id="",pw="")
browser.execute_script(input_js)


# 로그인 아이디
elem = browser.find_element(By.ID,"loginId--1") # CLASS_NAME, NAME, XPath로 찾아도 됨
elem.send_keys("aaa")
time.sleep(random.randint(2,5))

# 로그인 패스워드
elem = browser.find_element(By.ID,"password--2")
elem.send_keys("1111")
time.sleep(random.randint(2,5))

# 로그인 버튼클릭
elem = browser.find_element(By.CLASS_NAME,"btn_g highlight submit")
# elem.click()


# 완료
time.sleep(100)

    
    