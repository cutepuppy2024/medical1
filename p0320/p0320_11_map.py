def jegob(val):
    return val**2
def func(val):
    return val >=3
def int_change(val):
    return int(val)

a_list =[1,2,3,4,5]
str_list =["1","2","3","4","5"]

# 리스트 전체에 값의 변경이 필요할 때
map_list = list(map(jegob,a_list))
print(a_list)
print(map_list)

ss_list = list(map(int_change,str_list))
print(str_list)
print(ss_list)

ss_list2 = list(map(lambda val:int(val),str_list))  # 매개변수 : 리턴
print(ss_list2)


# 조건에 맞는 값만 추출
f_list= list(filter(func,a_list))
print(f_list)