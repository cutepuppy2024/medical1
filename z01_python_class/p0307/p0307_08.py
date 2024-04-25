# < 랜덤으로 key값 추출 >

import random

fruits = {'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grape':'포도','mango':'망고','kiwi':'키위'}  


print(fruits['peach'])
print(fruits['kiwi'])

f_list = ["peach","pear","kiwi"]  # 키값 선택하여 리스트
    
print(fruits[f_list[0]])

for f in f_list:
    print(fruits[f])          # 리스트에 있는 키값에 대한 value값 출력
    
# 랜덤으로 key값 추출                  / 리스트는 자리로 값을 찾지만 딕셔너리는 키값으로 값을 찾는다

f_list = list(fruits.keys())
print(f_list)

f_list_ran = random.sample(f_list,4)
print('랜덤추출 :', end=':')
for f in f_list_ran :
    print(fruits[f], end=':')