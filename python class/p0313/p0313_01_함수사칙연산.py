# 함수선언 def 이름() 정의
# 함수값은 return
# 함수호출 이름()
# 매개변수 : 함수로 데이터 전달하는 변수, 매개변수 개수는 항상 같아야 한다.
# 가변매개변수선언 *value, 가변매개변수는 일치하지 않아도 된다.
# 리스트, 딕셔너리 매개변수는 주소값이 전달이 된다.

# 퀴즈.1
# 함수를 사용하여 두수를 입력받아, 더하기,빼기,곱하기,나누기 결과값을 출력하시오

def cal(n1,n2):
    r1 = n1 + n2
    r2 = n1 - n2
    r3 = n1 * n2
    r4 = n1 / n2
    result = [r1,r2,r3,r4]  
    return result  

n1 = int(input('첫번째 숫자 입력 >>'))    
n2 = int(input('두번째 숫자 입력 >>'))

result = []

calA = cal(n1,n2)
print(calA)

# 내가 풀이한 것 : 매개변수를 리스트로 지정하지 않은것이라 return을 해야한다
#----------------------------------------------------------------------------

def cal(n1,n2):
    r1 = n1 + n2
    r2 = n1 - n2
    r3 = n1 * n2
    r4 = n1 / n2
    results = r1,r2,r3,r4 
    return results  

n1 = int(input('첫번째 숫자 입력 >>'))    
n2 = int(input('두번째 숫자 입력 >>'))


r1,r2,r3,r4 = cal(n1,n2)
print('{},{} 결과값: {}{}{}{}'.format(n1,n2,r1,r2,r3,r4))


#----------------------------------------------------------------------------


def cal(num1,num2,c):
    if c == 1 :
        result = num1 + num2
    elif c == 2 :
        resuls = num1 - num2
    elif c == 3 :
        result = num1 * num2
    elif c == 4 :
        result = num1 / num2

    return result
                     

num1 = int(input('첫번째 숫자 입력 >>'))    
num2 = int(input('두번째 숫자 입력 >>'))
print('1. + 2.- 3.* 4./')
c = int(input('원하는 사칙연산을 입력하세요>>'))

result = cal(num1,num2,c)  # 이곳에 있는 변수와 def()에 있는 값은 같은 값이 아니다

print('{},{} 결과값: {}'.format(num1,num2,result))



# clear