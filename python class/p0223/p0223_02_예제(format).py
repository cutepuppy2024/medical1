# 해보세요
# 1. 숫자 두개를 입력받아서 나누기값 몫값 나머지값을 출력

num1 = int(input("첫번째 숫자를 입력하세요>> "))
num2 = int(input("두번째 숫자를 입력하세요>> "))
result1 = num1/num2
result2 = num1//num2
result3 = num1%num2
print(result1,result2,result3)
print('{},{:.2f},{:.3f}'.format(result1,result2,result3))



# 2. 3개의 수의 합을 구하세요
s1, s2, s3 = '100', '100.123', '99.9'
s1 = int(s1)
s2 = float(s2)
s3 = float(s3)
result = s1+s2+s3
print('{}+{}+{} = {}'.format(s1,s2,s3,result))
print('3개의 수의 합을 구하세요: {}'.format(result))