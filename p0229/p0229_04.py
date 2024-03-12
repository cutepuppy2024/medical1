# while문과 if 문을 사용
# 숫자 두개를 입력받고,

# 연산자를 입력받아서 (+=*/) input

# 계산결과 출력 (if)


# 무한히 계산하는 계산기를 만드는데 (while)

# result = 0
# while True:
    
# # 첫번째 숫자에 0을 입력하면 프로그램이 종료가 되는 코드를 만드세요 break
# if n1 = 0:
#     print('종료되었습니다')
#     break


# while 조건식 : # 조건식이 참일때 실행문 수행 , 즉 조건식이 거짓일때 while 종료
# 실행문
while True: # 무조건 참이기 때문에 while 안에 있는 것 계속 반복
    n1 = int(input('첫번째 숫자를 입력하세요 >>'))
    if n1 == 0:                                        # 종료 시점을 선택하는 것이 중요
        print('종료되었습니다')
        break
    n2 = int(input('두번째 숫자를 입력하세요 >>'))
    cal = input('연산자를 입력하세요 >>')
    if cal == '+':
        print('{} + {} ={}'.format(n1,n2,n1+n2))
    elif cal == '-':
        print('{} - {} ={}'.format(n1,n2,n1-n2))
    elif cal == '*':
        print('{} * {} ={}'.format(n1,n2,n1*n2))
    elif cal == '/':
        print('{} / {} ={}'.format(n1,n2,n1/n2))
    else:
        print('잘못입력하였습니다. 다시 연산자를 입력해주세요')
        
        
