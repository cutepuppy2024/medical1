# 1. 변수선언
score =[
    [80,90,85],[70,80,90],[84,92,80],[72,81,76]
]
name = ['홍길동', '유관순', '이순신','김구']
total = []

# 2. 코딩
# 2 -1) 요소 하나하나 출력해보세요 80 90 85 70 80 90 ....
for i in score :        
    for j in i:         
        print(j)

# 2 -2) 작은 요소의 합을 구해서 total 넣어주세요
t1 = 0              # 누적되는 식
for a in score:
    print('리스트입니다', a)
    for b in a :
        print('요소입니다',b)
        t1 =t1 +b
    print(t1)
    
for i in range(len(score)): # i = 0,1,2,3
    sum = 0        # => 전체가 더해지지 않게 하는 가장 중요한 위치!!
    #print(score[i])
    # i = 0, score [0][0] + score[0][1] +score[0][2] = sum
    # i = 1, 
    for j in range(len(score[i])):  # j = 0,1,2  # print(score[i][j])
        sum += score[i][j]  #=> 전체를 출력하게 된다
    total.append(sum)


# 3. 출력
# 3 - 1) total = [255,240,256,226] 
print(total)
# 3 - 2) 250 미만 불합격 250 이상 합격 ex) 홍길동님 합격입니다 출력
for i in range(len(total)):
    if total[i] >= 250 :
        print('{}님 합격입니다'.format(name[i]))
    else:
        print('{}님 불합격입니다'.format(name[i]))