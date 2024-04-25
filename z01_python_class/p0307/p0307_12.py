# < 컴프리헨션 >

list = [
    [1,2,3], [4,5,6], [7,8,9]
]

for i in list :
    print(i)
    
for i in list :
    for j in i :
        print(j,end='\t')
    print()
    
# 1차원 리스트에 1-9까지의 숫자를 입력하시오
list = []

for i in range(9):
    list.append(i+1)
print(list)

# 컴프리헨션
list2 = [n+1 for n in range(9) ]   # for의 값을 리스트 안에 넣어서 계산 1-9
print(list2) 
list2 = [n for n in range(9) ]   # 8까지
print(list2) 
list2 = [2*n for n in range(9) ]
print(list2) 

list3 = [[0]*3 for n in range(3)]
print(list3)

numList = [num*num for num in range(1,6)]   # 제곱근 만드는 형식 
print(numList)

# 1-9까지의 2차원 리스트에 숫자를입력하시오
# [ [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9] ]
a = []
for i in range(3):
    n = []
    for j in range(3):
        n.append((3*i)+j+1)
    a.append(n)
print(a)




# for i in list:
#     for f in i:
#         print(f,end="\t")
#     print()    