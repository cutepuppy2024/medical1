import random
a = []
# 1-25까지 숫자를 list에 넣기
for i in range(0,25):
    a.append(i+1)
print(a)
# 리스트를 섞기
random.shuffle(a)  # shuffle : 0번방과 임의방의 값을 계속 교환하여 섞음

# 2차원 리스트에 랜덤으로 섞은 숫자 넣기
arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
for i in range(0,5):  # 0,1,2,3,4         => 2차원 리스트 frame을 먼저 만들고, for문의 반복되는 수를 이용
    for j in range(0,5):  # 0,1,2,3,4
        arr[i][j] = a[(5*i) +j]   #(5*i) +j -> 0,24 (데이터값)!!!  
#출력
while True:
    print('='*50)
    print('[좌표맞추기 프로그램]')
    print('='*50)
    print('순번','ㅣ',0,1,2,3,4,sep='\t')
    print('='*50)
    for i in range(0,5):
        print(i,'\t','ㅣ',end='\t')
        for j in range(0,5):
            print(arr[i][j],end='\t')       
        print()
    print('-'*50)
    x = int(input('X좌표를 입력하세요 >>'))
    y = int(input('Y좌표를 입력하세요 >>'))
    arr[x][y] = 'X'        
    
