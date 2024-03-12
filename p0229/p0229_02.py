#리스트변수명 =[요소1, 요소2,.. 요소n]
#요소가 될수 있는 타입이 :bool, int, float, string, list

fruits = ['딸기','사과','배','수박','귤']
# 귤을 출력
print(fruits[4])
print(fruits[-1])
print(fruits[len(fruits)-1])
# 리스트에 요소를 추가
fruits.append('포도')
print(fruits)
fruits.remove('딸기')
print(fruits)
del(fruits[3])
print(fruits)

if '한라봉' in fruits :
    print('있습니다')
    
for f in fruits:
    print(f)
for i in range(len(fruits)):
    print(fruits[i])
    
num = [[10,20,30],[100,200,300],[1,2,3]]
for n in num :
    print(n)    
    
for n in num:
    for a in n :
        print(a)
print('-'*25)

for i in range(len(num)):
    print(num[i])
for i in range(len(num)):
    for j in range(len(num[i])):
        print(num[i][j])
        
        
# 리스트에 숫자 넣을때 한줄로 표현하기
aa = []
for i in range(1,11):
    aa.append(i)

print(aa)      

a = [i for i in range(1,11)]
a = [0 for _ in range(10)]
print(a)  
a = [[0] for i in range(10)]

# [표현식 for 항목 i in 리스트 if 조건문]

a =[i*j for i in range(1,3) for j in range(1,3)]  # 리스트 안dp, 중복으로 for와 if문을 써서 간단하게!!
# [1,2,2,4]
a =[i for i in range(100) if i%2 == 0]
print(a)
b = [i for i in range(1,11)]
print(b) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c =[i+1 for i in b]
print(c) # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


names =['홍길동','유관순','이순신','강감찬','김구']
# 출력
# 1. 홍길동 2. 유관순 3. 이순신 4. 강감찬. 5. 김구
for i in range(len(names)):
    print('{}.{}'.format(i+1,names[i]),end=' ')
print()
   
for i in range(5):
    print(i,'.',names[i],end=' ')
print()
# 변수 1개 더 필요
i = 0  
for name in names:
    i+= 1
    print('{}.{}'.format(i,name),end=' ')
    
# enumerate 함수
# index를 넣고 싶을때 사용
for i, name in enumerate(names): # indx : 0부터시작
    print('{}.{}'.format(i+1,name))
    
for i, name in enumerate(names, start =1): # index : 1부터 시작
    print('{}.{}'.format(i,name))
    
for i, name in enumerate(names): # indx : 0부터시작
    print('{}는{}번째 있습니다'.format(name,i))
    
for i, name in enumerate(names):
    if '홍길동' in names:
        del(names[i])
        print(names)
    