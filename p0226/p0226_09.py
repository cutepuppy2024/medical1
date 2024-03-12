# 반복문
print('안녕하세요'*5)
print('안녕하세요')
print('안녕하세요')
print('안녕하세요')
print('안녕하세요')
print('안녕하세요')

# for 변수 in 반복 가능한 데이터:
#    수행할 문장
    
for i in range(0,5,1) : # range(시작값, 끝값+1, 증가값)
                        # i가 0,1,2,3,4
    print('안녕')
for i in range(0,5,1) :
    print(i,'안녕')
for i in range(0,3) : # 증가값이 1인 경우 생략가능
    print(i,'Hi')
for i in range(4) : # n번 반복할 경우 range(n)을 사용할 수 있다
    print('hello')
for _ in range(2):
    print(('반갑습니다')) # i를 사용하지 않을 경우 _ 사용할 수 있다.

for i in range(5):  #5번 반복해라
    num = input('숫자를 입력하세요 >> ')
    print('입력하신 숫자는 : {}'.format(num))
    
# i, j 카운터 변수, k, l .. i, j를 자주 사용
# 카운터변수는 반복 실행 될때마다 현재 실행 횟수에 해당하는 숫자가
# 들어감 가장처음은 실행한 적이 없으므로 0이 된다

for i in range(3): # 증가값 1인 경우 생략
    print(i)
    #0 1 2 가 순차적으로 출력됨
    
str1 = "안녕하세요"
for i in str1:
    print(i)
    
# 1. 1에서부터 15까지 출력해보세요
for i in range(16):  #range(1,15,1)  
    print(i)         # range(15) print(i+1)
    
# 2. 10을 4번 반복해서 출력해보세요
for i in range(4):
    print(10)

# 3. helloworld를 6번 반복해서 출력해보세요
for _ in range(6):
    print(i+1,'helloworld')
    
# 4. 1-100사이의 2의 배수를 출력해 보세요 (2,4,6,,)
for i in range(2,100,2):
    print(i, end=',')  # end: 줄바꿈 없이
    
#5. 1-100 사이의 5의 배수를 출력해 보세요
for i in range(5,100,5) :
    print(i, end='')
