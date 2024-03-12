print('2단 출력')
for i in range(1,10): # i = 1,2,3,4,5,...9
    print('2 * {} = {}'.format(i,2*i))
for i in range(1,10): # i = 1,2,3,4,5,...9
    print('{} * {} = {}'.format(2, i, 2 *i))
    
print('3단 출력')
for i in range(1,10):
    print('3 *{} = {}'.format(i,2*i))
    
n1 = int(input('숫자를 입력하세요 >>'))
for i in range(1,10):
    print('{} *{} = {}'.format(i,n1, i*n1))
    

for i in range(9):
    mul = int(input('숫자를 입력하세요 >>'))
    for i in range(1,10): 
        print('{} * {} = {}'.format(mul,i,i*mul))