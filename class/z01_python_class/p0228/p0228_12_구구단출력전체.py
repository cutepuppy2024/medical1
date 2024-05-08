# for 문을 사용해서 2단을 출력

for i in range(1,10):
    print('{}*{}={}'.format(2,i,2*i))
    
# 입력받은 숫자의 단을 출력하세요 >>
# 3을 입력받으면 3단 출력, 4를 입력받으면 4단 출력

n = int(input('단 수를 입력하세요 >>>'))
for p in range(1,10):
    print('{}*{}={}'.format(n,p,n*p))

    
# 중첩 for
# for 안에 for
for i in range(3):  # i = 0,1,2
    print('안녕')
    for j in range(2): # j = 0,1
        print('반가워')
        
n = 9     
for i in range(1,10):
    print('{}*{}={}'.format(n,i,n*i))  # n단

for i in range(2,10):  # 2단부터 9단까지 출력
    for j in range(1,10) :  # *1~*9
        print('{}*{}={}'.format(i,j,i*j))        
        
        
# 출력 형태
# 1 2 3 4 5       
# 1 2 3 4 5     
# 1 2 3 4 5     
# 1 2 3 4 5     
# 1 2 3 4 5      
for j in range(5):  # j = 0 1 2 3 4
    print(j+1, '번째 출력')
    for i in range(1,6):  # i = 1 2 3 4 5
        print(i,end=' ')   # 1 2 3 4 5를 한줄로 출력
    print()   # 줄바꿈

# 구구단 전체단 출력  
for i in range(2,10):
    # print(i,'단')
    print('[{} 단]'.format(i))
    for j in range(1,10):
        print('{}*{} ={}'.format(i,j,i*j), end=' ')
    print()   #들여쓰기 어디에서 하는지!!
    
    
# 짝수단만 출력해주세요
for i in range(2,10):
    if i%2 == 0 :
        print('[{}단]'.format(i))
        for j in range(1,10):
            print('{}*{}={}'.format(i,j,i*j),end=' ')
        print()
        
# 홀수단만 출력해보세요

for i in range(2,10):
    if i%2 == 1 :
        print('[{}]단'.format(i))
        for j in range(1,10):
            print('{}*{}={}'.format(i,j,i*j),end=' ')
        print()

# 구구단 전체 출력 다시
for i in range(2,10) :
    print('[{}단]'.format(i))
    for j in range(1,10):
        if j%2 == 1 :
            print('{}*{}={}'.format(i,j,i*j),end=' ')
    print()
  