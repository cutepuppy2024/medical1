# 좌표
import random

a =[0]*100
for i in range(10):
    a[i] = 1
    
random.shuffle(a)

c_List =[[0]*10 for i in range(10)]
for i in range(10):
    for j in range(10):
        c_List[i][j] = a[10*i+j]
print(c_List[i][j],end=' ')
        
v_List =[['추첨']*10 for i in range(10)]

count = 1
right = 0
my_xy = []
r_xy = []
while True:
           
    for i in range(10):
        for j in range(10):
            print(v_List[i][j],end=' ')
        print()
        
    x = int(input('x좌표 입력 >>'))
    y = int(input('y좌표 입력 >>'))  
    my_xy = [[x,y]]
    count += 1
    
    if c_List[x][y] == 1:
        v_List[x][y] = '당첨'
        r_xy = [[x,y]]
        right += 1
        
    else:
        v_List[x][y] = '[꽝]'
    
    if right == 3:
        print('모두당첨')
        break   
    print()
    
    if count == 10:
        print('기회를 모두 사용하셨습니다')
        
print('당첨좌표는 {}, 선택하신 좌표는 {}입니다.'.format(r_xy,my_xy))    
        