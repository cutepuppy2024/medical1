# 리스트 처리속도
list = []
# 1- 10까지 있는 숫자 입력

# 기본문법
for i in range(10):
    list.append(i)
print(list)   

# 공간을 먼저 만들기
list = [0]*10
for i in range(10):
    list[i] = i+1
print(list)   


# 컴프리헨션
list = [i+1 for i in range(10)]
print(list)