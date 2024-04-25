from random import *

n1 = randrange(1,10) # 1-9 사이의 정수
n2 = randrange(10)  # 0-10 사이의 정수
n3 = randrange(1,10) # 1-10 사이의 정수
print(n1,n2,n3)

for i in range(6):
    a = randint(1,10) #   print(randiant(1,10))
    print(a)

# lotto에 1-10사이의 랜덤한 숫자 6개를 넣어보세요  
lotto =[]
for i in range(6):
    a = randint(1,10)
    lotto.append(a)
print(lotto)

mynum=[]
for i in range(6):
    b = int(input("숫자를 입력하세요>>"))
    mynum.append(b)
print(mynum) 
    
# 내가 직접 입력한 숫자 6개를 넣어보세요