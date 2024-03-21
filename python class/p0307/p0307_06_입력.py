# <랜덤>

import random

w_list = ['토마토','바나나','사과','배','수박','메론','복숭아']



# random.random()
print(random.random())
# 0-1 사이의 실수를 랜덤실수 생성 : 0.00000 ~ 0.999999999

# 범위를 지정하는만큼 정수형 랜덤숫자 생성 : 마지막 숫자 포함
print(random.randint(0,44))

# 0,2 까지 랜덤숫자를 생성 : 마지막 숫자 포함시키지 않음
print(random.randrange(0,3))

# 리스트를 랜덤으로 섞기
list = [1,2,3,4,5,6,7]
print(list)
random.shuffle(list)
print(list)

# list에서 1개를 랜덤으로 추출
print(random.choice(list))

# 리스트에서 해당되는 개수만큼 랜덤으로추출, 중복은 불가능
print(random.sample(list,2))

w_list = ['토마토','바나나','사과','배','수박','메론','복숭아']

print(random.sample(w_list,3))  # 리스트에서 가지고 온다
