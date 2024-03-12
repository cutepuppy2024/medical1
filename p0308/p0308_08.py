import random

# 2조 711
# 4조 740

# 조 : 1-9
# 0-999999
first_num = random.randint(1,9)
last_num = random.randint(0,999999)
print('당첨 번호는 : {}조{}입니다.'.format(first_num,last_num))
print('당첨 번호는 : {}조{}입니다.'.format(str(first_num),str(last_num)))

lotto = str(first_num)+'조'+'{:6d}'.format(last_num)  # => 6자리 숫자를 맞추어 주기 위해
print(lotto)




lotto = '1조740'
l_input = input('복권을 입력하세요(예: 1조111)')
# 예: 2조 711 => 1개 번호가 맞았습니다.
cnt = 0
for i in range(len(lotto)):
    for j in l_input:
        if lotto[i] == l_input[i]:
            cnt += 1
print('맞는개수 :{}'.format(cnt-1))  # => 글자수 한개 빼기 
        
cnt = 0
for i in range(len(lotto)) :
    if lotto[i] == l_input[i]:
        print(lotto[i])
        cnt += 1
    else:
        print(lotto[i],l_input[i])
print(lotto,l_input,'맞는 숫자의 개수:{}',format(cnt-1))