# 1. 해보세요
# 나이가 10살 이상이고 150 이상만 탑승가능
# 나이, 키를 입력받아
#[탑승가능] [탑승불가능]을 출력해보세요

age = int(input('나이를 입력하세요 >>'))
height = int(input('키를 입력하세요 >>'))

if age >= 10 :
    if height >= 150 :
        print('탑승가능')
    else :
        print('탑승불가능')
else :
    print('탑승불가능')

# 2. 숫자3개 (정수)를 입력받고, 연산1개를 입력받아
# +++  ---  ***  //// (나누기 값은 둘째자리까지 표현)
# ex) a + b + c = d의 형태로 출력 (1 + 2 + 3 = 6)

n1 = int(input("첫번째 숫자를 입력하세요 >>"))
n2 = int(input("두번째 숫자를 입력하세요 >>"))
n3 = int(input("세번째 숫자를 입력하세요 >>"))
cal = input('수식을 입력하세요 >>')
if cal == '+' :
    print('{}+{}+{} = {}'.format(n1,n2,n3,n1+n2+n3)) 
elif cal == '-':
    print('{}-{}-{} = {}'.format(n1,n2,n3,n1-n2-n3))
elif cal == '*':
    print('{}*{}*{} = {}'.format(n1,n2,n3,n1*n2*n3))
elif cal == '/':
    print('{}/{}/{} = {:.2f}'.format(n1,n2,n3,n1/n2/n3))
else :
    print('수식을 잘못 입력하셨습니다. 다시 입력해 주세요')
    
    
if cal == '+':
    result = n1 + n2 + n3
    print(result)
elif cal == '-':
    result = n1 - n2 - n3
    print(result)
elif cal == '*':
    result = n1 * n2 * n3
    print(result)   
elif cal == '/':
    result = n1 / n2 / n3
    print(result)
else:
    print('잘못 입력하셨습니다')    
    
    
if cal == '+' :
    result = n1 + n2 + n3
    print('{}+{}+{} = {}'.format(n1,n2,n3,result)) 
elif cal == '-':
    result =  n1 - n2 - n3
    print('{}-{}-{} = {}'.format(n1,n2,n3,result))
elif cal == '*':
    result = n1 * n2 * n3
    print('{}*{}*{} = {}'.format(n1,n2,n3,result))
elif cal == '/':
    result = n1 / n2 / n3
    print('{}/{}/{} = {:.2f}'.format(n1,n2,n3,result))
else :
    print('수식을 잘못 입력하셨습니다. 다시 입력해 주세요')
