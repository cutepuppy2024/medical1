from random import *


# 1. 변수 선언
mynum = [] # 입력을 1 - 45 사이의 숫자를 입력받음 (6개)
lotto = [] # 1-45 사이의 랜덤한 숫자 6자리를 입력

# 2. 입력받은 숫자 6개:
# mynum = [] input()를 통해서 숫자 6개를 넣을 예정
for p in range(6):
    n = int(input('1-45 사이의 숫자를 입력하세요 >>'))  #  n = int(input('{}번째 숫자를 입력하세요 >>'.format(i)))
    mynum.append(n)
print('{}번째 선택하신 숫자는 {}입니다.'.format(p,n))
print('선택하신 6개의 숫자는 {}입니다.'.format(mynum))

# for q in range(6):
#     q = randint(1,45)
#     lotto.append(q)
print(lotto)

# 3. 로또 번호 생성하기 :
# 1-45 까지의 숫자
l = []
for u in range(46):
    l.append(u)
print(l) # print('로또 숫자 : {}'.format(l))  => 중복이 없는 1-45까지의 숫자가 들어있음.

# num = [0,1,2]
# num[0], num[2] = num[2],num[0]

# 4. 숫자들을 섞는다
for i in range(100):
    r = randint(0,44)
    l[0],l[r] = l[r],l[0]
print(l)
# print(l[0:6])

for i in range(6):
    lotto.append(i)
print(lotto)

ok = []    
for i in range(6):
    if mynum[i] in lotto :
        ok.append(mynum[i])
print(ok)

print('입력한 숫자 : {}'.format(mynum))
print('로또 숫자 : {}'.format(lotto))
print('당첨된 숫자 : {}'.format(ok))


    
# for t in range(6):
#     if l[t] in lotto:
#         print('일치합니다')
#     else:
#         print('일치하지 않습니다')
        
# for t in range(6):
#     if l[t] in mynum:
#         print('일치합니다')
#     else:
#         print('일치하지 않습니다')
        