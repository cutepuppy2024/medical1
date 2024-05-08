# random 함수
from random import *

print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
print(random())
print(int(random()*10)) # 0~10 미만의 임의의 값 생성
print(int(random()*10))
print(int(random()*10))
print(int(random()*10)+1) # 1~10 이하의 임의의 값 생성
print(int(random()*10)+1)
print(int(random()*10)+1)

print(int(random()*45)+1) # 1~45 이하의 임의의 값 생성
print(int(random()*45)+1)
print(int(random()*45)+1)

print(randrange(1,46)) # 1~46 이하의 임의의 값 생성
print(randrange(1,46))
print(randrange(1,46))

print(randint(1,45)) # 1~45 이하의 임의의 값 생성

# 해보세요 >>
# 1~10 사이의 숫자를 입력받아서  => 변수1
# 변수1 1~10 사이의 랜덤한 숫자
# 랜덤한 숫자와 비교해 같으면 [당첨] 
# 다르면 [랜덤숫자는 {}롤 일치하지 않습니다.]

var1 = int(input('1~10사이의 숫자를 입력하세요 >>'))
var2 = int(random()*10)  #randrange/randint(1,10)
print(var1,var2)

if var1 == var2 :
    print('당첨')
else:
    print('랜덤숫자는 {}와 일치하지 않습니다.'.format(var1))
