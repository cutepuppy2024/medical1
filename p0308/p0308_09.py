# [랜덤숫자 맞추기]

import random
random_num = random.randint(10000,99999)


print(('[랜덤숫자 맞추기]'))

a_input = str(input('숫자 5자리를 입력하세요'))
random_num = str(random_num)

# 숫자자리로 해서 맞춤 갯수를 출력하시오
# cnt = 0
# for i in range(len(random_num)):
#     if random_num[i] == a_input[i]:
#         cnt += 1
# print('맞춘갯수 : {}'.format(cnt))
# print('랜덤숫자 : {} , 입력숫자: {}'.format(random_num,a_input))    # print('랜덤 숫자는 {} 입니다'.format(random_num))

# 자릿수로 맞추기
cnt = 0
for i in range(len(random_num),0,-1):
    # print(i)
    if random_num[i-1] == a_input[i-1]:
        cnt += 1
    else :
        break

if cnt == 0 :
    print('완전 꽝입니다')
else :
    print('{}개를 맞추셨습니다'.format(cnt))
    if cnt == 1 :
        print('1만원 당첨!')
    elif cnt == 2 :
        print('10만원 당첨!')
    elif cnt == 3 :
        print('100만원')
    elif cnt == 4 :
        print('1000만원')
    elif cnt == 5 :
        print('1억원! 축하합니다!')
    elif cnt == 1 :
        print('10억원! 대박입니다!')
print('랜덤숫자 : {} , 입력숫자: {}'.format(random_num,a_input)) 

