import requests


# 웹 크롤링 형태
# res = requests.get("https://www.google.com/")
res = requests.get("https://www.naver.com/")
res.raise_for_status() # 에러코드이면 자동멈춤, 200코드가 아니면
print(type(res.text))  # str타입, 데이터 찾기가 힘들다, HTML로 파싱하면 위치점, 범위 등을 지정하기가 찾기가 쉬워진다. 

print("총 문자 길이 :" ,len(res.text))   

with open("google.html","w",encoding='utf8') as f:
    f.write(res.text)   
    
    