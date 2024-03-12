# < 리스트에서 data가 변경되지 않게 하려면 >

list = [1,2,3]
alist = list   # 공간을 같이 쓴다. data가 같이 바뀜
print(list)
print(alist)

#data가 바뀌지 않게 하려면
# alist = [*list]   # 1
alist = [list[:]]  # 2  [[1, 2, 3]]
list[0] = 100
print(list)
print(alist)  # =>복사

list[0] = 100
print(list)
print(alist)  # =>  동기화

a = 100
b = a
print(a)
print(b) # 100

a = 10
print(a)
print(b)
