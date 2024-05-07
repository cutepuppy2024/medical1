from random import *
# 랜덤한 숫자를 만들어서(1-100 사이)
# 내가 입력한 값이 랜덤한 숫자랑 같으면 당첨
# 아니면 다시 입력해주세요
# 를 출력하는 프로그램을 만들어보세요

# # print(randint(1,100))
# # print(randint(1,100))
# # print(randint(1,100))
# # print(randint(1,100))


# # 입력한 숫자가 랜덤숫자보다 작으면 작습니다 더 큰수를 입력해주세요

# n1 = randint(1,100)   # 정답에 가까운 수를 찾고자 할 때 무한루프 안으로 들어가지 않게 하기 위해서 밖으로 빼면 된다
# while True :
#     n2 = int(input('숫자를 입력해 주세요 >> '))
#     if n2 < n1 :                                # continue를 쓰게 되면 그 수를 제외하라는 의미이므로 쓸 필요가 없다
#         print('작습니다 더 큰수를 입력해주세요')
#     elif n2 > n1 :
#         print('다시 입력해주세요')
#     elif n1 == n2 :
#         print('당첨')
#         break
# print()   


# for i in range(100000000000):   # for 문에서는 무한반복되는 명령어가 없다
#     n1 = int(randint(1,100))
#     n2 = int(input('숫자를 입력해 주세요 >> ')) 
#     if n1 == n2:
#         print('당첨')
#         break
#     else:
#         print('다시 입력해주세요')
#         continue
    
    
    
# 1. 숫자 입력하여 당첨숫자 찾기   
# while                                 
# n1 = int(randint(1,100))
# while True:
#     n2 = int(input('숫자를 입력해 주세요 >>'))
#     if n1 == n2 :
#         print('당첨')
#         break
#     elif n2 < n1 :
#         print('입력하신 숫자가 랜덤숫자보다 큽니다. 더 작은 수를 입력해주세요')
#     else :
#         print('입력하신 숫자가 랜덤숫자보다 작습니다. 더 큰수를 입력해주세요')



from random import*
# 2. 10회 도전 후 프로그램이 종료가 되게 해주세요
randNum = int(randint(1,100))
inputList = []
for i in range(10):
    pick = int(input('숫자를 입력해 주세요 >>'))
    inputList.append(pick)
    print('{}번째 입력한 숫자는 {}입니다.'.format(i,pick))
    if randNum == pick :
        print('당첨')
        break
    elif randNum < pick :
        print('입력하신 숫자가 랜덤숫자보다 큽니다. 더 작은 수를 입력해주세요')
    else :
        print('입력하신 숫자가 랜덤숫자보다 작습니다. 더 큰수를 입력해주세요')
print('사용자가 입력한 숫자들은 :', inputList)   



# 3. 10회 도전이 실패한 사람에게 랜덤숫자 알려주기   
from random import *

cnt = 0 
while cnt < 10:  # => 10번까지 반복할것이다  => 내가 한것과 다른 것은 : while사용, 횟수를 사용한다면 for가 간단할거라고 생각함. while을 써야 10회 이상인 경우 10회초과되었다는 커멘트를 쓸 수 있는듯?
    cnt += 1
    userInput = int(input('{}번째 도전! 숫자를 입력해주세요 >> '.format(cnt)))  # => 출력형태
    inputList.append(userInput)   #print는 마지막에만
    if randNum == userInput :
        print('당첨')
        break
    elif userInput > randNum :
        print('입력하신 숫자가 랜덤숫자보다 큽니다.')
        print('더 작은수를 입력해주세요')
    else: 
        print('입력하신 숫자가 랜덤숫자보다 작습니다.')
        print('더 큰수를 입력해주세요')
        
# 3. 10회 도전이 실패한 사람에게 랜덤숫자 알려주기 
if cnt == 10 :
    print('10회입력을 초과하셨습니다. 정답은', randNum)           
print("사용자가 입력한 숫자들은 : ", inputList)
