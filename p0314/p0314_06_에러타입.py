# < 예외 타입 >


# 1. ValueError
try:
    txt = int(input('숫자를 입력하세요'))   # 숫자를 입력하세요 안녕
    print(txt)
except Exception as e:
    print('-- 예외가 발생했습니다')
    print('타입:', type(e))   # 타입: <class 'ValueError'>
    print(e)                  # invalid literal for int() with base 10: '안녕'
    
# 2. ZeroDivisionError   
try:
    print(1/0)
    txt = int(input('숫자를 입력하세요'))   # 숫자를 입력하세요 안녕
    print(txt)
except Exception as e:
    print('-- 예외가 발생했습니다')
    print('타입:', type(e))   #  타입: <class 'ZeroDivisionError'>
    print(e)                  # division by zero
    
# 3. IndexError  
a_list = [1,2,3]   
try:
    print(a_list[5])
    txt = int(input('숫자를 입력하세요'))   # 숫자를 입력하세요 안녕
    print(txt)
except IndexError:                         # 예외명을 알고 있을 때, Exception이 최상위라 위에 기재해야 함.
    print('리스트 주소가 잘못 입력되었습니다')      
except Exception as e:
    print('-- 예외가 발생했습니다')
    print('타입:', type(e))   #  타입: <class 'IndexError'>
    print(e)                  #   list index out of range
       
       
       

# clear 
    
    