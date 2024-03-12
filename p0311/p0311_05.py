# 함수선언
def plus(n1,n2): # def 이름(매개변수) => 현재 2개
    result = 0
    result = n1 + n2
    print('결과값 :',result)
    
print('프로그램을 실행합니다') # 함수 호출이 없었다

plus(1,2) # 매개변수가 2개면 무조건 2개 들어와야 함. 아니면 에러
plus(10,20) # 함수호출 : 함수이름(매개변수 개수를 맞춰주면 됨.)
plus(50,100)

# n1,n2 = 1,2
# result = 0
# result = n1 + n2
# print('결과값 :',result)


# n1,n2 = 50,100
# result = 0
# result = n1 + n2
# print('결과값 :',result)   반복하지 않고 함수사용