# < map : 각 값의 type 변환 >


today_list = ['2024','03','08']
# today_list[0] = today_list[0] + 10  #error
# today_list[0] = int(today_list[0] + 10)
# print(today_list[0])
print(today_list)


# map : 문자열을 정수형으로 모두 변환해서 리스트 저장
t_list = list(map(int,today_list))   
print(t_list)


# map : 문자열을 정수형으로 모두 변환해서 리스트 저장

int_list = [10,20,30,40,50]
str_list = list(map(str,int_list))
print(str_list)


# 리스트의 데이터 타입 : int
list5 = []
for i in range(5):
    list5.append(i) # 데이터타입 : int 
print(list5)

# 리스트의 데이터 타입을 str으로 

a_list = list(map(str,range(10)))
print(a_list)

# a_list = list(map(int,range(input('숫자입력:'))))
# print(a_list)
# 5개의 숫자를 입력하시오
# list = []
# for i in range(5):
#     # list.append(input('숫자를 입력하세요')) # ['1', '2', '3', '4', '5']
#     # list.append(int(input('숫자를 입력하세요')))   #[1, 2, 3, 4, 5]
#     list(map(int,input('숫자를 입력하세요')))
# print(list) 


