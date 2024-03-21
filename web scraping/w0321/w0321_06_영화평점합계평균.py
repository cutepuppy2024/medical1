import requests
from bs4 import BeautifulSoup

# url = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%98%81%ED%99%94'   # 주소 갖고오기
year_rate_sum = [0]*3
year_rate_avg = [0]*3
for y_i, y in enumerate(range(2021,2024)):
    url = f'https://search.daum.net/search?w=tot&q={y}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
    headers = {"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}  # headers를 딕셔너리로
    res= requests.get(url,headers=headers)  # res 변수사용, HTML 가지고오기
    res.raise_for_status() # 이상체크


    soup = BeautifulSoup(res.text,'lxml')  # HTML 주소를 lxml 언어로

    movie_list = soup.find("ol",{'class':"movie_list"})  # 전체 HTML 주소를 변환한 파일 중에서 ol이라는 태그, 속성값 2개를 찾는다
    print(movie_list)


    m_lists = movie_list.find_all("li")  # 속성값 2개를 가지고 있는 리스트 가운데서 "li"가 들어간 리스트를 다시 지정
    print(type(m_lists))  # <class 'bs4.element.ResultSet'>
    sum = 0
    for i, m in enumerate(m_lists):  #  리스트에서 5개만 찾기
        if i == 5: break  
        print(f"[번호 {i+1}]")
        print("제목 :",m.find("div",{"class":"info_tit"}).a.text)
        rate = float(m.find("em",{"class":"rate"}).text)
        print("평점 :", m.find("em",{"class":"rate"}).text)
        sum += rate
        for i in range(5):
            sum += rate
        img_screen = m.find("img")["data-original-src"]
        print(img_screen)  # 파일이름의 내용을 저장
        # 이미지 저장부분
        # with open(f"movie_{y}_{i}.jpg",'wb') as f:
        #     re_img = requests.get(img_screen)   # url링크를 다시 읽어와야 함  => 서버주소를 다시 가지고 와야 하기 때문에 재지정 필요
        #     f.write(re_img.content)
    print(f"{y}년도 평점 합계")
    year_rate_sum[y_i] = f'{sum:.2f}'
    year_rate_avg[y_i] = f'{sum/5:.2f}'
    
print("개수 :",len(m_lists))
print("연도별 평점합계 :", year_rate_sum)
print("연도별 평점평균 :", year_rate_avg)
print("종료")


