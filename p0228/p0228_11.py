from random import *
# 1. 변수선언 1 -10
lotto = []
# 2. 입력받은 숫자 6개
mynum = [2,5,1,9,3,7]
# 3. 로또 번호 생성하기

# for i in range(6):
#     n = randint(1,10)
#     if n not in lotto:
#         lotto.append(n)
# print(lotto)

num = [1,2,3,4,5,6,7,8,9,10] # 특징: 중복이 없다, 1 - 10까지다  => 섞으면 중복이 없을 것이므로
#      0                  9
# [1,2,3,4,5,6]
# [2,3,4,5,6,7]
for i in range(10):
    tmp = randint(0,9)
    print(tmp)
    num[0],num[tmp] = num[tmp],num[0]
print(num)  # [5, 2, 3, 4, 1, 6, 10, 8, 7, 9]

for i in range(6):
    lotto.append(num[i])  # [6, 8, 3, 4, 7, 5]
print(lotto) 

ok = []
for i in range(len(mynum)):  # i = 0,1,2,3,4,5, ////
    print(mynum[i])  # 리스트에 있는 숫자 출력
    if mynum[i] in lotto:
        ok.append(mynum[i])
print(ok)