def stu_update(stuNo,name,kor,eng,math): # 지역변수 
    stuNo = stuNo+1
    name = '유관순'
    total = kor + eng + math  # 지역변수
    avg = total/3             # 지역변수
    return stuNo,name,total,avg



stuNo = 1
name = "홍길동"
kor = 100
eng = 100
math = 100
total = 0
avg = 0


# 함수호출
stuNo, name, total,avg = stu_update(stuNo,name,kor,eng,math)   # 리턴받는 = 매개변수    => 1개만 들어가는 변수(일반변수)

print('학생2:', stuNo,name,kor,eng,math,total,avg)


def cal(num1,num2):
    sum = 0
    temp = 0
    if num1 > num2:
        # num1,num2 = num2,num1    
        temp = num1
        num1 = num2
        num2 = temp
    for i in range(num1,num2+1):
        sum += i
    return sum

# 1,10 -> 1+2+3+4+5+...10 = 55
# 두수를 입력받아, 입력한 사이의 합계를 구하는 프로그램을 구현하시오

sum = 0
num1 = int(input('1번째 숫자를 입력하세요 >>'))
num2 = int(input('2번째 숫자를 입력하세요 >>'))

sum = cal(num1,num2)

print('합계:', sum)

