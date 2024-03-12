
# 1. 10*10 좌표 만들기
# 2. 영어단어게임
# 3. 로또
# 4. 학생성적
# 5. 주택복권

import random
a = [0]*100 
for i in range(10):
    a[i] = 1
    
random.shuffle(a)

# => 2차원리스트

c_List = [[0]*10 for i in range(10)]

for i in range(10):
    for j in range(10):
        c_List[i][j] = a[10*i+j]

v_List =[['추첨']*10 for i in range(10)]

count = 0
right = 1

while True :
    print('   [추첨좌표]  ')
    print('-'*50)
    print('',0,1,2,3,4,5,6,7,8,9,sep=('\t')) 
    print('-'*50)
    for i in range(10):
        print(i,end='\t')
        for j in range(10):
            print(c_List[i][j],end='\t')
        print()
        
    print('   [게임좌표]  ')
    print('-'*50)
    print('',0,1,2,3,4,5,6,7,8,9,sep=('\t')) 
    print('-'*50)
    for i in range(10):
        print(i,end='\t')
        for j in range(10):
            print(v_List[i][j],end='\t')
        print()
        
    x = input('x 좌표 선택')
    y = input('y 좌표 선택')
    if c_List[x][y] == v_List[x][y]:
        print('당첨')
        right += 1
    else:
        print('[꽝]')
        
        

