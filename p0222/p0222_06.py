# 산술 연산자
# + - * /
a = 5
b = 3
result = a + b
result = a - b
result = a * b
result = a / b
print(result)

result = a//b # 몫 4//2 몫:2 나머지:0 =>기본 실수로 표현
print(result)
result = a%b # 나머지 => 꼭 기억하기!!!
print(result)
result = a**b # 제곱
print(result)

c = 10
d = 20
c,d = 100,200

# 산술연산자 우선순위
# 곱셈, 나눗셈 먼저 -> 덧셈 뺄샘 순으로 진행
# 괄호가 없을 경우 왼쪽에서 오른쪽 방향으로 계산
r1 = 2 + 2 - 2 * 2 / 2 * 2  # 혼선을 피하기 위해 ()사용

# 괄호 사용을 추천
r2 = 2 -(2/2)

# 다른 자료형으로 연산
str1 = "문자열"
n1 = 10

print(str1*n1)
#print(str1+n1) # 오류 error

# 문자열이 정수나 실수일 경우 int() float()를 사용해서 변환
s1 = "100"
s2 = "10.123"
print(int(s1)+1) #문자열이기 때문에 숫자로 변환하도록 명령어 
print(float(s2)+1)

# 숫자가 아닌것을 변환할 수 없다
# n = int("안녕하세요") #error

# 숫자를 문자로 바꾸고 싶으면 str()사용
s1 = 100
s2 = 10.123
print(str(s1)+"1") 
print(str(s2)+"1")

p = 12341234
print("010"+str(p))

# 숫자 두개를 입력받아서 나누기값, 몫, 나머지 값을 구하세요
# ex) n1 = 4 n2=2
# 출력:
# 나누기값:(2.0), 몫:(2), 나머지 : (0)

a = 4
b = 2
result = a/b
print(result)
result1 = a//b
print(result1)
result2 = a%b
print(result2)

a = input("첫번째 숫자를 입력하세요 >>")
a = int(a)
b = input("두번째 숫자를 입력하세요 >>")
b = int(b)
result = a/b
result1 = a//b
result2 = a%b
print(result)
print(result1)
print(result2)
print("나누기값 :",result, "몫 :", result1, "나머지 :", result2)


# 풀이
# result = a//b # 몫 4//2 몫 : 2 나머지 : 0
# result = a%b # 나머지
n1 = input("첫번째 숫자를 입력하세요 >>")
n2 = input("두번째 숫자를 입력하세요 >>")
# 문자를 숫자로 변경
n1, n2 = int(n1), int(n2)
# 출력
print('나누기: {:.1f}\n몫: {}\n나머지: {}'. format(n1/n2, n1//n2,n1%n2)) #format으로 간단히 표현, 소숫점은 {} 안에
