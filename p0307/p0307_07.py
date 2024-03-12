# < 딕셔너리에서 랜덤 key값 >
import random

fruits = {'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grape':'포도','mango':'망고','kiwi':'키위'}  

print('개수 : ', len(fruits))
# 랜덤으로 4개를 출력 - 랜덤으로 4개를 추출
# 랜덤은 리스트
# key를 리스트 타입으로 변경
print(fruits.keys())
print(random.sample(list(fruits.keys()),4))

# 4개의 랜덤 key를 출력하시오
f_list = random.sample(list(fruits.keys()),4)

f_list2 = ['kiwi','grape','peach','pear']
print(fruits[f_list2[0]])
print(fruits[f_list2[1]])
print(fruits[f_list2[2]])
print(fruits[f_list2[3]])

# value 값을 전체출력
# for key in fruits :
#     print(fruits[key])
    
    
