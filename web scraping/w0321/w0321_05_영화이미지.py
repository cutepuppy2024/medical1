import requests
from bs4 import BeautifulSoup

url = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%98%81%ED%99%94'   # 주소 갖고오기
headers = {"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}  # headers를 딕셔너리로
res= requests.get(url,headers=headers)  # res 변수사용, HTML 가지고오기
res.raise_for_status() # 이상체크


soup = BeautifulSoup(res.text,'lxml')  # HTML 주소를 lxml 언어로

movie_list = soup.find("ol",{'class':"movie_list"})  # 전체 HTML 주소를 변환한 파일 중에서 ol이라는 태그, 속성값 2개를 찾는다
print(movie_list)


m_lists = movie_list.find_all("li")  # 속성값 2개를 가지고 있는 리스트 가운데서 "li"가 들어간 리스트를 다시 지정
print(type(m_lists))  # <class 'bs4.element.ResultSet'>

for i, m in enumerate(m_lists):  #  리스트에서 5개만 찾기
    if i == 5: break  
    print(f"[번호 {i+1}]")
    print("-"*50)
    img_screen = m.find("img")["data-original-src"]
    # print(m.find(img_screen.content))  # 파일이름의 내용을 저장
    print(img_screen)
    # 파일열기
    with open(f"movie_{i}.jpg",'wb') as f:
        re_img = requests.get(img_screen)   # url링크를 다시 읽어와야 함  => 서버주소를 다시 가지고 와야 하기 때문에 재지정 필요
        f.write(re_img.content)

print("개수 :",len(m_lists))
print("종료")

# 웹소스 
# 파싱
