from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/bestChallenge"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

print(soup.prettify())

# with open("webtoons1.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
    
print("완료")

# browser = webdriver.Chrome()
# browser.get("http://www.naver.com/")

# time.sleep(10)

# elem = browser.find_element("MyView-module__link_login___HpHMW")
# elem
# elem.click()

