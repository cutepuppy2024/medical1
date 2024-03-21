# < 주택복권 >

import random



# print(a[0])
# print(a[-1])
# print(a[-2])

first_num = random.randint(1,9)
last_num = random.randint(0,999999)
lotto = str(first_num)+'조'+'{:6d}'.format(last_num)  # => 6자리 숫자를 맞추어 주기 위해
print(lotto)

# l_input = input('복권을 입력하세요(예: 1조111)')
# # 예: 2조 711 => 1개 번호가 맞았습니다.
# cnt = 0
# for i in range(len(lotto)):
#     for j in l_input:
#         if lotto[i] == l_input[i]:
#             cnt += 1
# print('맞는개수 :{}'.format(cnt-1))  # => 글자수 한개 빼기 

# 1조 123456
# 6번째 1개 -> 1만원, 5,6번째 자리 2개  -> 10만원,  4,5,6번째자리 -> 100만원,3456번째 자리 -> 1000만원

# 6번째 1개 -> 1만원 출력

a = "1조23456"
b = "7조77756"

cnt = 0  # 맞는 갯수
for i in range(len(a),0,-1):
    # print(a[i-1])
    if a[i-1] != b[i-1]:
        break
    else:
        cnt += 1  #맞는 횟수 1증가
        
if cnt == 0:
    print('완전 꽝입니다')
elif cnt == 1:
    print('6번째 자리가 맞았습니다. 당첨금액: 1만원')
elif cnt == 2:
    print('5,6번째 자리가 맞았습니다. 당첨금액: 10만원')
elif cnt == 3:
    print('4,5,6번째 자리가 맞았습니다. 당첨금액: 100만원')
elif cnt == 4:
    print('3,4,5,6번째 자리가 맞았습니다. 당첨금액: 1000만원')
elif cnt == 5:
    print('2,3,4,5,6번째 자리가 맞았습니다. 당첨금액: 1억원')
elif cnt == 6:
    print('1,2,3,4,5,6번째 자리가 맞았습니다. 당첨금액: 10억원')
        
    
# for i in range(len(a)):
#     print(a[len(a)-1-i])
    
    # if j in l_input :
    #     if lotto[len(a)] == l_input[i]:
    #         cnt += 1
            
            
a = "1조123456"
b = "7조177756"

cnt = 0  # 맞는 갯수
for i in range(len(a),0,-1):
    if i == 2 :
        continue  #조 는 건너뛰기
    # print(a[i-1])
    if a[i-1] != b[i-1]:
        break
    else:
        cnt += 1  #맞는 횟수 1증가
        
if cnt == 0:
    print('완전 꽝입니다')
elif cnt == 1:
    print('6번째 자리가 맞았습니다. 당첨금액: 1만원')
elif cnt == 2:
    print('5,6번째 자리가 맞았습니다. 당첨금액: 10만원')
elif cnt == 3:
    print('4,5,6번째 자리가 맞았습니다. 당첨금액: 100만원')
elif cnt == 4:
    print('3,4,5,6번째 자리가 맞았습니다. 당첨금액: 1000만원')
elif cnt == 5:
    print('2,3,4,5,6번째 자리가 맞았습니다. 당첨금액: 1억원')
elif cnt == 6:
    print('1,2,3,4,5,6번째 자리가 맞았습니다. 당첨금액: 10억원')
elif cnt == 7:
    print('1,2,3,4,5,6,7번째 자리가 맞았습니다. 당첨금액: 10억원')


