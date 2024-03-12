# 0~20 사이의 5의 배수로 이루어진 리스트를 만들어보세요
# 출력: [0,5,10,15]
num =[]
for i in range(0,20,5):
    print(i)
    num.append(i)
    print(num)
    
for i in range(21):
    if i%5 == 0:
        print(i)
        num.append(i)
        print(num)
        
for i in range(21):
    num.append(i)
    print(num)
    
for i in range(21):
    if i%5 == 0 :
        num.append(i)
        print(num)
        
lan = ['c', 'python', 'java', 'jquery', 'css']
# 1. 하나하나 출력해보기
#   1) in 리스트명 사용 
for language in lan:
    print(language)
#   2) in range() 사용
for i in range(len(lan)): # for i in range(5) i = 1,2,3...
    print(lan[i])
    
# # 2. 카운터변수 i 사용해서
# #    1.c
# #    2.python 
# #    3.java 
# #    4.jquery
# #    5.css

lan = ['c', 'python', 'java', 'jquery', 'css']
for i in lan:
    print(i)
    
for i in range(len(lan)):
    print(lan[i])
    
# for i in range(lan):
#     print(i)
    
for i in range(5):
    print(i)
    print(lan[i])
    print('{}. {}'.format(i+1, lan[i]))  # i + 1 => 번호 (i,lin[i-1])
    

num = [1,-1,2,3,-4,5,6,-8,9,-10] 
# 양수면 양수 음수면 음수 출력 for 사용
# 1: 양수
# -1: 음수
# 2 : 양수 ....
# for  변수 in 리스트명:

for i in num: 
    print(i)
    
for i in num: 
    print(i, end =':')
    if i >= 0 :
        print('양수')
    else:
        print('움수') 
    
for i in num:
    if i >= 0 :
        print('{} : 양수'.format(i))
    else:
        print('{} : 음수'.format(i)) 
       
for i in range(len(num)):
    if num[i] >= 0 :
        print('{} : {}, {}'.format(i+1,num[i],'양수'))
    else:
        print('{} : {}, {}'.format(i+1,num[i],'음수'))
    

