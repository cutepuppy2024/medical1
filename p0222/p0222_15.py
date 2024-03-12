import datetime # 날짜 관련 기능을 가져옴
now = datetime.datetime.now() # 오늘 날짜 시분초 가져옴

# print(now) # => 2024-02-22 

# print(now.year) # 연도
# print(now.month) # 월
# print(now.day) # 일

# print(now.hour)
# print(now.minute)
# print(now.second)


# 시간을 사용해서
# 지금이 오전이면 오전입니다. 오후면 오후입니다 출력



year = now.year # 2024
h = now.hour # 시간
m = now.month

if h >= 12: # h<12
    print("오후")
else:
    print("오전")
# [현재는 17시로 오후입니다.]  

if year >= 2024 :
    print("present") 
else:
    print("past")
    
# 1. 짝수달입니다. 홀수달입니다.
m = now.month
if m%2 == 0 :
    print('짝수달입니다.')
else:
    print('홀수달입니다.')
    
# 월
# 겨울입니다

m = now.month
if m == 12 or m == 1 or m == 2 : 
    print('겨울입니다')
else :
    print('겨울이 아닙니다')

m = now.month
if 3 <= m <= 11 :
    print('겨울이 아닙니다')
else :
    print('겨울입니다')
 
y = now.year
if y%4 == 0 :
    print('아시안게임이 있는 해입니다')  
else :
    print('아시안게임이 열리지 않는 해입니다.')
    
m = now.month
print(type(m)) # type을 알아보는 방법: <class 'int'>