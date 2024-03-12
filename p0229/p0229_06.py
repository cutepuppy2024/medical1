# continue 예제


# [1,2,4,5,7,8,10....]
# while or for
# 1-100 까지 출력, 3의 배수는 제외하고 출력
# 1-100 까지의 합계를 구하는데 3의 배수는 제외하고 더하기
i = 0
sum = 0
while i < 100:
    i += 1
    if i%3 == 0:
        continue
    print(i,end=' ')
    sum += i
print(sum)


for i in range(1,101):
    if i%3 == 0:
        continue
    print(i, end=' ')   # 3의 배수를 제외하고 출력
print()

i = 1                         #아래와 같이 i와 sum을 다른 라인으로 쓰면 sum값만 따로 뺄 수 있음
while i<101:
    if i%3 == 0:
        i = i+1
        continue
    print(i, end=' ')
    i = i+1
    
# 3의 배수를 제외하고 더하기
sum = 0
for i in range(1,101):
    if i%3 == 0:
        continue
    sum += i
print('\n 배수 제외한 합', sum)      # sum1 정의로 강의하신 내용 확인하기!!!
                    