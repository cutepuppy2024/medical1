# 함수선언 : def 이름()
# 함수호출 : 이름()
# 함수선언 매개변수 개수는 맞춰야 함: def 이름(매개변수) -> 이름(매개변수)
# 리턴의 결과값을 받지 않아도 되지만, 개수는 맞춰야 함.
# 함수내의 변수는 지역변수여서, 함수가 종료되면 사라짐.
# 함수내의 변경된 변수값을 전역변수에 반영하고 싶으면 return으로 돌려줘야 함
# 함수내 globa이라고 하면, 전역변수에 선언되어 있는 변수주소를 가져와서 return사용하지 않아도 됨
# 매개변수 리스트, 딕셔너리를  사용하는 경우 return 할 필요가 없음

def cal(v1):
    sum = 500
    v1 = 200


v1 = 100
cal(v1)
print(v1)  # 100  => return 하지 않았으므로 지역변수로 출력됨
print(sum) # 함수에 있는 sum을 쓸 수 없다


def calc(ver1,sum):
    sum = 500
    ver1 = 200
    return ver1,sum

sum = 10  # 전역변수는 함수 바깥에서 선언, 여러개의 함수 안에서 사용가능
ver1 = 100
ver = calc(ver1,sum)
calc(ver1,sum)
print(ver) # 200 => 전역변수
print(sum)


def func1():
    global a # 전역변수를 가져옴
    a = 100
    # print('func1 a=',a)  # 지역변수를 출력
    print('func1 a=',a)
    # 지역변수 값을 전역변수에 적용시키는 방법
    return a

    
def func2():
    print('func2 b=',a+10)  # a가 정의되지 않아 전역변수를 가지고 온다
    
a = 20 # 전역변수
a = func1()

func2()
print('결과값',a)

# 함수선언
def func1(a,a_list):
    a = 100
    a_list[0] = 100  #지역변수  a_list[0] = [100]
    return a
    
a = 10   # 전역변수
a_list = [1,2,3]
# 함수호출
a = func1(a,a_list)  #2개 이상의 데이터를 저장하는 변수 - 주소값을 저장함
print(a)
print(a_list)