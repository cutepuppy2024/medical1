import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)

res.raise_for_status()

# print(res.text)                                          # 파싱하면 데이트를 찾는 것이 쉬워질 수 있다

soup = BeautifulSoup(res.text,"lxml")                      # 파싱해서 soup에 넣어달라 

# print(soup)
# HTML Hyper Text Markup Language  웹에서 사용하는 언어   장점: 국제표준

# with open("test.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())                             # text의 형태로 파일에 들어간다

print(soup.title.text)   # <title> 랭킹뉴스 여러개라도 첫번째것을 찾는다, lxml로 읽어왔기 때문에 가능한 것    # soup 태그사용해서 text글자를 출력
# ytn
print(soup.a)            # 메인메뉴로 바로가기  soup에는 모든 소스들이 들어가있다                            # soup 태그사용
print(soup.a.attrs)      # 속성값만 딕셔너리 형태로 나옴  => 위치점을 찾아가는 것                            # soup a 태그의 속성값 출력
print(soup.a["href"])    # value값이 출력됨                                        
print(soup.div)          # div를 찍으면 가장 첫번째 <div 태그: 클릭하는 페이지로 이동하라 / 뒤에 있는 것을 모두 속성           > 
# print(soup.find("div",atters={"id":"footer"})) # div id="footer"   
print(soup.find("div",{"id":"footer"}))                                                                  # soup에서 find 태그, 속성 모두를 찾을 수 있다
  


# find : 1개
# find all : 해당되는 모든것을 찾는다
# 


