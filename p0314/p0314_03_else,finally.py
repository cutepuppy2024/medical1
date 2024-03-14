# 예외 구문 try, except, else, finally


a_list = [1,2,3,4,5,6,7,8,'9',10]


for i in a_list:
    try:
        print(i+1)
    except:
        print('데이터 오류가 있습니다')  # 오류가 난 자리에 cnt 또는 문자로 출력하는 형태가 좋음
        # pass

#---------------------------------------------------------
# 1
print('프로그램실행')
try:
    print(1)
    print(2)
    print(1/0)    # 에러가 발생
    print(3)
except:           # 예외 발생한 경우
    print(4)        
    print(5)
else:
    print(6)
print('프로그램종료')


# 2
print('프로그램실행')
try:
    print(1)
    print(2)
    # print(1/0)    
    print(3)
except:           
    print(4)
    print(5)
else:              # 예외 발생하지 않은 경우
    print(6)
print('프로그램종료')

# 3
print('프로그램실행')
try:
    print(1)
    print(2)
    # print(1/0)    
    print(3)
except:
    print(4)
    print(5)
else:            
    print(6)   
finally:           # 예외가 발생하거나, 하지 않거나 무조건 실행
    print(7)
print('프로그램종료')

# clear
