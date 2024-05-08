from random import *

n1 = randrange(1,11) # 1-10까지의 정수
n2 = randint(1,10) # 1- 10까지의 정수

# 랜덤한 숫자 6개 lott리스트에 넣고
# 1. 변수선언
lotto = []
mynum = []

# 2. 숫자 6개 입력받기(내가 입력한 숫자 6개는 mynum리스트에)
for i in range(6):
    p = randint(1,10)
    lotto.append(p)
print(lotto)
print('lotto 숫자는{} 입니다.'.format(lotto))

for i in range(6):
    n2 = int(input("{}번째 숫자를 (1-10 중) 숫자를 입력해 주세요 >>".format(i+1)))
    mynum.append(n2)

print('입력하신 숫자는 {}입니다.'.format(mynum))

#3. 로또 숫자 생성(랜덤한 숫자 6개lotto 리스트에 넣고)
# 중복없이 숫자를 입력받고 싶다.
for i in range(6):
    p = randint(1,10)  # 만약에 랜덤숫자
    if p not in lotto:
        lotto.append(p)

# 입력숫자와 랜덤숫자 비교
cnt = 0
for i in range(6):
    if lotto == mynum:
        cnt += 1
        
print("맞춘 숫자의 개수 : ", cnt,"개")
        

