import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"en-US,en;q=0.9"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# print(soup)

# with open("coupang.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print("완료")

ul_search = soup.find("ul",{"class":"search-product-list"})

lis = ul_search.find_all("li")

# print("리스트 개수 :", len(lis))
# print("-"*30)
# print(lis[1])
# print(ul_search.find("li"))

for i,li in enumerate(lis[0:10]):
    print("[ ",i+1,"번째 상품 ]")
    print("li class :",li["class"])
    
    # 광고상품 제외
    if "search-product__ad-badge" in li['class']:
        continue
    
    # 평점이 5.0 이상인것만 출력 - 문자와 숫자 비교 에러, 실수형으로 변경  
    if float(li.find("em",{"class":"rating"}).text) < 5.0:
        continue
    
    # 평가인원수 200명 이상인 사람만 출력 - 정수형으로 변경
    if int(li.find("span",{"class":"rating-total-count"}).text[1:-1]) < 200:
        continue
    
    # 왼쪽, 오른쪽 공백제거
    print("제목 : ", li.find("div",{"class":"name"}).text.strip())
    print("가격 : ", li.find("strong",{"class":"price-value"}).text)
    print("평점 : ", li.find("em",{"class":"rating"}).text)
    print("평가인원수 : ", li.find("span",{"class":"rating-total-count"}).text[1:-1])
    print("-"*30)














