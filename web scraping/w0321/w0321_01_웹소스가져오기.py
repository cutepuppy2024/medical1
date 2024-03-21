import requests
# 웹에 접근해서 html 소스를 가져옴.
# res = requests.get("https://www.google.com/")   # 구글에서 우클릭, 소스코드를 가져온 것과 같다
# res = requests.get("https://www.daum.net/")
res = requests.get("https://www.melon.com/")      # 406 : 오류가 아니라 웹스크래핑이라  차단시킨것
# 200 : 정상, 403,404 : 페이지없음  500: 프로그램에러
print(res)  # 코드상태 출력   #  <Response [406]>
print("코드 :",res.status_code)  #  코드 : 406  => 리턴한 소스의 코드값을 출력
print(type(res.status_code))     # <class 'int'>
res.raise_for_status() # 코드가 200이 아니면 오류처리해서 자동멈춤 => 

if res.status_code == requests.codes.ok :      # 200
    print("정상페이지 호출입니다.")
else :
    print("에러코드 발생")

print(res)
print(type(res))
print("-"*40)

# res 변수는 requests를 통해 html소스를 출력
print(res.text)        # HTML에 있는 소스들이 들어온다