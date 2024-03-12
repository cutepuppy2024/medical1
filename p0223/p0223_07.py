#  해보세요
 # cal은 문자로 입력받는다
# n1 = 24
# n2 = 5

n1 = int(input("첫번째 숫자를 입력하세요 >>>"))
n2 = int(input("두번째 숫자를 입력하세요 >>>"))
cal = input('수식을 입력하세요(+,-,*,/) >>')

if cal == '+':
    print(n1 + n2)
elif cal == '-' :  
    print(n1 - n2)
elif cal == '*' :
    print(n1*n2) 
elif cal == '/' :
    print(n1/n2)
else :
    print("수식을 잘못입력 하셨습니다. 다시 입력해 주세요")
