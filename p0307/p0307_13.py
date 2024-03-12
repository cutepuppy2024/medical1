# < 리스트 만드는 3가지 방법 >

list = [
    [],[],[]
    
]

# 2차원 리스트 크기가 지정이 안됨
# append 사용하여 추가
a_list = []
a_list.append(0)
a_list.append(1)
a_list.append(2)
# a_list[3] = 3
print(a_list)

# 공간을 만들어 놓고 for문 사용
list1 = [0]*10
for i in range(10) :
    list1[i] = i+1
print(list1)

# 컴프리헨션을 사용하는 방법
list2 = [i+1 for i in range(10)]  
print(list2)