import random
# 크기가 10인 리스트를 생성하는데, 7개는 0으로 3개는 1로 채우시오. 
# [1,1,1,0,0,0,0,0,0,0]

list = [0]*10
for i in range(3):
    list[i] = 1
print(list)


# a = []
# for i in range(10):
#     if i < 3:
#         i = 1
#         a.append(i)
#     else:
#         i = 0
#         a.append(i)
# print(a)
        
        

# 크기가 100인 리스트 생성, 10개는 1로 채우시오
# 랜덤으로 섞어서 출력하시오

aList = [0 for i in range(100)]
for i in range(10):
    aList[i] = 1
# print(aList)  # 파괴
random.shuffle(aList)
print(aList)
print('-'*30)

# a = 10
# print(a+10) #비파괴형태
# a = a+10 # 파괴형태
# print('a:',a)

# list100 = [0]*100
# for j in range(10):
#     list100[j] = 1
# print(list100)
# random.shuffle(list100)
# print(random.sample(list100,7))


#[10*10] 2차원 배열을 생성하시오

bLists = []
bList = []
for i, j in enumerate(aList):  # => i 횟수, i의 element가 j
    if (i+1)%10 == 0:   # 0,1,2,3,4,5,6,7,8,9 # => 10으로 나누었을 때의 나머지가 0이면 
      #  print(i,end=' ') 9 19 29 39 49 59 69 79 89 99 일때 , 즉 10번째 숫자인 j
        bList.append(j)  #bList에 j를 추가하고
        bLists.append(bList) # bLists에 2차원 리스트를 추가 후
        bList = [] # 초기화시키겠다 => 결과: 다 돌면 2차원배열 생성 [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
    else :
        bList.append(j)
print(bLists)

# for i in range(10):      => 위의 2차원 배열과 비교
#     for j in range(10):
#         print(j,end='\t')
#     print()
    
# 10*10 전체가 [추첨]이라고 씌여진 리스트 1개 추가
newList = [['추첨']*10 for i in range(10)]
print(newList)



# 10*10 [추첨]좌표로 만들기
cnt = 0  # 당첨횟수
while True:
    print("[ 10*10 좌표 ]")
    print("-"*60)
    print('   ', 0,1,2,3,4,5,6,7,8,9,sep="     ")
    print("-"*60)
    for i, b in enumerate(newList): # i 횟수는 newList 안에 있는 element인 b 숫자만큼 => b는 10 
        print(i,end='  ')
        for bb in b:    
            print(bb,end="  ")
        print()
    print("-"*60)

    x = int(input('가로 좌표를 입력하세요'))
    y = int(input('세로 좌표를 입력하세요'))
    
# bLists - 값을 비교, newLists - 표시
    if bLists[x][y] == 1 :  #당첨
        newList[x][y] = "당첨"
        cnt += 1
        if cnt == 2 :
            print('게임이 종료되었습니다')
            break
    else : # 꽝
        newList[x][y] = "[꽝]"
    
    